# Mockup tool (not site code): assortiment-3.html = the main mockup (index.html) with round 3 of the homepage ASSORTIMENT
# block in place of the ".between" placeholder (after Waarom wij, before the founder block). Three variants, switched by
# html.a3-1/2/3 from the review bar:
#   1 · Сад    built separately. This script only inserts tools/as3-sad.html (a <section id="as3-1">) and tools/as3-sad.css
#              when they exist; otherwise a placeholder section. It never writes those files.
#   2 · Прайс  a price list: one row per variety (flower + bush thumbnail, name, colour, bloom, height) and the four sizes
#              as right-aligned price columns, so all 28 prices are on screen and each row is one link. On the phone the
#              same list keeps one price per row and a four-way size switch above it chooses which.
#              21st (reference only): Spec Sheet 39793 (label column + value columns, stacks on narrow screens),
#              Comparison Table 26827 (footer row with the call to action), Segmented Control 43311 (radiogroup, roving arrows).
#   3 · Ряд    all seven in ONE row as a photo matrix: the flowers form the top line, the bushes the line under it, then
#              name, colour and price on shared baselines (subgrid). No heading cell, no second row. Under 1200 px the
#              same row becomes a swipe rail with the next item peeking.
#              21st (reference only): Gallery Grid with Captions 26909 (caption under the tile).
# All plant data is read from ../../src/data/content.ts (mirror of the live site's lib/products.ts); nothing is typed in here.
# Usage: python3 tools/build_assortiment3.py [dir]
import re, pathlib, sys, shutil, html
from PIL import Image

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


V = []
for o in re.findall(r"\{\s*slug: .*?\n  \},", vblock, re.S):
    m = re.search(r'sizes: (sizes[A-Z])', o)
    sizes = size_sets[m.group(1)] if m else re.findall(r"label: '([^']+)', price: '([^']+)'", o[o.index('sizes:'):])
    V.append(dict(slug=field(o, 'slug'), name=field(o, 'name'), color=field(o, 'color'), bloei=field(o, 'bloei'), stand=field(o, 'standplaats'),
                  hoogte=field(o, 'hoogte'), frm=field(o, 'from'), sizes=sizes))
assert [v['name'] for v in V] == ['Nova Zembla', "Cunningham's White", 'Roseum Elegans', 'Catawbiense Boursault', 'Catawbiense Grandiflorum',
                                  'Ponticum Roseum', 'Ponticum']
assert [v['frm'] for v in V] == ['29', '25', '27', '27', '29', '22', '22']
LABELS = ['40–60 cm', '60–80 cm', '80–100 cm', '100–120 cm']
for v in V:
    assert [l for l, _ in v['sizes']] == LABELS and v['sizes'][0][1] == v['frm'] + ',00', v['name']
    assert all(p.endswith(',00') for _, p in v['sizes'])
    v['pr'] = [p[:-3] for _, p in v['sizes']]

# ---------- photos: <slug>-sm = flower close-up, <slug>-2-sm = bush. Real pixel sizes are read. ----------
# Frames: flower 1:1, bush 3:4. A 3:4 flower photo loses only leaf margin in a square (the truss stays whole; the vertical
# focus is set per photo below). Roseum Elegans' bush photo is square: it is cropped to 3:4 like the others (the bush
# touches the frame edges, as several other bush photos do). A mirrored-background extension was tried and dropped
# (11 Nov): the mirrored strips showed reflected flowers and leaves.
FOCUS = {'cunninghams-white': 46, 'catawbiense-boursault': 60, 'catawbiense-grandiflorum': 50, 'ponticum-roseum': 46, 'ponticum': 40}
for v in V:
    for suf, key in (('-sm', 'fl'), ('-2-sm', 'bu')):
        dst = D / 'img' / (v['slug'] + suf + '.webp')
        if not dst.exists():
            shutil.copyfile(SRC / 'assets' / 'img' / dst.name, dst)
        v[key] = Image.open(dst).size

e = html.escape
nb = lambda t: t.replace(' ', '&nbsp;')
low = lambda t: t[0].lower() + t[1:]
ARW = '<svg class="a3-arw" viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'
ALL = '<a class="a3-all" href="#assortiment">Naar het assortiment' + ARW + '</a>'


