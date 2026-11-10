# Mockup tool (not site code): fd-telefoon.html = the main mockup with two new PHONE treatments of the founder block (10 Nov).
# Desktop is unchanged. Owner: the navy phone card was made before the soft-gradient card style existed, so
#   1 · Накладка: the part that the photo melts into is redone as a soft-gradient card with grain;
#   2 · Две части: the photo stands on its own, the card with the text follows below it.
# Colourways: Синий (the jacket tones, as now) and Поле (the Waarom wij facts card). 1 is navy only: a light card under the
# dark jacket was tried and dropped, the jacket can only fade into it through a grey haze band.
# Switch via html.fm-0/1/2 (0 = the approved navy card as it is now) and html.fc-b/v.
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

GRAIN = '<div class="wh-grain fd-gr" aria-hidden="true"></div>'
rep('<div class="fd-card"><figure class="fd-ph">', '<div class="fd-card">' + GRAIN + '<figure class="fd-ph">')
rep('<div class="fd-pn"><div class="fd-name">', '<div class="fd-pn">' + GRAIN + '<div class="fd-name">')

CSS = r'''
/* ===== founder block, phone treatments (10 Nov); desktop untouched ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
.fd-gr{display:none}
@media (max-width:860px){
  /* shared: colour tokens */
  .fc-b,.fm-1{--fd-ink:#f5f2ea;--fd-sub:#c9cfdb;--fd-rule:#a9b894;--fd-gr:.26;--fd-gb:overlay}
  .fc-v:not(.fm-1){--fd-ink:#141413;--fd-sub:#3d3c37;--fd-rule:var(--moss);--fd-gr:.3;--fd-gb:soft-light}
  :is(.fm-1,.fm-2) .fd-gr{display:block;--gr:var(--fd-gr);--gb:var(--fd-gb)}
  :is(.fm-1,.fm-2) .fd-pn{color:var(--fd-ink)}
  :is(.fm-1,.fm-2) .fd-role,:is(.fm-1,.fm-2) .fd-txt{color:var(--fd-sub)}
  :is(.fm-1,.fm-2) .fd-q{border-left-color:var(--fd-rule)}
  :is(.fm-1,.fm-2) .fd-q p{color:var(--fd-ink)}

  /* 1 · Накладка: one card, the photo melts into a soft gradient with grain (the photo itself is not grained) */
  .fm-1 .fd-card{position:relative;isolation:isolate}
  .fm-1 .fd-pn .fd-gr{display:none}
  .fm-1 .fd-card{background:
    radial-gradient(ellipse 90% 22% at 6% 56%,rgba(82,99,138,.62) 0%,transparent 70%),
    radial-gradient(ellipse 60% 16% at 100% 60%,rgba(16,19,31,.55) 0%,transparent 70%),
    radial-gradient(ellipse 95% 28% at -4% 102%,rgba(108,126,90,.7) 0%,transparent 70%),
    radial-gradient(ellipse 65% 26% at 104% 80%,rgba(132,100,132,.5) 0%,transparent 70%),
    linear-gradient(to bottom,#2b3552 0%,#252e48 56%,#1d2439 100%)}

  /* 2 · Две части: the photo on its own, then the card; same corner radius, a small gap between them */
  .fm-2 .fd-card{background:none;border-radius:0;overflow:visible;gap:10px}
  .fm-2 .fd-card > .fd-gr{display:none}
  .fm-2 .fd-ph{aspect-ratio:1200/1418;border-radius:22px;overflow:hidden}
  .fm-2 .fd-ph picture{display:contents}
  .fm-2 .fd-ph .ph-in img.ph-m{display:none}
  .fm-2 .fd-ph .ph-in{-webkit-mask-image:none;mask-image:none}
  .fm-2 .fd-pn{margin-top:0;position:relative;isolation:isolate;overflow:hidden;border-radius:22px;padding:30px 22px 32px}
  .fm-2.fc-b .fd-pn{background:
    radial-gradient(ellipse 80% 55% at 0% 0%,rgba(78,94,130,.6) 0%,transparent 70%),
    radial-gradient(ellipse 70% 50% at 0% 104%,rgba(104,121,88,.5) 0%,transparent 70%),
    radial-gradient(ellipse 55% 45% at 104% 92%,rgba(126,96,126,.34) 0%,transparent 70%),
    linear-gradient(to bottom,#2a3451 0%,#232c45 55%,#1c2337 100%)}
  .fm-2.fc-v .fd-pn{--p:#ebece3;--b1:#adbb98;--b2:#f1f0e8;--b3:#d9cbb0;--b4:#c7b893;--b5:#ecd6d2;background:
    radial-gradient(ellipse 90% 50% at 50% -10%,var(--b2) 0%,transparent 70%),
    radial-gradient(ellipse 30% 40% at 94% 18%,var(--b5) 0%,transparent 70%),
    radial-gradient(ellipse 55% 80% at -4% 50%,var(--b1) 0%,transparent 68%),
    radial-gradient(ellipse 120% 50% at 50% 108%,var(--b3) 0%,transparent 72%),
    radial-gradient(ellipse 45% 60% at 104% 104%,var(--b4) 0%,transparent 70%),
    linear-gradient(to bottom,#eceee6 0%,var(--p) 46%,#e8e3d4 100%)}
}
/* the colour buttons do nothing on 0 · Сейчас and 1 · Накладка (navy only) */
:is(.fm-0,.fm-1) .rv .rv-fc{opacity:.35;pointer-events:none}
@media (min-width:861px){.rv::after{content:"Варианты только для телефона";font:500 12px/1 Manrope,system-ui,sans-serif;color:#a9a79f;margin-left:8px}}
'''
s = s.replace('</head>', '<style id="fd-telefoon">' + CSS + '</style></head>', 1)
RV = ('<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Блок Герта</i>'
      '<button type="button" data-g="fm" data-v="0" aria-pressed="false">0<span class="l"> · Сейчас</span></button>'
      '<button type="button" data-g="fm" data-v="1" aria-pressed="true">1<span class="l"> · Накладка</span></button>'
      '<button type="button" data-g="fm" data-v="2" aria-pressed="false">2<span class="l"> · Две части</span></button></div>'
      '<span class="sep" aria-hidden="true"></span><div class="rv-g rv-fc"><i>Цвет</i>'
      '<button type="button" data-g="fc" data-v="b" aria-pressed="true">Синий</button>'
      '<button type="button" data-g="fc" data-v="v" aria-pressed="false">Поле</button></div></div>')
rep('<div id="root">', RV + '<div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} fm-1 fc-b">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Gert Top · telefoon</title>', 1)
(D / 'fd-telefoon.html').write_text(s)
print('ok', len(s))
