# Mockup tool (not site code): garantie4-fable.html = garantie4.html with three designs of the plant label's cord (Fable).
# Only the cord and the hole change; the label, its tilt and the page stay as they are. The owner: the cord must visibly go
# THROUGH the hole and the label must hang on it. In all three the label hangs on a small pin (at the point it turns around),
# the cord is a closed loop over that pin, one part runs in front of the paper into the hole and one part behind the paper.
#   (round 2: the bar shows kd-2 with the knot, kd-4 and kd-5 without it, kd-3; kd-0 and kd-1 are no longer on the page)
#   kd-0 the cord of garantie4.html · kd-1 "Петля" (a lark's head: two strands out of the hole, a collar over the top edge)
#   kd-2 "Узел и люверс" (one loop tied with a knot, through a metal eyelet) · kd-3 "Прямой шнур" (a taut doubled cord, a paper ring)
# Geometry (SVG 120 x 180, as in garantie4): the label's top edge at y 128, the hole at 60,160, the pin at 60,40.
# Usage: python3 tools/build_garantie4_fable.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'garantie4.html').read_text()

JUTE = dict(o='#6b603d', b='#cbbd8f', t='#8a7d52', h='#ece3c2')
MOSS = dict(o='#333c2d', b='#6f8062', t='#414c38', h='#a9b89b')
DARK = dict(o='#2c3327', b='#56634b', t='#333c2d', h='#93a285')

def strand(d, w, p, dim=1.0, cap='round'):
    # a twisted cord: a dark edge, the body, the turns of the twist as soft bands, a light along the upper left side
    return (f'<g opacity="{dim}" stroke-linecap="{cap}"><path d="{d}" stroke="{p["o"]}" stroke-width="{w + 1.3:.1f}"/><path d="{d}" stroke="{p["b"]}" stroke-width="{w:.1f}"/>'
            f'<path d="{d}" stroke="{p["t"]}" stroke-width="{w:.1f}" stroke-dasharray=".9 2.1" stroke-linecap="butt" opacity=".34"/>'
            f'<path d="{d}" stroke="{p["h"]}" stroke-width="{w * .26:.1f}" opacity=".7" transform="translate({-w * .2:.2f} {-w * .08:.2f})"/></g>')

def shadow(d, w):
    return f'<path d="{d}" stroke="rgba(38,44,32,.42)" stroke-width="{w:.1f}" filter="url(#ID-bl)" transform="translate(1.7 2.3)"/>'

def hole(r, ring):
    # what is seen through the hole is the page behind the label, in shade; the paper has a thickness: dark under the top
    # rim (owner, round 3: no light crescent on the bottom rim, no inner ring on the eyelet: just the ring and the dark hole)
    return (ring +
            f'<circle cx="60" cy="160" r="{r}" fill="url(#ID-hol)"/>'
            f'<path d="M{60 - r + .8} 158.2A{r - .6} {r - .6} 0 0 1 {60 + r - .8} 158.2A{r + 2.2} {r + 1.2} 0 0 0 {60 - r + .8} 158.2Z" fill="rgba(28,33,24,.5)" filter="url(#ID-bs)"/>'
            f'<circle cx="60" cy="160" r="{r}" stroke="rgba(52,58,44,.55)" stroke-width=".9"/>')

def dive(xs):
    # where a strand goes down into the hole it turns away from us: it darkens and is gone under the rim
    return ''.join(f'<ellipse cx="{x}" cy="158.6" rx="3.6" ry="2.7" fill="#3d4337" filter="url(#ID-bs)"/>' for x in xs)

PIN = ('<ellipse cx="62.2" cy="43.6" rx="6.4" ry="5.6" fill="rgba(38,44,32,.4)" filter="url(#ID-bl)"/>'
       '<circle cx="60" cy="40" r="5.8" fill="url(#ID-pin)" stroke="#333c2d" stroke-width=".9"/>'
       '<ellipse cx="58.1" cy="37.9" rx="2.1" ry="1.5" fill="#fff" opacity=".55"/>')
DEFS = ('<defs><filter id="ID-bl" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="1.3"/></filter>'
        '<filter id="ID-bs" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation=".8"/></filter>'
        '<linearGradient id="ID-hol" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6d6b60"/><stop offset=".55" stop-color="#a9a699"/><stop offset="1" stop-color="#c9c6ba"/></linearGradient>'
        '<radialGradient id="ID-pin" cx=".36" cy=".3" r=".8"><stop offset="0" stop-color="#b7c3a8"/><stop offset=".55" stop-color="#6f8062"/><stop offset="1" stop-color="#3f4a37"/></radialGradient>'
        '<linearGradient id="ID-met" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f4f1e6"/><stop offset=".5" stop-color="#c3c1ad"/><stop offset="1" stop-color="#85846f"/></linearGradient>'
        '<clipPath id="ID-pap"><rect x="0" y="128.4" width="120" height="60"/></clipPath></defs>')
