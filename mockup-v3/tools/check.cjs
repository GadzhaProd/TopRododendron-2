// Serves dist/ under the strict CSP of the artifact viewer and checks every page
// in Chromium at several viewports: console/page errors, failed requests, React
// root rendered, hero video playing, broken images, horizontal overflow.
// Usage: node tools/check.cjs [--shots] [--pages index,product] [--widths 390,1440]
const http = require('http')
const fs = require('fs')
const path = require('path')
const { chromium } = require('playwright')

const dist = path.join(__dirname, '..', 'dist')
const CSP = "default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com data:; img-src 'self' data: blob:; media-src 'self' blob:"
const types = { '.html': 'text/html; charset=utf-8', '.mp4': 'video/mp4', '.webp': 'image/webp', '.jpg': 'image/jpeg', '.svg': 'image/svg+xml', '.js': 'text/javascript', '.css': 'text/css' }

function serve() {
  return new Promise((resolve) => {
    const srv = http.createServer((req, res) => {
      const url = decodeURIComponent(req.url.split('?')[0].split('#')[0])
      let file = path.join(dist, url === '/' ? 'index.html' : url)
      if (!file.startsWith(dist) || !fs.existsSync(file)) { res.writeHead(404); res.end('nf'); return }
      const stat = fs.statSync(file)
      const ext = path.extname(file)
      const headers = { 'Content-Type': types[ext] || 'application/octet-stream', 'Content-Security-Policy': CSP, 'Accept-Ranges': 'bytes' }
      const range = req.headers.range
      if (range && ext === '.mp4') {
        const [s, e] = range.replace('bytes=', '').split('-').map((x) => parseInt(x, 10))
        const start = s || 0, end = Number.isFinite(e) ? e : stat.size - 1
        res.writeHead(206, { ...headers, 'Content-Range': `bytes ${start}-${end}/${stat.size}`, 'Content-Length': end - start + 1 })
        fs.createReadStream(file, { start, end }).pipe(res)
        return
      }
      res.writeHead(200, { ...headers, 'Content-Length': stat.size })
      fs.createReadStream(file).pipe(res)
    })
    srv.listen(0, '127.0.0.1', () => resolve(srv))
  })
}

const args = process.argv.slice(2)
const flag = (n) => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : null }
const shots = args.includes('--shots')
const pages = (flag('--pages') || 'index,assortiment,product,plantgids,groothandel').split(',')
const widths = (flag('--widths') || '360,375,390,768,1024,1366,1440').split(',').map(Number)
const heights = { 360: 640, 375: 667, 390: 844, 768: 1024, 1024: 768, 1366: 768, 1440: 900 }
const shotDir = path.join(__dirname, '..', '.shots')

;(async () => {
  const srv = await serve()
  const port = srv.address().port
  const browser = await chromium.launch()
  let failures = 0
  if (shots) fs.mkdirSync(shotDir, { recursive: true })
  for (const page of pages) {
    for (const w of widths) {
      const h = heights[w] || 900
      const ctx = await browser.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 1, isMobile: w < 768, hasTouch: w < 768 })
      const p = await ctx.newPage()
      const errors = [], failed = []
      p.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()) })
      p.on('pageerror', (e) => errors.push('pageerror: ' + e.message))
      p.on('requestfailed', (r) => failed.push(r.url()))
      p.on('response', (r) => { if (r.status() >= 400) failed.push(r.status() + ' ' + r.url()) })
      const hash = page === 'product' ? '#nova-zembla' : ''
      await p.goto(`http://127.0.0.1:${port}/${page}.html${hash}`, { waitUntil: 'load' })
      await p.waitForTimeout(1800)
      const info = await p.evaluate(async () => {
        const root = document.getElementById('root')
        const v = document.querySelector('video')
        let video = 'none'
        if (v) { await new Promise((r) => setTimeout(r, 600)); video = v.paused ? 'paused' : v.currentTime > 0 ? 'playing' : 'stalled' }
        const imgs = Array.from(document.images)
        const broken = imgs.filter((i) => i.complete && i.naturalWidth === 0 && i.getAttribute('src')).map((i) => i.getAttribute('src'))
        const sw = document.documentElement.scrollWidth, iw = window.innerWidth
        // find elements that overflow horizontally
        const over = []
        if (sw > iw) for (const el of document.querySelectorAll('body *')) { const r = el.getBoundingClientRect(); if (r.right > iw + 1 && r.width > 0) { over.push(el.tagName + '.' + String(el.className).slice(0, 60)); if (over.length > 8) break } }
        return { rendered: !!root && root.children.length > 0, video, broken, sw, iw, over, docH: document.documentElement.scrollHeight }
      })
      const probs = []
      if (!info.rendered) probs.push('root not rendered')
      if (errors.length) probs.push('console: ' + errors.slice(0, 3).join(' | '))
      if (failed.length) probs.push('failed: ' + failed.slice(0, 3).join(' | '))
      // hero is a static photo now (no video expected)
      if (info.broken.length) probs.push('broken imgs: ' + info.broken.slice(0, 3).join(','))
      if (info.sw > info.iw) probs.push(`hscroll ${info.sw}>${info.iw} ${info.over.join(' ; ')}`)
      if (probs.length) failures++
      console.log(`${probs.length ? 'FAIL' : 'ok  '} ${page.padEnd(12)} ${String(w).padStart(4)}×${h}  h=${info.docH}  video=${info.video}  ${probs.join(' // ')}`)
      if (shots) {
        // viewport screenshots at steps down the page
        const steps = Math.ceil(info.docH / h)
        for (let i = 0; i < steps; i++) {
          await p.evaluate((y) => window.scrollTo(0, y), i * h)
          await p.waitForTimeout(i === 0 ? 400 : 250)
          await p.screenshot({ path: path.join(shotDir, `${page}-${w}-${String(i).padStart(2, '0')}.png`) })
        }
      }
      await ctx.close()
    }
  }
  await browser.close()
  srv.close()
  console.log(failures ? `\n${failures} view(s) with problems` : '\nall views clean')
  process.exit(failures ? 1 : 0)
})()
