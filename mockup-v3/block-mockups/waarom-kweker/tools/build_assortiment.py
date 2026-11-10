# Mockup tool (not site code): assortiment.html = the main mockup (index.html) with the homepage ASSORTIMENT block
# in place of the ".between" placeholder (after Waarom wij, before the founder block). Three variants, switched by
# html.as-1/2/3 from the review bar:
#   1 · Ряд      the seven plants stand in one row like in the field: seven tall photos, the one under the cursor
#                opens and shows its four sizes with prices (pattern: 21st "Hover Expand Gallery", id 27010).
#                Below 1200 px / on touch: a swipe row, every card complete, the next one peeks.
#   2 · Палитра  one soft-gradient card (the «Поле» palette + grain): seven round flower close-ups are the palette,
#                the chosen variety is shown large with its facts and four accented prices; the card picks up a
#                tint of the chosen flower.
#   3 · Подбор   the 3-question picker (standplaats / hoogte / kleur) in a tall «Поле» card, next to a typographic
#                list of all seven with photo and price (pattern: 21st "Index List Image Gallery", id 36226, without
#                the numbering). Answers filter on standplaatsFilter / hoogteFilter / kleurFilter from content.ts.
# All plant data is read from ../../src/data/content.ts (mirror of the live site's lib/products.ts); nothing is typed in here.
# Photos are copied from ../../src/assets/img (the -sm versions) into img/. Nothing else on the page is changed.
# Usage: python3 tools/build_assortiment.py [dir]
import re, pathlib, sys, shutil, html

D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
SRC = D.parent.parent / 'src'
s = (D / 'index.html').read_text()


def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70])
    s = s.replace(a, b)


# ---------- data: parsed from content.ts ----------
ts = (SRC / 'data' / 'content.ts').read_text()
size_sets = {m.group(1): re.findall(r"label: '([^']+)', price: '([^']+)'", m.group(2))
             for m in re.finditer(r"const (sizes[A-Z]): Size\[\] = (\[.*?\])\n", ts)}
vblock = ts[ts.index('export const varieties'):ts.index('export const bySlug')]


def field(o, k):
    m = re.search(k + r""": (?:'((?:[^'\\]|\\.)*)'|"((?:[^"\\]|\\.)*)")""", o)
    assert m, k
    return (m.group(1) if m.group(1) is not None else m.group(2)).replace("\\'", "'")


def arr(o, k):
    return re.findall(r"'([^']+)'", re.search(k + r': \[([^\]]*)\]', o).group(1))


V = []
for o in re.findall(r"\{\s*slug: .*?\n  \},", vblock, re.S):
    m = re.search(r'sizes: (sizes[A-Z])', o)
    sizes = size_sets[m.group(1)] if m else re.findall(r"label: '([^']+)', price: '([^']+)'", o[o.index('sizes:'):])
    V.append(dict(slug=field(o, 'slug'), name=field(o, 'name'), color=field(o, 'color'), hex=field(o, 'hex'), bloei=field(o, 'bloei'),
                  stand=field(o, 'standplaats'), standF=arr(o, 'standplaatsFilter'), kleurF=arr(o, 'kleurFilter'), hoogte=field(o, 'hoogte'),
                  hoogteF=field(o, 'hoogteFilter'), frm=field(o, 'from'), short=field(o, 'short'), sizes=sizes))
assert [v['name'] for v in V] == ['Nova Zembla', "Cunningham's White", 'Roseum Elegans', 'Catawbiense Boursault', 'Catawbiense Grandiflorum',
                                  'Ponticum Roseum', 'Ponticum']
assert [v['frm'] for v in V] == ['29', '25', '27', '27', '29', '22', '22']
for v in V:
    assert [l for l, _ in v['sizes']] == ['40–60 cm', '60–80 cm', '80–100 cm', '100–120 cm'] and v['sizes'][0][1] == v['frm'] + ',00', v['name']

# ---------- photos ----------
for v in V:
    for suf in ('-sm', '-2-sm'):
        dst = D / 'img' / (v['slug'] + suf + '.webp')
        if not dst.exists():
            shutil.copyfile(SRC / 'assets' / 'img' / dst.name, dst)

e = html.escape
eur = lambda p: '€&nbsp;' + (p[:-3] if p.endswith(',00') else p)
low = lambda t: t[0].lower() + t[1:]
bloei = lambda v: v['bloei'].lower()
ARW = '<svg class="as-arw" viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'


