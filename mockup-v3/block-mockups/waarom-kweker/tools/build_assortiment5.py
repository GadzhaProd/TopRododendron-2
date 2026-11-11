# Mockup tool (not site code): assortiment-5.html = the main mockup with two treatments of the Assortiment heading corner
# (owner, 11 Nov: "между заголовком и кнопкой очень много места, там пустота посередине"). The cards already have no colour line.
#   html.hd-0  как сейчас: the heading is the grid's first cell, the button at the bottom of the cell (the void in the middle)
#   html.hd-1  заголовок над сеткой: the heading row spans the full width (H2 left, lead right on its baseline); the grid is
#              4 columns from 768 px up and 2 below, 7 cards + the «Bekijk alle planten» tile, so it closes with no gap
#   html.hd-2  в ячейке, но собрано: the heading, lead and button stay together at the top of the cell, the button right under
#              the lead; the free space moves below the button, beside the captions row
# Usage: python3 tools/build_assortiment5.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

CSS = r'''
/* ===== Assortiment heading corner, review (11 Nov) ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}

/* 1 · заголовок над сеткой */
html.hd-1 .sd-hd{grid-column:1/-1;grid-row:auto;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,auto);column-gap:clamp(32px,5vw,96px);
  align-items:end;padding:0 0 clamp(32px,3.4vw,52px)}
html.hd-1 .sd-hd h2{font-size:clamp(34px,4.2vw,58px);line-height:1.04;letter-spacing:-.035em}
html.hd-1 .sd-lead{margin:0!important;max-width:34ch;padding-bottom:.35em}
html.hd-1 .sd-hd .sd-all{display:none}
html.hd-1 .sd-tile{display:flex}
@media (max-width:999px){html.hd-1 .sd-grid{grid-template-columns:repeat(4,minmax(0,1fr));column-gap:16px}
  html.hd-1 .sd-it h3{font-size:17px}html.hd-1 .sd-pr b{font-size:23px}html.hd-1 .sd-tile{padding:18px}}
@media (max-width:767px){html.hd-1 .sd-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
  html.hd-1 .sd-hd{grid-template-columns:1fr;row-gap:14px}html.hd-1 .sd-lead{max-width:none;padding:0}}
@media (max-width:599px){html.hd-1 .sd-hd{padding-bottom:26px}html.hd-1 .sd-hd h2{font-size:clamp(30px,8.6vw,40px)}}

/* 2 · в ячейке, но собрано: heading, lead and button together at the top; the photo row's height no longer pulls them apart */
html.hd-2 .sd-hd{justify-content:flex-start}
html.hd-2 .sd-hd .sd-all{margin-top:28px}
'''
rep('</head>', '<style id="as5">' + CSS + '</style></head>')
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Заголовок</i>'
    '<button type="button" data-g="hd" data-v="0" aria-pressed="false">0 · Как сейчас</button>'
    '<button type="button" data-g="hd" data-v="1" aria-pressed="true">1 · Над сеткой</button>'
    '<button type="button" data-g="hd" data-v="2" aria-pressed="false">2 · Собрать в ячейке</button></div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} hd-1">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Assortiment · заголовок</title>', 1)
assert '.rv{' in s and 'set(' in s   # the review bar styles and its click script come with index.html
(D / 'assortiment-5.html').write_text(s)
print('ok', len(s))