def tag(v, key, alt, cls=''):
    w, h = v[key]
    st = ''
    if key == 'fl' and v['slug'] in FOCUS:
        st = ' style="object-position:50% ' + str(FOCUS[v['slug']]) + '%"'
    return ('<img' + (' class="' + cls + '"' if cls else '') + ' src="img/' + v['slug'] + ('-sm' if key == 'fl' else '-2-sm') + '.webp" width="' + str(w) +
            '" height="' + str(h) + '" alt="' + e(alt) + '" loading="lazy"' + st + '>')


def flower(v, alt):
    return '<div class="a3-fl">' + tag(v, 'fl', alt) + '</div>'


def bush(v, alt):
    w, h = v['bu']
    if abs(w / h - .75) < .02:
        return '<div class="a3-bu">' + tag(v, 'bu', alt) + '</div>'
    assert w == h, (v['slug'], w, h)
    return '<div class="a3-bu">' + tag(v, 'bu', alt) + '</div>'


alt_fl = lambda v: v['name'] + ', bloem, ' + low(v['color'])
alt_bu = lambda v: v['name'] + ', bloeiende struik'

# ---------- 2 · Прайс ----------
sw = ''
for i, lab in enumerate(LABELS):
    sw += ('<button type="button" role="radio" class="p-sz" data-i="' + str(i) + '" aria-checked="' + ('true' if i == 0 else 'false') + '">' +
           lab[:-3] + '<span class="a3-sr"> cm</span></button>')
rows = ''
for v in V:
    prs = ''.join('<div class="p-pr' + (' on' if i == 0 else '') + '"><b>€&nbsp;' + p + '</b><span class="p-lab"> ' + nb(l) + ', met kluit</span></div>'
                  for i, (l, p) in enumerate(zip(LABELS, v['pr'])))
    rows += ('<li><a class="p-row" href="#assortiment"><div class="p-ph">' + flower(v, alt_fl(v)) + bush(v, alt_bu(v)) + '</div>'
             '<div class="p-nm"><h3>' + e(v['name']) + '</h3><p>' + e(v['color']) + '</p></div>'
             '<p class="p-bl"><span class="a3-sr">Bloei: </span>' + e(v['bloei']) + '</p><p class="p-st"><span class="a3-sr">Standplaats: </span>' + e(v['stand']) + '</p><p class="p-ht"><span class="a3-sr">Hoogte: </span>' + e(v['hoogte']) + '</p>' +
             prs + ARW + '</a></li>')
S2 = ('<section class="a3 a3-p" id="as3-2" aria-labelledby="h-as3-2"><div class="in">'
      '<div class="a3-head"><h2 class="a3-h" id="h-as3-2">Zeven soorten, elk in vier maten.</h2>'
      '<p class="a3-lead">Eén gewas, zeven soorten van eigen veld in Otterlo. U ziet per soort wat elke maat kost.</p></div>'
      '<div class="p-sw"><p id="p-swl">Kies een maat <span>(hoogte in cm)</span></p><div class="p-szs" role="radiogroup" aria-labelledby="p-swl">' + sw + '</div></div>'
      '<div class="p-tb"><div class="p-hd" aria-hidden="true"><span class="p-h1">Soort</span><span class="p-bl">Bloei</span><span class="p-st">Standplaats</span><span class="p-ht">Hoogte</span>'
      '<span class="p-grp">Prijs per plant, met kluit</span>' + ''.join('<span class="p-hs">' + nb(l) + '</span>' for l in LABELS) + '</div>'
      '<ul class="p-rows">' + rows + '</ul></div>'
      '<div class="p-ft"><p>Bestellen kan vanaf 1&nbsp;plant.</p>' + ALL + '</div></div></section>')

# ---------- 3 · Ряд ----------
it3 = ''
for v in V:
    it3 += ('<li class="r-it"><a href="#assortiment"><div class="r-ph">' + flower(v, alt_fl(v)) + bush(v, alt_bu(v)) + '</div>'
            '<h3>' + e(v['name']) + '</h3><p class="r-col">' + e(v['color']) + '</p>'
            '<p class="r-pr"><span class="r-v">vanaf </span><b>€&nbsp;' + v['frm'] + '</b><span class="r-sz">' + nb(LABELS[0]) + ', met&nbsp;kluit</span></p></a></li>')
