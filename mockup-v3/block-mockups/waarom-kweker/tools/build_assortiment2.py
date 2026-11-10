# Mockup tool (not site code): assortiment-2.html = the main mockup (index.html) with round 2 of the homepage ASSORTIMENT
# block in place of the ".between" placeholder (after Waarom wij, before the founder block). No picker this round; every
# photo is shown in its own aspect ratio, so no flower or bush is cut. Three variants, switched by html.a2-1/2/3:
#   1 · Полка  mirrors Waarom wij: a tall «Поле» card on the left with the four sizes as accented numbers and the price
#              range of each; the chosen size sets the price under every plant. Right: a rail of seven whole flower photos,
#              each card as wide as its photo. 21st: Product Carousel 8297 (rail, arrows, header link), Product Card 28199
#              (image well, title left, price footer), Sneaker Product Page Hero 44658 (size choice drives the price).
#   2 · Сад    all seven bushes at once in a staggered grid, the heading is the first cell, captions under the photos.
#              21st: Team Showcase 10098 (staggered photo columns), Gallery Grid with Captions 26909 (caption under tile).
#   3 · Сорт   one variety at a time on a wide «Поле» card: the list of seven names, the bush and the flower side by side,
#              facts and the four prices. 21st: Featured Product Showcase 29291 (split: text and price / image),
#              Feature List Showcase 27506 (list item swaps the image), Editorial Collage Hero 19074 (two images of
#              different size standing together).
# All plant data is read from ../../src/data/content.ts (mirror of the live site's lib/products.ts); nothing is typed in here.
# Usage: python3 tools/build_assortiment2.py [dir]
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
    V.append(dict(slug=field(o, 'slug'), name=field(o, 'name'), color=field(o, 'color'), hex=field(o, 'hex'), bloei=field(o, 'bloei'),
                  stand=field(o, 'standplaats'), hoogte=field(o, 'hoogte'), frm=field(o, 'from'), sizes=sizes))
assert [v['name'] for v in V] == ['Nova Zembla', "Cunningham's White", 'Roseum Elegans', 'Catawbiense Boursault', 'Catawbiense Grandiflorum',
                                  'Ponticum Roseum', 'Ponticum']
assert [v['frm'] for v in V] == ['29', '25', '27', '27', '29', '22', '22']
LABELS = ['40–60 cm', '60–80 cm', '80–100 cm', '100–120 cm']
for v in V:
    assert [l for l, _ in v['sizes']] == LABELS and v['sizes'][0][1] == v['frm'] + ',00', v['name']
    assert all(p.endswith(',00') for _, p in v['sizes'])
    v['pr'] = [p[:-3] for _, p in v['sizes']]
# price range per size over the seven varieties
RNG = [(min(int(v['pr'][i]) for v in V), max(int(v['pr'][i]) for v in V)) for i in range(4)]

# ---------- photos: copied once, real pixel sizes read so every frame has the photo's own aspect ratio ----------
for v in V:
    for suf, key in (('-sm', 'fl'), ('-2-sm', 'bu')):
        dst = D / 'img' / (v['slug'] + suf + '.webp')
        if not dst.exists():
            shutil.copyfile(SRC / 'assets' / 'img' / dst.name, dst)
        v[key] = Image.open(dst).size

e = html.escape
nb = lambda t: t.replace(' ', '&nbsp;')
low = lambda t: t[0].lower() + t[1:]
ARW = '<svg class="bs-arw" viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'
ALL = '<a class="bs-all" href="#assortiment">Bekijk alle planten' + ARW + '</a>'


def img(v, key, alt):
    w, h = v[key]
    return ('<img src="img/' + v['slug'] + ('-sm' if key == 'fl' else '-2-sm') + '.webp" width="' + str(w) + '" height="' + str(h) +
            '" alt="' + e(alt) + '" loading="lazy">')


ar = lambda v, key: '%.4f' % (v[key][0] / v[key][1])
alt_fl = lambda v: v['name'] + ', bloem, ' + low(v['color'])
alt_bu = lambda v: v['name'] + ', bloeiende struik'

