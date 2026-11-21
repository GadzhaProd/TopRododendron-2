# Mockup tool (not site code): garantie5-fable.html = garantie4.html with two directions for colour on the label
# (Fable, 21 Nov, round 2). The owner: no logo on the label; the round seal stays as it is; either the WHOLE card in colour,
# or the card light and only the seal in colour, "the same seal, a blurred glow of our colours".
#   bk-0 as it is now
#   bk-1 "A1 · Цветная бирка, светлая": the whole card in a soft blurred light of the palette (sage, blush, butter), pale
#   bk-2 "A2 · Цветная бирка, насыщенная": the same, deeper: the card is clearly coloured from edge to edge
#   bk-3 "B1 · Цветной значок": the card light; the glow fills the seal's disc, the moss rings and lettering on top
#   bk-4 "B2 · Значок с ореолом": the same, and a soft halo of the same colours round the seal
# The cord is 2б everywhere (it is in garantie4.html). Usage: python3 tools/build_garantie5_fable.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'garantie4.html').read_text()

# the seal gets a wrapper (it carries the size and the tilt), so a glow can lie under the ink
m = re.search(r'(<div class="gt-tag"><p class="gt-lbrand">Top Rhododendrons</p>)(<svg class="gt-seal .*?</svg>)', s, flags=re.S)
assert m and s.count('<div class="gt-tag">') == 1
s = s[:m.start()] + m.group(1) + '<span class="bk-sw">' + m.group(2) + '</span>' + s[m.end():]

CSS = '''/* ===== Review: colour on the label (Fable, round 2). bk-0 now · bk-1/2 the whole card · bk-3/4 only the seal ===== */
body{padding-top:48px}header.fixed{top:48px}
@media (min-width:900px){ .gt-lab{top:calc(80px + 28px - 40px + 48px)} }
@media (min-width:900px) and (max-height:860px){ .gt-lab{top:calc(80px + 20px - 40px + 48px)} .gt-tag{padding:50px 20px 64px} .gt-short{margin-top:8px;padding-top:8px} .gt-short li + li{margin-top:2px} .gt-lpdf{margin-top:2px} }
@media (max-width:520px){ .rv{justify-content:flex-start} }
/* the wrapper takes over the seal's box; without a variant it changes nothing */
.gt-tag .bk-sw{position:relative;display:block;width:min(100%,184px);margin:12px auto 0;transform:rotate(6deg)}
.gt-tag .bk-sw .gt-seal{width:100%;margin:0;transform:none;position:relative}
@media (min-width:900px) and (max-height:860px){ .gt-tag .bk-sw{width:140px;margin-top:8px} .gt-tag .bk-sw .gt-seal{width:100%;margin:0} }

/* ---- A: the whole card in colour ---- */
html.bk-1 .gt-tag{background:
  radial-gradient(ellipse 90% 30% at 8% 4%,#dee4d1 0%,transparent 72%),
  radial-gradient(ellipse 80% 26% at 100% 32%,rgba(236,214,210,.85) 0%,transparent 72%),
  radial-gradient(ellipse 100% 30% at 18% 66%,#eae1bf 0%,transparent 74%),
  radial-gradient(ellipse 90% 26% at 92% 96%,#e4e9d8 0%,transparent 72%),
  #f4f2ea}
html.bk-2 .gt-tag{background:
  radial-gradient(ellipse 110% 34% at 0% 0%,#cfdabd 0%,transparent 74%),
  radial-gradient(ellipse 95% 30% at 104% 30%,#edcfc9 0%,transparent 74%),
  radial-gradient(ellipse 120% 34% at 10% 64%,#e6d9a6 0%,transparent 76%),
  radial-gradient(ellipse 110% 30% at 100% 98%,#d3ddc2 0%,transparent 74%),
  #ebece3}
html:is(.bk-1,.bk-2) .gt-short{border-top-color:rgba(63,74,55,.3)}
html:is(.bk-1,.bk-2) .gt-short li{color:#33322e}

/* ---- B: only the seal in colour: the glow fills the disc inside the outer ring (r 104 of 120) ---- */
html:is(.bk-3,.bk-4) .bk-sw::before{content:"";position:absolute;inset:6.67%;border-radius:50%;background:
  radial-gradient(ellipse 62% 58% at 24% 22%,#cfdbbb 0%,transparent 72%),
  radial-gradient(ellipse 56% 54% at 84% 36%,#efccc6 0%,transparent 72%),
  radial-gradient(ellipse 70% 56% at 46% 92%,#e8d99c 0%,transparent 74%),
  #eef0e3}
html.bk-4 .bk-sw::after{content:"";position:absolute;z-index:-1;inset:-16%;border-radius:50%;filter:blur(16px);opacity:.9;background:
  radial-gradient(ellipse 60% 56% at 22% 22%,#cfdbbb 0%,transparent 72%),
  radial-gradient(ellipse 56% 54% at 86% 38%,#efccc6 0%,transparent 72%),
  radial-gradient(ellipse 70% 54% at 46% 92%,#e8d99c 0%,transparent 74%)}
html.bk-4 .gt-tag{isolation:isolate}
'''
mh = re.search(r'<html lang="nl" class="([^"]*)">', s); assert mh and not any(c.startswith('bk-') for c in mh.group(1).split())
s = s.replace(mh.group(0), '<html lang="nl" class="' + mh.group(1) + ' bk-2">', 1)
def btn(v, code, name, on=False):
    return f'<button type="button" data-g="bk" data-v="{v}" aria-pressed="{"true" if on else "false"}">{code}<span class="l"> · {name}</span></button>'
BAR = ('<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Цвет</i>' + btn(0, '0', 'Сейчас') + btn(1, 'A1', 'Бирка, светлая')
       + btn(2, 'A2', 'Бирка, насыщенная', True) + btn(3, 'B1', 'Цветной значок') + btn(4, 'B2', 'Значок с ореолом') + '</div></div>')
assert '<div class="rv"' not in s and s.count('<div id="root">') == 1 and s.count('</head>') == 1
s = s.replace('<div id="root">', BAR + '<div id="root">').replace('</head>', '<style id="brand-fable-css">' + CSS + '</style></head>')
(D / 'garantie5-fable.html').write_text(s)
print('ok', len(s))
