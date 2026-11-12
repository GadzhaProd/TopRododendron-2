# Mockup tool (not site code): assortiment-6.html = the main mockup with more treatments of the Assortiment heading corner
# (owner, 11 Nov: "между заголовком и кнопкой очень много места, там пустота посередине"). Follows assortiment-5.html.
#   html.hf-0  как сейчас: the heading is the grid's first cell, the button at the bottom of the cell (the void in the middle)
#   html.hf-1  заголовок над сеткой (= hd-1 of assortiment-5.html): heading row full width, 4 columns of 7 cards + the link tile
#   html.hf-a  «Четыре размера»: the heading stays the first cell; the void is filled with what the cards do not say: the four
#              sizes with their price range across the seven varieties (from content.ts). The lead drops "van 40 tot 120 cm"
#              because the list right under it shows exactly that. Tablet: same cell, the tile closes the grid. Phone: 2 x 2.
#   html.hf-b  «Размеры в конце»: heading row above the grid (H2 at the Waarom wij size, lead on its baseline); the grid's
#              closing cell is no longer an empty link tile but the price-per-size panel with the filled button.
#              4 columns = 7 + panel; 3 columns = 7 + panel over two columns; 2 columns = 7 + panel.
# The size ranges are computed from mockup-v3/src/data/content.ts (min and max price per size over the seven varieties).
# Usage: python3 tools/build_assortiment6.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

# ---- the four sizes with their price range, from content.ts ----
ts = (D / '..' / '..' / 'src' / 'data' / 'content.ts').read_text()
ts = ts[:ts.index('export const parsePrice')] if 'export const parsePrice' in ts else ts
named = {m.group(1): m.group(2) for m in re.finditer(r'const (sizes\w+): Size\[\] = (\[.*?\])\n', ts)}
lists = re.findall(r'\n\s+sizes: (sizes\w+|\[\{.*?\}\]),', ts)
assert len(lists) == 7, len(lists)
rng = {}
for l in lists:
    for label, price in re.findall(r"label: '([^']+)', price: '([\d,]+)'", named.get(l, l)):
        rng.setdefault(label, []).append(int(float(price.replace(',', '.'))))
assert list(rng) == ['40–60 cm', '60–80 cm', '80–100 cm', '100–120 cm'] and all(len(v) == 7 for v in rng.values()), rng
rows = ''.join(f'<div><dt>{k.replace(" ", "&nbsp;")}</dt><dd>€&nbsp;{min(v)}–{max(v)}</dd></div>' for k, v in rng.items())
NOTE = 'Per plant, met kluit. De prijs verschilt per soort.'

# ---- markup: new elements are hidden unless their option is on ----
rep('Elke soort is er in vier maten, van 40 tot 120&nbsp;cm. U bestelt vanaf 1&nbsp;plant.</p>',
    'Elke soort is er in vier maten<span class="sd-rng">, van 40 tot 120&nbsp;cm</span>. U bestelt vanaf 1&nbsp;plant.</p>'
    f'<dl class="sd-mt">{rows}</dl><p class="sd-mn">{NOTE}</p>')
rep('<a class="sd-tile" href="#assortiment"><span>Alle zeven soorten, maten en prijzen</span>',
    '<a class="sd-tile" href="#assortiment"><span>Alle zeven soorten, maten en prijzen</span>'
    f'<strong class="sd-th">Prijs per maat</strong><dl class="sd-mt">{rows}</dl><em class="sd-mn">{NOTE}</em>')