G = '<g fill="none" stroke-linecap="round" stroke-linejoin="round">'

def svg(n, back, front):
    b = f'<svg class="gt-cord gt-cord-b kc kc{n}" viewBox="0 0 120 180" aria-hidden="true">{G}{back}</g></svg>'
    f = f'<svg class="gt-cord kc kc{n}" viewBox="0 0 120 180" aria-hidden="true">{DEFS}{G}{front}</g></svg>'
    return b.replace('ID', f'kc{n}'), f.replace('ID', f'kc{n}')

LOOP = 'C52.4 80 51 53 55 42C57 36 63 36 65 42C69 53 67.6 80 61.6 90'      # the loop over the pin, from the knot and back
def knot(y, p):
    return (f'<ellipse cx="60" cy="{y}" rx="5.6" ry="4.5" fill="{p["b"]}" stroke="{p["o"]}" stroke-width="1.1" transform="rotate(-12 60 {y})"/>'
            f'<path d="M55.6 {y - .6}C58 {y + 2.4} 61.6 {y + 2.8} 64.6 {y + .6}M56.6 {y - 2.6}C59 {y - 1.2} 62 {y - 1} 64 {y - 2}" stroke="{p["o"]}" stroke-width="1"/>')

# ---- 1 · Петля: a lark's head. Two strands come out of the hole and run up the paper; the loop of the same cord comes over
#      the top edge from behind and holds them (the collar); above it a knot, then the loop over the pin ----
w = 3.2
L1, R1 = 'M57.3 157C57.2 148 57.3 138 57.5 128C57.6 116 57.8 106 58.3 97', 'M62.7 157C62.8 148 62.7 138 62.5 128C62.4 116 62.2 106 61.7 97'
COLL = 'M52.9 128.3C51.6 118.6 68.4 118.6 67.1 128.3'
b1 = strand('M52.9 124C52.7 130 52.8 136 53 142', w, JUTE) + strand('M67.1 124C67.3 130 67.2 136 67 142', w, JUTE)
f1 = (hole(9.2, '<circle cx="60" cy="160" r="14.6" fill="#efe9d6" stroke="rgba(63,74,55,.28)" stroke-width=".8"/>')
      + f'<g clip-path="url(#ID-pap)">{shadow(L1, w)}{shadow(R1, w)}</g>'
      + strand('M58.4 90' + LOOP, w, JUTE)
      + strand(L1, w, JUTE) + strand(R1, w, JUTE) + dive([57.3, 62.7])
      + f'<path d="{COLL}" stroke="rgba(38,44,32,.4)" stroke-width="{w}" filter="url(#ID-bs)" transform="translate(.6 1.8)"/>' + strand(COLL, w, JUTE, cap='butt')
      + knot(93, JUTE) + PIN)
# ---- 2 · Узел и люверс: one loop tied with a knot; one part runs down the front of the paper into a metal eyelet, the other
#      goes behind the top edge ----
w = 4
F2 = 'M58.6 95C54 105 54 118 56.6 128C58 136 58.8 146 59.2 157'
B2 = 'M61.4 95C66.4 105 67.4 118 65 128C64.4 132 63.8 137 63.4 142'
EYE = ('<circle cx="61" cy="161.4" r="14" fill="rgba(38,44,32,.3)" filter="url(#ID-bl)"/><circle cx="60" cy="160" r="13.4" fill="url(#ID-met)" stroke="rgba(52,58,44,.5)" stroke-width=".8"/>')
b2 = strand(B2, w, MOSS)
f2 = (hole(8.8, EYE) + f'<g clip-path="url(#ID-pap)">{shadow(F2, w)}</g>'
      + strand('M58.4 90' + LOOP, w, MOSS)
      + strand('M57.4 95C54.6 96.6 52.6 99 51.8 102.4', w - 1, MOSS) + strand('M62.8 95C65.6 96.4 67.6 98.6 68.6 101.8', w - 1, MOSS)
      + strand(F2, w, MOSS) + dive([59.3]) + knot(93, MOSS) + PIN)