# ---------- 1 · Полка ----------
szb = ''
for i, lab in enumerate(LABELS):
    szb += ('<li><button type="button" class="b1-sz" data-i="' + str(i) + '" aria-pressed="' + ('true' if i == 0 else 'false') + '">'
            '<b>' + nb(lab) + '</b><span>€&nbsp;' + str(RNG[i][0]) + ' tot €&nbsp;' + str(RNG[i][1]) + '<em> per plant</em></span><i aria-hidden="true"></i></button></li>')
it1 = ''
for v in V:
    it1 += ('<li class="b1-it" style="--ar:' + ar(v, 'fl') + '"><a href="#assortiment"><div class="b1-ph">' + img(v, 'fl', alt_fl(v)) + '</div>'
            '<h3>' + e(v['name']) + '</h3><p class="b1-m">' + e(v['color']) + '</p><p class="b1-m">Bloeit ' + e(v['bloei'].lower()) + '</p>'
            '<p class="b1-pr" data-p="' + '|'.join(v['pr']) + '"><b>€&nbsp;' + v['pr'][0] + '</b><span><span class="b1-lab">' + nb(LABELS[0]) + '</span>, met kluit</span></p></a></li>')
S1 = ('<section class="bs bs-s1" aria-labelledby="h-bs1"><div class="in">'
      '<div class="bs-head"><div><h2 class="bs-h" id="h-bs1">Zeven soorten, elk in vier maten.</h2>'
      '<p class="bs-lead">Kies een maat en u ziet wat elke soort kost. Bestellen kan vanaf 1&nbsp;plant.</p></div>'
      '<div class="b1-nav">' + ALL + '<button type="button" class="b1-ar b1-prev" aria-label="Vorige soorten" disabled>' + ARW + '</button>'
      '<button type="button" class="b1-ar b1-next" aria-label="Volgende soorten">' + ARW + '</button></div></div>'
      '<div class="b1-grid"><div class="b1-card"><div class="b1-bg" aria-hidden="true"></div><div class="wh-grain" aria-hidden="true"></div>'
      '<h3 class="b1-ct">Welke maat wilt u?</h3><ul class="b1-szs" aria-label="Maten">' + szb + '</ul>'
      '<p class="b1-note">Hoogte van de plant bij levering.</p></div>'
      '<ul class="b1-rail" tabindex="0" aria-label="Soorten">' + it1 + '</ul></div></div></section>')

# ---------- 2 · Сад ----------
it2 = ''
for v in V:
    it2 += ('<article class="b2-it"><a href="#assortiment"><div class="b2-ph" style="aspect-ratio:' + ar(v, 'bu') + '">' + img(v, 'bu', alt_bu(v)) + '</div>'
            '<div class="b2-cap"><div><h3>' + e(v['name']) + '</h3><p>' + e(v['color']) + '</p><p>Bloeit ' + e(v['bloei'].lower()) + '</p></div>'
            '<p class="b2-pr"><span>vanaf</span><b>€&nbsp;' + v['frm'] + '</b></p></div></a></article>')
S2 = ('<section class="bs bs-s2" aria-labelledby="h-bs2"><div class="in"><div class="b2-grid">'
      '<div class="b2-hd"><h2 class="bs-h" id="h-bs2">Zeven soorten uit eigen kweek.</h2>'
      '<p class="bs-lead">Elke soort is er in vier maten, van 40 tot 120&nbsp;cm. De vanaf-prijs geldt voor 40–60&nbsp;cm, per plant met kluit.</p>' + ALL + '</div>' +
      it2 + '</div></div></section>')

