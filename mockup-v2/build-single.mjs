// Builds every page as one self-contained HTML file: JS (classic IIFE) and CSS
// are inlined, so no module/CORS requests are needed. Images and videos stay as
// separate files in dist/assets. Used for hosts that block external module scripts.
import { build } from 'vite'
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const root = path.dirname(fileURLToPath(import.meta.url))
const out = path.join(root, 'dist')
const tmp = path.join(root, '.build-tmp')

const pages = [
  { html: 'a/index.html', depth: 1 },
  { html: 'a/groothandel.html', depth: 1 },
  { html: 'b/index.html', depth: 1 },
  { html: 'b/groothandel.html', depth: 1 },
  { html: 'c/index.html', depth: 1 },
  { html: 'c/groothandel.html', depth: 1 },
]

fs.rmSync(out, { recursive: true, force: true })
fs.rmSync(tmp, { recursive: true, force: true })
fs.mkdirSync(path.join(out, 'assets'), { recursive: true })

for (const page of pages) {
  const prefix = '../'.repeat(page.depth)
  const pageTmp = path.join(tmp, page.html.replace(/[/.]/g, '_'))
  await build({
    root,
    configFile: path.join(root, 'vite.config.ts'),
    logLevel: 'warn',
    base: './',
    experimental: {
      // Asset URLs resolve against the page itself (the script is inline).
      renderBuiltUrl: (filename) => prefix + filename,
    },
    build: {
      outDir: pageTmp,
      emptyOutDir: true,
      assetsInlineLimit: 0,
      cssCodeSplit: false,
      modulePreload: false,
      rollupOptions: {
        input: path.join(root, page.html),
        output: { format: 'iife', inlineDynamicImports: true },
      },
    },
  })

  let html = fs.readFileSync(path.join(pageTmp, page.html), 'utf8')
  let js = ''
  html = html.replace(/<script[^>]*src="([^"]+)"[^>]*><\/script>\s*/g, (_, src) => {
    js += fs.readFileSync(path.join(path.dirname(path.join(pageTmp, page.html)), src), 'utf8')
    return ''
  })
  html = html.replace(/<link rel="stylesheet"[^>]*href="(\.\.?\/[^"]+)"[^>]*>\s*/g, (_, href) => {
    const css = fs.readFileSync(path.join(path.dirname(path.join(pageTmp, page.html)), href), 'utf8')
    return `<style>${css}</style>\n`
  })
  html = html.replace(/<link rel="modulepreload"[^>]*>\s*/g, '')
  const safeJs = js.replace(/<\/script/gi, '<\\/script')
  html = html.replace('</body>', `<script>${safeJs}</script>\n</body>`)

  const dest = path.join(out, page.html)
  fs.mkdirSync(path.dirname(dest), { recursive: true })
  fs.writeFileSync(dest, html)

  // Copy media assets (skip js/css — they are inlined).
  const assetsDir = path.join(pageTmp, 'assets')
  if (fs.existsSync(assetsDir)) {
    for (const f of fs.readdirSync(assetsDir)) {
      if (/\.(js|css)$/.test(f)) continue
      fs.copyFileSync(path.join(assetsDir, f), path.join(out, 'assets', f))
    }
  }
  console.log('built', page.html, (fs.statSync(dest).size / 1024).toFixed(0) + ' KB')
}

// Hub page is plain HTML; screenshots it references live in public/shots.
fs.copyFileSync(path.join(root, 'index.html'), path.join(out, 'index.html'))
const shots = path.join(root, 'public', 'shots')
if (fs.existsSync(shots)) fs.cpSync(shots, path.join(out, 'shots'), { recursive: true })
fs.rmSync(tmp, { recursive: true, force: true })