S3 = ('<section class="a3 a3-r" id="as3-3" aria-labelledby="h-as3-3"><div class="in">'
      '<div class="a3-head"><div><h2 class="a3-h" id="h-as3-3">Zeven soorten, naast elkaar.</h2>'
      '<p class="a3-lead">Boven de bloem, daaronder de struik in bloei. Elke soort is er in vier maten, van 40 tot 120&nbsp;cm.</p></div>'
      '<div class="r-nav"><button type="button" class="r-ar r-prev" aria-label="Vorige soorten" disabled>' + ARW + '</button>'
      '<button type="button" class="r-ar r-next" aria-label="Volgende soorten">' + ARW + '</button>' + ALL + '</div></div>'
      '<ul class="r-rail" tabindex="0" aria-label="Zeven soorten">' + it3 + '</ul>'
      '<div class="r-ft">' + ALL + '</div></div></section>')

# ---------- 1 · Сад: built separately, only inserted here ----------
sad_html, sad_css = D / 'tools' / 'as3-sad.html', D / 'tools' / 'as3-sad.css'
if sad_html.exists():
    S1 = sad_html.read_text().strip()
    assert 'id="as3-1"' in S1, 'as3-sad.html must be a <section id="as3-1">'
else:
    S1 = ('<section id="as3-1" class="a3-ph1"><div class="in"><p>Вариант 1 · Сад собирается отдельно</p></div></section>')
SAD_CSS = ('\n/* ===== 1 · Сад (tools/as3-sad.css) ===== */\n' + sad_css.read_text() + '\n') if sad_css.exists() else ''

rep('<div class="between"><div class="in"><span>… hier volgen Assortiment en Hoe het werkt …</span></div></div>',
    '<div id="assortiment">' + S1 + S2 + S3 + '</div>')

# ---------- review bar ----------
rep('<html lang="nl" class="m-n3 t-0 d-k lp-u fd-podpis">', '<html lang="nl" class="m-n3 t-0 d-k lp-u fd-podpis a3-1">')
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Ассортимент · 3</i>'
    '<button type="button" data-g="a3" data-v="1" aria-pressed="true">1 · Сад</button>'
    '<button type="button" data-g="a3" data-v="2" aria-pressed="false">2 · Прайс</button>'
    '<button type="button" data-g="a3" data-v="3" aria-pressed="false">3 · Ряд</button></div></div><div id="root">')