def sz(v, cls=''):
    return '<ul class="as-sz' + cls + '" aria-label="Maten en prijzen">' + ''.join(
        '<li><span>' + l.replace(' ', '&nbsp;') + '</span><b>' + eur(p) + '</b></li>' for l, p in v['sizes']) + '</ul>'


def head(n, h, lead):
    return ('<div class="as-head"><div><h2 class="as-h" id="h-as' + n + '">' + h + '</h2><p class="as-lead">' + lead + '</p></div>'
            '<a class="as-all" href="#assortiment">Bekijk alle planten' + ARW + '</a></div>')


LEAD = 'Elke soort in vier maten, van 40 tot 120&nbsp;cm. De vanaf-prijs geldt voor 40–60&nbsp;cm, per plant met kluit.'

# ---------- 1 · Ряд ----------
it1 = ''
for i, v in enumerate(V):
    it1 += ('<li class="as1-it as1-' + v['slug'] + (' on' if i == 0 else '') + '"><a class="as1-a" href="#assortiment" aria-label="' + e(v['name']) + ', vanaf € ' + v['frm'] + '">'
            '<div class="as1-ph"><img src="img/' + v['slug'] + '-2-sm.webp" alt="' + e(v['name']) + ', ' + e(low(v['color'])) + ' bloeiende struik" loading="lazy"></div>'
            '<div class="as1-cap"><h3>' + e(v['name']) + '</h3><p>vanaf <b>' + eur(v['frm']) + '</b></p></div>'
            '<div class="as1-ov"><p class="as1-n">' + e(v['name']) + '</p><p class="as1-m">' + e(v['color']) + '&nbsp;<i class="as-sep">·</i> <span class="nb">bloeit ' + bloei(v) + '</span></p>'
            '<p class="as1-m">' + e(v['stand']) + '&nbsp;<i class="as-sep">·</i> <span class="nb">' + e(v['hoogte']) + ' hoog</span></p>' + sz(v) +
            '<span class="as1-go">Bekijk ' + e(v['name']) + ARW + '</span></div></a></li>')
S1 = ('<section class="as as-s1" aria-labelledby="h-as1"><div class="in">' + head('1', 'Kies uw rhododendron.', LEAD) +
      '<ul class="as1-row">' + it1 + '</ul></div></section>')

# ---------- 2 · Палитра ----------
tabs = panels = ''
for i, v in enumerate(V):
    tabs += ('<button type="button" class="as2-t' + (' on' if i == 0 else '') + '" role="tab" id="as2-t' + str(i) + '" aria-controls="as2-p' + str(i) + '" aria-selected="' +
             ('true' if i == 0 else 'false') + '" data-hex="' + v['hex'] + '"><span class="as2-c"><img src="img/' + v['slug'] + '-sm.webp" alt="" loading="lazy"></span>'
             '<span class="as2-n">' + e(v['name']) + '</span><span class="as2-p">vanaf ' + eur(v['frm']) + '</span></button>')
    panels += ('<article class="as2-pn' + (' on' if i == 0 else '') + '" role="tabpanel" id="as2-p' + str(i) + '" aria-labelledby="as2-t' + str(i) + '">'
               '<div class="as2-ph"><img src="img/' + v['slug'] + '-2-sm.webp" alt="' + e(v['name']) + ', ' + e(low(v['color'])) + ' bloeiende struik" loading="lazy"></div>'
               '<div class="as2-tx"><h3>' + e(v['name']) + '</h3><p class="as2-sh">' + e(v['short']) + '</p>'
               '<dl class="as2-f"><div><dt>Kleur</dt><dd>' + e(v['color']) + '</dd></div><div><dt>Bloei</dt><dd>' + e(v['bloei']) + '</dd></div>'
               '<div><dt>Standplaats</dt><dd>' + e(v['stand']) + '</dd></div><div><dt>Hoogte</dt><dd>' + e(v['hoogte']) + '</dd></div></dl>' +
               sz(v, ' as-sz-l') + '<div class="as2-cta"><a class="as-btn" href="#assortiment">Bekijk ' + e(v['name']) + ARW + '</a>'
               '<span>Prijs per plant, met kluit</span></div></div></article>')
S2 = ('<section class="as as-s2" aria-labelledby="h-as2"><div class="in">' + head('2', 'Kies uw rhododendron.', LEAD) +
      '<div class="as2-card" style="--fl:' + V[0]['hex'] + '"><div class="as2-bg"></div><div class="wh-grain"></div>'
      '<div class="as2-tabs" role="tablist" aria-label="Soorten">' + tabs + '</div><div class="as2-pns">' + panels + '</div></div></div></section>')

