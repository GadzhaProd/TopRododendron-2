# Mockup tool (not site code): fd-dve.html = the main mockup with reworks of the PHONE variant "2 · Две части · Поле"
# (fd-telefoon.html, fm-2 fc-v) of the founder block (10 Nov). The idea stays: the real, undoctored photo
# (img/owner-portrait.webp, no fade, nothing painted below the chin) plus a text card in the Поле palette.
# What is fixed: the break between the two pieces (two rounded boxes with a 10 px gap).
#   0 · Было    fm-2 fc-v exactly as on fd-telefoon.html.
#   1 · Лист    one card. The text card is a sheet of paper lying on the photo: it covers the photo's last 22 px
#               (the frame ends at 94.7 % of the photo; desktop ends at 93.5 %), its rounded top corners show the
#               jacket behind it. The sheet picks up the photo's own backdrop: pink bloom on the left, sage on the
#               right, as if the backdrop went on behind the jacket.
#   2 · Оттиск  the Поле card is the ground, the photo is a print laid on it: the print stands 30 % above the
#               card's top edge and lies on the card with the rest, so the photo itself bridges the two parts.
# No derived images: both reworks use the original photo file as it is.
# Desktop (>=861 px) is unchanged: every rule sits inside @media (max-width:860px); the quote's second sentence gets
# its <span> by script on phone widths only (same as build_fd_fable.py), so the desktop DOM equals index.html.
# 0 · Было gets no span either (it must match fd-telefoon.html to the pixel); the script follows the variant switch.
# Switch via html.dv-0/1/2. Usage: python3 tools/build_fd_dve.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

Q2 = ("<script>(function(){var r=document.documentElement,p=document.querySelector('#kweker .fd-q p'),m=matchMedia('(max-width:860px)');if(!p)return;"
      "function f(){var t=p.textContent,i=t.indexOf('. ');if(m.matches&&i>0&&!r.classList.contains('dv-0')){p.textContent=t.slice(0,i+2);var s=document.createElement('span');"
      "s.className='q2';s.textContent=t.slice(i+2);p.appendChild(s)}else if(p.firstElementChild){p.textContent=t}}f();m.addEventListener('change',f);"
      "new MutationObserver(f).observe(r,{attributes:true,attributeFilter:['class']})})();</script>")
rep('</body>', Q2 + '</body>')

GRAIN = ("url(\"data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E"
         "%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E"
         "%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E\")")

