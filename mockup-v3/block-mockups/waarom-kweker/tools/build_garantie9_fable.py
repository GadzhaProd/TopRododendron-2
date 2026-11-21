# Mockup tool (not site code): garantie9-fable.html = garantie4.html with four treatments of the LETTERING of the embossed
# seal (Fable, an experiment). The owner: the seal is in relief, the text beside it looks flat; can the text be richer?
# The relief, the card and the page stay; only the seal's text group changes. Each seal keeps the main seal's box.
#   tx-0 as it is (flat moss ink)
#   tx-1 "Высокая печать": letterpress: the ink pressed into the paper (a shade inside the upper left edge of every letter,
#        a hairline of light under the lower right)
#   tx-2 "Глубокая тройка": the same, and the "3" larger and pressed deeper, its ink darker at the top
#   tx-3 "Слепые надписи": the arc lettering blind-embossed like the rings (tinted, no ink); only "3 maanden" printed
#   tx-4 "Фольга": moss foil: a quiet sheen runs across the letters
# FROZEN (21 Nov): the owner chose tx-2; it is now in seal_emboss() of tools/build_garantie4.py, so this script no longer
# applies to garantie4.html. Do not rebuild; garantie9-fable.html stays as the record of the round.
# Usage: python3 tools/build_garantie9_fable.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'garantie4.html').read_text()
m = re.search(r'<svg class="gt-seal".*?</svg>', s, flags=re.S); assert m and len(re.findall('<svg class="gt-seal', s)) == 1
seal = m.group(0)
g = re.search(r'<g fill="#3f4a37"><text.*?</g></svg>$', seal, flags=re.S); assert g
base, SERIF, SANS = seal[:g.start()], 'Newsreader,Georgia,serif', 'Manrope,system-ui,sans-serif'

def press(i, depth=1.0):
    # the ink pressed in: light under the lower right edge, the ink, a shade inside the upper left edge
    d = depth
    return (f'<filter id="{i}" x="-8%" y="-8%" width="116%" height="116%" color-interpolation-filters="sRGB">'
            f'<feOffset in="SourceAlpha" dx="{.8 * d:.2f}" dy="{.9 * d:.2f}" result="o"/><feFlood flood-color="#fff" flood-opacity=".95"/><feComposite in2="o" operator="in" result="hi"/>'
            '<feComponentTransfer in="SourceAlpha" result="inv"><feFuncA type="table" tableValues="1 0"/></feComponentTransfer>'
            f'<feOffset in="inv" dx="{.9 * d:.2f}" dy="{1 * d:.2f}"/><feGaussianBlur stdDeviation="{.35 * d:.2f}" result="ib"/>'
            f'<feFlood flood-color="#141a10" flood-opacity="{min(.95, .7 * d):.2f}"/><feComposite in2="ib" operator="in"/><feComposite in2="SourceAlpha" operator="in" result="sh"/>'
            '<feMerge><feMergeNode in="hi"/><feMergeNode in="SourceGraphic"/><feMergeNode in="sh"/></feMerge></filter>')
def arcs(u, attrs):
    return (f'<g {attrs}><text font-family="{SANS}" font-size="15" font-weight="700" letter-spacing="2.6"><textPath href="#{u}-st" startOffset="50%" text-anchor="middle">TOP RHODODENDRONS</textPath></text>'
            f'<text font-family="{SANS}" font-size="13.5" font-weight="700" letter-spacing="2.4"><textPath href="#{u}-sb" startOffset="50%" text-anchor="middle">OTTERLO · SINDS 2001</textPath></text></g>')
def hero(attrs, size=62, y=131, attrs3=''):
    return (f'<g {attrs}><text x="120" y="{y}" text-anchor="middle" font-family="{SERIF}" font-size="{size}" font-weight="500" {attrs3}>3</text>'
            f'<text x="120" y="152" text-anchor="middle" font-family="{SERIF}" font-size="19" font-weight="500">maanden</text></g>')
def make(n, body, defs=''):
    u = f'tx{n}'
    b = base.replace('class="gt-seal"', f'class="gt-seal tz tz{n}"').replace('gt-st', u + '-st').replace('gt-sb', u + '-sb').replace('gt-ss', u + '-ss')
    return b.replace('</defs>', defs.replace('ID', u) + '</defs>', 1) + body.replace('ID', u) + '</svg>'