# ---------- 3 · Подбор ----------
KLEUR = {'Rood': '#b9293d', 'Wit': '#f6f2ea', 'Roze': '#d9679a', 'Paars': '#8a62b8'}
Q = [('st', 'Hoeveel zon krijgt de plek?', [('Volle zon', 'Zon'), ('Halfschaduw', 'Halfschaduw'), ('Schaduw', 'Schaduw')]),
     ('h', 'Hoe hoog mag hij worden?', [('1–2 m', '1–2 m'), ('2–3 m', '2–3 m'), ('3+ m', '3 m en hoger')]),
     ('k', 'Welke kleur wilt u?', [(k, k) for k in KLEUR])]
# every answer must exist in the data
assert {x for v in V for x in v['standF']} == {a for a, _ in Q[0][2]}
assert {v['hoogteF'] for v in V} == {a for a, _ in Q[1][2]}
assert {x for v in V for x in v['kleurF']} == set(KLEUR)
qs = ''
for key, legend, opts in Q:
    qs += '<fieldset class="as3-q"><legend>' + legend + '</legend><div class="as3-ch">' + ''.join(
        '<button type="button" aria-pressed="false" data-q="' + key + '" data-a="' + a + '">' +
        ('<i style="background:' + KLEUR[a] + '"></i>' if key == 'k' else '') + lab + '</button>' for a, lab in opts) + '</div></fieldset>'
rows = ''
for v in V:
    rows += ('<li class="as3-r" data-st="' + '|'.join(v['standF']) + '" data-h="' + v['hoogteF'] + '" data-k="' + '|'.join(v['kleurF']) + '">'
             '<a href="#assortiment"><span class="as3-th"><img src="img/' + v['slug'] + '-sm.webp" alt="" loading="lazy"></span>'
             '<div class="as3-tx"><h3>' + e(v['name']) + '</h3><p class="as3-m"><span class="nb">' + e(v['color']) + '</span>&nbsp;<i class="as-sep">·</i> <span class="nb">bloeit ' + bloei(v) + '</span></p>'
             '<p class="as3-m"><span class="nb">' + e(' en '.join(v['standF']).capitalize()) + '</span>&nbsp;<i class="as-sep">·</i> <span class="nb">' + e(v['hoogte']) + ' hoog</span></p></div>'
             '<p class="as3-pr"><span>vanaf</span> <b>' + eur(v['frm']) + '</b> <span>40–60&nbsp;cm, met kluit</span></p></a></li>')
S3 = ('<section class="as as-s3" aria-labelledby="h-as3"><div class="in"><div class="as3-grid">'
      '<div class="as-head as3-hd"><div><h2 class="as-h" id="h-as3">Welke rhododendron past in uw tuin?</h2>'
      '<p class="as-lead">Beantwoord drie vragen en u ziet welke van onze zeven soorten passen.</p></div>'
      '<a class="as-all" href="#assortiment">Bekijk alle planten' + ARW + '</a></div>'
      '<div class="as3-card"><div class="as3-bg"></div><div class="wh-grain"></div><div class="as3-qs">' + qs + '</div>'
      '<div class="as3-res"><p aria-live="polite"><b class="as3-cnt">7 soorten</b><span class="as3-say">Kies een antwoord en u ziet wat past.</span></p>'
      '<button type="button" class="as3-clr" hidden>Wis keuze</button></div></div>'
      '<ul class="as3-list">' + rows + '<li class="as3-rest" hidden>Past niet bij uw keuze</li></ul></div></div></section>')

rep('<div class="between"><div class="in"><span>… hier volgen Assortiment en Hoe het werkt …</span></div></div>',
    '<div id="assortiment">' + S1 + S2 + S3 + '</div>')

# ---------- review bar ----------
rep('<html lang="nl" class="m-n3 t-0 d-k lp-u fd-podpis">', '<html lang="nl" class="m-n3 t-0 d-k lp-u fd-podpis as-1">')
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Ассортимент</i>'
    '<button type="button" data-g="as" data-v="1" aria-pressed="true">1 · Ряд</button>'
    '<button type="button" data-g="as" data-v="2" aria-pressed="false">2 · Палитра</button>'
    '<button type="button" data-g="as" data-v="3" aria-pressed="false">3 · Подбор</button></div></div><div id="root">')

