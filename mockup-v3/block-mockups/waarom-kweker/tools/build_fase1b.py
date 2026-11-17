# Mockup tool (not site code): fase1b.html = the main mockup with phase 1, step B switched on and off (17 Nov):
#   1.1 the H1 breaks by meaning: "Rhododendrons / die aanslaan. / Met aangroeigarantie." (2 lines where the first sentence fits)
#   1.2 the hero line no longer repeats Waarom wij (veenrijke bodem, vers gerooid, eigen transport are all there):
#       A "Rechtstreeks van onze familiekwekerij in Otterlo, sinds 2001."
#       B "Van onze familiekwekerij in Otterlo: zeven soorten, van 40 tot 225 cm."
#   1.3 Waarom wij: the two Otterlo reasons ("Welkom op de kwekerij", "Eigen transport of afhalen") become one,
#       "Bezorgd of zelf uitzoeken", so the block is shorter and the range starts higher
#   1.7 "Groothandel": a text link in the hero instead of a second button; in the menu the same weight as the other items
#   html.sb-0 до · html.sb-1 после;  html.hl-a / hl-b the hero line (only after). All new Dutch copy is a draft.
# Usage: python3 tools/build_fase1b.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

# 1.1 a line break after "aanslaan.", and two word groups that never split: "die aanslaan." and "Met aangroeigarantie."
#     (the H1 words sit in an inline flex row, so a full-width item starts a new line and a nowrap group wraps as one word).
#     The result: "Rhododendrons / die aanslaan. / Met aangroeigarantie." on desktop and phone,
#     "Rhododendrons die aanslaan. / Met aangroeigarantie." where the first sentence fits on one line.
W = lambda t, m='0.26em': f'<span class="inline-block" style="margin-right: {m}; opacity: 1; transform: none;">{t}</span>'
rep(W('die') + W('aanslaan.'), '<span class="h1-g">' + W('die') + W('aanslaan.') + '</span><span class="h1-br" aria-hidden="true"></span>')
rep(W('Met') + W('aangroeigarantie.', '0px'), '<span class="h1-g">' + W('Met') + W('aangroeigarantie.', '0px') + '</span>')
# 1.2 the hero line
OLD = 'Gekweekt op veenrijke bodem, met een sterk wortelstelsel. Vers gerooid voor uw levering, bezorgd met eigen transport of af te halen in Otterlo.'
rep(OLD, '<span class="hl0">' + OLD + '</span>'
    '<span class="hla">Rechtstreeks van onze familiekwekerij in Otterlo, <span class="nb">sinds 2001.</span></span>'
    '<span class="hlb">Van onze familiekwekerij in Otterlo: zeven soorten, <span class="nb">van 40 tot 225&nbsp;cm.</span></span>')
# 1.3 Waarom wij: the two Otterlo reasons and the merged one
rep('<li><div><h3>Welkom op de kwekerij</h3>', '<li class="r34"><div><h3>Welkom op de kwekerij</h3>')
rep('<li><div><h3>Eigen transport of afhalen</h3>', '<li class="r34"><div><h3>Eigen transport of afhalen</h3>')
rep('<p>Bezorgd met eigen transport door heel Nederland, of af te halen in Otterlo.</p></div></li></ol>',
    '<p>Bezorgd met eigen transport door heel Nederland, of af te halen in Otterlo.</p></div></li>'
    '<li class="rm"><div><h3>Bezorgd of zelf uitzoeken</h3><p>Wij bezorgen met eigen transport door heel Nederland. '
    'Of kies uw planten zelf uit in Otterlo, <span class="nb">ook zonder afspraak.</span></p></div></li></ol>')
# 1.7 mark the hero's Groothandel button and the menu item
rep('hover:bg-white hover:text-[#141414] hover:border-white h-12 text-[14px] rounded-ui group/btn px-5 split:h-14 split:px-8 split:text-[15px]" href="#">Groothandel</a>',
    'hover:bg-white hover:text-[#141414] hover:border-white h-12 text-[14px] rounded-ui group/btn px-5 split:h-14 split:px-8 split:text-[15px] gh-btn" href="#">Groothandel</a>')
