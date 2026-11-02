// Screenshots of interactive states (mobile menu, cart drawer, filters, lightbox,
// prijslijst dialog, tuinturf product) under the same strict CSP server.
const path = require('path')
const fs = require('fs')
const { chromium } = require('playwright')
const { serve } = require('./server.cjs')

const out = path.join(__dirname, '..', '.shots', 'states')
fs.mkdirSync(out, { recursive: true })

;(async () => {
  const srv = await serve()
  const base = `http://127.0.0.1:${srv.address().port}`
  const browser = await chromium.launch()
  const shot = async (p, name) => p.screenshot({ path: path.join(out, name + '.png') })
  const ctx = async (w, h) => (await browser.newContext({ viewport: { width: w, height: h }, isMobile: w < 768, hasTouch: w < 768 })).newPage()

  // mobile menu
  let p = await ctx(390, 844)
  await p.goto(`${base}/index.html`); await p.waitForTimeout(1200)
  await p.click('[aria-controls="mobile-menu"]'); await p.waitForTimeout(500); await shot(p, 'menu-390')
  await p.keyboard.press('Escape'); await p.waitForTimeout(300)
  // product: add to cart -> drawer
  await p.goto(`${base}/product.html#nova-zembla`); await p.waitForTimeout(1200)
  await p.click('button[aria-pressed="false"] >> nth=1'); await p.click('text=In winkelwagen'); await p.waitForTimeout(600); await shot(p, 'cart-390')
  await p.keyboard.press('Escape'); await p.waitForTimeout(300)
  await p.goto(`${base}/product.html#tuinturf-substraat`); await p.waitForTimeout(1200); await shot(p, 'turf-390')
  // lightbox
  await p.goto(`${base}/product.html#roseum-elegans`); await p.waitForTimeout(1000)
  await p.click('[aria-label="Foto vergroten"]'); await p.waitForTimeout(500); await shot(p, 'lightbox-390')
  await p.keyboard.press('Escape')
  // assortiment filters
  await p.goto(`${base}/assortiment.html`); await p.waitForTimeout(1000)
  await p.click('button:has-text("Paars")'); await p.click('button:has-text("Schaduw")'); await p.waitForTimeout(500); await shot(p, 'filters-390')
  // groothandel prijslijst
  await p.goto(`${base}/groothandel.html`); await p.waitForTimeout(1000)
  await p.click('text=Prijslijst ontvangen >> nth=0'); await p.waitForTimeout(500); await shot(p, 'prijslijst-390')
  await p.close()

  p = await ctx(1440, 900)
  await p.goto(`${base}/product.html#cunninghams-white`); await p.waitForTimeout(1200)
  await p.click('#turf'); await p.click('text=In winkelwagen'); await p.waitForTimeout(600); await shot(p, 'cart-1440')
  await p.keyboard.press('Escape'); await p.waitForTimeout(300)
  await p.goto(`${base}/product.html#tuinturf-substraat`); await p.waitForTimeout(1000); await shot(p, 'turf-1440')
  await p.goto(`${base}/assortiment.html`); await p.waitForTimeout(1000)
  await p.click('button:has-text("Rood")'); await p.click('button:has-text("Wit")'); await p.waitForTimeout(400); await shot(p, 'filters-1440')
  await p.selectOption('select[aria-label="Sorteren"]', 'prijs'); await p.click('text=Wis filters'); await p.waitForTimeout(400); await shot(p, 'sort-1440')
  await p.goto(`${base}/groothandel.html`); await p.waitForTimeout(1000)
  await p.click('text=Prijslijst ontvangen >> nth=0'); await p.waitForTimeout(500); await shot(p, 'prijslijst-1440')
  await p.keyboard.press('Escape')
  await p.goto(`${base}/plantgids.html`); await p.waitForTimeout(1000)
  await p.click('th button:has-text("Hoogte")'); await p.waitForTimeout(300); await p.evaluate(() => document.getElementById('vergelijken').scrollIntoView()); await p.waitForTimeout(400); await shot(p, 'sort-table-1440')
  await p.close()

  // tablet + small phone key views
  for (const [w, h] of [[768, 1024], [360, 640], [1024, 768]]) {
    p = await ctx(w, h)
    for (const page of ['index', 'groothandel', 'plantgids']) {
      await p.goto(`${base}/${page}.html`); await p.waitForTimeout(1200); await shot(p, `${page}-${w}-top`)
      await p.evaluate(() => window.scrollTo(0, document.documentElement.scrollHeight * 0.35)); await p.waitForTimeout(400); await shot(p, `${page}-${w}-mid`)
    }
    await p.close()
  }
  await browser.close(); srv.close()
  console.log('states saved to', out)
})()