CSS = r'''
/* ===== homepage Assortiment block, review page (10 Nov): 1 · Ряд, 2 · Палитра, 3 · Подбор ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
#assortiment{scroll-margin-top:120px}
.as{display:none;background:var(--page);color:var(--ink)}
html.as-1 .as-s1,html.as-2 .as-s2,html.as-3 .as-s3{display:block}
.as :is(h2,h3,p,ul,dl,dd,fieldset){margin:0;padding:0}
.as ul{list-style:none}.as a{color:inherit;text-decoration:none}.as img{display:block;width:100%;height:100%;object-fit:cover}
.as :is(a,button):focus-visible{outline:2px solid var(--moss);outline-offset:3px}
.as-head{display:grid;grid-template-columns:minmax(0,1fr) auto;column-gap:48px;align-items:end;margin-bottom:clamp(28px,3.2vw,48px)}
.as-h{font-size:clamp(34px,4.2vw,58px);line-height:1.04;letter-spacing:-.035em;font-weight:600;text-wrap:balance}
.as-lead{margin-top:18px!important;font-size:clamp(16px,1.25vw,18px);line-height:1.55;color:var(--ink2);max-width:50ch;text-wrap:pretty}
.as-sep{font-style:normal}
.as-arw{width:16px;height:16px;flex:none;fill:none;stroke:currentColor;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
.as-all,.as-btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:48px;padding:0 22px;border-radius:999px;font-size:15.5px;font-weight:600;white-space:nowrap}
.as-all{border:1px solid #a9a69c}
.as-all:hover{background:#e7e4dc}
.as .as-btn{background:var(--moss);color:#fff}
.as .as-btn:hover{background:#333c2c}
/* sizes with prices: four values on hairlines, the price in moss like the numbers of the facts card */
.as-sz{display:grid;grid-template-columns:repeat(4,minmax(0,1fr))}
.as-sz li{display:flex;flex-direction:column;gap:3px;padding-left:12px;border-left:1px solid rgba(20,20,19,.16)}
.as-sz li:first-child{padding-left:0;border-left:0}
.as-sz span{font-size:12.5px;line-height:1.3;color:#3d3c37;white-space:nowrap}
.as-sz b{font-size:19px;line-height:1.1;font-weight:600;letter-spacing:-.02em;color:var(--moss);font-variant-numeric:tabular-nums;white-space:nowrap}
@media (max-width:860px){
  /* phones: heading, then the plants; the link to the full catalogue closes the block */
  .as > .in,.as .as3-grid{display:flex;flex-direction:column}
  .as-head{display:contents}
  .as-head > div{margin-bottom:26px}
  .as-h{font-size:clamp(30px,8.6vw,40px)}
  .as-lead{margin-top:14px!important}
  .as-all{order:9;margin-top:28px;align-self:flex-start}
}

/* ---------- 1 · Ряд ---------- */
.as1-row{display:flex;gap:12px}
.as1-a{display:flex;flex-direction:column;height:100%}
.as1-ph{border-radius:22px;overflow:hidden;background:#dcd9d0}
.as1-cap h3{font-size:15.5px;line-height:1.25;font-weight:600;letter-spacing:-.01em;text-wrap:balance}
.as1-cap p{margin-top:4px;font-size:14.5px;line-height:1.3;color:#3d3c37}
.as1-cap b,.as3-pr b{font-weight:600;color:var(--moss);font-variant-numeric:tabular-nums}
.as1-n{font-size:22px;line-height:1.1;font-weight:600;letter-spacing:-.025em}
.as1-m{font-size:14.5px;line-height:1.45;color:#3d3c37}
.as1-go{display:inline-flex;align-items:center;gap:8px;font-size:15px;font-weight:600;color:var(--moss)}
/* swipe row: phones, tablets and anything without a pointer; every card is complete, the next one peeks */
@media not ((min-width:1200px) and (hover:hover)){
  .as1-row{overflow-x:auto;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;scrollbar-width:none;margin-inline:calc(-1 * var(--gut));padding-inline:var(--gut);scroll-padding-inline:var(--gut)}
  .as1-row::-webkit-scrollbar{display:none}
  .as1-it{flex:0 0 min(78vw,320px);scroll-snap-align:start}
  .as1-ph{aspect-ratio:4/5}
  .as1-cap{padding-top:16px}
  .as1-cap h3{font-size:21px;letter-spacing:-.02em}
  .as1-cap p,.as1-n{display:none}
  .as1-ov{display:flex;flex-direction:column;gap:2px;padding-top:6px;flex:1}
  .as1-ov .as-sz{margin-top:14px;padding-top:14px;border-top:1px solid var(--line);grid-template-columns:1fr 1fr;gap:10px 0}
  .as1-ov .as-sz li{flex-direction:row;align-items:baseline;justify-content:space-between;gap:8px;padding:0 14px 0 0;border:0}
  .as1-ov .as-sz li:nth-child(even){padding:0 0 0 14px;border-left:1px solid rgba(20,20,19,.16)}
  .as1-ov .as-sz span{font-size:13.5px}
  .as1-ov .as-sz b{font-size:17px}
  .as1-go{margin-top:auto;padding-top:8px;min-height:44px}
}
/* desktop with a pointer: one row of seven tall photos, the active one opens */
@media (min-width:1200px) and (hover:hover){
  .as1-it{flex:1 1 0;min-width:0;transition:flex-grow .3s ease}
  .as1-it.on{flex-grow:3.7}
  .as1-ph img{transition:transform .3s ease}
  .as1-it.on .as1-ph img{object-position:50% 18%}
  /* this photo is square with a wall above the bush: in the narrow strip it is zoomed onto the flowers */
  .as1-roseum-elegans:not(.on) .as1-ph img{transform:scale(1.42);transform-origin:50% 78%}
  .as1-a{position:relative}
  .as1-ph{height:clamp(450px,38vw,560px)}
  .as1-cap{height:76px;padding-top:14px}
  .as1-it.on .as1-cap{visibility:hidden}
  .as1-ov{display:none;position:absolute;left:12px;right:12px;bottom:88px;flex-direction:column;gap:3px;padding:20px 22px 12px;border-radius:16px;
    background:rgba(249,247,242,.93);-webkit-backdrop-filter:blur(14px);backdrop-filter:blur(14px);box-shadow:0 1px 0 rgba(255,255,255,.6) inset}
  .as1-it.on .as1-ov{display:flex}
  .as1-n{margin-bottom:5px!important}
  .as1-ov .as-sz{margin-top:14px;padding-top:14px;border-top:1px solid rgba(20,20,19,.14)}
  .as1-go{margin-top:6px;min-height:44px}
}
@media (prefers-reduced-motion:reduce){.as1-it,.as1-ph img{transition:none}}

/* ---------- 2 · Палитра ---------- */
.as2-card{position:relative;isolation:isolate;overflow:hidden;border-radius:28px;padding:clamp(28px,3vw,44px);--gr:.3;--gb:overlay;
  --flp:color-mix(in srgb,var(--fl) 34%,#f4efe8)}
.as2-bg{position:absolute;inset:0;z-index:-2;background:
  radial-gradient(ellipse 52% 44% at 46% -6%,#f1f0e8 0%,transparent 70%),
  radial-gradient(ellipse 30% 46% at 97% 6%,var(--flp) 0%,transparent 70%),
  radial-gradient(ellipse 30% 70% at -5% 42%,#b4c1a0 0%,transparent 68%),
  radial-gradient(ellipse 60% 40% at 42% 108%,#d9cbb0 0%,transparent 72%),
  radial-gradient(ellipse 30% 46% at 103% 104%,#c7b893 0%,transparent 70%),
  linear-gradient(to bottom,#eceee6 0%,#ebece3 46%,#e8e3d4 100%)}
.as2-tabs{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:8px;padding-bottom:clamp(24px,2.6vw,36px);border-bottom:1px solid rgba(20,20,19,.16)}
.as2-t{appearance:none;border:0;background:none;padding:0;margin:0;font:inherit;color:inherit;cursor:pointer;display:flex;flex-direction:column;align-items:center;text-align:center;min-width:0}
.as2-c{width:clamp(64px,7vw,96px);aspect-ratio:1;border-radius:50%;overflow:hidden;box-shadow:0 0 0 0 var(--moss);margin:4px 0 14px;outline:1px solid rgba(20,20,19,.1);outline-offset:-1px}
.as2-t.on .as2-c{box-shadow:0 0 0 3px #f1efea,0 0 0 5px var(--moss)}
.as2-n{font-size:clamp(13px,1.15vw,15.5px);line-height:1.25;font-weight:600;letter-spacing:-.01em;text-wrap:balance;color:#2b2a26}
.as2-t.on .as2-n{color:var(--ink)}
.as2-p{margin-top:4px;font-size:clamp(12.5px,1vw,14px);color:#3d3c37;font-variant-numeric:tabular-nums}
.as2-pn{display:none;grid-template-columns:minmax(0,.82fr) minmax(0,1fr);gap:clamp(28px,4.2vw,64px);align-items:center;padding-top:clamp(24px,2.6vw,36px)}
.as2-pn.on{display:grid}
.as2-ph{border-radius:20px;overflow:hidden;aspect-ratio:1/1;max-height:480px;width:100%;background:#dcd9d0}
.as2-ph img{object-position:50% 46%}
.as2-tx h3{font-size:clamp(30px,3.4vw,48px);line-height:1;letter-spacing:-.04em;font-weight:600}
.as2-sh{margin-top:14px!important;font-size:clamp(16px,1.25vw,18px);line-height:1.5;color:#2f2e2a;max-width:44ch;text-wrap:pretty}
.as2-f{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:14px 24px;margin-top:24px!important}
.as2-f dt{font-size:13.5px;line-height:1.3;color:#3d3c37}
.as2-f dd{margin-top:2px!important;font-size:15.5px;line-height:1.35;font-weight:600;color:#1d1d1b}
.as-sz-l{margin-top:26px!important;padding-top:22px!important;border-top:1px solid rgba(20,20,19,.16)}
.as-sz-l li{gap:6px;padding-left:clamp(12px,1.6vw,22px)}
.as-sz-l span{font-size:14px}
.as-sz-l b{font-size:clamp(26px,2.7vw,38px);line-height:1;letter-spacing:-.035em}
.as2-cta{display:flex;flex-wrap:wrap;align-items:center;gap:12px 20px;margin-top:28px}
.as2-cta span{font-size:14.5px;color:#3d3c37}
@media (max-width:899px){
  .as2-pn{grid-template-columns:minmax(0,1fr);gap:22px}
  .as2-ph{aspect-ratio:4/3;max-height:none}
}
@media (max-width:719px){
  .as2-card{border-radius:22px;padding:20px 20px 24px}
  /* the palette becomes a swipe row inside the card; the fourth circle peeks */
  .as2-tabs{display:flex;gap:6px;overflow-x:auto;scroll-snap-type:x proximity;scrollbar-width:none;margin-inline:-20px;padding-inline:14px;scroll-padding-inline:14px;padding-bottom:18px;border-bottom:0}
  .as2-tabs::-webkit-scrollbar{display:none}
  .as2-t{flex:0 0 86px;scroll-snap-align:start;padding:2px 0}
  .as2-c{width:66px;margin:5px 0 10px}
  .as2-n{font-size:13px}.as2-p{font-size:13px}
  .as2-pn{padding-top:6px;gap:20px}
  .as2-ph{aspect-ratio:1/1;border-radius:16px}
  .as2-tx h3{font-size:clamp(30px,8.6vw,36px)}
  .as2-sh{margin-top:12px!important;font-size:16px}
  .as2-f{margin-top:20px!important;grid-template-columns:1fr 1fr;gap:12px 16px}
  .as2-f dd{font-size:15px}
  .as-sz-l{grid-template-columns:1fr 1fr;row-gap:18px;margin-top:22px!important;padding-top:20px!important}
  .as-sz-l li:nth-child(odd){padding-left:0;border-left:0}
  .as-sz-l li:nth-child(even){padding-left:18px}
  .as-sz-l b{font-size:30px}
  .as2-cta{margin-top:24px}
  .as2-cta .as-btn{width:100%;white-space:normal;text-align:center;min-height:52px}
}

/* ---------- 3 · Подбор ---------- */
.as3-grid{display:grid;grid-template-columns:clamp(340px,34%,452px) minmax(0,1fr);column-gap:clamp(40px,5.5vw,96px);grid-template-areas:"hd hd" "card list"}
.as3-hd{grid-area:hd}
.as3-card{grid-area:card;position:relative;isolation:isolate;overflow:hidden;border-radius:28px;padding:clamp(28px,2.8vw,40px);display:flex;flex-direction:column;justify-content:space-between;gap:36px;--gr:.3;--gb:overlay}
.as3-bg{position:absolute;inset:0;z-index:-2;background:
  radial-gradient(ellipse 75% 38% at 50% -4%,#f1f0e8 0%,transparent 70%),
  radial-gradient(ellipse 34% 20% at 90% 46%,#ecd6d2 0%,transparent 70%),
  radial-gradient(ellipse 70% 40% at -8% 62%,#b4c1a0 0%,transparent 68%),
  radial-gradient(ellipse 120% 30% at 50% 104%,#d9cbb0 0%,transparent 72%),
  radial-gradient(ellipse 52% 30% at 102% 102%,#c7b893 0%,transparent 70%),
  linear-gradient(to bottom,#eceee6 0%,#ebece3 46%,#e8e3d4 100%)}
.as3-qs{display:flex;flex-direction:column;gap:clamp(22px,2.2vw,30px)}
.as3-q{border:0;min-width:0}
.as3-q legend{padding:0;font-size:clamp(18px,1.5vw,21px);line-height:1.2;font-weight:600;letter-spacing:-.02em}
.as3-ch{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}
.as3-ch button{appearance:none;display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:0 14px;border-radius:999px;border:1px solid rgba(20,20,19,.34);background:rgba(251,250,248,.62);
  font:600 15px/1 Manrope,system-ui,sans-serif;color:#1d1d1b;cursor:pointer;white-space:nowrap}
.as3-ch button:hover{background:rgba(251,250,248,.9)}
.as3-ch button[aria-pressed="true"]{background:var(--moss);border-color:var(--moss);color:#fff}
.as3-ch i{width:14px;height:14px;border-radius:50%;flex:none;box-shadow:0 0 0 1px rgba(20,20,19,.28)}
.as3-ch button[aria-pressed="true"] i{box-shadow:0 0 0 1.5px #fff}
.as3-res{display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:12px 16px;padding-top:24px;border-top:1px solid rgba(20,20,19,.16)}
.as3-res p{display:flex;flex-direction:column;gap:8px;min-width:0;flex:1 1 200px}
.as3-cnt{font-size:clamp(36px,3.4vw,48px);line-height:1;font-weight:600;letter-spacing:-.035em;color:var(--moss);font-variant-numeric:tabular-nums}
.as3-say{font-size:15px;line-height:1.4;color:#33322e}
.as3-clr{appearance:none;border:0;background:none;min-height:44px;padding:0 2px;font:600 15px/1 Manrope,system-ui,sans-serif;color:#1d1d1b;text-decoration:underline;text-underline-offset:4px;cursor:pointer}
.as3-list{grid-area:list;display:flex;flex-direction:column;border-bottom:1px solid var(--line)}
.as3-r{border-top:1px solid var(--line)}
.as3-r a{display:grid;grid-template-columns:auto minmax(0,1fr) auto;column-gap:clamp(16px,1.8vw,24px);align-items:center;padding:clamp(13px,1.2vw,17px) 0}
.as3-th{width:clamp(72px,6vw,84px);aspect-ratio:1;border-radius:18px;overflow:hidden;background:#dcd9d0}
.as3-tx h3{font-size:clamp(20px,1.9vw,26px);line-height:1.15;font-weight:600;letter-spacing:-.02em;margin-bottom:5px}
.as3-m{font-size:15px;line-height:1.45;color:var(--soft)}
.as3-pr{display:grid;justify-items:end;text-align:right;gap:3px;font-size:13.5px;line-height:1.3;color:var(--soft);white-space:nowrap}
.as3-pr b{font-size:clamp(26px,2.4vw,34px);line-height:1;letter-spacing:-.035em}
.as3-r a:hover h3{color:var(--moss)}
/* answers given: the plants that do not fit step back to one quiet line each, below the ones that fit */
.as3-r.off{order:2;border-top-color:transparent}
.as3-r.off a{grid-template-columns:minmax(0,1fr);padding:0;min-height:44px}
.as3-r.off :is(.as3-th,.as3-m,.as3-pr){display:none}
.as3-r.off h3{margin:0;font-size:16.5px;font-weight:500;letter-spacing:-.01em;color:var(--soft)}
.as3-rest{order:1;margin:28px 0 6px;padding:0 0 8px;font-size:14px;color:var(--soft);border-bottom:1px solid var(--line)}
.as3-rest[hidden]{display:none}
.as3-rest + .as3-r{border-top:0}
@media (max-width:959px){
  .as3-grid{grid-template-columns:minmax(0,1fr);grid-template-areas:"hd" "card" "list"}
  .as3-card{border-radius:22px;padding:24px 20px;gap:26px}
  .as3-list{margin-top:28px}
}
@media (max-width:599px){
  .as3-ch button{padding:0 14px}
  .as3-res{padding-top:20px}
  .as3-cnt{font-size:34px}
  .as3-r a{grid-template-columns:auto minmax(0,1fr);column-gap:14px;align-items:start;padding:16px 0}
  .as3-th{width:68px;border-radius:16px;grid-row:1/3}
  .as3-tx h3{font-size:19px}
  .as3-m{font-size:14.5px}
  .as3-pr{grid-column:2;display:block;text-align:left;white-space:normal;margin-top:8px!important;font-size:14px}
  .as3-pr b{font-size:20px;letter-spacing:-.02em}
  .as3-pr span:last-child::before{content:"· "}
}
'''
rep('</head>', '<style id="assortiment-css">' + CSS + '</style></head>')

