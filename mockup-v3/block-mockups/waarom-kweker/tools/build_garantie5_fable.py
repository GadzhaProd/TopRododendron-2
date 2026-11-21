# Mockup tool (not site code): garantie5-fable.html = garantie4.html with two directions for the brand identity of the
# label (Fable, 21 Nov). The owner: "either the card or the badge itself in our house style: make two versions".
#   bk-0 as it is now
#   bk-1 "A · Бирка": the label carries the identity: the logo lockup of the header (the mark and the wordmark), the paper in
#        the soft light of our surfaces (sage, butter, a faint blush), the tip of the label dipped in moss. The seal stays.
#   bk-2 "B · Значок": the label stays; the seal becomes a badge in the shape of the logo mark (the rounded square), in moss,
#        with the monogram, "3 maanden" in Newsreader and the name and place in straight Manrope lines (legible on the phone)
#   bk-3 "B2 · Значок контурный": the same badge drawn in line, like a stamp in the brand's own shape
# The cord is 2б everywhere (it is in garantie4.html). Usage: python3 tools/build_garantie5_fable.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'garantie4.html').read_text()

MARK = '<path d="M12 13h16M20 13v15" stroke="{c}" stroke-width="2.6" stroke-linecap="round" fill="none"/><path d="M20 28c0-6 3.5-9.5 9-9.5 0 6-3.5 9.5-9 9.5Z" fill="{c}"/>'
LOCK = ('<p class="bk-lock"><svg viewBox="0 0 40 40" aria-hidden="true"><rect x="1" y="1" width="38" height="38" rx="11" fill="#141413"/>'
        + MARK.format(c='#f1efea') + '</svg><span>Top Rhododendrons</span></p>')
LABEL_ARIA = 'Keurmerk: Top Rhododendrons, Otterlo, sinds 2001. 3 maanden aangroeigarantie'
TXT = ('<text x="120" y="139" text-anchor="middle" font-family="Newsreader,Georgia,serif" font-size="84" font-weight="500" fill="{c}">3</text>'
       '<text x="120" y="164" text-anchor="middle" font-family="Newsreader,Georgia,serif" font-size="24" font-weight="500" fill="{c}">maanden</text>'
       '<text x="120" y="192" text-anchor="middle" font-family="Manrope,system-ui,sans-serif" font-size="17" font-weight="700" letter-spacing=".2" fill="{c}">Top Rhododendrons</text>'
       '<text x="120" y="213" text-anchor="middle" font-family="Manrope,system-ui,sans-serif" font-size="16" font-weight="500" fill="{c}" opacity="{o}">Otterlo · sinds 2001</text>')
# B: the solid badge: the logo mark's rounded square in moss, everything on it in the page colour
B1 = ('<svg class="gt-seal bz bz2" viewBox="0 0 240 240" role="img" aria-label="' + LABEL_ARIA + '">'
      '<rect x="4" y="4" width="232" height="232" rx="67" fill="#3f4a37"/><rect x="12.5" y="12.5" width="215" height="215" rx="59" fill="none" stroke="#f1efea" stroke-width="1.2" opacity=".5"/>'
      '<g transform="translate(96 22) scale(1.2)">' + MARK.format(c='#f1efea') + '</g>' + TXT.format(c='#f6f4ee', o='.92') + '</svg>')
# B2: the same badge in line: two rounded squares, the mark as on the header (solid, small), the type in moss
B2 = ('<svg class="gt-seal bz bz3" viewBox="0 0 240 240" role="img" aria-label="' + LABEL_ARIA + '">'
      '<rect x="4" y="4" width="232" height="232" rx="67" fill="none" stroke="#3f4a37" stroke-width="2.4"/><rect x="12" y="12" width="216" height="216" rx="59" fill="none" stroke="#3f4a37" stroke-width="1"/>'
      '<g transform="translate(98.4 24) scale(1.08)"><rect x="1" y="1" width="38" height="38" rx="11" fill="#3f4a37"/>' + MARK.format(c='#fbfaf8') + '</g>'
      + TXT.format(c='#3f4a37', o='1').replace('fill="#3f4a37">Top Rhododendrons', 'fill="#141413">Top Rhododendrons') + '</svg>')

