# Mockup tool (not site code): sv.html = the main mockup with three switches that weave the three surfaces together
# (owner, 16 Nov): the Waarom wij facts card (soft top, hard bottom), the assortment field (soft on every side) and the
# guarantee card (hard edges, Gert's portrait).
#   Края карточки фактов   html.ek-0 как сейчас · ek-1 нежно растворяется и снизу · ek-2 чёткие края со всех сторон
#   Цвет карточки фактов   html.ec-0 как сейчас (песок/земля снизу) · ec-1 общая палитра: снизу масло и шалфей, как у поля
#                          ассортимента
#   Воздух над головой     html.hd-0 как сейчас · hd-1 чуть больше · hd-2 больше (desktop portrait scaled down, anchored at
#                          the same bottom; its top edge blends into the card, whose top colour matches the photo backdrop)
# Only the facts card's background layers are masked or retinted; its text is untouched. The guarantee card keeps its height.
# Usage: python3 tools/build_sv.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

CSS = r'''
/* ===== weaving the three surfaces together (review, 16 Nov) ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}

/* the facts card's field, rewritten with variables (identical to card-veld.css at the defaults) */
.wh2-card{--top:#eceee6;--bot:#e8e3d4}
.wh2-bg{background:
  radial-gradient(ellipse 75% 38% at 50% -4%,var(--b2) 0%,transparent 70%),
  radial-gradient(ellipse 34% 20% at 88% 20%,var(--b5) 0%,transparent 70%),
  radial-gradient(ellipse 78% 50% at -6% 46%,var(--b1) 0%,transparent 68%),
  radial-gradient(ellipse 46% 32% at 30% 100%,#c2cca9 0%,transparent 68%),
  radial-gradient(ellipse 120% 34% at 50% 104%,var(--b3) 0%,transparent 72%),
  radial-gradient(ellipse 52% 34% at 102% 102%,var(--b4) 0%,transparent 70%),
  linear-gradient(to bottom,var(--top) 0%,var(--p) 46%,var(--bot) 100%)}
@media (max-width:860px){
  .wh2-bg{background:
    radial-gradient(ellipse 90% 60% at 50% -10%,var(--b2) 0%,transparent 70%),
    radial-gradient(ellipse 30% 50% at 92% 20%,var(--b5) 0%,transparent 70%),
    radial-gradient(ellipse 55% 90% at -4% 50%,var(--b1) 0%,transparent 68%),
    radial-gradient(ellipse 120% 55% at 50% 108%,var(--b3) 0%,transparent 72%),
    radial-gradient(ellipse 45% 70% at 104% 104%,var(--b4) 0%,transparent 70%),
    linear-gradient(to bottom,var(--top) 0%,var(--p) 46%,var(--bot) 100%)}
}

/* ek-1 · the bottom dissolves too, gently: a long ramp that keeps a hint of the edge (the text is not masked) */
html.ek-1 .wh2-card :is(.wh2-bg,.wh-grain){
  -webkit-mask-image:linear-gradient(to bottom,#000 0%,#000 66%,rgba(0,0,0,.78) 78%,rgba(0,0,0,.46) 89%,rgba(0,0,0,.16) 100%);
          mask-image:linear-gradient(to bottom,#000 0%,#000 66%,rgba(0,0,0,.78) 78%,rgba(0,0,0,.46) 89%,rgba(0,0,0,.16) 100%)}
/* ek-2 · clear edges on every side: the top takes a light sage tone instead of the page colour, so its rounded edge reads
   like the bottom one and like the guarantee card */
html.ek-2 .wh2-card{--top:#e2e6d7;--b2:#e9ecdf}

/* ec-1 · one palette with the assortment field: the sandy ground becomes butter and soft sage (field: #ece2b9, #c3d5ae) */
html.ec-1 .wh2-card{--b3:#e6dcb2;--b4:#d6cd9c;--bot:#ece6cd}

/* hd · air above Gert's head on desktop: the portrait is scaled down and keeps the same bottom (the shoulder still runs out
   of the card); its top edge fades into the card over 3% of its height, above the hair (which starts at 3.9%) */
@media (min-width:861px){
  html.hd-1 #kweker .fd-ph .ph-in{--w:88.825cqh;top:2.21cqh}
  html.hd-2 #kweker .fd-ph .ph-in{--w:84.15cqh;top:7.73cqh}
  html:is(.hd-1,.hd-2) #kweker .fd-ph .ph-in{
    -webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 3%);mask-image:linear-gradient(to bottom,transparent 0%,#000 3%)}
}
'''
rep('</head>', '<style id="sv">' + CSS + '</style></head>')
B = lambda g, v, t, on: f'<button type="button" data-g="{g}" data-v="{v}" aria-pressed="{"true" if on else "false"}">{t}</button>'
bar = ('<div class="rv" role="group" aria-label="Варианты">'
       '<div class="rv-g"><i>Края</i>' + B('ek', '0', '0 · сейчас', 0) + B('ek', '1', '1 · нежно снизу', 0) + B('ek', '2', '2 · чёткие', 1) + '</div>'
       '<div class="rv-g"><i>Цвет</i>' + B('ec', '0', 'сейчас', 0) + B('ec', '1', 'общая палитра', 1) + '</div>'
       '<div class="rv-g"><i>Над головой</i>' + B('hd', '0', '0', 0) + B('hd', '1', '1', 1) + B('hd', '2', '2', 0) + '</div>'
       '</div>')
rep('<div id="root">', bar + '<div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} ek-2 ec-1 hd-1">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Сплести воедино</title>', 1)
(D / 'sv.html').write_text(s)
print('ok', len(s))