JS = r'''<script>(function(){var $=function(q,r){return [].slice.call((r||document).querySelectorAll(q))};
/* a middle dot that ends up at the end of a wrapped line is hidden (it is glued to the word before it, so it never starts a line) */
function seps(){$('.as-sep').forEach(function(d){var b=d.nextElementSibling;d.style.cssText='';if(!d.offsetParent)return;if(b&&b.offsetTop>d.offsetTop+2)d.style.visibility='hidden'})}
seps();addEventListener('resize',seps);addEventListener('load',seps);if(window.ResizeObserver){var ro=new ResizeObserver(seps);$('.as1-ov,.as3-tx').forEach(function(x){ro.observe(x)})}if(document.fonts&&document.fonts.ready)document.fonts.ready.then(seps);new MutationObserver(seps).observe(document.documentElement,{attributes:true,attributeFilter:['class']});
/* 1 · Ряд: the photo under the pointer (or with keyboard focus) opens */
var it=$('.as1-it');it.forEach(function(el){function on(){it.forEach(function(x){x.classList.toggle('on',x===el)});seps()}el.addEventListener('mouseenter',on);el.addEventListener('focusin',on)});
/* 2 · Палитра: tabs; the card takes a tint of the chosen flower */
var tabs=$('.as2-t'),pns=$('.as2-pn'),card=document.querySelector('.as2-card');
function pick(i,f){tabs.forEach(function(t,j){t.classList.toggle('on',j===i);t.setAttribute('aria-selected',j===i?'true':'false');t.tabIndex=j===i?0:-1;pns[j].classList.toggle('on',j===i)});
card.style.setProperty('--fl',tabs[i].getAttribute('data-hex'));if(f)tabs[i].focus()}
tabs.forEach(function(t,i){t.tabIndex=i?-1:0;t.addEventListener('click',function(){pick(i)});t.addEventListener('keydown',function(e){var d=e.key==='ArrowRight'?1:e.key==='ArrowLeft'?-1:0;if(d){e.preventDefault();pick((i+d+tabs.length)%tabs.length,true)}})});
/* 3 · Подбор: one answer per question; a plant fits when it has every chosen value (standplaatsFilter, hoogteFilter, kleurFilter) */
var ch=$('.as3-ch button'),rows=$('.as3-r'),cnt=document.querySelector('.as3-cnt'),say=document.querySelector('.as3-say'),clr=document.querySelector('.as3-clr'),rest=document.querySelector('.as3-rest'),sel={};
function upd(){var ks=Object.keys(sel),n=0;rows.forEach(function(r){var ok=ks.every(function(k){return r.getAttribute('data-'+k).split('|').indexOf(sel[k])>=0});r.classList.toggle('off',!ok);if(ok)n++});
ch.forEach(function(b){b.setAttribute('aria-pressed',sel[b.getAttribute('data-q')]===b.getAttribute('data-a')?'true':'false')});
clr.hidden=!ks.length;rest.hidden=!ks.length||n===rows.length;
if(!ks.length){cnt.textContent='7 soorten';say.textContent='Kies een antwoord en u ziet wat past.'}
else{cnt.textContent=n+' van 7';say.textContent=n===0?'Geen soort past bij al uw antwoorden. Laat één antwoord los.':n===1?'soort past bij uw keuze.':'soorten passen bij uw keuze.'}}
ch.forEach(function(b){b.addEventListener('click',function(){var q=b.getAttribute('data-q'),a=b.getAttribute('data-a');if(sel[q]===a)delete sel[q];else sel[q]=a;upd()})});
clr.addEventListener('click',function(){sel={};upd()});})();</script>'''
rep('</body>', JS + '</body>')

(D / 'assortiment.html').write_text(s)
print('assortiment.html', len(s), 'bytes;', len(V), 'varieties')