# ---- 3 · Прямой шнур: a taut doubled cord from the pin straight down; the front part into the hole, the other behind the
#      paper; a paper ring keeps the hole from tearing ----
w = 3
F3 = 'M58.4 157C58.3 146 58.2 136 58 128C57.4 100 56.4 70 55.2 46'
B3 = 'M62.6 142C62.5 137 62.4 132 62.3 128C62.8 100 63.8 70 64.8 46'
TOP3 = 'M55.2 47C54.6 40 56.6 35.4 60 35.4C63.4 35.4 65.4 40 64.8 47'
RING = ('<circle cx="60.6" cy="160.8" r="15.6" fill="rgba(38,44,32,.22)" filter="url(#ID-bs)"/><circle cx="60" cy="160" r="15.4" fill="#ddd3ad" stroke="rgba(88,78,44,.5)" stroke-width=".8"/>')
b3 = strand(B3, w, DARK)
f3 = (hole(8.6, RING) + f'<g clip-path="url(#ID-pap)">{shadow(F3, w)}</g>' + strand(TOP3, w, DARK) + strand(F3, w, DARK) + dive([58.4]) + PIN)

# ---- 2а · Без узла, с перехлёстом: one closed loop over the pin, no knot. The two halves cross once where the knot was, so the
#      outline of variant 2 stays: the half that comes down on the right crosses over to the left and runs down the front of
#      the paper into the eyelet; the other half goes behind the top edge ----
w = 4
F4 = 'M60 36.2C63.8 36.2 65.8 40 66.2 46C66.8 60 65.2 80 60.8 91C58.4 97 54.4 107 55.2 119C55.7 125 57.6 137 59.2 157'
B4 = 'M60 36.2C56.2 36.2 54.2 40 53.8 46C53.2 60 54.8 80 59.2 91C61.6 97 65.8 107 65.6 119C65.5 123 64.9 126 64.5 128C64 132 63.6 137 63.4 142'
b4 = strand(B4, w, MOSS)
f4 = (hole(8.8, EYE) + f'<g clip-path="url(#ID-pap)">{shadow(F4, w)}</g>'
      + '<path d="M61.6 88C60.4 91 59.2 93.4 58 95.6" stroke="rgba(30,36,26,.5)" stroke-width="4" filter="url(#ID-bs)" transform="translate(1 1.4)"/>'
      + strand(F4, w, MOSS) + dive([59.3]) + PIN)
# ---- 2б · Без узла, простая петля: the same closed loop without the crossing: two taut strands from the pin, a narrow V;
#      the left one runs down the front into the eyelet, the right one goes behind the top edge ----
F5 = 'M58.9 157C58.8 146 58.6 136 58.2 128C57.2 100 55.6 70 54.4 47C53.8 40 56.4 35.6 60 35.6'
B5 = 'M60 35.6C63.6 35.6 66.2 40 65.6 47C64.6 70 63.4 100 62.9 128C62.9 132 63 137 63 142'
b5 = strand(B5, w, MOSS)
f5 = (hole(8.8, EYE) + f'<g clip-path="url(#ID-pap)">{shadow(F5, w)}</g>' + strand(F5, w, MOSS) + dive([58.9]) + PIN)

# ---- round 3: variant 2 with the join redone (the owner: the round knot is out of place; rework it) ----
def wraps(y0, n=5):
    # a whipping: a few tight turns of the same cord round both strands, a flat band instead of a ball
    turns = ''.join(strand(f'M54.6 {y0 + k * 2.9 + .9:.1f}L65.4 {y0 + k * 2.9 - .9:.1f}', 2.3, MOSS) for k in range(n))
    return f'<rect x="54" y="{y0 - 1}" width="13" height="{n * 2.9 + .6:.1f}" rx="2" fill="rgba(30,36,26,.45)" filter="url(#ID-bs)" transform="translate(1 1.4)"/>' + turns
# 2в · Обмотка: the two halves of the loop are bound together where the knot was
LP6 = 'M58.2 87C52.4 78 51 53 55 42C57 36 63 36 65 42C69 53 67.6 78 61.8 87'
F6 = 'M58.2 99C54.6 107 54.4 119 56.6 128C58 136 58.8 146 59.2 157'
B6 = 'M61.8 99C66 107 67 119 65 128C64.4 132 63.8 137 63.4 142'
MID6 = strand('M58.2 86V100', w, MOSS) + strand('M61.8 86V100', w, MOSS)
b6 = strand(B6, w, MOSS)
f6 = (hole(8.8, EYE) + f'<g clip-path="url(#ID-pap)">{shadow(F6, w)}</g>' + strand(LP6, w, MOSS) + strand(F6, w, MOSS) + MID6 + dive([59.3]) + wraps(87.2) + PIN)
# 2г · Обжим: a small metal sleeve pressed round both strands, the same metal as the eyelet
FER = ('<rect x="53.4" y="86.6" width="13.2" height="11.6" rx="2.8" fill="rgba(30,36,26,.4)" filter="url(#ID-bs)" transform="translate(1.2 1.6)"/>'
       '<rect x="53.4" y="86.6" width="13.2" height="11.6" rx="2.8" fill="url(#ID-met)" stroke="rgba(52,58,44,.7)" stroke-width=".9"/>'
       '<path d="M54.6 92.1H65.4" stroke="rgba(52,58,44,.55)" stroke-width=".9"/><path d="M54.8 93.2H65.2" stroke="rgba(255,255,255,.7)" stroke-width=".7"/>')
