# Mockup tool (not site code): fd-kop-fable.html = Fable's take on the move from the assortment to the guarantee card
# (owner, 16 Nov: "they sit close, different colours; the jump catches the eye"). Compare with fd-kop.html.
# Diagnosis: the clash is not a missing heading. (1) There is no clean page between the two surfaces: the field's bottom
# feather runs to the card's top edge (desktop) or under it (phone: the card starts inside the butter glow), so a soft
# edge and a hard edge touch. (2) Temperature: the field ends in its warmest corner (butter, bottom right, under the
# pill) and the card answers with its coldest one (a blue-grey white panel) on a warm page.
#   html.fb-0  как сейчас
#   html.fb-1  воздух и тон: the field finishes fading, then a band of clean page, then the card; the card's text panel
#              goes from cold grey-white to warm paper (the portrait side and the card height are untouched)
#   html.fb-2  = fb-1 + the promise as the section H2 on the clean page (assortment H2 type, one sentence per line).
#              The card keeps an anchor: the name of the guarantee ("3 maanden aangroeigarantie na levering.") leads
#              the panel at a sub-heading size, so the panel is not a small paragraph adrift in a tall card.
# No new copy: every word is already on the approved card. In production the visible H2 takes id="h-kweker".
# Usage: python3 tools/build_fd_kop_fable.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

rep('<section class="fd fp fp-1" id="kweker" aria-labelledby="h-kweker"><div class="in"><div class="fd-card">',
    '<section class="fd fp fp-1" id="kweker" aria-labelledby="h-kweker"><div class="in">'
    '<div class="fb-hd"><h2 class="fb-h"><span>Slaat een plant niet aan?</span> <span>Dan krijgt u een nieuwe.</span></h2></div>'
    '<div class="fd-card">')

CSS = r'''
/* ===== from the assortment to the guarantee card: air and tone (Fable, 16 Nov) ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
.fb-hd{display:none}

/* --- 1 + 2 · air: the field's feather ends (it overhangs the assortment section by --fb-tail), then clean page --- */
html:is(.fb-1,.fb-2) .fp-1{--fb-tail:calc(clamp(84px,9vw,150px) * .3);--fb-air:clamp(40px,4.4vw,72px)}
html:is(.fb-1,.fb-2) .fp-1 > .in{padding-top:calc(var(--fb-tail) + var(--fb-air))}
@media (max-width:599px){
  html:is(.fb-1,.fb-2) .fp-1{--fb-tail:27px;--fb-air:32px}
}

/* --- 1 + 2 · tone: the text panel as warm paper (a shade lighter than the page) instead of cold grey-white.
   Only the veil over the right part changes; the photo's own backdrop on the left and the sage foot stay. --- */
@media (min-width:861px){
  html:is(.fb-1,.fb-2) #kweker .fd-card .fd-pn{background:linear-gradient(to right,rgba(249,246,237,0) 0%,rgba(249,246,237,0) 20%,rgba(249,246,237,.5) 40%,rgba(251,248,240,.86) 100%)}
}
@media (min-width:861px) and (max-width:1199px){
  html:is(.fb-1,.fb-2) #kweker .fd-card .fd-pn{background:linear-gradient(to right,rgba(249,246,237,0) 0%,rgba(249,246,237,0) 34%,rgba(249,246,237,.5) 56%,rgba(251,248,240,.86) 100%)}
}

/* --- 2 · the promise as the section heading on the clean page --- */
html.fb-2 .fb-hd{display:block;padding-bottom:clamp(28px,3.2vw,48px)}
.fb-h{margin:0;font-size:clamp(34px,4.2vw,58px);line-height:1.04;letter-spacing:-.035em;font-weight:600;color:#141413}
.fb-h span{display:block}
html.fb-2 #kweker .fp-h{display:none}
html.fb-2 #kweker .fp-txt{margin-top:0!important}
/* the name of the guarantee leads the panel */
html.fb-2 #kweker .fp-txt b{display:block;margin-bottom:clamp(10px,1vw,14px);font-size:clamp(23px,1.9vw,28px);line-height:1.14;letter-spacing:-.028em;text-wrap:balance}
@media (min-width:861px) and (max-width:1199px){
  html.fb-2 #kweker .fp-txt b{font-size:22px}
}
@media (max-width:860px){
  .fb-h{font-size:clamp(26px,7.1vw,34px);line-height:1.08}
  html.fb-2 .fb-hd{padding-bottom:22px}
  html.fb-2.fd-podpis #kweker .fp-txt{padding-top:28px}
  html.fb-2 #kweker .fp-txt b{font-size:clamp(19px,5.3vw,21px);line-height:1.2;margin-bottom:8px}
}
'''
rep('</head>', '<style id="fd-kop-fable">' + CSS + '</style></head>')
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Переход к гарантии</i>'
    '<button type="button" data-g="fb" data-v="0" aria-pressed="false">0 · Как сейчас</button>'
    '<button type="button" data-g="fb" data-v="1" aria-pressed="true">1 · Воздух и тон</button>'
    '<button type="button" data-g="fb" data-v="2" aria-pressed="false">2 · Воздух, тон и заголовок</button></div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} fb-1">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Переход к гарантии · Fable</title>', 1)
(D / 'fd-kop-fable.html').write_text(s)
print('ok', len(s))