# ---------- 3 · Сорт ----------
tabs = pns = ''
for i, v in enumerate(V):
    tabs += ('<button type="button" class="b3-t' + (' on' if i == 0 else '') + '" role="tab" id="b3-t' + str(i) + '" aria-controls="b3-p' + str(i) + '" aria-selected="' +
             ('true' if i == 0 else 'false') + '"><i style="background:' + v['hex'] + '" aria-hidden="true"></i><span>' + e(v['name']) + '</span></button>')
    pns += ('<article class="b3-pn' + (' on' if i == 0 else '') + '" role="tabpanel" id="b3-p' + str(i) + '" aria-labelledby="b3-t' + str(i) + '">'
            '<div class="b3-phs" style="--a1:' + ar(v, 'bu') + ';--a2:' + ar(v, 'fl') + '"><div class="b3-ph b3-bu">' + img(v, 'bu', alt_bu(v)) + '</div>'
            '<div class="b3-ph b3-fl">' + img(v, 'fl', alt_fl(v)) + '</div></div>'
            '<div class="b3-tx"><h3>' + e(v['name']) + '</h3>'
            '<div class="b3-row"><dl class="b3-f"><div><dt>Kleur</dt><dd>' + e(v['color']) + '</dd></div><div><dt>Bloei</dt><dd>' + e(v['bloei']) + '</dd></div>'
            '<div><dt>Standplaats</dt><dd>' + e(v['stand']) + '</dd></div><div><dt>Hoogte</dt><dd>' + e(v['hoogte']) + '</dd></div></dl>'
            '<div class="b3-ph b3-fl2" style="aspect-ratio:' + ar(v, 'fl') + '">' + img(v, 'fl', '') + '</div></div>'
            '<ul class="b3-sz" aria-label="Maten en prijzen">' + ''.join('<li><b>€&nbsp;' + p + '</b><span>' + nb(l) + '</span></li>' for l, p in zip(LABELS, v['pr'])) + '</ul>'
            '<p class="b3-note">Prijs per plant, met kluit.</p>'
            '<a class="bs-btn" href="#assortiment">Bekijk ' + e(v['name']) + ARW + '</a></div></article>')
S3 = ('<section class="bs bs-s3" aria-labelledby="h-bs3"><div class="in">'
      '<div class="bs-head"><div><h2 class="bs-h" id="h-bs3">Kies uw rhododendron.</h2>'
      '<p class="bs-lead">Zeven soorten, elk in vier maten van 40 tot 120&nbsp;cm. Bestellen kan vanaf 1&nbsp;plant.</p></div>' + ALL + '</div>'
      '<div class="b3-card"><div class="b3-bg" aria-hidden="true"></div><div class="wh-grain" aria-hidden="true"></div>'
      '<div class="b3-tabs" role="tablist" aria-label="Soorten">' + tabs + '</div><div class="b3-pns">' + pns + '</div></div></div></section>')

rep('<div class="between"><div class="in"><span>… hier volgen Assortiment en Hoe het werkt …</span></div></div>',
    '<div id="assortiment">' + S1 + S2 + S3 + '</div>')

# ---------- review bar ----------
rep('<html lang="nl" class="m-n3 t-0 d-k lp-u fd-podpis">', '<html lang="nl" class="m-n3 t-0 d-k lp-u fd-podpis a2-1">')
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Ассортимент · 2</i>'
    '<button type="button" data-g="a2" data-v="1" aria-pressed="true">1 · Полка</button>'
    '<button type="button" data-g="a2" data-v="2" aria-pressed="false">2 · Сад</button>'
    '<button type="button" data-g="a2" data-v="3" aria-pressed="false">3 · Сорт</button></div></div><div id="root">')

