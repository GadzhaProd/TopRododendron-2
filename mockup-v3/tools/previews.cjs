// Records a smooth top-to-bottom scroll-through of every page as MP4 (H.264):
// phone 390×844 @2x (780×1688) and desktop 1440×900. Frames are real @2x
// screenshots (Playwright's screencast only records CSS pixels), assembled at
// 24 fps. The hero video is stepped frame-accurately (currentTime), so it plays
// at real speed for ~3 s before the page scrolls section by section with pauses.
// Output: previews/<page>-telefon.mp4 and previews/<page>-kompyuter.mp4.
const path = require('path')
const fs = require('fs')
const { execFileSync } = require('child_process')
const { chromium } = require('playwright')
const { serve } = require('./server.cjs')

const outDir = path.join(__dirname, '..', 'previews')
const tmp = path.join(__dirname, '..', '.preview-tmp-' + process.pid)
fs.mkdirSync(outDir, { recursive: true })

const args = process.argv.slice(2)
const only = args.includes('--pages') ? args[args.indexOf('--pages') + 1].split(',') : ['index', 'assortiment', 'product', 'plantgids', 'groothandel']
const FPS = 24
const devices = {
  telefon: { width: 390, height: 844, scale: 2, mobile: true },
  kompyuter: { width: 1440, height: 900, scale: 1, mobile: false },
}
const ease = (t) => (t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2)

async function record(page, dev, srvPort) {
  const d = devices[dev]
  const frames = path.join(tmp, `${page}-${dev}`)
  fs.rmSync(frames, { recursive: true, force: true }); fs.mkdirSync(frames, { recursive: true })
  const browser = await chromium.launch()
  const ctx = await browser.newContext({ viewport: { width: d.width, height: d.height }, deviceScaleFactor: d.scale, isMobile: d.mobile, hasTouch: d.mobile })
  const p = await ctx.newPage()
  const hash = page === 'product' ? '#nova-zembla' : ''
  await p.goto(`http://127.0.0.1:${srvPort}/${page}.html${hash}`, { waitUntil: 'load' })
  await p.waitForTimeout(1500)
  // take control of the hero video so it advances exactly 1/FPS per frame
  const hasVideo = await p.evaluate(() => { const v = document.querySelector('video'); if (!v) return false; v.pause(); v.currentTime = 0.5; return true })
  await p.waitForTimeout(400)
  const plan = await p.evaluate(() => {
    const tops = Array.from(document.querySelectorAll('main > section, main > div > section, footer')).map((el) => Math.max(0, el.getBoundingClientRect().top + window.scrollY - 72))
    const max = document.documentElement.scrollHeight - window.innerHeight
    const stops = [...new Set(tops.filter((t) => t > 200 && t < max - 50).map((t) => Math.round(t)))].sort((a, b) => a - b)
    return { stops: [...stops, max], max }
  })
  // timeline: hold, then per stop: travel (ease) + pause
  const hold = page === 'index' ? 3.0 : 1.6
  const pause = 1.0
  const total = Math.min(36, Math.max(20, hold + plan.max / 450 + plan.stops.length * pause))
  const travelTotal = Math.max(6, total - hold - plan.stops.length * pause)
  const pxPerS = plan.max / travelTotal
  const segs = []
  let y = 0
  for (const stop of plan.stops) { const dur = Math.max(0.45, (stop - y) / pxPerS); segs.push({ from: y, to: stop, dur }); y = stop }
  // frame list
  const positions = []
  for (let i = 0; i < Math.round(hold * FPS); i++) positions.push(0)
  for (const s of segs) {
    const n = Math.round(s.dur * FPS)
    for (let i = 1; i <= n; i++) positions.push(s.from + (s.to - s.from) * ease(i / n))
    for (let i = 0; i < Math.round(pause * FPS); i++) positions.push(s.to)
  }
  for (let i = 0; i < Math.round(0.8 * FPS); i++) positions.push(plan.max)

  let t = 0.5
  for (let i = 0; i < positions.length; i++) {
    const yy = positions[i]
    await p.evaluate(async ({ yy, t, hasVideo }) => {
      window.scrollTo(0, yy)
      if (hasVideo && yy < window.innerHeight) {
        const v = document.querySelector('video')
        if (v && v.readyState >= 2) { v.currentTime = t; await new Promise((r) => { const done = () => { v.removeEventListener('seeked', done); r() }; v.addEventListener('seeked', done); setTimeout(r, 120) }) }
      }
      await new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r)))
    }, { yy, t, hasVideo })
    t += 1 / FPS; if (t > 7.9) t = 0.2
    await p.screenshot({ path: path.join(frames, `f${String(i).padStart(4, '0')}.jpg`), type: 'jpeg', quality: 92 })
  }
  await browser.close()
  const mp4 = path.join(outDir, `${page}-${dev}.mp4`)
  execFileSync('ffmpeg', ['-v', 'error', '-y', '-framerate', String(FPS), '-i', path.join(frames, 'f%04d.jpg'), '-c:v', 'libx264', '-preset', 'medium', '-crf', '23', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', '-vf', 'scale=trunc(iw/2)*2:trunc(ih/2)*2', mp4])
  fs.rmSync(frames, { recursive: true, force: true })
  const mb = (fs.statSync(mp4).size / 1048576).toFixed(1)
  console.log(`${path.basename(mp4)}  ${mb} MB  ${(positions.length / FPS).toFixed(1)} s  ${positions.length} frames`)
}

;(async () => {
  const srv = await serve()
  const port = srv.address().port
  for (const page of only) for (const dev of Object.keys(devices)) await record(page, dev, port)
  srv.close()
  fs.rmSync(tmp, { recursive: true, force: true })
})()
