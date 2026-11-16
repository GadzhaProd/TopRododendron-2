# Mockup tool (not site code): sv-fable.html = Fable's review of sv.html (weaving the facts card, the assortment field and
# the guarantee card together). Reads index.html, writes sv-fable.html. Existing files are not touched.
#   Карточка фактов  html.fk-0 сейчас · fk-1 предложение (sv.html: ek-2 ec-1) · fk-2 Fable: the top a shade deeper (its edge
#                    reads as strongly as the guarantee card's top edge), the butter ground paler (the field's own butter as
#                    it shows on the page, not the mustard of the raw swatch)
#   Кант             html.fr-0 нет · fr-1 one hairline (1 px, moss 12 %) inside BOTH cards: the same clear edge on every
#                    side, also where a card's own colour comes close to the page (facts card right side, guarantee card
#                    warm panel)
#   Над головой      html.fh-0 сейчас · fh-1 предложение (sv.html hd-1: 95 %, flat card colour above the photo, a tone step
#                    of 8 levels on the left) · fh-2 Fable 95 % without the step · fh-3 Fable 92.5 % without the step
#                    The strip above the scaled portrait is filled with the photo backdrop's own colours (sampled from the
#                    top row of img/owner-portrait-ext.webp, left to right), so the photo's top edge has nothing to step to.
# The guarantee card keeps its height; text is untouched. Usage: python3 tools/build_sv_fable.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

CSS = r'''
/* ===== Fable's review of "weaving the three surfaces together" (16 Nov) ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}

/* the facts card's field with variables (identical to card-veld.css at the defaults) */
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
/* fk-1 · the proposal as on sv.html (ek-2 ec-1) */
html.fk-1 .wh2-card{--top:#e2e6d7;--b2:#e9ecdf;--b3:#e6dcb2;--b4:#d6cd9c;--bot:#ece6cd}
/* fk-2 · Fable: top a shade deeper, butter paler */
html.fk-2 .wh2-card{--top:#dee4d1;--b2:#e4e9d8;--b3:#eae1bf;--b4:#e0d7ad;--bot:#ede8d4}

/* fr-1 · one hairline inside both cards */
html.fr-1 :is(.wh2-card,#kweker .fd-card){position:relative}
html.fr-1 :is(.wh2-card,#kweker .fd-card)::after{content:"";position:absolute;inset:0;z-index:3;border-radius:inherit;pointer-events:none;
  box-shadow:inset 0 0 0 1px rgba(63,74,55,.12)}

/* fh · air above Gert's head on desktop: the portrait is scaled down and keeps the same bottom */
@media (min-width:861px){
  html.fh-1 #kweker .fd-ph{--pw:88.825cqh}
  html.fh-2 #kweker .fd-ph{--pw:88.825cqh}
  html.fh-3 #kweker .fd-ph{--pw:86.4875cqh}
  html:is(.fh-1,.fh-2,.fh-3) #kweker .fd-ph .ph-in{--w:var(--pw);top:calc(107.171cqh - var(--pw) * 1.18167);
    -webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 3%);mask-image:linear-gradient(to bottom,transparent 0%,#000 3%)}
  /* fh-2/3 · the strip above the photo carries the photo backdrop's own top-row colours (x in fractions of the 1580 px image);
     it ends under the photo's opaque part, and on the right it runs out where the photo's own alpha does */
  html:is(.fh-2,.fh-3) #kweker .fd-ph::before{content:"";position:absolute;top:0;
    left:min(0px,max(calc((100cqw - var(--pw)) * .75),calc(var(--pw) * -.12)));width:calc(var(--pw) * 1.31667);
    height:calc(107.171cqh - var(--pw) * 1.18167 + var(--pw) * .0414);
    background:linear-gradient(to right,#e7eae8 0%,#e6e9e7 16.6%,#e4e8e8 24.9%,#e0e3e4 33.2%,#dce1e2 41.5%,#dce1e2 50%,rgba(222,224,226,.7) 58%,rgba(222,224,226,0) 68%)}
}
'''
rep('</head>', '<style id="sv-fable">' + CSS + '</style></head>')
B = lambda g, v, t, on: f'<button type="button" data-g="{g}" data-v="{v}" aria-pressed="{"true" if on else "false"}">{t}</button>'
bar = ('<div class="rv" role="group" aria-label="Варианты">'
       '<div class="rv-g"><i>Факты</i>' + B('fk', '0', '0 · сейчас', 0) + B('fk', '1', '1 · предложение', 0) + B('fk', '2', '2 · Fable', 1) + '</div>'
       '<div class="rv-g"><i>Кант</i>' + B('fr', '0', 'нет', 0) + B('fr', '1', 'есть', 1) + '</div>'
       '<div class="rv-g"><i>Над головой</i>' + B('fh', '0', '0', 0) + B('fh', '1', '1 · предл.', 0) + B('fh', '2', '2 · Fable', 1) + B('fh', '3', '3 · Fable+', 0) + '</div>'
       '</div>')
rep('<div id="root">', bar + '<div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} fk-2 fr-1 fh-2">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Сплести воедино · Fable</title>', 1)
(D / 'sv-fable.html').write_text(s)
print('ok', len(s))
