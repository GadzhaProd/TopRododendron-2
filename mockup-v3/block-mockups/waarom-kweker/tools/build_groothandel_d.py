# Mockup tool (not site code): groothandel-d.html, variant D of the wholesale page: the compact page (owner, 27 Nov:
# variant A reads long and scattered: six blocks of a heading and a few short lines, each in 2 x --sec of air).
# Four bands, each filling both sides by itself, 1 x --sec between them:
#   1  the head as the homepage's hero: the company's truck full-bleed, text and the white pill on it (owner, 28 Nov)
#   2  "U koopt bij de kweker zelf." six rows     | "Van aanvraag tot levering, in vier stappen." four rows (one table, two halves)
#   3  "Zeven soorten rhododendrons, van 40 tot 225 cm.": the seven in a row; the large sizes and "Alle maten en prijzen" in one row
#   4  "Vraag een offerte aan.": the intro and the four questions | the form card
# Copy: docs/groothandel-tekst-2026-11-26.md; no new facts (docs/b2b-besluiten-2026-11-26.md). Left out, because said elsewhere on
# the page: the seven names in the varieties paragraph (they are the photo captions) and three of the head's five facts
# ("7 soorten" and "40 tot 225 cm" are the varieties heading, "met kluit" is in the line above the button).
# It reuses the existing build: header, cart, phone menu, footer, variant A's styles, form and form script are taken from the
# built groothandel.html (tools/build_groothandel.py from index.html; neither file is touched). Styles: tools/groothandel_d.css.
# Kept from groothandel-a-foto.html: the photo-first head, the bottom bar under 1024 px, the form fix (an error line clears
# while typing), the 46 px crumb.
# Usage: python3 tools/build_groothandel.py && python3 tools/build_groothandel_d.py [dir]
import pathlib, re, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'groothandel.html').read_text()
i = s.index('<main id="main"'); j = s.index('</main>') + len('</main>')
head, old, tail = s[:i], s[i:j], s[j:]


def part(pat):
    x = re.search(pat, old, flags=re.S); assert x, pat; return x.group(0)


ARROW = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" '
         'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')
TEL = '<a href="tel:+31620104312">06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</a>'

# ---------- 1. the head: A's own elements; the facts line keeps what the page says nowhere else ----------
CRUMB = part(r'<nav class="gh-crumb".*?</nav>')
H1 = part(r'<h1 id="h-gh">.*?</h1>')
LEAD = part(r'<p class="gh-lead">.*?</p>')
CTA = part(r'<div class="gh-cta">.*?</div>').replace('class="gh-cta"', 'class="gh-cta ghd-cta"')
FACTS = ['Sinds 2001', '10.000 planten op voorraad']
for f in FACTS: assert f in old, f
# the head as the homepage's hero (owner, 28 Nov: "make the head like on the main page", with his own picture of the
# company's truck, img/gh-truck.webp): the photo full-bleed under the header, the text bottom-left on a soft scrim, the white
# pill and a text link. The homepage's own markup and classes, so its hero styles (Tailwind, hero-bottom-left, fase1b) apply.
# Its "Bestellen" logic looks for the homepage button (href="#assortiment"); without it the header button simply shows.
# the homepage H1 sets its lines by nowrap groups (.h1-g) in a flex row that is as wide as its widest group, so a lone word
# would stand on its own line; here four groups: "Groothandel in / rhododendrons. / Rechtstreeks van / de kweker."
def group(ws):
    return '<span class="h1-g">' + ''.join(f'<span class="inline-block" style="margin-right:{0 if k == len(ws) - 1 else .26}em">{w}</span>' for k, w in enumerate(ws)) + '</span>'
H1_IN = (group(['Groothandel', 'in']) + group(['rhododendrons.']) + '<span class="h1-br" aria-hidden="true"></span>'
         + group(['Rechtstreeks', 'van']) + group(['de', 'kweker.']))
ARR_W = ('<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
         'stroke-linecap="round" stroke-linejoin="round" class="size-4 transition-transform duration-300 group-hover/btn:translate-x-1" aria-hidden="true">'
         '<path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>')
