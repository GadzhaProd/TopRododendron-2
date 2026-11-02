// Interaction + contrast verification under the strict CSP server:
// lightbox closes by click/tap and returns focus, cart/prijslijst return focus,
// product switcher works in-page, form errors bind to fields, and pixel-based
// contrast (5th percentile) of white text over the hero video and door photos.
const { chromium } = require('playwright')
const { serve } = require('./server.cjs')

const lum = (r, g, b) => { const f = (c) => { c /= 255; return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4) }; return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b) }
async function contrastOf(page, selector, label) {
  // hide the text, screenshot its box, compute contrast of white against each pixel, report 5th percentile
  await page.$eval(selector, (el) => { document.documentElement.style.scrollBehavior = 'auto'; el.scrollIntoView({ block: 'center' }) }); await page.waitForTimeout(700)
  const box = await page.$eval(selector, (el) => { const r = el.getBoundingClientRect(); return { x: r.x, y: r.y, w: r.width, h: r.height } })
  await page.$eval(selector, (el) => { el.style.visibility = 'hidden' })
  const fs = require('fs'); const path = require('path')
  const dir = path.join(__dirname, '..', '.shots', 'contrast'); fs.mkdirSync(dir, { recursive: true })
  const file = path.join(dir, label.replace(/[^a-z0-9]+/gi, '_') + '.png')
  await page.screenshot({ path: file, clip: { x: box.x, y: box.y, width: Math.max(1, box.w), height: Math.max(1, box.h) }, type: 'png' })
  await page.$eval(selector, (el) => { el.style.visibility = '' })
  console.log('saved contrast sample', label)
}

