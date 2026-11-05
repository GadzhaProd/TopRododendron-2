// vite build, then inline the IIFE script and CSS into dist/index.html -> one self-contained file.
import { build } from 'vite'
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
const root = path.dirname(fileURLToPath(import.meta.url))
await build({ root, configFile: path.join(root, 'vite.config.ts'), logLevel: 'warn' })
const dist = path.join(root, 'dist')
let html = fs.readFileSync(path.join(dist, 'index.html'), 'utf8')
let js = ''
html = html.replace(/<script[^>]*src="([^"]+)"[^>]*><\/script>\s*/g, (_, s) => { js += fs.readFileSync(path.join(dist, s), 'utf8'); return '' })
html = html.replace(/<link rel="stylesheet"[^>]*href="(\.\/[^"]+)"[^>]*>\s*/g, (_, h) => `<style>${fs.readFileSync(path.join(dist, h), 'utf8')}</style>\n`)
html = html.replace('</body>', () => '<script>' + js.replace(/<\/script/gi, '<\\/script') + '</script>\n</body>')
fs.rmSync(dist, { recursive: true, force: true }); fs.mkdirSync(dist)
fs.writeFileSync(path.join(dist, 'index.html'), html)
console.log('dist/index.html', (fs.statSync(path.join(dist, 'index.html')).size / 1024).toFixed(0), 'KB')
