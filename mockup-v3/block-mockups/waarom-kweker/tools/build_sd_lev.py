# Mockup tool (not site code): sd-lev.html = the main mockup with delivery and payment shown by the prices, before the
# cart (audit item 2). Facts from the owner, 15 Nov: delivery in the Netherlands only, with own transport; cost by distance
# and volume; the day by agreement; pick-up in Otterlo; payment by iDEAL, bank transfer, or card or cash on receipt;
# businesses on invoice. All new Dutch copy is a DRAFT.
#   html.lv-0  как сейчас (nothing by the prices)
#   html.lv-1  строка под ценами: one quiet line under the grid, "Bezorgen … · Afhalen … · Betalen …"; on phone, three lines
#   html.lv-2  три факта: a short label | text list under the grid, three columns on desktop, stacked on phone
# The details (how the day is agreed, the pick-up step) belong in Hoe het werkt, which is still a placeholder.
# Usage: python3 tools/build_sd_lev.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

L1 = ('<p class="lv lv-1x"><span><b>Bezorgen</b> in heel Nederland, kosten naar afstand en aantal</span>'
      '<span class="lv-dot" aria-hidden="true"> · </span><span><b>Afhalen</b> in Otterlo</span>'
      '<span class="lv-dot" aria-hidden="true"> · </span><span><b>Betalen</b> met iDEAL, overboeking of bij ontvangst</span></p>')
L2 = ('<dl class="lv lv-2x">'
      '<div><dt>Bezorgen</dt><dd>In heel Nederland, met eigen transport. De kosten hangen af van afstand en aantal; '
      'de dag spreken we met u af.</dd></div>'
      '<div><dt>Afhalen</dt><dd>In Otterlo: wij zetten uw bestelling klaar.</dd></div>'
      '<div><dt>Betalen</dt><dd>iDEAL, overboeking, of pin of contant bij ontvangst. Zakelijk op factuur.</dd></div>'
      '</dl>')
# the grid is the last thing in the assortment block: put the options right after it
m = re.search(r'(<div class="sd-grid">.*?</div>)(</div></section>)', s, re.S)
assert m and s.count(m.group(0)) == 1
s = s.replace(m.group(0), m.group(1) + L1 + L2 + m.group(2), 1)

CSS = r'''
/* ===== delivery and payment by the prices (audit item 2, review 15 Nov) ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
.lv{display:none;margin:0}
html.lv-1 .lv-1x{display:block}
html.lv-2 .lv-2x{display:grid}
.lv b,.lv dt{font-weight:600;color:var(--ink)}

/* 1 · one quiet line under the prices, on the cards' left edge */
.lv-1x{margin-top:clamp(28px,3vw,44px);font-size:15px;line-height:1.55;color:var(--ink2);text-wrap:pretty}
.lv-1x > span:not(.lv-dot){white-space:nowrap}
.lv-dot{color:var(--soft);padding:0 .35em}

/* 2 · three facts: label above a short text, on the grid's columns */
.lv-2x{margin-top:clamp(32px,3.4vw,52px);padding-top:clamp(18px,1.8vw,24px);border-top:1px solid rgba(20,20,19,.12);
  grid-template-columns:repeat(3,minmax(0,1fr));column-gap:clamp(24px,3vw,56px);row-gap:18px}
.lv-2x dt{font-size:14px;line-height:1.4}
.lv-2x dd{margin:4px 0 0;max-width:36ch;font-size:15px;line-height:1.5;color:var(--ink2);text-wrap:pretty}

@media (max-width:999px){
  /* tablet and phone: one fact per line, no dots (a dot never dangles at a line end) */
  .lv-1x > span:not(.lv-dot){display:block;white-space:normal}
  .lv-1x > span + .lv-dot + span{margin-top:4px}
  .lv-dot{display:none}
}
@media (max-width:767px){
  .lv-1x{font-size:14.5px}
  .lv-2x{grid-template-columns:1fr;row-gap:14px}
  .lv-2x dd{max-width:none;font-size:14.5px}
}
'''
rep('</head>', '<style id="sd-lev">' + CSS + '</style></head>')
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Доставка и оплата</i>'
    '<button type="button" data-g="lv" data-v="0" aria-pressed="false">0 · Сейчас</button>'
    '<button type="button" data-g="lv" data-v="1" aria-pressed="true">1 · Строка под ценами</button>'
    '<button type="button" data-g="lv" data-v="2" aria-pressed="false">2 · Три факта</button></div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} lv-1">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Доставка и оплата</title>', 1)
(D / 'sd-lev.html').write_text(s)
print('ok', len(s))
