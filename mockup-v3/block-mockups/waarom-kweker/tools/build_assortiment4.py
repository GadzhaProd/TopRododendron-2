# Mockup tool (not site code): assortiment-4.html = the main mockup (index.html) with the settled «Сад» Assortiment block
# in place of the ".between" placeholder, plus three candidate "изюминки" switched from the review bar:
#   html.iz-0   Сад как есть (reference)
#   html.iz-a   A · Цветок-медальон: a round close-up of the variety's flower on the lower right corner of the bush photo
#   html.iz-b   B · Цвет сорта: every card is a soft grained gradient in its own flower colour (hex from the data, softened)
#   html.iz-c   C · Заголовок-карточка: the heading cell is a «Поле» gradient card with a large moss "7"
#   html.iz-ac  A + C
#   html.iz-d   D · Общий фон (owner, 11 Nov): one light «Поле» gradient behind the whole grid, feathered edges, no card edge
#   html.fp-1..4  the field palette for D and D+C (Поле, Цветение, Листва, Рассвет).
#   html.iz-dc  D + C. The medallion states (A, A+C) stay in the CSS but are off the review bar: the owner rejected them.
#   html.sb-n / html.sb-y   the substrate line under the grid, off / on
# The base markup and CSS are copies of tools/build_as3_sad.py and tools/as3-sad.css (those files are not touched);
# the additions live in tools/as4.css. All plant and substrate data is read from mockup-v3/src/data/content.ts.
# Usage: python3 tools/build_assortiment4.py [dir]
import re, pathlib, sys, shutil, html

D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
SRC = D.parent.parent / 'src'
s = (D / 'index.html').read_text()


def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70])
    s = s.replace(a, b)


ts = (SRC / 'data' / 'content.ts').read_text()
vblock = ts[ts.index('export const varieties'):ts.index('export const bySlug')]
tblock = ts[ts.index('export const tuinturf'):ts.index('export const company')]


def field(o, k):
    m = re.search(k + r""": (?:'((?:[^'\\]|\\.)*)'|"((?:[^"\\]|\\.)*)")""", o)
    assert m, k
    return (m.group(1) if m.group(1) is not None else m.group(2)).replace("\\'", "'")


V = [dict(slug=field(o, 'slug'), name=field(o, 'name'), color=field(o, 'color'), hex=field(o, 'hex'), bloei=field(o, 'bloei'), frm=field(o, 'from'))
     for o in re.findall(r"\{\s*slug: .*?\n  \},", vblock, re.S)]
assert [v['frm'] for v in V] == ['29', '25', '27', '27', '29', '22', '22'], [v['frm'] for v in V]
assert len(V) == 7
T = dict(name=field(tblock, 'name'), price=field(tblock, 'price'), unit=field(tblock, 'unit'), upsell=field(tblock, 'upsell'))
assert T['price'] == '14,95' and T['unit'] == 'per zak van 40 liter'

for name in [v['slug'] + suf + '.webp' for v in V for suf in ('-sm', '-2-sm')] + ['tuinturf-sm.webp']:
    if not (D / 'img' / name).exists():
        shutil.copyfile(SRC / 'assets' / 'img' / name, D / 'img' / name)

# where each bush sits in its photo, so the 4:5 frame keeps it whole (same as «Сад»)
POS = {'roseum-elegans': '50% 60%', 'nova-zembla': '50% 70%', 'cunninghams-white': '50% 40%'}
# A · medallion: where the truss sits in the flower photo (x%, y%) and how far to zoom so it fills the circle
MED = {'nova-zembla': (47, 44, 1.0), 'cunninghams-white': (50, 46, 1.0), 'roseum-elegans': (50, 46, 1.0),
       'catawbiense-boursault': (50, 62, 1.25), 'catawbiense-grandiflorum': (50, 49, 1.2), 'ponticum-roseum': (50, 46, 1.25),
       'ponticum': (60, 40, 1.0)}
e = html.escape
ARW = '<svg class="sd-arw" viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'
GRAIN = '<span class="wh-grain sd-gr" aria-hidden="true"></span>'