CSS = r'''
/* ===== homepage Assortiment block, round 2 (10 Nov): 1 · Полка, 2 · Сад, 3 · Сорт ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
#assortiment{scroll-margin-top:120px}
.bs{display:none;background:var(--page);color:var(--ink)}
html.a2-1 .bs-s1,html.a2-2 .bs-s2,html.a2-3 .bs-s3{display:block}
.bs :is(h2,h3,p,ul,dl,dd){margin:0;padding:0}
.bs ul{list-style:none}.bs a{color:inherit;text-decoration:none}
.bs img{display:block;width:100%;height:100%;object-fit:cover}
.bs :is(a,button,ul):focus-visible{outline:2px solid var(--moss);outline-offset:3px}
.bs-head{display:grid;grid-template-columns:minmax(0,1fr) auto;column-gap:48px;align-items:end;margin-bottom:clamp(28px,3.2vw,48px)}
.bs-h{font-size:clamp(34px,4.2vw,58px);line-height:1.04;letter-spacing:-.035em;font-weight:600;text-wrap:balance}
.bs-lead{margin-top:18px!important;font-size:clamp(16px,1.25vw,18px);line-height:1.55;color:var(--ink2);max-width:52ch;text-wrap:pretty}
.bs-arw{width:16px;height:16px;flex:none;fill:none;stroke:currentColor;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
.bs-all,.bs-btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:48px;padding:0 22px;border-radius:999px;font-size:15.5px;font-weight:600;white-space:nowrap}
.bs-all{border:1px solid #a9a69c}
.bs-all:hover{background:#e7e4dc}
.bs .bs-btn{background:var(--moss);color:#fff}
.bs .bs-btn:hover{background:#333c2c}
.bs-pb{--gr:.3;--gb:overlay}
@media (max-width:860px){
  .bs-s1 > .in,.bs-s3 > .in{display:flex;flex-direction:column}
  .bs-head{display:contents}
  .bs-head > div:first-child{margin-bottom:26px}
  .bs-h{font-size:clamp(30px,8.6vw,40px)}
  .bs-lead{margin-top:14px!important}
  .bs-all{order:9;margin-top:28px;align-self:flex-start}
}

/* ---------- 1 · Полка ---------- */
.b1-nav{display:flex;align-items:center;gap:10px}
.b1-ar{appearance:none;width:48px;height:48px;border-radius:50%;border:1px solid #a9a69c;background:none;color:var(--ink);display:inline-flex;align-items:center;justify-content:center;cursor:pointer;padding:0}
.b1-ar:hover{background:#e7e4dc}
.b1-ar[disabled]{color:#76746c;border-color:#d6d3cb;cursor:default;background:none}
.b1-prev svg{transform:scaleX(-1)}
.b1-nav .bs-all{margin-right:10px}
.b1-grid{display:grid;grid-template-columns:clamp(300px,33%,452px) minmax(0,1fr);column-gap:clamp(28px,3.4vw,56px);--h:clamp(300px,26.4vw,384px)}
.b1-card{position:relative;isolation:isolate;overflow:hidden;border-radius:28px;padding:clamp(26px,2.6vw,38px);display:flex;flex-direction:column;--gr:.3;--gb:overlay;--ln:rgba(20,20,19,.16)}
.b1-bg{position:absolute;inset:0;z-index:-2;background:
  radial-gradient(ellipse 75% 38% at 50% -4%,#f1f0e8 0%,transparent 70%),
  radial-gradient(ellipse 34% 20% at 12% 22%,#ecd6d2 0%,transparent 70%),
  radial-gradient(ellipse 78% 50% at 106% 46%,#adbb98 0%,transparent 68%),
  radial-gradient(ellipse 46% 32% at 70% 100%,#c2cca9 0%,transparent 68%),
  radial-gradient(ellipse 120% 34% at 50% 104%,#d9cbb0 0%,transparent 72%),
  radial-gradient(ellipse 52% 34% at -2% 102%,#c7b893 0%,transparent 70%),
  linear-gradient(to bottom,#eceee6 0%,#ebece3 46%,#e8e3d4 100%)}
.b1-ct{font-size:clamp(19px,1.5vw,21px);line-height:1.2;font-weight:600;letter-spacing:-.02em}
.b1-szs{display:flex;flex-direction:column;flex:1;margin-top:8px!important}
.b1-szs li{display:flex;flex:1}
.b1-szs li+li{border-top:1px solid var(--ln)}
.b1-sz{appearance:none;border:0;background:none;margin:0;padding:clamp(10px,1vw,13px) 0;width:100%;text-align:left;font:inherit;color:inherit;cursor:pointer;
  display:grid;grid-template-columns:minmax(0,1fr) auto;column-gap:16px;row-gap:6px;align-items:center;align-content:center}
.b1-sz b{grid-column:1;font-size:clamp(30px,2.9vw,42px);line-height:1;font-weight:600;letter-spacing:-.035em;color:var(--moss);font-variant-numeric:tabular-nums;white-space:nowrap}
.b1-sz span{grid-column:1;font-size:15px;line-height:1.4;color:#3d3c37}
.b1-sz em{font-style:normal}
.b1-sz i{grid-column:2;grid-row:1/3;width:26px;height:26px;border-radius:50%;border:1.5px solid #5d6653;box-sizing:border-box;position:relative}
.b1-sz[aria-pressed="true"] i{border-color:var(--moss);background:var(--moss)}
.b1-sz[aria-pressed="true"] i::after{content:"";position:absolute;left:7.5px;top:4.5px;width:6px;height:11px;border:solid #fff;border-width:0 2px 2px 0;transform:rotate(45deg)}
.b1-sz:hover i{border-color:var(--moss)}
.b1-note{margin-top:14px!important;font-size:14px;line-height:1.45;color:#3d3c37}
/* the rail: every card is as wide as its photo (the photo's own aspect ratio at one common height), nothing is cropped */
.b1-rail{display:flex;gap:clamp(14px,1.5vw,22px);overflow-x:auto;scroll-snap-type:x proximity;scrollbar-width:none;-webkit-overflow-scrolling:touch;
  margin-right:calc(-1 * var(--gut));padding-right:var(--gut);scroll-padding-inline:0 var(--gut);align-items:stretch;border-radius:22px 0 0 22px}
.b1-rail::-webkit-scrollbar{display:none}
/* desktop: the cut card on the right fades out, so the rail reads as 'more this way' */
@media (min-width:861px){.b1-rail{-webkit-mask-image:linear-gradient(to right,#000 calc(100% - 64px),transparent);mask-image:linear-gradient(to right,#000 calc(100% - 64px),transparent)}}
.b1-it{flex:none;width:calc(var(--h) * var(--ar));scroll-snap-align:start}
.b1-it a{display:flex;flex-direction:column;height:100%}
.b1-ph{height:var(--h);border-radius:22px;overflow:hidden;background:#dcd9d0;margin-bottom:16px}
.b1-it h3{font-size:clamp(18px,1.5vw,21px);line-height:1.2;font-weight:600;letter-spacing:-.02em;margin-bottom:5px;text-wrap:balance}
.b1-m{font-size:14.5px;line-height:1.45;color:var(--soft)}
.b1-pr{margin-top:auto!important;padding-top:14px;display:flex;flex-wrap:wrap;align-items:baseline;gap:2px 10px}
.b1-pr b{font-size:clamp(26px,2.3vw,32px);line-height:1;font-weight:600;letter-spacing:-.035em;color:var(--moss);font-variant-numeric:tabular-nums;white-space:nowrap}
.b1-pr > span{font-size:13.5px;line-height:1.3;color:var(--soft);white-space:nowrap}
.b1-it a:hover h3{color:var(--moss)}
@media (max-width:860px){
  .b1-nav{display:contents}
  .b1-ar{display:none}
  .b1-grid{display:flex;flex-direction:column;gap:28px;--h:264px}
  .b1-card{border-radius:22px;padding:22px 20px}
  .b1-szs{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:16px!important}
  .b1-szs li+li{border-top:0}
  .b1-sz{grid-template-columns:minmax(0,1fr);row-gap:5px;padding:13px 14px 12px;border-radius:16px;border:1px solid rgba(20,20,19,.32);background:rgba(251,250,248,.6);min-height:72px}
  .b1-sz b{font-size:21px;letter-spacing:-.025em}
  .b1-sz em{display:none}
  .b1-sz span{font-size:13.5px;line-height:1.3}
  .b1-sz i{display:none}
  .b1-sz[aria-pressed="true"]{background:var(--moss);border-color:var(--moss)}
  .b1-sz[aria-pressed="true"] :is(b,span){color:#fff}
  .b1-rail{margin-inline:calc(-1 * var(--gut));padding-inline:var(--gut);scroll-padding-inline:var(--gut);border-radius:0;gap:14px}
}
@media (min-width:600px) and (max-width:860px){.b1-szs{grid-template-columns:repeat(4,1fr)}}
@media (max-width:374px){.b1-sz b{font-size:20px}.b1-sz{padding-inline:12px}}

/* ---------- 2 · Сад ---------- */
.b2-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));column-gap:clamp(18px,1.8vw,26px);row-gap:clamp(36px,3.4vw,52px);align-items:start;--off:clamp(40px,4.4vw,64px);padding-bottom:var(--off)}
.b2-grid > :nth-child(even){margin-top:var(--off)}
.b2-hd{align-self:start;padding-right:8px}
.b2-hd .bs-h{font-size:clamp(32px,3.5vw,50px)}
.b2-hd .bs-all{margin-top:28px}
.b2-it a{display:block}
.b2-ph{border-radius:22px;overflow:hidden;background:#dcd9d0}
.b2-cap{display:grid;grid-template-columns:minmax(0,1fr) auto;column-gap:14px;align-items:start;padding-top:14px}
.b2-cap h3{font-size:clamp(18px,1.5vw,21px);line-height:1.2;font-weight:600;letter-spacing:-.02em;margin-bottom:5px;text-wrap:balance}
.b2-cap p{font-size:14.5px;line-height:1.45;color:var(--soft)}
.b2-cap .b2-pr{display:flex;flex-direction:column;align-items:flex-end;gap:2px;font-size:13px;line-height:1.2;white-space:nowrap}
.b2-pr b{font-size:clamp(24px,2.1vw,30px);line-height:1;font-weight:600;letter-spacing:-.035em;color:var(--moss);font-variant-numeric:tabular-nums}
.b2-it a:hover h3{color:var(--moss)}
@media (max-width:1099px){
  /* three columns: the heading goes on top, the middle column sits a step lower, the link stands next to the seventh plant */
  .b2-grid{grid-template-columns:repeat(3,minmax(0,1fr))}
  .b2-hd{grid-column:1/-1;padding:0}
  .b2-hd .bs-all{display:none}
  .b2-grid > :nth-child(n){margin-top:0}
  .b2-grid > :nth-child(3n){margin-top:var(--off)}
  .b2-grid > .b2-it:nth-child(8){margin-top:calc(-1 * var(--off))}
  .b2-grid > .b2-m-all{display:flex;grid-column:2/-1;justify-self:start;align-self:center;margin-top:0}
}
@media (max-width:860px){
  /* the heading goes on top, the photos keep three columns down to 600 px and two below */
  .b2-grid{column-gap:14px;row-gap:30px;--off:32px;padding-bottom:0}
  .b2-hd{margin-bottom:-2px}
  .b2-hd .bs-h{font-size:clamp(30px,8.6vw,40px)}
  .b2-ph{border-radius:18px}
  .b2-cap{grid-template-columns:minmax(0,1fr);padding-top:12px}
  .b2-cap h3{font-size:17.5px}
  .b2-cap p{font-size:14px}
  .b2-cap .b2-pr{flex-direction:row;align-items:baseline;gap:6px;margin-top:8px!important;font-size:13.5px}
  .b2-pr b{font-size:24px}
}
@media (max-width:599px){
  .b2-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
  .b2-grid > :nth-child(n){margin-top:0}
  .b2-grid > :nth-child(odd):not(:first-child){margin-top:var(--off)}
  .b2-grid > .b2-it:nth-child(n+4):nth-child(even){margin-top:calc(-1 * var(--off))}
  .b2-grid > .b2-m-all{grid-column:1/-1;margin-top:0}
}
.b2-m-all{display:none}

/* ---------- 3 · Сорт ---------- */
.b3-card{position:relative;isolation:isolate;overflow:hidden;border-radius:28px;padding:clamp(28px,3vw,44px);--gr:.3;--gb:overlay;--ln:rgba(20,20,19,.16);
  display:grid;grid-template-columns:minmax(190px,.62fr) minmax(0,2.6fr);column-gap:clamp(28px,3.2vw,52px)}
.b3-bg{position:absolute;inset:0;z-index:-2;background:
  radial-gradient(ellipse 52% 44% at 46% -6%,#f1f0e8 0%,transparent 70%),
  radial-gradient(ellipse 26% 40% at 99% 8%,#ecd6d2 0%,transparent 70%),
  radial-gradient(ellipse 28% 70% at -5% 46%,#b4c1a0 0%,transparent 68%),
  radial-gradient(ellipse 60% 40% at 42% 108%,#d9cbb0 0%,transparent 72%),
  radial-gradient(ellipse 30% 46% at 103% 104%,#c7b893 0%,transparent 70%),
  linear-gradient(to bottom,#eceee6 0%,#ebece3 46%,#e8e3d4 100%)}
.b3-tabs{display:flex;flex-direction:column;align-self:center}
.b3-t{appearance:none;border:0;background:none;margin:0;padding:0;font:inherit;color:#33322e;cursor:pointer;text-align:left;display:flex;align-items:center;gap:12px;min-height:52px;border-top:1px solid var(--ln)}
.b3-t:first-child{border-top:0}
.b3-t i{flex:none;width:14px;height:14px;border-radius:50%;box-shadow:0 0 0 1px rgba(20,20,19,.3)}
.b3-t span{font-size:clamp(16px,1.3vw,18.5px);line-height:1.2;font-weight:500;letter-spacing:-.015em}
.b3-t:hover{color:var(--ink)}
.b3-t.on{color:var(--ink)}
.b3-t.on span{font-weight:700}
.b3-t.on i{box-shadow:0 0 0 3px #eeeee6,0 0 0 5px var(--moss)}
.b3-pns{display:grid}
/* all seven panels share one cell, so the card keeps one height whichever variety is open */
.b3-pn{grid-area:1/1;visibility:hidden;display:grid;grid-template-columns:minmax(0,1.22fr) minmax(0,1fr);column-gap:clamp(28px,3.2vw,52px);align-items:center;height:100%}
.b3-pn.on{visibility:visible}
/* two photos standing on one line: the bush and the flower, each in its own aspect ratio; widths are split so both keep it */
.b3-phs{display:grid;grid-template-columns:minmax(0,1.62fr) minmax(0,1fr);gap:clamp(10px,1vw,14px);align-items:end}
.b3-ph{border-radius:20px;overflow:hidden;background:#dcd9d0}
.b3-bu{aspect-ratio:var(--a1)}.b3-fl{aspect-ratio:var(--a2)}
.b3-fl2{display:none}
.b3-tx h3{font-size:clamp(30px,3.1vw,44px);line-height:1.02;letter-spacing:-.04em;font-weight:600;text-wrap:balance}
.b3-f{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:14px 20px;margin-top:22px!important}
.b3-f dt{font-size:13.5px;line-height:1.3;color:#3d3c37}
.b3-f dd{margin-top:2px!important;font-size:15.5px;line-height:1.35;font-weight:600;color:#1d1d1b}
.b3-sz{display:grid;grid-template-columns:repeat(4,auto);justify-content:space-between;column-gap:12px;margin-top:24px!important;padding-top:22px!important;border-top:1px solid var(--ln)}
.b3-sz li{display:flex;flex-direction:column;gap:6px}
.b3-sz b{font-size:clamp(26px,2.5vw,36px);line-height:1;font-weight:600;letter-spacing:-.035em;color:var(--moss);font-variant-numeric:tabular-nums;white-space:nowrap}
.b3-sz span{font-size:14px;line-height:1.3;color:#3d3c37;white-space:nowrap}
.b3-note{margin-top:14px!important;font-size:14px;line-height:1.45;color:#3d3c37}
.b3-tx .bs-btn{margin-top:24px}
@media (max-width:1179px){
  .b3-card{grid-template-columns:minmax(0,1fr);row-gap:26px}
  .b3-tabs{flex-direction:row;flex-wrap:wrap;gap:8px}
  .b3-t{min-height:44px;padding:0 15px 0 12px;gap:9px;border:1px solid rgba(20,20,19,.32);border-radius:999px;background:rgba(251,250,248,.6)}
  .b3-t:first-child{border-top:1px solid rgba(20,20,19,.32)}
  .b3-t span{font-size:15px;font-weight:600;white-space:nowrap}
  .b3-t.on{background:var(--moss);border-color:var(--moss);color:#fff}
  .b3-t.on span{font-weight:600}
  .b3-t.on i{box-shadow:0 0 0 1.5px #fff}
}
@media (max-width:860px){
  .b3-card{border-radius:22px;padding:20px 20px 24px;row-gap:20px}
  /* the seven names: a swipe row inside the card, the next name peeks */
  .b3-tabs{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;margin-inline:-20px;padding-inline:20px;scroll-padding-inline:20px;scroll-snap-type:x proximity}
  .b3-tabs::-webkit-scrollbar{display:none}
  .b3-t{flex:none;scroll-snap-align:start}
  .b3-pn{grid-template-columns:minmax(0,1fr);row-gap:22px;align-content:start;height:auto}
  .b3-ph{border-radius:16px}
  .b3-tx h3{font-size:clamp(30px,8.6vw,36px)}
  .b3-phs{grid-template-columns:minmax(0,1fr)}
  .b3-fl{display:none}
  .b3-row{display:grid;grid-template-columns:minmax(0,1fr) 38%;column-gap:16px;align-items:start;margin-top:18px}
  .b3-fl2{display:block;border-radius:14px}
  .b3-f{margin-top:0!important;grid-template-columns:minmax(0,1fr);gap:11px}
  .b3-f dd{font-size:15px}
  .b3-sz{grid-template-columns:1fr 1fr;row-gap:18px;justify-content:stretch;margin-top:22px!important;padding-top:20px!important}
  .b3-sz b{font-size:30px}
  .b3-tx .bs-btn{width:100%;white-space:normal;text-align:center;min-height:52px;box-sizing:border-box}
}
@media (min-width:600px) and (max-width:860px){
  .b3-pn{grid-template-columns:minmax(0,.9fr) minmax(0,1fr);column-gap:28px;align-items:start}
}
'''
rep('</head>', '<style id="assortiment2-css">' + CSS + '</style></head>')