f7 = (hole(8.8, EYE) + f'<g clip-path="url(#ID-pap)">{shadow(F6, w)}</g>' + strand(LP6, w, MOSS) + strand(F6, w, MOSS) + MID6 + dive([59.3]) + FER + PIN)
# 2д · Обмотка у бирки: the same binding, low, just above the label: one long loop on the pin, a short V into the label
LP8 = 'M58.2 109C53 96 51 56 55 42C57 36 63 36 65 42C69 56 67 96 61.8 109'
F8 = 'M58.2 120C57.5 123 57.5 126 57.8 128C58.4 138 58.9 147 59.2 157'
B8 = 'M61.8 120C62.7 123 63 126 63 128C63 133 63.1 138 63.2 142'
b8 = strand(B8, w, MOSS)
f8 = (hole(8.8, EYE) + f'<g clip-path="url(#ID-pap)">{shadow(F8, w)}</g>' + strand(LP8, w, MOSS) + strand(F8, w, MOSS)
      + strand('M58.2 108V121', w, MOSS) + strand('M61.8 108V121', w, MOSS) + dive([59.3]) + wraps(108.4, 4) + PIN)

backs, fronts = zip(svg(2, b2, f2), svg(6, b6, f6), svg(7, b6, f7), svg(8, b8, f8), svg(4, b4, f4), svg(5, b5, f5), svg(3, b3, f3))
m = re.search(r'(<div class="gt-lab">)(<svg class="gt-cord gt-cord-b".*?</svg>)(<svg class="gt-cord".*?</svg>)(<div class="gt-tag">)', s, flags=re.S)
assert m and len(re.findall(r'<div class="gt-lab">', s)) == 1
s = s[:m.start()] + m.group(1) + m.group(2) + ''.join(backs) + m.group(3) + ''.join(fronts) + m.group(4) + s[m.end():]

CSS = '''/* ===== Review: the cord of the label (Fable). Only the cord and the hole differ ===== */
body{padding-top:48px}header.fixed{top:48px}
.kc{display:none}
html.kd-2 .kc2,html.kd-3 .kc3,html.kd-4 .kc4,html.kd-5 .kc5,html.kd-6 .kc6,html.kd-7 .kc7,html.kd-8 .kc8{display:block}
.gt-cord:not(.kc){display:none}
@media (min-width:900px){ .gt-lab{top:calc(80px + 20px - 40px + 48px)} }
@media (min-width:900px) and (max-height:860px){ .gt-lab{top:calc(80px + 12px - 40px + 48px)} }
'''
mh = re.search(r'<html lang="nl" class="([^"]*)">', s); assert mh and not any(c.startswith('kd-') for c in mh.group(1).split())
s = s.replace(mh.group(0), '<html lang="nl" class="' + mh.group(1) + ' kd-6">', 1)
BAR = ('<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Шнурок</i>'
       '<button type="button" data-g="kd" data-v="2" aria-pressed="false">2 · С узлом (было)</button>'
       '<button type="button" data-g="kd" data-v="6" aria-pressed="true">2в · Обмотка</button>'
       '<button type="button" data-g="kd" data-v="7" aria-pressed="false">2г · Обжим</button>'
       '<button type="button" data-g="kd" data-v="8" aria-pressed="false">2д · Обмотка у бирки</button>'
       '<button type="button" data-g="kd" data-v="4" aria-pressed="false">2а · Без узла, перехлёст</button>'
       '<button type="button" data-g="kd" data-v="5" aria-pressed="false">2б · Без узла, простая петля</button>'
       '<button type="button" data-g="kd" data-v="3" aria-pressed="false">3 · Прямой шнур</button></div></div>')
assert '<div class="rv"' not in s and s.count('<div id="root">') == 1 and s.count('</head>') == 1
s = s.replace('<div id="root">', BAR + '<div id="root">').replace('</head>', '<style id="cord-fable-css">' + CSS + '</style></head>')
(D / 'garantie4-fable.html').write_text(s)
print('ok', len(s))
