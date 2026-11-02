// Builds every page as ONE self-contained HTML file: the JS bundle (classic IIFE)
// and the CSS are inlined, so no module/CORS requests are needed. Images and
// videos stay as separate files in dist/assets, referenced as "assets/..." from
// every page (all pages live flat in dist/). This is what the claude.ai artifact
// viewer on a phone can show: inline scripts + Google Fonts only, media relative.
import { build } from 'vite'
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const root = path.dirname(fileURLToPath(import.meta.url))
const out = path.join(root, 'dist')
const tmp = path.join(root, '.build-tmp')

const pages = ['index.html', 'assortiment.html', 'product.html', 'plantgids.html', 'groothandel.html']

fs.rmSync(out, { recursive: true, force: true })
fs.rmSync(tmp, { recursive: true, force: true })
fs.mkdirSync(path.join(out, 'assets'), { recursive: true })

for (const page of pages) {
  const pageTmp = path.join(tmp, page.replace(/[/.]/g, '_'))
  await build({
    root,
    configFile: path.join(root, 'vite.config.ts'),
    logLevel: 'warn',
    base: './',
    experimental: {
      // Asset URLs resolve against the page itself (the script is inline).
      renderBuiltUrl: (filename) => filename,
    },
    build: {
      outDir: pageTmp,
      emptyOutDir: true,
      assetsInlineLimit: 0,
      cssCodeSplit: false,
      modulePreload: false,
      rollupOptions: {
        input: path.join(root, page),
        output: { format: 'iife', inlineDynamicImports: true },
      },
    },
  })

  let html = fs.readFileSync(path.join(pageTmp, page), 'utf8')
  let js = ''
  html = html.replace(/<script[^>]*src="([^"]+)"[^>]*><\/script>\s*/g, (_, src) => {
    js += fs.readFileSync(path.join(pageTmp, src), 'utf8')
    return ''
  })
  html = html.replace(/<link rel="stylesheet"[^>]*href="(\.?\/?assets\/[^"]+)"[^>]*>\s*/g, (_, href) => {
    const css = fs.readFileSync(path.join(pageTmp, href), 'utf8')
    return `<style>${css}</style>\n`
  })
  html = html.replace(/<link rel="modulepreload"[^>]*>\s*/g, '')
  html = html.replace(/crossorigin\s*/g, '')
  const safeJs = js.replace(/<\/script/gi, '<\\/script')
  html = html.replace('</body>', `<script>${safeJs}</script>\n</body>`)

  const dest = path.join(out, page)
  fs.writeFileSync(dest, html)

  // Copy media assets (skip js/css — they are inlined).
  const assetsDir = path.join(pageTmp, 'assets')
  if (fs.existsSync(assetsDir)) {
    for (const f of fs.readdirSync(assetsDir)) {
      if (/\.(js|css)$/.test(f)) continue
      fs.copyFileSync(path.join(assetsDir, f), path.join(out, 'assets', f))
    }
  }
  console.log('built', page, (fs.statSync(dest).size / 1024).toFixed(0) + ' KB')
}

// Public extras (og image, logo.svg) next to the pages.
const pub = path.join(root, 'public')
if (fs.existsSync(pub)) fs.cpSync(pub, out, { recursive: true })
fs.rmSync(tmp, { recursive: true, force: true })

// Sanity: no "../" asset references and every referenced asset exists.
for (const page of pages) {
  const html = fs.readFileSync(path.join(out, page), 'utf8')
  const refs = [...html.matchAll(/["'(](assets\/[^"')\s]+)["')]/g)].map((m) => m[1])
  const up = [...html.matchAll(/(?:src|href|poster|content)="(\.\.\/[^"]+)"/g)].map((m) => m[1])
  const bad = [...up, ...refs.filter((r) => !fs.existsSync(path.join(out, r)))]
  if (bad.length) { console.error('BROKEN asset refs in', page, [...new Set(bad)]); process.exitCode = 1 }
}