CSS = r'''
/* ===== Assortiment heading corner, review 2 (12 Nov) ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
.sd-mt,.sd-mn,.sd-th{display:none;margin:0;font-style:normal}

/* shared: the size list. Hairline rows straight on the field, no panel of its own */
.sd-mt div{display:flex;justify-content:space-between;align-items:baseline;gap:12px;padding:9px 0;border-top:1px solid rgba(20,20,19,.16)}
.sd-mt div:last-child{border-bottom:1px solid rgba(20,20,19,.16)}
.sd-mt dt{font-size:15px;line-height:1.3;color:var(--ink2);white-space:nowrap}
.sd-mt dd{margin:0;font-size:17px;line-height:1.3;font-weight:600;letter-spacing:-.02em;color:var(--moss);font-variant-numeric:tabular-nums;white-space:nowrap}
.sd-mn{font-size:13px;line-height:1.4;color:var(--ink2)}

/* 1 · заголовок над сеткой (hd-1 of assortiment-5.html) */
html.hf-1 .sd-hd{grid-column:1/-1;grid-row:auto;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,auto);column-gap:clamp(32px,5vw,96px);
  align-items:end;padding:0 0 clamp(32px,3.4vw,52px)}
html.hf-1 .sd-hd h2{font-size:clamp(34px,4.2vw,58px);line-height:1.04;letter-spacing:-.035em}
html.hf-1 .sd-lead{margin:0!important;max-width:34ch;padding-bottom:.35em}
html.hf-1 .sd-hd .sd-all{display:none}
html.hf-1 .sd-tile{display:flex}
@media (max-width:999px){html.hf-1 .sd-grid{grid-template-columns:repeat(4,minmax(0,1fr));column-gap:16px}
  html.hf-1 .sd-it h3{font-size:17px}html.hf-1 .sd-pr b{font-size:23px}html.hf-1 .sd-tile{padding:18px}}
@media (max-width:767px){html.hf-1 .sd-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
  html.hf-1 .sd-hd{grid-template-columns:1fr;row-gap:14px}html.hf-1 .sd-lead{max-width:none;padding:0}}
@media (max-width:599px){html.hf-1 .sd-hd{padding-bottom:26px}html.hf-1 .sd-hd h2{font-size:clamp(30px,8.6vw,40px)}}

/* a · «Четыре размера»: the cell keeps its place; the sizes fill the void, the button stays on the price row */
html.hf-a .sd-rng{display:none}
html.hf-a .sd-hd .sd-mt{display:block;align-self:stretch;max-width:300px;margin-top:clamp(16px,1.6vw,24px)}
html.hf-a .sd-hd .sd-mn{display:block;margin-top:10px!important;max-width:300px}
html.hf-a .sd-hd .sd-all{margin-top:auto}
@media (min-width:1000px) and (max-width:1239px){   /* narrow desktop: the cell is ~220 px wide, keep it inside the card height */
  html.hf-a .sd-hd h2{font-size:clamp(30px,3vw,36px)}
  html.hf-a .sd-lead{margin-top:12px!important;font-size:15px;line-height:1.5}
  html.hf-a .sd-hd .sd-mt{margin-top:14px}
  html.hf-a .sd-mt div{padding:6px 0}html.hf-a .sd-mt dt{font-size:14px}html.hf-a .sd-mt dd{font-size:15.5px}
  html.hf-a .sd-hd .sd-mn{display:none}
  html.hf-a .sd-hd .sd-all{min-height:44px;padding:0 18px;font-size:15px}
}
@media (max-width:999px){
  html.hf-a .sd-hd h2{font-size:clamp(28px,4.2vw,36px)}
  html.hf-a .sd-lead{margin-top:12px!important;font-size:15px;line-height:1.5}
  html.hf-a .sd-hd .sd-mt{margin-top:14px}
  html.hf-a .sd-mt div{padding:7px 0}html.hf-a .sd-mt dt{font-size:14px}html.hf-a .sd-mt dd{font-size:16px}
}
@media (max-width:767px){html.hf-a .sd-hd .sd-mn{display:none}}
@media (max-width:599px){
  html.hf-a .sd-hd h2{font-size:clamp(30px,8.6vw,40px)}
  html.hf-a .sd-lead{font-size:16px;line-height:1.55}
  html.hf-a .sd-hd .sd-mt{display:grid;grid-template-columns:1fr 1fr;column-gap:20px;max-width:none;margin-top:16px}
  html.hf-a .sd-mt div{padding:9px 0}
  html.hf-a .sd-mt div:nth-child(-n+2){border-top-color:rgba(20,20,19,.16)}
  html.hf-a .sd-mt div:nth-child(n+3){border-bottom:1px solid rgba(20,20,19,.16)}
  html.hf-a .sd-hd .sd-mn{display:block;max-width:none}
}

/* b · «Размеры в конце»: heading row above, the closing cell is the price-per-size panel with the button */
html.hf-b .sd-hd{grid-column:1/-1;grid-row:auto;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,auto);column-gap:clamp(32px,5vw,96px);
  align-items:end;padding:0 0 clamp(32px,3.4vw,52px)}
html.hf-b .sd-hd h2{font-size:clamp(34px,4.2vw,58px);line-height:1.04;letter-spacing:-.035em}
html.hf-b .sd-lead{margin:0!important;max-width:34ch;padding-bottom:.35em}
html.hf-b .sd-hd .sd-all{display:none}
html.hf-b .sd-tile{display:flex;justify-content:flex-start;gap:0;padding:clamp(20px,1.9vw,28px)}
html.hf-b .sd-tile > span{display:none}
html.hf-b .sd-tile .sd-th{display:block;font-size:clamp(18px,1.45vw,21px);line-height:1.2;font-weight:600;letter-spacing:-.02em;color:var(--ink)}
html.hf-b .sd-tile .sd-mt{display:flex;flex-direction:column;flex:1;margin-top:clamp(14px,1.4vw,20px)}
html.hf-b .sd-tile .sd-mt div{flex:1;align-items:center;padding:8px 0}
html.hf-b .sd-tile .sd-mt dd{font-size:clamp(19px,1.6vw,23px)}
html.hf-b .sd-tile .sd-mn{display:block;margin-top:12px}
html.hf-b .sd-tile b{margin-top:clamp(16px,1.6vw,24px);align-self:flex-start;display:block;padding:0 22px;border-radius:999px;
  background:var(--moss);color:#fff;font-size:15.5px;line-height:48px;white-space:nowrap}
html.hf-b .sd-tile:hover b{background:#333c2c}
@media (min-width:1000px) and (max-width:1239px){
  html.hf-b .sd-tile{padding:18px}html.hf-b .sd-tile b{padding:0 16px;font-size:14.5px}html.hf-b .sd-tile .sd-arw{margin-left:6px}
  html.hf-b .sd-tile .sd-mt div{padding:4px 0}
}
@media (min-width:600px) and (max-width:999px){   /* 3 columns: 7 cards + the panel over two columns = 9 cells */
  html.hf-b .sd-tile{grid-column:span 2;display:grid;grid-template-columns:auto minmax(0,1fr);grid-template-rows:auto 1fr auto;column-gap:20px;padding:24px}
  html.hf-b .sd-tile .sd-th{grid-column:1/-1;grid-row:1;font-size:21px}
  html.hf-b .sd-tile .sd-mt{grid-column:1/-1;grid-row:2;margin:16px 0 0;display:grid;grid-template-columns:1fr 1fr;column-gap:clamp(20px,4vw,36px)}
  html.hf-b .sd-tile .sd-mt div{flex-direction:column;align-items:flex-start;justify-content:center;gap:4px;padding:10px 0}
  html.hf-b .sd-tile .sd-mt div:nth-child(3){border-bottom:1px solid rgba(20,20,19,.16)}
  html.hf-b .sd-tile .sd-mt dt{font-size:15px}html.hf-b .sd-tile .sd-mt dd{font-size:clamp(24px,3.4vw,30px);letter-spacing:-.03em;line-height:1.1}
  html.hf-b .sd-tile b{grid-column:1;grid-row:3;align-self:center;margin-top:20px}
  html.hf-b .sd-tile .sd-mn{grid-column:2;grid-row:3;align-self:center;margin-top:20px}
}
@media (max-width:767px){html.hf-b .sd-hd{grid-template-columns:1fr;row-gap:14px}html.hf-b .sd-lead{max-width:none;padding:0}}
@media (max-width:599px){
  html.hf-b .sd-hd{padding-bottom:26px}html.hf-b .sd-hd h2{font-size:clamp(30px,8.6vw,40px)}
  html.hf-b .sd-tile{padding:14px}
  html.hf-b .sd-tile .sd-th{font-size:16.5px}
  html.hf-b .sd-tile .sd-mt{margin-top:10px}
  html.hf-b .sd-tile .sd-mt div{padding:7px 0;gap:6px}
  html.hf-b .sd-tile .sd-mt dt{font-size:13px}html.hf-b .sd-tile .sd-mt dd{font-size:15px}
  html.hf-b .sd-tile .sd-mn{display:none}
  html.hf-b .sd-tile b{align-self:stretch;text-align:center;line-height:44px;padding:0 6px;margin-top:12px;font-size:13.5px}
  html.hf-b .sd-tile b .sd-arw{display:none}
}
'''
rep('</head>', '<style id="as6">' + CSS + '</style></head>')
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Заголовок</i>'
    '<button type="button" data-g="hf" data-v="0" aria-pressed="false">0 · Как сейчас</button>'
    '<button type="button" data-g="hf" data-v="1" aria-pressed="false">1 · Над сеткой</button>'
    '<button type="button" data-g="hf" data-v="a" aria-pressed="true">A · Четыре размера</button>'
    '<button type="button" data-g="hf" data-v="b" aria-pressed="false">B · Размеры в конце</button></div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} hf-a">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Assortiment · заголовок · Fable</title>', 1)
assert '.rv{' in s and 'set(' in s and '<title>Assortiment · заголовок · Fable</title>' in s   # bar styles and click script come with index.html
(D / 'assortiment-6.html').write_text(s)
print('ok', len(s), {k: (min(v), max(v)) for k, v in rng.items()})