HEAD = ('<section id="hero" class="relative flex min-h-[100svh] w-full flex-col justify-end overflow-hidden bg-black text-white on-dark tabp:justify-start split:justify-center ghd-hero" aria-labelledby="h-gh">'
        '<div class="absolute inset-0"><img src="img/gh-truck.webp" alt="Vrachtwagen van Top Rhododendrons op een polderweg" width="2000" height="1116" '
        'fetchpriority="high" decoding="async" class="absolute inset-0 h-full w-full object-cover ghd-hero-img">'
        '<div class="pointer-events-none absolute inset-0 bg-black/10 split:hidden sc-veil"></div>'
        '<div aria-hidden="true" class="hero-scrim hero-scrim-photo pointer-events-none absolute inset-0 hidden split:block"></div>'
        '<div class="pointer-events-none absolute inset-x-0 bottom-0 bg-gradient-to-t to-transparent tabp:hidden split:hidden h-[68%] from-black/90 via-black/72 sc-phone"></div>'
        '<div class="pointer-events-none absolute inset-x-0 top-0 hidden h-[62%] bg-gradient-to-b from-black/80 via-black/45 to-transparent tabp:block sc-tab"></div></div>'
        '<div class="relative w-full container-x pt-28 pb-7 shortphone:pb-5 tabp:pt-32 split:py-28">'
        '<div class="flex max-w-4xl flex-col items-start gap-3 md:gap-5 tabp:max-w-[21.5rem] split:max-w-[36rem]">'
        '<h1 id="h-gh" class="font-display text-balance text-[clamp(30px,8.4vw,38px)] font-medium leading-[0.98] tracking-[-0.04em] tabp:text-[36px] split:text-[clamp(38px,4.6vw,72px)]">'
        '<span class="inline-flex flex-wrap">' + H1_IN + '</span></h1>'
        '<p class="max-w-xl text-[15px] leading-relaxed text-white/90 shortphone:hidden md:text-lg split:text-[17px]">Voor hoveniers, tuinarchitecten, gemeenten '
        'en projectontwikkelaars: rhododendrons per partij, <span class="nb">vers gerooid</span> en met kluit.</p>'
        '<div class="mt-1 flex flex-wrap items-center gap-3 ghd-cta">'
        '<a class="inline-flex items-center justify-center gap-2 whitespace-nowrap font-medium transition-all duration-300 select-none bg-white text-[#141414] hover:bg-white/90 h-12 text-[14px] rounded-ui group/btn px-5 split:h-14 split:px-8 split:text-[15px]" href="#offerte">Vraag een offerte aan' + ARR_W + '</a>'
        '<a class="hero-link" href="tel:+31620104312"><span>Bel 06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</span></a></div>'
        '<p class="ghd-hero-facts">Sinds 2001 · 10.000 planten op voorraad</p>'
        '</div></div></section>')

# ---------- 2. what you get | how it works ----------
ROWS = [('Partij', 'Vanaf 25 planten krijgt u een partijprijs. Hoe groter de partij, hoe lager de prijs per plant.'),
        ('Rooien', 'Pas vlak voor de levering, met kluit.'),
        ('Bezorgen', 'Met eigen transport door heel Nederland, vanaf €&nbsp;75 per bestelling.'),
        ('Afhalen', 'Gratis, op ons veld in Wekerom.'),
        ('Betalen', 'Zakelijk op factuur.'),
        ('Plantenpaspoort', 'Bij elke partij.')]
STEPS = [('Aanvragen', 'U stuurt ons de soorten, maten en aantallen, en de week waarin u de planten nodig heeft.'),
         ('Offerte', 'U krijgt binnen één werkdag een offerte met de prijs per soort en maat, exclusief btw.'),
         ('Afspreken', 'Na uw akkoord kiezen wij samen de dag van bezorgen of afhalen.'),
         ('Ontvangen', 'Wij rooien vlak voor de levering. U krijgt de planten bezorgd, of u haalt ze af in Wekerom.')]
DUO = ('<section class="ghd-band" aria-label="Wat u krijgt en hoe het werkt"><div class="in ghd-duo">'
       '<h2 id="h-get">U koopt bij de kweker zelf.</h2>'
       '<dl class="ghd-rows ghd-get" aria-labelledby="h-get">' + ''.join(f'<div><dt>{t}</dt><dd>{d}</dd></div>' for t, d in ROWS) + '</dl>'
       '<h2 id="h-st">Van aanvraag tot levering, in vier stappen.</h2>'
       '<ol class="ghd-rows ghd-steps" aria-labelledby="h-st">' + ''.join(f'<li><h3>{t}</h3><p>{p}</p></li>' for t, p in STEPS) + '</ol>'
       '</div></section>')

# ---------- 3. the varieties: the names once, as the photo captions ----------
SORTS = [('nova-zembla', 'Nova Zembla'), ('catawbiense-grandiflorum', 'Catawbiense Grandiflorum'), ('cunninghams-white', 'Cunningham’s White'),
         ('catawbiense-boursault', 'Catawbiense Boursault'), ('roseum-elegans', 'Roseum Elegans'), ('ponticum', 'Ponticum'),
         ('ponticum-roseum', 'Ponticum Roseum')]
ALL = 'Alle maten en prijzen'
SORTS_UL = ('<ul class="ghd-sorts" aria-label="De zeven soorten">' + ''.join(
    f'<li><a href="soort-{sl}.html"><img src="img/{sl}-sm.webp" alt="" width="900" height="900" loading="lazy" decoding="async"><span>{n}</span></a></li>'
    for sl, n in SORTS)
    # under 700 px the list is two columns; its eighth cell is the link to all sizes (the link in the row below is hidden there)
    + f'<li class="ghd-all"><a href="index.html#assortiment"><span>{ALL}</span>{ARROW}</a></li></ul>')