T1 = make(1, arcs('tx1', 'fill="#3a4532" filter="url(#ID-p)"') + hero('fill="#3a4532" filter="url(#ID-p)"'), press('ID-p'))
T2 = make(2, arcs('tx2', 'fill="#3a4532" filter="url(#ID-p)"')
          + f'<g filter="url(#ID-d)"><text x="120" y="132" text-anchor="middle" font-family="{SERIF}" font-size="68" font-weight="500" fill="url(#ID-g)">3</text></g>'
          + f'<g fill="#3a4532" filter="url(#ID-p)"><text x="120" y="153" text-anchor="middle" font-family="{SERIF}" font-size="19" font-weight="500">maanden</text></g>',
          press('ID-p') + press('ID-d', 1.7) + '<linearGradient id="ID-g" gradientUnits="userSpaceOnUse" x1="0" y1="86" x2="0" y2="134"><stop offset="0" stop-color="#27301f"/><stop offset="1" stop-color="#4c5b41"/></linearGradient>')
EMB = ('<g filter="url(#ID-ss)" transform="translate(1 1.1)">' + arcs('tx3', 'fill="rgba(40,50,32,.8)"') + '</g>'
       '<g filter="url(#ID-ss)" transform="translate(-.9 -1)">' + arcs('tx3', 'fill="#fff"') + '</g>' + arcs('tx3', 'fill="#8d9a80"'))
T3 = make(3, EMB + hero('fill="#3a4532" filter="url(#ID-p)"'), press('ID-p'))
T4 = make(4, arcs('tx4', 'fill="url(#ID-f)" filter="url(#ID-p)"') + hero('fill="url(#ID-f)" filter="url(#ID-p)"'),
          press('ID-p', .7) + '<linearGradient id="ID-f" gradientUnits="userSpaceOnUse" x1="20" y1="30" x2="220" y2="210"><stop offset="0" stop-color="#2f3a28"/><stop offset=".5" stop-color="#3f4d35"/>'
          '<stop offset=".66" stop-color="#8a9b79"/><stop offset=".74" stop-color="#55654a"/><stop offset=".9" stop-color="#2f3a28"/><stop offset="1" stop-color="#4f5f44"/></linearGradient>')
s = s[:m.end()] + T1 + T2 + T3 + T4 + s[m.end():]
CSS = '''/* ===== Review: the lettering of the embossed seal (Fable, an experiment). tx-0 now · tx-1..4 ===== */
body{padding-top:48px}header.fixed{top:48px}
@media (min-width:900px){ .gt-lab{top:calc(80px + 28px - 40px + 48px)} }
@media (min-width:900px) and (max-height:860px){ .gt-lab{top:calc(80px + 20px - 40px + 48px)} .gt-short{margin-top:8px;padding-top:8px} .gt-short li + li{margin-top:3px} }
@media (max-width:520px){ .rv{justify-content:flex-start} }
.gt-tag .tz{display:none}
html:not(.tx-0) .gt-tag .gt-seal:not(.tz){display:none}
html.tx-1 .gt-tag .tz1,html.tx-2 .gt-tag .tz2,html.tx-3 .gt-tag .tz3,html.tx-4 .gt-tag .tz4{display:block}
'''
mh = re.search(r'<html lang="nl" class="([^"]*)">', s); assert mh and not any(c.startswith('tx-') for c in mh.group(1).split())
s = s.replace(mh.group(0), '<html lang="nl" class="' + mh.group(1) + ' tx-2">', 1)
def btn(v, name, on=False):
    return f'<button type="button" data-g="tx" data-v="{v}" aria-pressed="{"true" if on else "false"}">{v}<span class="l"> · {name}</span></button>'
BAR = ('<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Надписи</i>' + btn(0, 'Сейчас') + btn(1, 'Высокая печать') + btn(2, 'Глубокая тройка', True)
       + btn(3, 'Слепые надписи') + btn(4, 'Фольга') + '</div></div>')
assert '<div class="rv"' not in s and s.count('<div id="root">') == 1 and s.count('</head>') == 1
s = s.replace('<div id="root">', BAR + '<div id="root">').replace('</head>', '<style id="text-fable-css">' + CSS + '</style></head>')
(D / 'garantie9-fable.html').write_text(s)
print('ok', len(s))