m = re.search(r'(<div class="gt-tag">)(<p class="gt-lbrand">Top Rhododendrons</p>)(<svg class="gt-seal .*?</svg>)', s, flags=re.S)
assert m and s.count('<div class="gt-tag">') == 1
s = s[:m.start()] + m.group(1) + m.group(2) + LOCK + m.group(3) + B1 + B2 + s[m.end():]

CSS = '''/* ===== Review: the label in the house style (Fable). bk-0 now · bk-1 the label · bk-2 / bk-3 the badge ===== */
body{padding-top:48px}header.fixed{top:48px}
@media (min-width:900px){ .gt-lab{top:calc(80px + 28px - 40px + 48px)} }
@media (min-width:900px) and (max-height:860px){ .gt-lab{top:calc(80px + 20px - 40px + 48px)} .gt-tag{padding:50px 20px 64px} .gt-short{margin-top:8px;padding-top:8px} .gt-short li + li{margin-top:2px} .gt-lpdf{margin-top:2px} }
@media (max-width:520px){ .rv{justify-content:flex-start} }
.bk-lock,.bz{display:none}
/* ---- A: the label carries the identity ---- */
html.bk-1 .gt-lbrand{display:none}
html.bk-1 .bk-lock{display:inline-flex;align-items:center;gap:9px;margin:0;font-family:var(--font-display,Manrope),system-ui,sans-serif;font-size:var(--t-body);line-height:1;font-weight:600;letter-spacing:-.02em;color:#141413}
html.bk-1 .bk-lock svg{width:28px;height:28px;flex:none}
html.bk-1 .gt-tag{background:
  radial-gradient(ellipse 80% 34% at 12% 6%,#dee4d1 0%,transparent 72%),
  radial-gradient(ellipse 70% 30% at 96% 34%,rgba(236,214,210,.75) 0%,transparent 72%),
  radial-gradient(ellipse 90% 34% at 30% 74%,#eae1bf 0%,transparent 74%),
  #f4f2ea}
/* the tip of the label, dipped in moss */
html.bk-1 .gt-tag::after{content:"";position:absolute;left:0;right:0;bottom:0;height:60px;background:#3f4a37}
html.bk-1 .gt-short{border-top-color:rgba(63,74,55,.3)}
html.bk-1 .gt-short li{color:#33322e}
/* ---- B: the badge ---- */
html:is(.bk-2,.bk-3) .gt-tag .gt-seal:not(.bz){display:none}
/* the badge carries the name itself, so the line above it goes */
html:is(.bk-2,.bk-3) .gt-lbrand{display:none}
html:is(.bk-2,.bk-3) .gt-tag .bz{margin-top:0}
html.bk-2 .gt-tag .bz2,html.bk-3 .gt-tag .bz3{display:block;mix-blend-mode:normal;width:min(100%,196px);transform:rotate(-4deg)}
@media (min-width:900px) and (max-height:860px){ html.bk-2 .gt-tag .bz2,html.bk-3 .gt-tag .bz3{width:138px} }
@media (max-width:899.98px){ html.bk-2 .gt-tag .bz2,html.bk-3 .gt-tag .bz3{width:208px} }
'''
mh = re.search(r'<html lang="nl" class="([^"]*)">', s); assert mh and not any(c.startswith('bk-') for c in mh.group(1).split())
s = s.replace(mh.group(0), '<html lang="nl" class="' + mh.group(1) + ' bk-1">', 1)
def btn(v, code, name, on=False):
    return f'<button type="button" data-g="bk" data-v="{v}" aria-pressed="{"true" if on else "false"}">{code}<span class="l"> · {name}</span></button>'
BAR = ('<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Фирменный стиль</i>' + btn(0, '0', 'Сейчас') + btn(1, 'A', 'Бирка', True)
       + btn(2, 'B', 'Значок') + btn(3, 'B2', 'Значок контурный') + '</div></div>')
assert '<div class="rv"' not in s and s.count('<div id="root">') == 1 and s.count('</head>') == 1
s = s.replace('<div id="root">', BAR + '<div id="root">').replace('</head>', '<style id="brand-fable-css">' + CSS + '</style></head>')
(D / 'garantie5-fable.html').write_text(s)
print('ok', len(s))
