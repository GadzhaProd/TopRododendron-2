// Interaction + contrast verification under the strict CSP server:
// lightbox closes by click/tap and returns focus, cart/prijslijst/product sheet
// return focus, product switcher works in-page, form errors bind to fields, no
// overflow at 360, and pixel-based contrast (5th percentile against white text)
// of the hero text over the video/panel and of the door panels' text.
const { chromium } = require('playwright')
const { serve } = require('./server.cjs')

async function contrastOf(page, selector, label, minRatio = 4.5) {
  // hide the text, screenshot its box, compute contrast of white against each pixel, report the 5th percentile
  await page.$eval(selector, (el) => { document.documentElement.style.scrollBehavior = 'auto'; el.scrollIntoView({ block: 'center' }) }); await page.waitForTimeout(500)
  const box = await page.$eval(selector, (el) => { const r = el.getBoundingClientRect(); return { x: r.x, y: r.y, w: r.width, h: r.height } })
  await page.$eval(selector, (el) => { el.style.visibility = 'hidden' })
  const png = await page.screenshot({ clip: { x: box.x, y: box.y, width: Math.max(1, box.w), height: Math.max(1, box.h) }, type: 'png' })
  await page.$eval(selector, (el) => { el.style.visibility = '' })
  const ratio = await page.evaluate(async (b64) => {
    const im = new Image(); im.src = 'data:image/png;base64,' + b64; await im.decode()
    const c = document.createElement('canvas'); c.width = im.width; c.height = im.height
    const ctx = c.getContext('2d'); ctx.drawImage(im, 0, 0)
    const d = ctx.getImageData(0, 0, c.width, c.height).data
    const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4) }
    const rs = []
    for (let i = 0; i < d.length; i += 16) { const L = 0.2126 * f(d[i]) + 0.7152 * f(d[i + 1]) + 0.0722 * f(d[i + 2]); rs.push(1.05 / (L + 0.05)) }
    rs.sort((a, b) => a - b)
    return rs[Math.floor(rs.length * 0.05)]
  }, png.toString('base64'))
  console.log((ratio >= minRatio ? 'ok   ' : 'FAIL ') + `${label}: 5th-percentile contrast of white text ${ratio.toFixed(2)}:1`)
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
  // --- product sheet on the homepage: opens, adds to cart, Escape returns focus ---
  await p.goto(`${base}/index.html`); await p.waitForTimeout(800)
  await p.evaluate(() => document.querySelector('#planten button')?.scrollIntoView({ block: 'center' })); await p.waitForTimeout(400)
  await p.tap('#planten button >> nth=0'); await p.waitForTimeout(500)
  ok(await p.$('[role="dialog"][aria-labelledby="sheet-title"]') !== null, 'product sheet opened from a card')
  await p.tap('[role="dialog"] button:has-text("In winkelwagen")'); await p.waitForTimeout(300)
  ok((await p.textContent('[role="dialog"]')).includes('Toegevoegd'), 'sheet: added to cart')
  await p.keyboard.press('Escape'); await p.waitForTimeout(400)
  ok(await p.$('[role="dialog"][aria-labelledby="sheet-title"]') === null, 'sheet closed by Escape')
  ok(await p.evaluate(() => document.activeElement?.closest('#planten') !== null), 'sheet focus returned to the card')
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
  // --- contact form errors are bound to fields (homepage, desktop) ---
  // (the C homepage has no form; the retail form lives in the B2B page's offerte section)
  await p.click('form button[type="submit"]'); await p.waitForTimeout(200)
  const inv = await p.$$eval('[aria-invalid="true"]', (els) => els.map((e) => e.getAttribute('aria-describedby')))
  ok(inv.length === 4 && inv.every(Boolean), `offerte errors bound (${inv.length} invalid fields)`)
  ok(await p.evaluate(() => document.activeElement?.getAttribute('name')) === 'bedrijf', 'focus on first invalid field')
  // --- contrast: hero text (split hero = solid panel), doors, phone hero over the video (several frames) ---
  await p.goto(`${base}/index.html`); await p.waitForTimeout(800)
  await contrastOf(p, '#hero .eyebrow', 'hero eyebrow 1440')
  await contrastOf(p, '#hero h1 + p', 'hero lead 1440')
  await contrastOf(p, '[data-door="pro"] .eyebrow', 'door professionals eyebrow 1440')
  await contrastOf(p, '[data-door="pro"] h2 + p', 'door professionals lead 1440')
  await contrastOf(p, '[data-door="tuin"] .eyebrow', 'door tuin eyebrow 1440')
  await contrastOf(p, '[data-door="tuin"] h2 + p', 'door tuin lead 1440')
  await p.close()
  for (const [w, h] of [[390, 844], [360, 640]]) {
    p = await page(w, h)
    await p.goto(`${base}/index.html`); await p.waitForTimeout(800)
    for (const t of [1, 4, 6.5]) {
      await p.evaluate((t) => { const v = document.querySelector('video'); if (v) { v.pause(); v.currentTime = t } }, t); await p.waitForTimeout(400)
      await contrastOf(p, '#hero .eyebrow', `hero eyebrow ${w} t=${t}`)
      if (w >= 390) await contrastOf(p, '#hero h1 + p', `hero lead ${w} t=${t}`)
      await contrastOf(p, '#hero h1', `hero h1 ${w} t=${t}`, 3)
    }
    await contrastOf(p, '[data-door="pro"] .eyebrow', `door professionals eyebrow ${w}`)
    await contrastOf(p, '[data-door="pro"] h2 + p', `door professionals lead ${w}`)
    await p.close()
  }
  await browser.close(); srv.close()
})()