# the phone link of 2 · Сад closes the grid
s = s.replace('</article></div></div></section><section class="bs bs-s3"', '</article><a class="bs-all b2-m-all" href="#assortiment">Bekijk alle planten' + ARW +
              '</a></div></div></section><section class="bs bs-s3"')
assert s.count('b2-m-all" href') == 1

JS = r'''<script>(function(){var $=function(q,r){return [].slice.call((r||document).querySelectorAll(q))};
/* 1 · Полка: the chosen size sets the price and the size label under every plant */
var sz=$('.b1-sz'),pr=$('.b1-pr'),labs=sz.map(function(b){return b.querySelector('b').innerHTML});
sz.forEach(function(b,i){b.addEventListener('click',function(){sz.forEach(function(x,j){x.setAttribute('aria-pressed',j===i?'true':'false')});
pr.forEach(function(p){p.querySelector('b').innerHTML='€&nbsp;'+p.getAttribute('data-p').split('|')[i];p.querySelector('.b1-lab').innerHTML=labs[i]})})});
/* the rail arrows */
var rail=document.querySelector('.b1-rail'),pv=document.querySelector('.b1-prev'),nx=document.querySelector('.b1-next');
function ends(){pv.disabled=rail.scrollLeft<2;nx.disabled=rail.scrollLeft>rail.scrollWidth-rail.clientWidth-2}
function go(d){rail.scrollBy({left:d*rail.clientWidth*.8,behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'auto':'smooth'})}
pv.addEventListener('click',function(){go(-1)});nx.addEventListener('click',function(){go(1)});rail.addEventListener('scroll',ends,{passive:true});addEventListener('resize',ends);ends();
/* 3 · Сорт: the list of names is a tab list */
var tabs=$('.b3-t'),pns=$('.b3-pn');
function pick(i,f){tabs.forEach(function(t,j){t.classList.toggle('on',j===i);t.setAttribute('aria-selected',j===i?'true':'false');t.tabIndex=j===i?0:-1;pns[j].classList.toggle('on',j===i)});
if(f)tabs[i].focus();if(tabs[i].scrollIntoView&&tabs[i].parentNode.scrollWidth>tabs[i].parentNode.clientWidth){var p=tabs[i].parentNode;p.scrollLeft=Math.max(0,tabs[i].offsetLeft-p.offsetLeft-20)}}
tabs.forEach(function(t,i){t.tabIndex=i?-1:0;t.addEventListener('click',function(){pick(i)});t.addEventListener('keydown',function(e){var d=(e.key==='ArrowRight'||e.key==='ArrowDown')?1:(e.key==='ArrowLeft'||e.key==='ArrowUp')?-1:0;if(d){e.preventDefault();pick((i+d+tabs.length)%tabs.length,true)}})});
})();</script>'''
rep('</body>', JS + '</body>')

rep('<title>Waarom wij · De kweker</title>', '<title>Assortiment · ronde 2</title>')
(D / 'assortiment-2.html').write_text(s)
print('assortiment-2.html', len(s), 'bytes;', len(V), 'varieties; price range per size', RNG)
