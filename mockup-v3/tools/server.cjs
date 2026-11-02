// Static server for dist/ with the strict CSP of the artifact viewer and byte
// ranges for video. Shared by check.cjs, states.cjs and previews.cjs.
const http = require('http')
const fs = require('fs')
const path = require('path')

const dist = process.env.DIST || path.join(__dirname, '..', 'dist')
const CSP = "default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com data:; img-src 'self' data: blob:; media-src 'self' blob:"
const types = { '.html': 'text/html; charset=utf-8', '.mp4': 'video/mp4', '.webp': 'image/webp', '.jpg': 'image/jpeg', '.svg': 'image/svg+xml', '.js': 'text/javascript', '.css': 'text/css' }

function serve() {
  return new Promise((resolve) => {
    const srv = http.createServer((req, res) => {
      const url = decodeURIComponent(req.url.split('?')[0].split('#')[0])
      const file = path.join(dist, url === '/' ? 'index.html' : url)
      if (!file.startsWith(dist) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) { res.writeHead(404); res.end('not found'); return }
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
module.exports = { serve, CSP }
