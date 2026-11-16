# Mockup tool (not site code): fd-kop.html = the main mockup with a section heading above the guarantee card, so the
# assortment and the card read as two sections (owner, 16 Nov: "they sit close, different colours; give this block a
# heading"). All Dutch copy is a DRAFT.
#   html.fk-0  как сейчас (no heading above the card)
#   html.fk-1  обещание наружу: the card's promise becomes the section H2 above the card, at the assortment H2 size;
#              the card keeps the guarantee paragraph and the contacts (no repeated headline)
#   html.fk-2  отдельный заголовок: a section H2 "Wij staan achter elke plant." above the card; the promise stays in the card
# The heading uses the assortment heading's type and spacing (one system for section headings).
# Usage: python3 tools/build_fd_kop.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

rep('<section class="fd fp fp-1" id="kweker" aria-labelledby="h-kweker"><div class="in"><div class="fd-card">',
    '<section class="fd fp fp-1" id="kweker" aria-labelledby="h-kweker"><div class="in">'
    '<div class="fk-hd"><h2 class="fk-h fk-h1"><span>Slaat een plant niet aan?</span> <span>Dan krijgt u een nieuwe.</span></h2>'
    '<h2 class="fk-h fk-h2">Wij staan achter elke plant.</h2></div><div class="fd-card">')

CSS = r'''
/* ===== a section heading above the guarantee card (review, 16 Nov) ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
.fk-hd,.fk-h{display:none}
html:is(.fk-1,.fk-2) .fk-hd{display:block;padding-bottom:clamp(28px,3vw,44px)}
html.fk-1 .fk-h1,html.fk-2 .fk-h2{display:block}
/* the assortment H2: one system for section headings */
.fk-h{margin:0;font-size:clamp(34px,4.2vw,58px);line-height:1.04;letter-spacing:-.035em;font-weight:600;color:#141413;text-wrap:balance}
/* 1 · the promise lives in the heading, so the card starts with the guarantee paragraph */
html.fk-1 #kweker .fp-h{display:none}
html.fk-1 #kweker .fp-txt{margin-top:0!important}
@media (max-width:860px){
  html.fk-1.fd-podpis #kweker .fp-txt{padding-top:28px}
}
/* phone: one sentence per line, at the size the promise had inside the card (no orphaned "aan?") */
@media (max-width:860px){ .fk-h1 span{display:block} .fk-h1{font-size:clamp(26px,7.1vw,34px);line-height:1.08} }
@media (max-width:599px){
  .fk-h2{font-size:clamp(30px,8.6vw,40px)}
  html:is(.fk-1,.fk-2) .fk-hd{padding-bottom:22px}
}
'''
rep('</head>', '<style id="fd-kop">' + CSS + '</style></head>')
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Заголовок блока</i>'
    '<button type="button" data-g="fk" data-v="0" aria-pressed="false">0 · Сейчас</button>'
    '<button type="button" data-g="fk" data-v="1" aria-pressed="true">1 · Обещание наружу</button>'
    '<button type="button" data-g="fk" data-v="2" aria-pressed="false">2 · Отдельный заголовок</button></div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} fk-1">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Заголовок над гарантией</title>', 1)
(D / 'fd-kop.html').write_text(s)
print('ok', len(s))
