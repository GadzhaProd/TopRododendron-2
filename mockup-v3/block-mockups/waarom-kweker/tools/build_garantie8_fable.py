# Mockup tool (not site code): garantie8-fable.html = garantie4.html with three more designs of the seal on the label
# (Fable, an experiment; the current seal stays on the main page). Only the seal changes. All carry "3 maanden",
# Top Rhododendrons, Otterlo, sinds 2001; no logo; moss ink, Newsreader + Manrope; every seal lies inside its own box
# (viewBox -4 -4 248 248, radius 124 from the centre 120,120).
#   zg-0 the seal as it is · zg-1 "Венок": a wreath of rhododendron leaves drawn in line · zg-2 "Круг": a clean typographic
#   roundel, no scallops, straight lines of type · zg-3 "Сургуч": a moss wax seal with an uneven edge and the impression
# Usage: python3 tools/build_garantie8_fable.py [dir]
import re, math, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'garantie4.html').read_text()
ARIA = 'Zegel: Top Rhododendrons, Otterlo, sinds 2001. 3 maanden aangroeigarantie'
def svg(cls, body):
    return f'<svg class="gt-seal zg {cls}" viewBox="-4 -4 248 248" role="img" aria-label="{ARIA}">{body}</svg>'
SERIF, SANS = 'Newsreader,Georgia,serif', 'Manrope,system-ui,sans-serif'

# ---- 1 · Венок: two sprays of leaves run up from the foot and meet at the top; the lettering inside ----
def leaf(adeg, tilt, L=17, w=5, r=110):
    a = math.radians(adeg)
    x, y = 120 + r * math.cos(a), 120 + r * math.sin(a)
    rot = adeg + tilt                          # a leaf points "up" at 0; adeg is the direction of growth up the right side
    return (f'<g transform="translate({x:.2f} {y:.2f}) rotate({rot:.1f})"><path d="M0 0C{w} {-L*.3:.1f} {w*.9:.1f} {-L*.72:.1f} 0 {-L}C{-w*.9:.1f} {-L*.72:.1f} {-w} {-L*.3:.1f} 0 0Z" fill="#3f4a37" fill-opacity=".16" stroke-width="1.2"/>'
            f'<path d="M0 -1.5V{-L + 4}" stroke-width=".7"/></g>')
half = '<path d="M%.2f %.2fA110 110 0 0 0 %.2f %.2f" stroke-width="1.2"/>' % (120 + 110 * math.cos(math.radians(80)), 120 + 110 * math.sin(math.radians(80)),
                                                                           120 + 110 * math.cos(math.radians(-80)), 120 + 110 * math.sin(math.radians(-80)))
for k in range(8):
    adeg = 70 - k * 20
    half += leaf(adeg, 36) + leaf(adeg, -36)
half += leaf(-80, 0, 15, 4.6)                  # the tip of the spray
leaves = half + '<g transform="translate(240 0) scale(-1 1)">' + half + '</g>'
W1 = ('<defs><path id="zg1-t" d="M45 120a75 75 0 0 1 150 0"/><path id="zg1-b" d="M31 120a89 89 0 0 0 178 0"/></defs>'
      '<g fill="none" stroke="#3f4a37" stroke-linecap="round" stroke-linejoin="round">' + leaves +
      '<circle cx="120" cy="120" r="58" stroke-width="1.1"/></g>'
      f'<g fill="#3f4a37"><text font-family="{SANS}" font-size="15" font-weight="700" letter-spacing="2.6"><textPath href="#zg1-t" startOffset="50%" text-anchor="middle">TOP RHODODENDRONS</textPath></text>'
      f'<text font-family="{SANS}" font-size="13.5" font-weight="700" letter-spacing="2.4"><textPath href="#zg1-b" startOffset="50%" text-anchor="middle">OTTERLO · SINDS 2001</textPath></text>'
      f'<text x="120" y="130" text-anchor="middle" font-family="{SERIF}" font-size="62" font-weight="500">3</text>'
      f'<text x="120" y="152" text-anchor="middle" font-family="{SERIF}" font-size="19" font-weight="500">maanden</text></g>')

# ---- 2 · Круг: a clean ring, straight lines of type, the "3" large ----
W2 = ('<g fill="none" stroke="#3f4a37"><circle cx="120" cy="120" r="121" stroke-width="2.6"/><circle cx="120" cy="120" r="113.5" stroke-width="1"/>'
      '<path d="M37.5 78H202.5M37.5 170H202.5" stroke-width="1"/></g>'
      f'<g fill="#3f4a37" text-anchor="middle"><text x="120" y="63" font-family="{SANS}" font-size="16.5" font-weight="700" letter-spacing=".3">Top Rhododendrons</text>'
      f'<text x="120" y="141" font-family="{SERIF}" font-size="74" font-weight="500">3</text>'
      f'<text x="120" y="162" font-family="{SERIF}" font-size="21" font-weight="500">maanden</text>'
      f'<text x="120" y="192" font-family="{SANS}" font-size="15.5" font-weight="600">Otterlo</text>'
      f'<text x="120" y="211" font-family="{SANS}" font-size="15.5" font-weight="600">sinds 2001</text></g>')

# ---- 3 · Сургуч: a disc of moss wax, pressed: an uneven edge, a sunk field, the type standing out light ----
pts = []
for k in range(72):
    t = 2 * math.pi * k / 72
    r = 114 + 4.2 * math.sin(3 * t + .6) + 3 * math.sin(5 * t + 2.1) + 2 * math.sin(8 * t + 4)
    pts.append((120 + r * math.cos(t), 120 + r * math.sin(t)))
