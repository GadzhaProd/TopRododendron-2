# Mockup tool (not site code): assortiment-7.html = the main mockup with the "view all" card removed (owner, 12 Nov: keep
# just the seven varieties) and three ways to lay out seven cards without an empty cell. The link to all plants becomes a
# plain text link under the lead in the heading row.
#   html.lay-1  4 + 3: two rows of equal cards, the second row of three centred under the first
#   html.lay-2  3 + 4: a 12-column grid, three wider cards on top, four below; both rows run the full width
#   html.lay-3  7 in one row from 1200 px (one line of seven whole bushes); below 1200 px as lay-1
# Phone (≤767 px), all three: two columns, the seventh card centred on its own row.
# Usage: python3 tools/build_assortiment7.py [dir]
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
html:is(.lay-1,.lay-3) .sd-it:nth-child(6) > a{grid-column:2 / span 2}

/* 2 · 3 + 4 (a 12-column grid: three cards span 4, four cards span 3) */
html.lay-2 .sd-grid{grid-template-columns:repeat(12,minmax(0,1fr))}
html.lay-2 .sd-it > a{grid-column:span 3}
html.lay-2 .sd-it:nth-child(-n+4) > a{grid-column:span 4}

/* 3 · seven in one row from 1200 px */
@media (min-width:1200px){
  html.lay-3 .sd-grid{grid-template-columns:repeat(7,minmax(0,1fr));column-gap:clamp(14px,1.2vw,22px)}
  html.lay-3 .sd-it > a,html.lay-3 .sd-it:nth-child(6) > a{grid-column:auto}
  html.lay-3 .sd-it h3{font-size:clamp(16px,1.15vw,19px)}
  html.lay-3 .sd-pr b{font-size:clamp(21px,1.6vw,26px)}
  html.lay-3 .sd-b{font-size:13.5px}
}

/* phone and small tablet: two columns, the seventh card centred */
@media (max-width:767px){
  html:is(.lay-1,.lay-2,.lay-3) .sd-grid{grid-template-columns:repeat(4,minmax(0,1fr))}
  html:is(.lay-1,.lay-2,.lay-3) .sd-it > a,html:is(.lay-1,.lay-2,.lay-3) .sd-it:nth-child(-n+4) > a,html:is(.lay-1,.lay-3) .sd-it:nth-child(6) > a{grid-column:span 2}
  html:is(.lay-1,.lay-2,.lay-3) .sd-it:nth-child(8) > a{grid-column:2 / span 2}
  .sd-hr{gap:4px}
}
'''
rep('</head>', '<style id="as7">' + CSS + '</style></head>')
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Сетка</i>'
    '<button type="button" data-g="lay" data-v="1" aria-pressed="true">1 · 4 + 3</button>'
    '<button type="button" data-g="lay" data-v="2" aria-pressed="false">2 · 3 + 4</button>'
    '<button type="button" data-g="lay" data-v="3" aria-pressed="false">3 · 7 в ряд</button></div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} lay-1">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Assortiment · 7 сортов</title>', 1)
(D / 'assortiment-7.html').write_text(s)
print('ok', len(s))