CSS = r'''
/* ===== founder block, phone: reworks of "2 · Две части · Поле" (10 Nov); desktop untouched ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
@media (max-width:860px){
  /* shared: light text colours, the original photo, grain on the text card */
  html:is(.dv-0,.dv-1,.dv-2) .fd-pn{color:#141413}
  html:is(.dv-0,.dv-1,.dv-2) :is(.fd-role,.fd-txt){color:#3d3c37}
  html:is(.dv-0,.dv-1,.dv-2) .fd-q{border-left-color:var(--moss)}
  html:is(.dv-0,.dv-1,.dv-2) .fd-q p{color:#141413}
  html:is(.dv-0,.dv-1,.dv-2) .fd-ph{aspect-ratio:1200/1418}
  html:is(.dv-0,.dv-1,.dv-2) .fd-ph picture{display:contents}
  html:is(.dv-0,.dv-1,.dv-2) .fd-ph .ph-in img.ph-m{display:none}
  html:is(.dv-0,.dv-1,.dv-2) .fd-ph .ph-in{-webkit-mask-image:none;mask-image:none}
  html:is(.dv-0,.dv-1) .fd-pn::before,html.dv-2 .fd-card::after{content:"";position:absolute;inset:0;z-index:-1;pointer-events:none;
    background:GRAIN;background-size:220px 220px;opacity:.3;mix-blend-mode:soft-light}

  /* ---------- 0 · Было: fd-telefoon.html fm-2 fc-v, rule for rule ---------- */
  html.dv-0 .fd-card{background:none;border-radius:0;overflow:visible;gap:10px}
  html.dv-0 .fd-ph{border-radius:22px;overflow:hidden}
  html.dv-0 .fd-pn{margin-top:0;position:relative;isolation:isolate;overflow:hidden;border-radius:22px;padding:30px 22px 32px;
    --p:#ebece3;--b1:#adbb98;--b2:#f1f0e8;--b3:#d9cbb0;--b4:#c7b893;--b5:#ecd6d2;background:
    radial-gradient(ellipse 90% 50% at 50% -10%,var(--b2) 0%,transparent 70%),
    radial-gradient(ellipse 30% 40% at 94% 18%,var(--b5) 0%,transparent 70%),
    radial-gradient(ellipse 55% 80% at -4% 50%,var(--b1) 0%,transparent 68%),
    radial-gradient(ellipse 120% 50% at 50% 108%,var(--b3) 0%,transparent 72%),
    radial-gradient(ellipse 45% 60% at 104% 104%,var(--b4) 0%,transparent 70%),
    linear-gradient(to bottom,#eceee6 0%,var(--p) 46%,#e8e3d4 100%)}

  /* shared by the reworks */
  html:is(.dv-1,.dv-2) .fd-card{position:relative;isolation:isolate;padding:0;max-width:520px;margin-inline:auto;grid-template-columns:minmax(0,1fr)}
  html:is(.dv-1,.dv-2) .fd-q .q2{display:block}
  html:is(.dv-1,.dv-2) .fd-q p{max-width:none;text-wrap:balance;font-size:clamp(24px,6.7vw,30px);line-height:1.16;letter-spacing:-.03em;font-weight:600}
  html:is(.dv-1,.dv-2) .fd-q{padding-left:18px}
  html:is(.dv-1,.dv-2) .fd-name h2{font-size:clamp(40px,11.4vw,52px);line-height:.95;letter-spacing:-.045em}
  html:is(.dv-1,.dv-2) .fd-role{margin-top:10px;font-size:15px}
  html:is(.dv-1,.dv-2) .fd-txt{margin-top:16px;font-size:16.5px;line-height:1.5;max-width:34ch}
  html:is(.dv-1,.dv-2) .fd-qw{padding-top:26px}

  /* ---------- 1 · Лист: the text card is a sheet lying on the photo ---------- */
  html.dv-1 .fd-card{background:#e9e6da;border-radius:22px;overflow:hidden}
  html.dv-1 .fd-ph{border-radius:0;overflow:hidden}
  /* the sheet covers the photo's last 22 px; its colours are the photo's backdrop: pink bloom left, sage right */
  html.dv-1 .fd-pn{margin-top:-22px;position:relative;isolation:isolate;overflow:hidden;border-radius:22px 22px 0 0;padding:30px 22px 34px;
    box-shadow:0 -1px 0 rgba(255,255,255,.55),0 -6px 14px -6px rgba(8,11,22,.55);
    background:
    radial-gradient(ellipse 78% 150px at -6% 0,rgba(232,206,214,.95) 0%,transparent 72%),
    radial-gradient(ellipse 62% 170px at 108% 26px,rgba(178,192,156,.9) 0%,transparent 72%),
    radial-gradient(ellipse 80% 130px at 46% -30px,#f1f1ec 0%,transparent 70%),
    radial-gradient(ellipse 120% 44% at 50% 108%,#d9cbb0 0%,transparent 72%),
    radial-gradient(ellipse 50% 46% at -6% 100%,#bcc8a6 0%,transparent 70%),
    linear-gradient(to bottom,#ecece6 0%,#ebece3 46%,#e8e3d4 100%)}

  /* ---------- 2 · Оттиск: the Поле card is the ground, the photo is a print laid across its top edge ---------- */
  html.dv-2 .fd-card{container-type:inline-size;background:none;border-radius:0;overflow:visible;--ph:calc((100cqw - 36px) * 1.18167)}
  html.dv-2 .fd-card::before,html.dv-2 .fd-card::after{content:"";position:absolute;inset:calc(var(--ph) * .3) 0 0 0;z-index:-1;border-radius:22px;pointer-events:none}
  html.dv-2 .fd-card::before{background:
    radial-gradient(ellipse 90% 34% at 50% -6%,#f1f0e8 0%,transparent 70%),
    radial-gradient(ellipse 34% 26% at 100% 10%,#ecd6d2 0%,transparent 70%),
    radial-gradient(ellipse 60% 52% at -6% 34%,#adbb98 0%,transparent 68%),
    radial-gradient(ellipse 120% 34% at 50% 106%,#d9cbb0 0%,transparent 72%),
    radial-gradient(ellipse 48% 34% at 104% 102%,#c7b893 0%,transparent 70%),
    linear-gradient(to bottom,#eceee6 0%,#ebece3 46%,#e8e3d4 100%)}
  html.dv-2 .fd-ph{margin:0 18px;border-radius:14px;overflow:hidden;
    box-shadow:0 1px 2px rgba(30,36,28,.16),0 22px 38px -20px rgba(30,36,28,.5)}
  html.dv-2 .fd-pn{margin-top:0;padding:28px 22px 34px;background:none}
}
@media (min-width:861px){.rv::after{content:"Варианты только для телефона";font:500 12px/1 Manrope,system-ui,sans-serif;color:#a9a79f;margin-left:8px}}
'''.replace('GRAIN', GRAIN)
s = s.replace('</head>', '<style id="fd-dve">' + CSS + '</style></head>', 1)
RV = ('<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Блок Герта</i>'
      '<button type="button" data-g="dv" data-v="0" aria-pressed="false">0<span class="l"> · Было</span></button>'
      '<button type="button" data-g="dv" data-v="1" aria-pressed="true">1<span class="l"> · Лист</span></button>'
      '<button type="button" data-g="dv" data-v="2" aria-pressed="false">2<span class="l"> · Оттиск</span></button></div></div>')
rep('<div id="root">', RV + '<div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} dv-1">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Gert Top · telefoon · Две части</title>', 1)
(D / 'fd-dve.html').write_text(s)
print('ok', len(s))
