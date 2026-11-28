# Mockup tool (not site code): groothandel-d.html, variant D of the wholesale page: the compact page (owner, 27 Nov:
# variant A reads long and scattered: six blocks of a heading and a few short lines, each in 2 x --sec of air).
# Since 28 Nov (owner: the photo small on desktop, the side-by-side tables foreign, no step-by-step flow) one section after
# the other, each heading over its own content; formerly four bands with two halves each, 1 x --sec between them:
#   1  the head on the light ground: heading, line, the company's truck, the action (owner, 28 Nov) | desktop: photo beside the text
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
# the head (owner, 28 Nov): A's own elements on the page's light ground, the company's truck as the photo (his picture,
# img/gh-truck.webp). Phone: heading, line, photo, then the action and the facts (his order). Desktop: heading, the line with
# the action beside it, then the photo large across the width (owner: "the photo is small on the computer").
HEAD = ('<section class="in gh-head ghd-head" aria-labelledby="h-gh">' + CRUMB + H1 + LEAD
        + '<figure class="gh-photo ghd-photo"><img src="img/gh-truck.webp" alt="Vrachtwagen van Top Rhododendrons op een polderweg" '
          'width="2000" height="1116" fetchpriority="high" decoding="async"></figure>'
        + CTA + '<ul class="gh-facts" aria-label="In het kort">' + ''.join(f'<li>{f}</li>' for f in FACTS) + '</ul></section>')

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
# one section after the other, each heading over its own content (owner, 28 Nov: the two tables side by side, different in
# meaning, looked foreign; the page should read step by step): the six points as a grid of 3 x 2, the four steps in a row
DUO = ('<section class="ghd-band" aria-labelledby="h-get"><div class="in">'
       '<h2 id="h-get">U koopt bij de kweker zelf.</h2>'
       '<dl class="ghd-get">' + ''.join(f'<div><dt>{t}</dt><dd>{d}</dd></div>' for t, d in ROWS) + '</dl></div></section>'
       '<section class="ghd-band" aria-labelledby="h-st"><div class="in">'
       '<h2 id="h-st">Van aanvraag tot levering, in vier stappen.</h2>'
       '<ol class="ghd-steps">' + ''.join(f'<li><h3><span>{k}</span>{t}</h3><p>{p}</p></li>' for k, (t, p) in enumerate(STEPS, 1)) + '</ol>'
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
# the questions as their own section (two stacks of two), then the request: its heading and line over the form card
REQ = ('<section class="ghd-band" aria-labelledby="h-faq"><div class="in">'
       '<h2 id="h-faq">Veelgestelde vragen.</h2>'
       '<div class="gh-faq ghd-faq"><div>' + ''.join(QS[:2]) + '</div><div>' + ''.join(QS[2:]) + '</div></div></div></section>'
       '<section class="ghd-band ghd-req" id="offerte" aria-labelledby="h-req"><div class="in">'
       '<div class="ghd-intro"><h2 id="h-req">Vraag een offerte aan.</h2>'
       '<p class="gh-p">Vertel ons wat u nodig heeft. U krijgt een offerte met de prijs per soort en maat, rechtstreeks van de kwekerij. '
       'Minder dan 25 planten nodig? Die bestelt u <a href="index.html#assortiment">direct via de site</a>. '
       '<span class="gh-tel">Of bel ' + TEL + '.</span></p></div>'
       '<div class="gh-card ghd-formcard">' + FORMBOX.replace('class="gh-r gh-req"', 'class="gh-req"') + '</div>'
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