rep('class="text-[14px] tracking-[0.01em] transition-colors hover:text-fg font-medium text-fg">Groothandel</a>',
    'class="text-[14px] tracking-[0.01em] transition-colors hover:text-fg font-medium text-fg gh-nav">Groothandel</a>')

CSS = r'''
/* ===== phase 1, step B (review, 17 Nov) ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
.h1-br,.hla,.hlb,.wh2-list li.rm{display:none}
/* 1.1 */
html.sb-1 .h1-br{display:block;flex-basis:100%;height:0}
.h1-g{display:contents}
html.sb-1 .h1-g{display:inline-flex;flex-wrap:nowrap;margin-right:.26em}
html.sb-1 .h1-g:last-child,html.sb-1 .h1-g > span:last-child{margin-right:0!important}
/* "Met aangroeigarantie." is about 9.7 em wide: the H1 column grows with the display size so the group always fits
   (desktop: 36rem up to 40rem, the 1600px width already; tablet portrait: 21.5rem up to 29rem). The scrim edge (--tc) follows. */
@media (min-width:1024px),(min-width:768px) and (orientation:landscape){
  html.sb-1{--hc:clamp(36rem,calc(var(--t-display) * 9.75),40rem);--tc:calc(clamp(20px,4vw,64px) + var(--hc))}
  html.sb-1 #hero .split\:max-w-\[36rem\]{max-width:var(--hc)}
}
@media (min-width:640px) and (max-width:1023px) and (orientation:portrait){
  html.sb-1 #hero .tabp\:max-w-\[21\.5rem\]{max-width:clamp(21.5rem,calc(var(--t-display) * 9.75),29rem)}
}
/* 1.2 */
html.sb-1 .hl0{display:none}
html.sb-1.hl-a .hla,html.sb-1.hl-b .hlb{display:inline}
/* 1.3 */
/* (the list items are grids, .wh2-list li{display:grid}, so these rules carry the list in their selector) */
html.sb-1 .wh2-list li.r34{display:none}
html.sb-1 .wh2-list li.rm{display:grid}
/* with three reasons the list is shorter than the facts card (by 100 px at 1440): the card follows the list, as before,
   ending on the list's last line, and the four facts share its height in equal slots */
@media (min-width:861px){
  html.sb-1 #waarom .wh2-facts{justify-content:stretch}
  html.sb-1 #waarom .wh2-facts li{flex:1 1 0;padding:12px 0;justify-content:center}
}
/* 1.7 the hero: a white text link with an arrow, the main button stays the one button */
html.sb-1 #hero a.gh-btn{height:auto!important;padding:0 2px!important;border:0!important;background:none!important;border-radius:0!important;
  font-size:var(--t-body)!important;font-weight:500;color:#fff!important;text-decoration:underline;text-decoration-thickness:1px;
  text-underline-offset:5px;text-decoration-color:rgba(255,255,255,.55);align-self:center;margin-left:8px}
html.sb-1 #hero a.gh-btn::after{content:"→";text-decoration:none;display:inline-block;margin-left:6px}
html.sb-1 #hero a.gh-btn:hover{text-decoration-color:#fff}
/* 1.7 the menu: Groothandel as quiet as the other items */
html.sb-1 header a.gh-nav{font-weight:400!important;color:var(--color-fg-2)!important}
html.sb-1 header a.gh-nav:hover{color:var(--color-fg)!important}
'''
rep('</head>', '<style id="fase1b">' + CSS + '</style></head>')
B = lambda g, v, t, on: f'<button type="button" data-g="{g}" data-v="{v}" aria-pressed="{"true" if on else "false"}">{t}</button>'
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты">'
    '<div class="rv-g"><i>Шаг Б</i>' + B('sb', '0', 'До', 0) + B('sb', '1', 'После', 1) + '</div>'
    '<div class="rv-g"><i>Строка под заголовком</i>' + B('hl', 'a', 'A · sinds 2001', 1) + B('hl', 'b', 'B · zeven soorten', 0) + '</div>'
    '</div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} sb-1 hl-a">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Этап 1 · шаг Б</title>', 1)
(D / 'fase1b.html').write_text(s)
print('ok', len(s))