VAR = ('<section class="ghd-band" aria-labelledby="h-var"><div class="in">'
       '<div class="ghd-var-top"><h2 id="h-var"><span>Zeven soorten rhododendrons,</span> <span>van 40 tot 225&nbsp;cm.</span></h2>'
       '<p>Alle planten groeien in de volle grond en wij leveren ze met kluit. Welke maten er zijn, verschilt per soort.</p></div>'
       + SORTS_UL +
       '<div class="ghd-big"><h3>Grote maten</h3><p>Voor projecten die meteen volume vragen, hebben wij ook grote maten, '
       'van 120 tot 225&nbsp;cm. Die leveren wij op aanvraag. U kunt ze zelf uitzoeken op ons veld.</p>'
       f'<p class="gh-more"><a href="index.html#assortiment">{ALL}{ARROW}</a></p></div>'
       '</div></section>')

# ---------- 4. the request: the intro and the questions left, A's form in the card right ----------
FORMBOX = part(r'<div class="gh-r gh-req">.*?</form><div class="gh-done".*?</div></div>')
QS = re.findall(r'<details>.*?</details>', part(r'<div class="gh-r gh-faq">.*?</div>'), flags=re.S)
assert len(QS) == 4
REQ = ('<section class="ghd-band ghd-req" id="offerte" aria-labelledby="h-req"><div class="in ghd-ask">'
       '<div class="ghd-intro"><h2 id="h-req">Vraag een offerte aan.</h2>'
       '<p class="gh-p">Vertel ons wat u nodig heeft. U krijgt een offerte met de prijs per soort en maat, rechtstreeks van de kwekerij. '
       'Minder dan 25 planten nodig? Die bestelt u <a href="index.html#assortiment">direct via de site</a>.</p>'
       '<p class="gh-tel">Of bel ' + TEL + '</p></div>'
       '<div class="gh-card ghd-formcard">' + FORMBOX.replace('class="gh-r gh-req"', 'class="gh-req"') + '</div>'
       '<div class="ghd-qa"><h3 id="h-faq">Veelgestelde vragen.</h3><div class="gh-faq">' + ''.join(QS) + '</div></div>'
       '</div></section>')

BAR = '<div class="ghd-bar" data-off><div class="ghd-bar-in"><a class="gh-btn" href="#offerte">Vraag een offerte aan' + ARROW + '</a></div></div>'

JS = r'''<script id="groothandel-d-js">(function(){
var bar=document.querySelector('.ghd-bar'),cta=document.querySelector('.ghd-cta'),box=document.querySelector('.gh-req'),card=document.querySelector('.ghd-formcard');
if(!bar||!cta||!box||!card)return;var f=box.querySelector('form'),tick=false;
/* the bar: shown once the head's button has left the screen, gone from the form card on (the questions and the footer follow it) */
function show(){tick=false;var on=cta.getBoundingClientRect().bottom<64&&card.getBoundingClientRect().top>window.innerHeight+8&&!box.classList.contains('gh-sent');
 if(on)bar.removeAttribute('data-off');else bar.setAttribute('data-off','')}
function q(){if(!tick){tick=true;requestAnimationFrame(show)}}
window.addEventListener('scroll',q,{passive:true});window.addEventListener('resize',q);show();
/* from 1024 px the first two questions (seeing the plants first, the guarantee on a batch) start open beside the form, so the
   column is as tall as the form card; on the phone all four stay closed */
if(window.matchMedia('(min-width:1024px)').matches)[].slice.call(document.querySelectorAll('.ghd-qa details'),0,2).forEach(function(d){d.open=true});
/* the form: an error line clears while typing, so the form does not jump under the next tap */
['bedrijf','naam','email','soorten'].forEach(function(k){var el=f.elements[k];el.addEventListener('input',function(){
 if(el.getAttribute('aria-invalid')!=='true')return;var v=el.value.trim(),ok=k==='email'?/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v):v.length>0;
 if(ok){el.setAttribute('aria-invalid','false');var e=document.getElementById('e-'+k);if(e)e.textContent=''}})});
})();</script>'''

MAIN = '<main id="main" tabindex="-1" class="ghm ghd">' + HEAD + DUO + VAR + REQ + BAR + '</main>'
s = head + MAIN + tail


def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:70]); s = s.replace(a, b)


rep('</head>', '<style id="groothandel-d-css">' + (D / 'tools' / 'groothandel_d.css').read_text() + '</style></head>')
rep('</body>', JS + '</body>')
rep('href="groothandel.html" aria-current="page"', 'href="groothandel-d.html" aria-current="page"', s.count('href="groothandel.html" aria-current="page"'))
assert 'gen/veld-L2' not in MAIN
(D / 'groothandel-d.html').write_text(s)
print('ok', len(s))