edge = 'M%.1f %.1f' % pts[0]
for i in range(len(pts)):
    p0, p1, p2, p3 = pts[i - 1], pts[i], pts[(i + 1) % 72], pts[(i + 2) % 72]
    edge += 'C%.1f %.1f %.1f %.1f %.1f %.1f' % (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6, p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6, p2[0], p2[1])
W3 = ('<defs><radialGradient id="zg3-w" cx=".34" cy=".28" r=".85"><stop offset="0" stop-color="#6b7d5e"/><stop offset=".5" stop-color="#465340"/><stop offset="1" stop-color="#2c3527"/></radialGradient>'
      '<radialGradient id="zg3-f" cx=".5" cy=".5" r=".5"><stop offset=".86" stop-color="#3a4533"/><stop offset="1" stop-color="#2e3729"/></radialGradient>'
      '<path id="zg3-t" d="M50 120a70 70 0 0 1 140 0"/><path id="zg3-b" d="M38.5 120a81.5 81.5 0 0 0 163 0"/></defs>'
      f'<path d="{edge}Z" fill="url(#zg3-w)"/><path d="{edge}Z" fill="none" stroke="#252d20" stroke-width="1" opacity=".6"/>'
      '<circle cx="120" cy="120" r="93" fill="url(#zg3-f)"/><path d="M38 164A93 93 0 0 0 202 164" fill="none" stroke="#8a9c7b" stroke-width="1.4" opacity=".7"/>'
      '<path d="M202 76A93 93 0 0 0 38 76" fill="none" stroke="#1f261b" stroke-width="1.6" opacity=".6"/>'
      '<ellipse cx="78" cy="42" rx="26" ry="9" fill="#fff" opacity=".13" transform="rotate(-32 78 42)"/>'
      '<circle cx="120" cy="120" r="52" fill="none" stroke="#dfe6d2" stroke-width="1" opacity=".75"/>'
      f'<g fill="#eef1e4"><text font-family="{SANS}" font-size="14.5" font-weight="700" letter-spacing="2.2"><textPath href="#zg3-t" startOffset="50%" text-anchor="middle">TOP RHODODENDRONS</textPath></text>'
      f'<text font-family="{SANS}" font-size="13.5" font-weight="700" letter-spacing="2"><textPath href="#zg3-b" startOffset="50%" text-anchor="middle">OTTERLO · SINDS 2001</textPath></text>'
      f'<text x="120" y="130" text-anchor="middle" font-family="{SERIF}" font-size="58" font-weight="500">3</text>'
      f'<text x="120" y="150" text-anchor="middle" font-family="{SERIF}" font-size="18" font-weight="500">maanden</text></g>')

m = re.search(r'(<div class="gt-tag"><p class="gt-lbrand">Top Rhododendrons</p>)(<svg class="gt-seal .*?</svg>)', s, flags=re.S)
assert m and len(re.findall('<svg class="gt-seal', s)) == 1
s = s[:m.end()] + svg('zg1', W1) + svg('zg2', W2) + svg('zg3', W3) + s[m.end():]
CSS = '''/* ===== Review: more designs of the seal (Fable, an experiment). zg-0 now · zg-1 wreath · zg-2 roundel · zg-3 wax ===== */
body{padding-top:48px}header.fixed{top:48px}
@media (min-width:900px){ .gt-lab{top:calc(80px + 28px - 40px + 48px)} }
@media (min-width:900px) and (max-height:860px){ .gt-lab{top:calc(80px + 20px - 40px + 48px)} .gt-short{margin-top:8px;padding-top:8px} .gt-short li + li{margin-top:3px} }
.gt-tag .zg{display:none}
html:not(.zg-0) .gt-tag .gt-seal:not(.zg){display:none}
html.zg-1 .gt-tag .zg1,html.zg-2 .gt-tag .zg2,html.zg-3 .gt-tag .zg3{display:block}
html.zg-1 .gt-tag .zg1{transform:rotate(0deg);mix-blend-mode:normal}
html.zg-2 .gt-tag .zg2{transform:rotate(-5deg);mix-blend-mode:normal}
html.zg-3 .gt-tag .zg3{transform:rotate(7deg);mix-blend-mode:normal;filter:drop-shadow(0 1px 1px rgba(30,36,26,.45)) drop-shadow(0 5px 7px rgba(30,36,26,.28))}
'''
mh = re.search(r'<html lang="nl" class="([^"]*)">', s); assert mh and not any(c.startswith('zg-') for c in mh.group(1).split())
s = s.replace(mh.group(0), '<html lang="nl" class="' + mh.group(1) + ' zg-1">', 1)
def btn(v, name, on=False):
    return f'<button type="button" data-g="zg" data-v="{v}" aria-pressed="{"true" if on else "false"}">{v}<span class="l"> · {name}</span></button>'
BAR = '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Значок</i>' + btn(0, 'Сейчас') + btn(1, 'Венок', True) + btn(2, 'Круг') + btn(3, 'Сургуч') + '</div></div>'
assert '<div class="rv"' not in s and s.count('<div id="root">') == 1 and s.count('</head>') == 1
s = s.replace('<div id="root">', BAR + '<div id="root">').replace('</head>', '<style id="seal-fable-css">' + CSS + '</style></head>')
(D / 'garantie8-fable.html').write_text(s)
print('ok', len(s))