CSS = r'''
/* ===== homepage Assortiment block, round 3: 1 · Сад (separate), 2 · Прайс, 3 · Ряд ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
#assortiment{scroll-margin-top:120px;background:var(--page)}
html:not(.a3-1) #as3-1{display:none!important}
.a3{display:none;background:var(--page);color:var(--ink)}
html.a3-2 #as3-2,html.a3-3 #as3-3{display:block}
.a3-ph1 .in{padding-top:120px;padding-bottom:120px;text-align:center;color:var(--soft);font-size:15px}
.a3 > .in{padding-top:clamp(64px,7vw,112px);padding-bottom:clamp(64px,7vw,112px)}
:where(.a3) :is(h2,h3,p,ul){margin:0;padding:0}
:where(.a3) ul{list-style:none}:where(.a3) a{color:inherit;text-decoration:none}
.a3 :is(a,button,ul):focus-visible{outline:2px solid var(--moss);outline-offset:3px}
.a3-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}
.a3-h{font-size:clamp(34px,4.2vw,58px);line-height:1.04;letter-spacing:-.035em;font-weight:600;text-wrap:balance}
.a3-lead{font-size:clamp(16px,1.25vw,17.5px);line-height:1.6;color:var(--ink2);max-width:46ch;text-wrap:balance}
.a3-arw{width:16px;height:16px;flex:none;fill:none;stroke:currentColor;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
.a3-all{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:48px;padding:0 22px;border-radius:999px;border:1px solid #a9a69c;font-size:15.5px;font-weight:600;white-space:nowrap}
.a3-all:hover{background:#e7e4dc}
/* photo frames shared by both variants: flower 1:1, bush 3:4 */
.a3-fl,.a3-bu{position:relative;overflow:hidden;background:#dedbd2}
.a3-fl{aspect-ratio:1}.a3-bu{aspect-ratio:3/4}
.a3-fl img,.a3-bu img{display:block;width:100%;height:100%;object-fit:cover}
@media (max-width:860px){.a3-h{font-size:clamp(30px,8.6vw,40px)}}

/* ---------- 2 · Прайс ---------- */
.a3-p .a3-head{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,clamp(300px,33%,452px));column-gap:clamp(40px,5.5vw,96px);align-items:end;margin-bottom:clamp(32px,3.6vw,52px)}
.p-sw{display:none}
.p-tb{display:grid;column-gap:clamp(14px,1.7vw,28px);
  grid-template-columns:auto minmax(0,1fr) auto minmax(0,200px) auto repeat(4,minmax(64px,auto)) 16px}
.p-hd,.p-rows,.p-rows li,.p-row{grid-column:1/-1;display:grid;grid-template-columns:subgrid}
.p-hd{grid-template-rows:auto auto;row-gap:6px;align-items:end;padding-bottom:14px;border-bottom:1px solid #b9b6ac;font-size:14px;line-height:1.3;color:var(--soft)}
.p-hd .p-h1{grid-column:1/3;grid-row:2}.p-hd .p-bl{grid-column:3;grid-row:2}.p-hd .p-st{grid-column:4;grid-row:2}.p-hd .p-ht{grid-column:5;grid-row:2}
.p-hd .p-grp{grid-column:6/10;grid-row:1;text-align:right;color:var(--ink);font-weight:600;font-size:14.5px}
.p-hd .p-hs{grid-row:2;text-align:right;white-space:nowrap}
.p-rows li+li{border-top:1px solid var(--line)}
.p-rows li:last-child{border-bottom:1px solid var(--line)}
.p-row{align-items:center;padding:12px 0;min-height:44px}
.p-row:hover{background:#e9e6df;box-shadow:-14px 0 0 #e9e6df,14px 0 0 #e9e6df}
.p-ph{display:flex;gap:4px;height:clamp(72px,6.2vw,88px)}
.p-ph > div{height:100%;border-radius:4px}
.p-ph .a3-fl{border-radius:12px 4px 4px 12px}.p-ph .a3-bu{border-radius:4px 12px 12px 4px}
.p-nm h3{font-size:clamp(18px,1.55vw,21px);line-height:1.2;font-weight:600;letter-spacing:-.02em;text-wrap:balance}
.p-nm p{margin-top:5px;font-size:15px;line-height:1.35;color:var(--ink2)}
.p-rows :is(.p-bl,.p-st,.p-ht){font-size:15px;line-height:1.4;color:var(--ink2)}
.p-rows :is(.p-bl,.p-ht){white-space:nowrap}.p-rows .p-st{text-wrap:balance}
.p-bl{min-width:88px}.p-ht{min-width:72px}
.p-pr{text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}
.p-pr b{font-size:clamp(17px,1.35vw,19px);font-weight:600;letter-spacing:-.01em}
.p-row .a3-arw{color:var(--soft)}.p-row:hover .a3-arw{color:var(--ink)}
.p-ft{display:flex;align-items:center;justify-content:space-between;gap:24px;margin-top:clamp(24px,2.4vw,32px)}
.p-ft p{font-size:16px;line-height:1.5;color:var(--ink2)}
@media (min-width:760px){
  .p-lab{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}
}
/* fewer fact columns as the row gets narrower; the name, the photos and the four prices always stay */
@media (max-width:1359px){.p-st{display:none}.p-tb{grid-template-columns:auto minmax(0,1fr) auto auto repeat(4,minmax(64px,auto)) 16px}
  .p-hd .p-ht{grid-column:4}.p-hd .p-grp{grid-column:5/9}}
@media (max-width:1099px){.p-bl{display:none}.p-tb{grid-template-columns:auto minmax(0,1fr) auto repeat(4,minmax(64px,auto)) 16px}
  .p-hd .p-ht{grid-column:3}.p-hd .p-grp{grid-column:4/8}}
@media (max-width:999px){.p-ht{display:none}.p-tb{grid-template-columns:auto minmax(0,1fr) repeat(4,minmax(60px,auto)) 16px;column-gap:12px}
  .p-hd .p-grp{grid-column:3/7}
  .p-hd{font-size:13.5px}.p-ph{height:68px}.p-nm p{font-size:14.5px}}
@media (max-width:860px){
  .a3-p .a3-head{grid-template-columns:1fr;row-gap:14px;margin-bottom:26px}
}
/* phone: one price per row, the size switch above the list chooses which */
@media (max-width:759px){
  .p-sw{display:block;margin-bottom:10px}
  .p-sw > p{font-size:15px;line-height:1.4;font-weight:600;margin-bottom:10px}
  .p-sw > p span{font-weight:500;color:var(--soft)}
  .p-szs{display:grid;grid-template-columns:repeat(4,1fr);gap:6px}
  .p-sz{appearance:none;margin:0;padding:0;height:48px;border-radius:12px;border:1px solid #a9a69c;background:none;color:var(--ink);font:600 15px/1 Manrope,system-ui,sans-serif;font-variant-numeric:tabular-nums;cursor:pointer}
  .p-sz[aria-checked="true"]{background:var(--moss);border-color:var(--moss);color:#fff}
  .p-tb{display:block}
  .p-hd{display:none}
  .p-rows,.p-rows li{display:block}
  .p-rows li:first-child{border-top:0}
  .p-row{grid-template-columns:auto minmax(0,1fr) 16px;column-gap:14px;grid-template-rows:auto auto;row-gap:5px;align-content:center;padding:13px 0}
  .p-row:hover{background:none;box-shadow:none}
  .p-ph{grid-row:1/3;height:68px}
  .p-nm{grid-column:2;align-self:end}
  .p-nm h3{font-size:17.5px}.p-nm p{margin-top:3px;font-size:14.5px}
  .p-rows :is(.p-bl,.p-st,.p-ht){display:none}
  .p-pr{display:none;grid-column:2;text-align:left;align-self:start;white-space:normal}
  .p-pr.on{display:block}
  .p-pr b{font-size:17.5px}
  .p-lab{font-size:14px;color:var(--soft);white-space:nowrap}
  .p-row .a3-arw{grid-column:3;grid-row:1/3}
  .p-ft{flex-direction:column;align-items:flex-start;gap:16px;margin-top:22px}
}
@media (max-width:374px){.p-ph{height:64px}.p-row{column-gap:12px}}

/* ---------- 3 · Ряд ---------- */
.a3-r .a3-head{display:grid;grid-template-columns:minmax(0,1fr) auto;column-gap:48px;align-items:end;margin-bottom:clamp(28px,3.2vw,48px)}
.a3-r .a3-lead{margin-top:18px;max-width:54ch}
.r-nav{display:flex;align-items:center;gap:10px}
.r-ar{display:none;appearance:none;width:48px;height:48px;border-radius:50%;border:1px solid #a9a69c;background:none;color:var(--ink);align-items:center;justify-content:center;cursor:pointer;padding:0}
.r-ar:hover{background:#e7e4dc}
.r-ar[disabled]{color:#76746c;border-color:#d6d3cb;cursor:default;background:none}
.r-prev svg{transform:scaleX(-1)}
.r-ft{display:none}
/* one row of seven; four shared row tracks (photos, name, colour, price) keep every baseline aligned */
.r-rail{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));grid-template-rows:repeat(4,auto);column-gap:clamp(10px,1.05vw,16px)}
.r-it,.r-it > a{display:grid;grid-row:1/span 4;grid-template-rows:subgrid}
.r-ph{display:grid;row-gap:3px;border-radius:18px;overflow:hidden}
.r-it h3{align-self:end;margin-top:14px;font-size:clamp(16px,1.2vw,17.5px);line-height:1.22;font-weight:600;letter-spacing:-.015em}
.r-col{margin-top:4px;font-size:14.5px;line-height:1.35;color:var(--ink2)}
.r-pr{margin-top:12px;padding-top:11px;border-top:1px solid var(--line);font-size:14.5px;line-height:1.35;color:var(--ink2);font-variant-numeric:tabular-nums}
.r-pr b{font-size:19px;font-weight:600;letter-spacing:-.015em;color:var(--ink)}
.r-sz{display:block;margin-top:2px;font-size:13.5px;color:var(--soft)}
.r-it > a:hover h3{text-decoration:underline;text-underline-offset:3px;text-decoration-thickness:1.5px}
@media (max-width:1199px){
  /* a swipe rail: 5, 4 or 2 whole items and a part of the next one */
  .r-rail{--n:5;--g:12px;grid-template-columns:none;grid-auto-flow:column;grid-auto-columns:calc((100vw - var(--gut) - var(--n) * var(--g)) / (var(--n) + .42));column-gap:var(--g);
    overflow-x:auto;overscroll-behavior-x:contain;scroll-snap-type:x proximity;scrollbar-width:none;-webkit-overflow-scrolling:touch;
    margin:0 calc(-1 * var(--gut));padding:4px var(--gut);scroll-padding-inline:var(--gut)}
  .r-rail::-webkit-scrollbar{display:none}
  .r-it{scroll-snap-align:start}
  .r-ar{display:inline-flex}
  .r-nav .a3-all{margin-left:10px}
}
@media (max-width:899px){.r-rail{--n:4}}
@media (max-width:860px){
  .a3-r .a3-head{column-gap:24px;margin-bottom:24px}
  .a3-r .a3-lead{margin-top:14px}
  .r-nav .a3-all{display:none}
  .r-ft{display:block;margin-top:26px}
}
@media (max-width:599px){.r-rail{--n:2;--g:10px}.r-ph{border-radius:16px}
  .a3-r .a3-head{grid-template-columns:1fr}.r-nav{display:none}}
'''
rep('</head>', '<style>' + CSS + SAD_CSS + '</style></head>')