items = ''
for v in V:
    light = v['hex'].lower() in ('#f1ece3',)
    x, y, z = MED[v['slug']]
    items += ('<article class="sd-it' + (' sd-lt' if light else '') + '" style="--hx:' + v['hex'] + '"><a href="#assortiment" aria-label="' + e(v['name']) + ', vanaf € ' + v['frm'] + ' voor 40–60 cm">'
              '<div class="sd-fig"><div class="sd-ph"><img src="img/' + v['slug'] + '-2-sm.webp" alt="' + e(v['name']) + ', bloeiende struik" loading="lazy"'
              + (' style="object-position:' + POS[v['slug']] + '"' if v['slug'] in POS else '') + '></div>'
              '<span class="sd-md"><img src="img/' + v['slug'] + '-sm.webp" alt="Bloem van ' + e(v['name']) + '" loading="lazy" style="object-position:%d%% %d%%;transform-origin:%d%% %d%%;transform:scale(%s)"></span></div>' % (x, y, x, y, z) +
              '<h3>' + e(v['name']) + '</h3>'
              '<p class="sd-c"><i' + (' class="lt"' if light else '') + ' style="background:' + v['hex'] + '" aria-hidden="true"></i>' + e(v['color']) + '</p>'
              '<p class="sd-b">Bloeit ' + e(v['bloei'].lower()) + '</p>'
              '<p class="sd-pr"><span class="sd-v">vanaf</span><b>€&nbsp;' + v['frm'] + '</b><span class="sd-s">40–60&nbsp;cm, met kluit</span></p>'
              + GRAIN + '</a></article>')

ALL = '<a class="sd-all" href="#assortiment">Bekijk alle planten' + ARW + '</a>'
SUB = ('<a class="sd-sub" href="#assortiment" aria-label="' + e(T['name']) + ', € ' + T['price'] + ' ' + e(T['unit']) + '">'
       '<img src="img/tuinturf-sm.webp" alt="" width="900" height="900" loading="lazy">'
       '<span class="sb-t"><b>' + e(T['name']) + '</b><span>' + e(T['upsell']) + '</span></span>'
       '<span class="sb-p"><b>€&nbsp;' + T['price'] + '</b><span>' + e(T['unit']).replace(' van ', ' van&nbsp;').replace('40 liter', '40&nbsp;liter') + '</span></span>'
       '<span class="sb-go">Bekijk substraat' + ARW + '</span></a>')
BLOCK = ('<section id="as4" class="sd" aria-labelledby="h-sd"><div class="in"><div class="sd-field" aria-hidden="true"><span class="sd-fbg"></span>' + GRAIN + '</div><div class="sd-grid">'
         '<div class="sd-hd"><span class="wh2-bg sd-hbg" aria-hidden="true"></span>' + GRAIN +
         '<h2 id="h-sd"><span class="sd-zv">Zeven</span><span class="sd-7">7</span> <span class="sd-ht">soorten uit eigen kweek.</span></h2>'
         '<p class="sd-lead">Elke soort is er in vier maten, van 40 tot 120&nbsp;cm. U bestelt vanaf 1&nbsp;plant.</p>' + ALL + '</div>'
         + items +
         '<a class="sd-tile" href="#assortiment">' + GRAIN + '<span>Alle zeven soorten, maten en prijzen</span><b>Bekijk alle <span class="nw">planten' + ARW + '</span></b></a>'
         '</div>' + SUB + '</div></section>')

rep('<div class="between"><div class="in"><span>… hier volgen Assortiment en Hoe het werkt …</span></div></div>',
    '<div id="assortiment">' + BLOCK + '</div>')

# ---------- review bar ----------
rep('<html lang="nl" class="m-n3 t-0 d-k lp-u fd-podpis">', '<html lang="nl" class="m-n3 t-0 d-k lp-u fd-podpis iz-d fp-1 sb-n">')


def btns(g, default, pairs):
    return ''.join('<button type="button" data-g="%s" data-v="%s" aria-pressed="%s">%s</button>' % (g, v, 'true' if v == default else 'false', l) for v, l in pairs)


rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g">'
    + btns('iz', 'd', [('0', '0 · Как есть'), ('b', 'B · Цвет сорта'), ('c', 'C · Карточка'), ('d', 'D · Общий фон'), ('dc', 'D+C')])
    + '</div><span class="sep"></span><div class="rv-g rv-fp">' + btns('fp', '1', [('1', 'Палитра 1 · Поле'), ('2', '2 · Цветение'), ('3', '3 · Листва'), ('4', '4 · Рассвет')])
    + '</div><span class="sep"></span><div class="rv-g">' + btns('sb', 'n', [('n', 'Субстрат: нет'), ('y', 'да')]) + '</div></div><div id="root">')

CSS = ('\n/* ===== homepage Assortiment block · «Сад» + изюминка (tools/build_assortiment4.py) ===== */\n'
       'body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}\n'
       '#assortiment{scroll-margin-top:120px;background:var(--page)}\n'
       + (D / 'tools' / 'as4.css').read_text())
rep('</head>', '<style>' + CSS + '</style></head>')
rep('<title>Waarom wij · De kweker</title>', '<title>Assortiment · изюминка</title>')
(D / 'assortiment-4.html').write_text(s)
print('assortiment-4.html', len(s), 'bytes;', len(V), 'varieties')
