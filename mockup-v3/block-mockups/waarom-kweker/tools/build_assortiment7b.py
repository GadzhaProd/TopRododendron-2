# Mockup tool (not site code): assortiment-7.html = build_assortiment7.py reproduced (lay-1, lay-2, lay-3 unchanged) plus a
# fourth option, html.lay-4 "Fable": one shelf of seven.
#   from 1000 px  all seven cards in one row, flush with the heading on the left and the lead on the right
#   below 1000 px the same row becomes a swipe shelf (scroll-snap): equal cards, the next one cut by the screen edge, so
#                 seven never has to end on an odd row; the bloom line stays visible on the phone (one row, room for it)
# Only markup change against build_assortiment7.py: the heading row .sd-hd moves out of .sd-grid to sit right before it
# (it spanned the grid at full width, so lay-1..3 render the same), which lets the grid alone scroll sideways in lay-4.
# (so the :nth-child numbers of lay-1..3 are one lower than in build_assortiment7.py). The page opens on lay-4. build_assortiment7.py itself is left as it is.
# Usage: python3 tools/build_assortiment7b.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

ARW = '<svg class="sd-arw" viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'
lead = re.search(r'<p class="sd-lead">.*?</p>', s).group(0)
rep(lead + '</div>', '<div class="sd-hr">' + lead + '<a class="sd-more" href="#assortiment">Bekijk alle planten' + ARW + '</a></div></div>')
tile = re.search(r'<a class="sd-tile".*?</a>(?=</div></div></section>)', s, re.S).group(0)
rep(tile, '')
hd = re.search(r'<div class="sd-hd">.*?</a></div></div>(?=<article)', s, re.S).group(0)
rep('<div class="sd-grid">' + hd, hd + '<div class="sd-grid">')

CSS = r'''
/* ===== Assortiment · seven cards, no "view all" card (review, 12 Nov) ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
.sd-hr{display:flex;flex-direction:column;align-items:flex-start;gap:10px;padding-bottom:.2em}
.sd-hr .sd-lead{padding-bottom:0}
.sd-more{display:inline-flex;align-items:center;gap:8px;min-height:44px;font-size:15.5px;font-weight:600;color:var(--moss);
  text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:5px;text-decoration-color:rgba(63,74,55,.4)}
.sd-more:hover{text-decoration-color:var(--moss)}
.sd-more:focus-visible{outline:2px solid var(--moss);outline-offset:4px;border-radius:4px}
.sd-more .sd-arw{transition:transform .3s ease}.sd-more:hover .sd-arw{transform:translateX(3px)}

/* 1 · 4 + 3 (an 8-column grid, each card spans 2; the second row starts at column 2) */
html:is(.lay-1,.lay-3) .sd-grid{grid-template-columns:repeat(8,minmax(0,1fr))}
html:is(.lay-1,.lay-3) .sd-it > a{grid-column:span 2}
html:is(.lay-1,.lay-3) .sd-it:nth-child(5) > a{grid-column:2 / span 2}

/* 2 · 3 + 4 (a 12-column grid: three cards span 4, four cards span 3) */
html.lay-2 .sd-grid{grid-template-columns:repeat(12,minmax(0,1fr))}
html.lay-2 .sd-it > a{grid-column:span 3}
html.lay-2 .sd-it:nth-child(-n+3) > a{grid-column:span 4}

/* 3 · seven in one row from 1200 px */
@media (min-width:1200px){
  html.lay-3 .sd-grid{grid-template-columns:repeat(7,minmax(0,1fr));column-gap:clamp(14px,1.2vw,22px)}
  html.lay-3 .sd-it > a,html.lay-3 .sd-it:nth-child(5) > a{grid-column:auto}
  html.lay-3 .sd-it h3{font-size:clamp(16px,1.15vw,19px)}
  html.lay-3 .sd-pr b{font-size:clamp(21px,1.6vw,26px)}
  html.lay-3 .sd-b{font-size:13.5px}
}

/* phone and small tablet: two columns, the seventh card centred */
@media (max-width:767px){
  html:is(.lay-1,.lay-2,.lay-3) .sd-grid{grid-template-columns:repeat(4,minmax(0,1fr))}
  html:is(.lay-1,.lay-2,.lay-3) .sd-it > a,html:is(.lay-1,.lay-2,.lay-3) .sd-it:nth-child(-n+3) > a,html:is(.lay-1,.lay-3) .sd-it:nth-child(5) > a{grid-column:span 2}
  html:is(.lay-1,.lay-2,.lay-3) .sd-it:nth-child(7) > a{grid-column:2 / span 2}
  .sd-hr{gap:4px}
}

/* 4 · Fable: one shelf of seven. From 1000 px all seven in one row; below that the same row is a swipe shelf. */
html.lay-4 .sd-grid{grid-template-columns:repeat(7,minmax(0,1fr));column-gap:clamp(12px,1.2vw,22px)}
html.lay-4 .sd-it > a{padding-bottom:clamp(12px,1.6vw,24px)}
html.lay-4 .sd-it h3{font-size:clamp(15px,1.25vw,19px)}
html.lay-4 .sd-b{font-size:clamp(12.5px,1vw,13.5px)}
html.lay-4 .sd-pr b{font-size:clamp(20px,1.7vw,26px)}
html.lay-4 .sd-s{font-size:clamp(12px,.95vw,13px)}
@media (max-width:999px){
  html.lay-4 .sd-grid{grid-template-columns:none;grid-template-rows:repeat(4,auto);grid-auto-flow:column;grid-auto-columns:clamp(198px,54vw,216px);column-gap:14px;
    margin:-8px calc(var(--gut)*-1);padding:8px var(--gut);overflow-x:auto;overscroll-behavior-x:contain;
    scroll-snap-type:x mandatory;scroll-padding-inline:var(--gut);scrollbar-width:none;-webkit-overflow-scrolling:touch}
  html.lay-4 .sd-grid::-webkit-scrollbar{display:none}
  html.lay-4 .sd-it > a{grid-row:span 4;scroll-snap-align:start;padding-bottom:8px}
  html.lay-4 .sd-b{display:block;font-size:13.5px}
  html.lay-4 .sd-it h3{margin-top:14px;font-size:17px}
  html.lay-4 .sd-pr{margin-top:10px}
  html.lay-4 .sd-pr b{font-size:23px}
  html.lay-4 .sd-s{font-size:13px}
}
@media (max-width:599px){html.lay-4 .sd-grid{column-gap:12px}html.lay-4 .sd-it h3{margin-top:12px;font-size:16px}}
'''
rep('</head>', '<style id="as7">' + CSS + '</style></head>')
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Сетка</i>'
    '<button type="button" data-g="lay" data-v="1" aria-pressed="false">1 · 4 + 3</button>'
    '<button type="button" data-g="lay" data-v="2" aria-pressed="false">2 · 3 + 4</button>'
    '<button type="button" data-g="lay" data-v="3" aria-pressed="false">3 · 7 в ряд</button><button type="button" data-g="lay" data-v="4" aria-pressed="true">4 · Fable</button></div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} lay-4">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Assortiment · 7 сортов</title>', 1)
(D / 'assortiment-7.html').write_text(s)
print('ok', len(s))