JS = r'''<script>(function(){var $=function(q,r){return [].slice.call((r||document).querySelectorAll(q))};
/* 2 · Прайс: on the phone the size switch chooses which of the four prices each row shows */
var sz=$('.p-sz'),rows=$('.p-row');
function pick(i,f){sz.forEach(function(b,j){b.setAttribute('aria-checked',j===i?'true':'false');b.tabIndex=j===i?0:-1});
rows.forEach(function(r){$('.p-pr',r).forEach(function(p,j){p.classList.toggle('on',j===i)})});if(f)sz[i].focus()}
sz.forEach(function(b,i){b.tabIndex=i?-1:0;b.addEventListener('click',function(){pick(i)});
b.addEventListener('keydown',function(e){var d=(e.key==='ArrowRight'||e.key==='ArrowDown')?1:(e.key==='ArrowLeft'||e.key==='ArrowUp')?-1:0;if(d){e.preventDefault();pick((i+d+sz.length)%sz.length,true)}})});
/* 3 · Ряд: arrows for the rail (shown only where the row scrolls) */
var rail=document.querySelector('.r-rail'),pv=document.querySelector('.r-prev'),nx=document.querySelector('.r-next');
function ends(){pv.disabled=rail.scrollLeft<2;nx.disabled=rail.scrollLeft>rail.scrollWidth-rail.clientWidth-2}
function go(d){rail.scrollBy({left:d*rail.clientWidth*.7,behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'auto':'smooth'})}
pv.addEventListener('click',function(){go(-1)});nx.addEventListener('click',function(){go(1)});rail.addEventListener('scroll',ends,{passive:true});addEventListener('resize',ends);ends();
/* the row is hidden while another variant is shown, so the ends are measured again when it gets a size */
if(window.ResizeObserver)new ResizeObserver(ends).observe(rail);
})();</script>'''
rep('</body>', JS + '</body>')

rep('<title>Waarom wij · De kweker</title>', '<title>Assortiment · ronde 3</title>')
(D / 'assortiment-3.html').write_text(s)
print('assortiment-3.html', len(s), 'bytes;', len(V), 'varieties;', 'Сад: ' + ('inserted' if sad_html.exists() else 'placeholder'))
