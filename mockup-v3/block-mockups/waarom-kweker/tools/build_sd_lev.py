# Mockup tool (not site code): sd-lev.html = the main mockup with delivery and payment shown by the prices, before the
# cart (audit item 2). Facts from the owner, 15 Nov, provisional until the company owner confirms them (16 Nov): delivery
# in the Netherlands only, with own transport; cost by distance and volume; the day by agreement; pick-up in Otterlo;
# payment by iDEAL, bank transfer, or card or cash on receipt; businesses on invoice. All new Dutch copy is a DRAFT.
# Owner, 16 Nov: option 1 (one line under the prices) plus the reassurance "u ziet de kosten vóór u betaalt"; the link to
# all plants is now a pill in the bottom right corner, so the line shares that bottom row (line left, pill right).
#   html.lv-0  как сейчас (the pill alone)
#   html.lv-1  строка + пилюля: "Bezorgen … · Afhalen … · Betalen …" on the left of the pill; on phone, three lines above it
# The details (cost by distance and volume, how the day is agreed, the pick-up step) belong in Hoe het werkt.
# Usage: python3 tools/build_sd_lev.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

L1 = ('<div class="lv"><ul aria-label="Bezorgen en betalen">'
      '<li><b>Bezorgen</b> in heel Nederland, u ziet de kosten <span>vóór u betaalt</span></li>'
      '<li><b>Afhalen</b> in Otterlo</li>'
      '<li><b>Betalen</b> met iDEAL, overboeking of bij ontvangst</li></ul></div>')
rep('<div class="sd-ft">', '<div class="sd-ft">' + L1)

CSS = r'''
/* ===== delivery and payment by the prices (audit item 2, review 16 Nov) ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
.lv{display:none}
/* the facts fill the bottom row left of the pill. Each fact stays whole; a dot separates them, and the dot that would
   start a line is clipped (the list is pulled left by one dot's width inside a wrapper with overflow:hidden), so no dot
   ever dangles at either end of a line */
html.lv-1 .lv{display:block;flex:1 1 auto;min-width:0;overflow:hidden;font-size:15px;line-height:1.55;color:var(--ink2)}
.lv ul{display:flex;flex-wrap:wrap;margin:0 0 0 -1.4em;padding:0;list-style:none}
.lv li{white-space:nowrap}
.lv li span{white-space:nowrap}
.lv li::before{content:"·";display:inline-block;width:1.4em;text-align:center;color:var(--soft)}
.lv b{font-weight:600;color:var(--ink)}
@media (max-width:767px){
  /* tablet portrait and phone: the facts as three lines above the pill */
  .sd-ft{flex-direction:column;align-items:flex-end}
  html.lv-1 .lv{align-self:stretch;margin:0 0 20px;overflow:visible;font-size:14.5px}
  .lv ul{display:block;margin:0}
  .lv li{white-space:normal;text-wrap:pretty}
  .lv li + li{margin-top:4px}
  .lv li::before{display:none}
}
@media (max-width:599px){ .sd-ft{align-items:stretch} html.lv-1 .sd-ft{margin-top:8px} }
'''
rep('</head>', '<style id="sd-lev">' + CSS + '</style></head>')
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Доставка и оплата</i>'
    '<button type="button" data-g="lv" data-v="0" aria-pressed="false">0 · Сейчас</button>'
    '<button type="button" data-g="lv" data-v="1" aria-pressed="true">1 · Строка + пилюля</button></div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} lv-1">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Доставка и оплата</title>', 1)
(D / 'sd-lev.html').write_text(s)
print('ok', len(s))