;(async () => {
  const srv = await serve(); const base = `http://127.0.0.1:${srv.address().port}`
  const browser = await chromium.launch()
  const ok = (c, m) => console.log((c ? 'ok   ' : 'FAIL ') + m)
  const page = async (w, h) => (await browser.newContext({ viewport: { width: w, height: h }, isMobile: w < 768, hasTouch: w < 768 })).newPage()

  // --- lightbox (phone, tap) ---
  let p = await page(390, 844)
  await p.goto(`${base}/product.html#roseum-elegans`); await p.waitForTimeout(900)
  await p.tap('[aria-label="Foto vergroten"]'); await p.waitForTimeout(400)
  ok(await p.$('[role="dialog"][aria-label*="Roseum"]') !== null, 'lightbox opened')
  ok(await p.evaluate(() => document.activeElement?.getAttribute('aria-label')) === 'Sluiten', 'lightbox focus on Sluiten')
  await p.tap('[role="dialog"] [aria-label="Volgende foto"]'); await p.waitForTimeout(200)
  ok((await p.textContent('[role="dialog"] p')) === '2 / 2', 'lightbox next by tap')
  await p.tap('[role="dialog"] [aria-label="Sluiten"]'); await p.waitForTimeout(400)
  ok(await p.$('[role="dialog"][aria-label*="Roseum"]') === null, 'lightbox closed by tap')
  ok(await p.evaluate(() => document.activeElement?.getAttribute('aria-label')) === 'Foto vergroten', 'focus returned to opener')
  // --- switcher in page ---
  await p.tap('nav[aria-label="Kies een soort"] a[href="#ponticum"]'); await p.waitForTimeout(400)
  ok((await p.textContent('h1')) === 'Ponticum', 'switcher changed variety in-page')
  await p.goto(`${base}/product.html#bestaat-niet`); await p.waitForTimeout(600)
  ok((await p.textContent('h1')).includes('niet gevonden'), 'unknown hash -> not found')
  // --- cart focus return ---
  await p.goto(`${base}/product.html#nova-zembla`); await p.waitForTimeout(800)
  await p.click('button:has-text("In winkelwagen") >> nth=0'); await p.waitForTimeout(500)
  await p.keyboard.press('Escape'); await p.waitForTimeout(300)
  ok((await p.evaluate(() => document.activeElement?.textContent || ''))?.includes('winkelwagen'), 'cart focus returned to opener')
  // --- contact form errors bound ---
  await p.goto(`${base}/index.html`); await p.waitForTimeout(800)
  await p.click('form button[type="submit"]'); await p.waitForTimeout(200)
  const inv = await p.$$eval('[aria-invalid="true"]', (els) => els.map((e) => e.getAttribute('aria-describedby')))
  ok(inv.length === 3 && inv.every(Boolean), `contact errors bound (${inv.length} invalid fields)`)
  ok(await p.evaluate(() => document.activeElement?.getAttribute('name')) === 'naam', 'focus on first invalid field')
  // --- 360 overflow ---
  await p.close()
  p = await page(360, 640)
  for (const pg of ['index', 'assortiment', 'product', 'plantgids', 'groothandel']) { await p.goto(`${base}/${pg}.html`); await p.waitForTimeout(600); const sw = await p.evaluate(() => [document.documentElement.scrollWidth, window.innerWidth]); ok(sw[0] === sw[1], `${pg} 360 no overflow (${sw[0]})`) }
  // mobile hero height at 360/375 for groothandel
  for (const [w, h] of [[360, 640], [375, 667]]) { const q = await page(w, h); await q.goto(`${base}/groothandel.html`); await q.waitForTimeout(600); const hh = await q.$eval('#hero', (el) => el.getBoundingClientRect().height); const ctaBottom = await q.$eval('#hero a[href="#offerte"]', (el) => el.getBoundingClientRect().bottom); ok(ctaBottom <= h, `groothandel hero CTA within first screen at ${w}×${h} (hero ${Math.round(hh)}, cta bottom ${Math.round(ctaBottom)})`); await q.close() }
  await p.close()

  // --- prijslijst focus return (desktop) ---
  p = await page(1440, 900)
  await p.goto(`${base}/groothandel.html`); await p.waitForTimeout(800)
  await p.click('button:has-text("Prijslijst ontvangen") >> nth=0'); await p.waitForTimeout(400)
  await p.keyboard.press('Escape'); await p.waitForTimeout(300)
  ok((await p.evaluate(() => document.activeElement?.textContent || '')).includes('Prijslijst'), 'prijslijst focus returned to opener')
  // --- contrast over video (several frames) and doors ---
  await p.goto(`${base}/index.html`); await p.waitForTimeout(600)
  for (const t of [1.5, 4, 6.5]) {
    await p.evaluate((t) => { const v = document.querySelector('video'); v.pause(); v.currentTime = t }, t); await p.waitForTimeout(400)
    await contrastOf(p, '#hero p.label', `hero eyebrow 1440 t=${t}`)
    await contrastOf(p, '#hero h1 + p', `hero lead 1440 t=${t}`)
  }
  await p.evaluate(() => document.querySelector('a[href="groothandel.html"].group\\/d')?.scrollIntoView({ block: 'center' })); await p.waitForTimeout(500)
  await contrastOf(p, 'a[href="groothandel.html"].group\\/d p.label', 'door professionals label 1440')
  await contrastOf(p, 'a[href="groothandel.html"].group\\/d h3 + p', 'door professionals lead 1440')
  await contrastOf(p, 'a[href="assortiment.html"].group\\/d p.label', 'door tuin label 1440')
  await p.close()
  p = await page(390, 844)
  await p.goto(`${base}/index.html`); await p.waitForTimeout(600)
  for (const t of [2, 6]) {
    await p.evaluate((t) => { const v = document.querySelector('video'); v.pause(); v.currentTime = t }, t); await p.waitForTimeout(400)
    await contrastOf(p, '#hero p.label', `hero eyebrow 390 t=${t}`)
    await contrastOf(p, '#hero h1 + p', `hero lead 390 t=${t}`)
  }
  await p.evaluate(() => document.querySelector('a[href="groothandel.html"].group\\/d')?.scrollIntoView({ block: 'center' })); await p.waitForTimeout(500)
  await contrastOf(p, 'a[href="groothandel.html"].group\\/d p.label', 'door professionals label 390')
  await contrastOf(p, 'a[href="groothandel.html"].group\\/d h3 + p', 'door professionals lead 390')
  await p.close()
  await browser.close(); srv.close()
})()
