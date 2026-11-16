# Mockup tool (not site code): fd-gar-fable.html = the main mockup with the founder card as the growth-guarantee block
# (owner's idea, 16 Nov), Fable's own version next to the four options on fd-gar.html.
# The guarantee is provisional until the owner confirms it; all new Dutch copy is a DRAFT.
#   html.gf-0  как сейчас (help in choosing)
#   html.gf-1  the promise leads, the help stays as one line: the headline is the promise in the grower's own "wij";
#              one paragraph carries the name of the guarantee, what the customer gets and the one thing that goes beyond
#              the law (no proof of the cause needed); a link to the conditions; then the same contact list, whose lead-in
#              now also covers advice before the purchase, so nothing of the helper card is lost but its headline.
# The first Waarom wij reason gets the same wording (one wording site-wide); it switches with the state.
# The approved portrait treatments and the card height are untouched: only texts and their sizes/gaps change.
# Usage: python3 tools/build_fd_gar_fable.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

# --- the card: both wordings in the DOM, one shown per state ---
rep('<h2 id="h-kweker" class="fp-h"><span>Twijfelt u welke soort past?</span> <span>Wij denken met u mee.</span></h2>',
    '<h2 id="h-kweker" class="fp-h"><span class="g0">Twijfelt u welke soort past?</span> <span class="g0">Wij denken met u mee.</span>'
    '<span class="g1">Slaat uw rhododendron niet aan?</span> <span class="g1">Dan krijgt u van ons een nieuwe.</span></h2>')
rep('<p class="fp-txt">', '<p class="fp-txt g1"><b>Aangroeigarantie tot eind volgend jaar.</b> Dezelfde soort en maat, kosteloos '
    'bezorgd of klaargezet in Otterlo. De oorzaak hoeft u niet aan te tonen: een paar foto’s volstaan. '
    '<a class="fp-more" href="#garantievoorwaarden">Lees de voorwaarden</a></p><p class="fp-txt g0">')
rep('<p class="fp-lead">', '<p class="fp-lead g1">Vragen over soort of garantie? Bel of app met <b class="nb">Gert Top</b>, '
    'oprichter en kweker, <span class="nb">of met zijn team:</span></p><p class="fp-lead g0">')

# --- Waarom wij, first reason: the same wording ---
rep('<h3>Aangroeigarantie op elke plant</h3><p>Slaat een plant in het eerste seizoen <span class="nb">niet aan?</span> Dan vervangen wij hem kosteloos.</p>',
    '<h3><span class="g0">Aangroeigarantie op elke plant</span><span class="g1">Aangroeigarantie tot eind volgend jaar</span></h3>'
    '<p class="g0">Slaat een plant in het eerste seizoen <span class="nb">niet aan?</span> Dan vervangen wij hem kosteloos.</p>'
    '<p class="g1">Slaat uw rhododendron niet aan? Dan krijgt u van ons een nieuwe: kosteloos bezorgd <span class="nb">of klaargezet in Otterlo.</span></p>')

CSS = r'''
/* ===== founder card as the growth guarantee, Fable's version (review 16 Nov) ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
html.gf-0 .g1,html.gf-1 .g0{display:none!important}
/* the name of the guarantee opens the paragraph in the ink colour: a fact in the sentence, not a label above it */
.fp-txt b{font-weight:600;color:#141413}
/* the link to the full conditions closes the paragraph on its own line */
.fp-more{display:block;width:max-content;margin-top:8px;font-size:15px}
@media (min-width:861px){
  /* the promise is two full sentences, a little longer than the helper headline: one step smaller, so each sentence
     keeps its own line and the group still fits the unchanged card height */
  html.gf-1 .fp-h{font-size:clamp(28px,2.8vw,40px)}
  html.gf-1 .fp-h span{white-space:nowrap}
  html.gf-1 .fp-txt{max-width:50ch}
  html.gf-1 .fp .fp-lead{max-width:50ch}
}
@media (min-width:861px) and (max-width:1199px){
  html.gf-1 .fp-h{font-size:clamp(22px,2.5vw,30px)}
  html.gf-1 .fp-txt{margin-top:14px!important}
  html.gf-1 .fp .fp-lead{margin-top:18px}
  html.gf-1 .fp-act{margin-top:10px}
  html.gf-1 .fp-act dl{row-gap:6px}
  /* narrow desktop: the link runs on in the paragraph, which saves a line */
  html.gf-1 .fp-more{display:inline;margin:0;font-size:inherit;white-space:nowrap}
}
@media (max-width:860px){
  html.gf-1.fd-podpis .fp-h{font-size:clamp(24px,6.7vw,32px)}
}
'''
rep('</head>', '<style id="fd-gar-fable">' + CSS + '</style></head>')
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Гарантия в карточке основателя · Fable</i>'
    '<button type="button" data-g="gf" data-v="0" aria-pressed="false">0 · Сейчас</button>'
    '<button type="button" data-g="gf" data-v="1" aria-pressed="true">1 · Обещание + помощь одной строкой</button></div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} gf-1">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Гарантия · карточка основателя (Fable)</title>', 1)
(D / 'fd-gar-fable.html').write_text(s)
print('ok', len(s))
