# Mockup tool (not site code): fd-gar.html = the main mockup with the founder card turned into the growth-guarantee
# block (owner, 16 Nov: "what if this card becomes the guarantee block?"). The guarantee follows the research report
# "Гарантия приживаемости у конкурентов": until 31 December of the year after delivery, a new plant delivered free,
# reporting with a photo. All Dutch copy is a DRAFT; the term and the promise are for the company owner to confirm.
#   html.gr-1  гарантия + номера: guarantee headline, three short points, the link to the conditions, the contact list
#   html.gr-2  обещание Герта: a headline with the term, the promise in Gert's words on a moss rule, signed, contacts
#   html.gr-3  помощь + гарантия: today's card ("Twijfelt u welke soort past?") with one guarantee line above the numbers
#   html.gr-4  только гарантия: today's text removed; headline, the promise, three steps to report, the conditions link
# In every option the first Waarom wij reason says the same thing (one wording on the whole page).
# Usage: python3 tools/build_fd_gar.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

# one wording: the Waarom wij reason
rep('<h3>Aangroeigarantie op elke plant</h3><p>Slaat een plant in het eerste seizoen <span class="nb">niet aan?</span> Dan vervangen wij hem kosteloos.</p>',
    '<h3>Aangroeigarantie tot eind volgend jaar</h3><p>Slaat een plant niet aan? Dan krijgt u <span class="nb">kosteloos een nieuwe.</span></p>')

m = re.search(r'(<div class="fd-pn">)(<h2 id="h-kweker".*?</dl></div>)(</div></div></div></section>)', s, re.S)
assert m
old = m.group(2)
contacts = re.search(r'<div class="fp-act"><dl>.*?</dl></div>', old, re.S).group(0)
contacts2 = re.sub(r'<div><dt>Open</dt>.*?</div>(?=</dl>)', '', contacts, flags=re.S)   # Bellen + WhatsApp only
WA = '<a href="https://wa.me/31620297849">06&nbsp;20&nbsp;29&nbsp;78&nbsp;49</a>'
CK = '<svg class="ck" viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8.5l3.2 3.2L13 4.8"/></svg>'
MORE = '<p class="g-more"><a href="#garantie">Lees de garantievoorwaarden</a></p>'

V1 = ('<div class="gv gv-1">'
      '<h2 id="h-kweker" class="fp-h"><span>Slaat een plant niet aan?</span> <span>Dan krijgt u een nieuwe.</span></h2>'
      '<ul class="gl"><li>' + CK + '<span>Aangroeigarantie tot eind volgend jaar</span></li>'
      '<li>' + CK + '<span>De nieuwe plant bezorgen wij kosteloos</span></li>'
      '<li>' + CK + '<span>Melden kan met een foto via WhatsApp</span></li></ul>' + MORE +
      '<p class="fp-lead">Een vraag of iets melden? Bel of app met <b>Gert Top</b>, oprichter en kweker, <span class="nb">of met zijn team:</span></p>'
      + contacts2 + '</div>')
V2 = ('<div class="gv gv-2">'
      '<h2 class="fp-h"><span>Elke plant met aangroeigarantie,</span> <span>tot eind volgend jaar.</span></h2>'
      '<blockquote class="gq"><p>Wij kweken elke rhododendron zelf. Slaat er toch een niet aan? Stuur ons een foto, '
      'dan brengen wij kosteloos een nieuwe.</p><footer>Gert Top, oprichter en kweker</footer></blockquote>'
      + MORE + contacts2 + '</div>')
V3 = ('<div class="gv gv-3">'
      '<h2 class="fp-h"><span>Twijfelt u welke soort past?</span> <span>Wij denken met u mee.</span></h2>'
      '<p class="fp-txt">Eén gewas, sinds 2001: daardoor weten wij wat een rhododendron nodig heeft. '
      '<span class="v3-2">Kom gerust langs in Otterlo, <span class="nb">ook zonder afspraak.</span></span></p>'
      '<p class="gk-line"><b>Aangroeigarantie tot eind volgend jaar.</b> Slaat een plant niet aan, '
      '<span class="nb">dan brengen wij kosteloos een nieuwe.</span></p>'
      '<p class="fp-lead">Bel of app met <b>Gert Top</b>, oprichter en kweker, <span class="nb">of met zijn team:</span></p>'
      + contacts + '</div>')
V4 = ('<div class="gv gv-4">'
      '<h2 class="fp-h"><span>Slaat een plant niet aan?</span> <span>Dan brengen wij een nieuwe.</span></h2>'
      '<p class="fp-txt">Aangroeigarantie op elke rhododendron, tot en met 31&nbsp;december van het jaar na levering. '
      'U hoeft niet uit te leggen <span class="nb">waardoor het misging.</span></p>'
      '<ol class="gs"><li><b>1</b><span>Stuur een foto via WhatsApp: ' + WA + '</span></li>'
      '<li><b>2</b><span>Binnen twee werkdagen hoort u van ons</span></li>'
      '<li><b>3</b><span>Wij bezorgen kosteloos een nieuwe plant</span></li></ol>' + MORE + '</div>')
s = s.replace(m.group(0), m.group(1) + V1 + V2 + V3 + V4 + m.group(3), 1)

CSS = r'''
/* ===== founder card as the guarantee block (review, 16 Nov) ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
.gv{display:none}
html.gr-1 .gv-1,html.gr-2 .gv-2,html.gr-3 .gv-3,html.gr-4 .gv-4{display:contents}
.gl,.gs{list-style:none;margin:0;padding:0}
.gl li > span,.gs li > span{text-wrap:pretty}
.gl{display:grid;gap:8px;font-size:16.5px;line-height:1.4;color:#2f2e2a}
.gl li{display:flex;gap:10px;align-items:baseline}
.ck{width:16px;height:16px;flex:none;fill:none;stroke:var(--moss);stroke-width:2;stroke-linecap:round;stroke-linejoin:round;position:relative;top:2px}
.g-more{font-size:15px;line-height:1.4}
.fp .g-more a{font-weight:500;text-underline-offset:4px;text-decoration-thickness:1px}
.gq{margin:0;border-left:2px solid var(--moss);padding-left:18px}
.gq p{font-size:17px;line-height:1.5;color:#2f2e2a;text-wrap:pretty}
.gq footer{margin-top:8px;font-size:14.5px;line-height:1.4;font-weight:600;color:#141413}
.gk-line{font-size:16px;line-height:1.5;color:#2f2e2a;padding:12px 16px;border-radius:14px;background:rgba(63,74,55,.08)}
.gk-line b{font-weight:600;color:#141413}
.gs{display:grid;gap:10px;font-size:16px;line-height:1.4;color:#2f2e2a}
.gs li{display:grid;grid-template-columns:26px minmax(0,1fr);align-items:baseline}
.gs b{font-weight:600;color:var(--moss);font-variant-numeric:tabular-nums}
.fp .gs a{font-weight:600}

@media (min-width:861px){
  .fp .gl,.fp .gq,.fp .gs{margin-top:clamp(18px,1.8vw,24px)}
  .fp .g-more{margin-top:12px}
  .fp .gk-line{margin-top:clamp(16px,1.6vw,22px)}
  html.gr-1 .fp .fp-lead{margin-top:clamp(20px,2vw,28px)}
  html.gr-2 .fp-act{margin-top:clamp(20px,2vw,28px)}
}
@media (min-width:861px) and (max-width:1199px){
  .gl{font-size:15.5px;gap:6px} .gq p{font-size:15.5px} .gs{font-size:15px;gap:8px} .g-more{font-size:14px}
  .gk-line{font-size:15px;padding:8px 12px}
  html.gr-3 .fp .gk-line{margin-top:14px}
  html.gr-3 .fp .fp-lead{margin-top:18px}
}
/* 3 keeps today's text plus the guarantee line: up to 1279 px the hours row goes (they are in the footer), so the card
   keeps its height and the portrait its scale */
@media (min-width:861px) and (max-width:1279px){ html.gr-3 .fp-act dl > div:last-child > *{display:none} }
@media (min-width:861px) and (max-width:999px){ html.gr-3 .v3-2{display:none} }
@media (max-width:860px){
  html.fd-podpis :is(.gl,.g-more,.gs){order:2;padding:16px 22px 0}
  html.fd-podpis .g-more{padding-top:12px}
  html.fd-podpis .gq{order:2;margin:18px 22px 0}
  html.fd-podpis .gk-line{order:2;margin:16px 22px 0}
  .gl{font-size:16px} .gq p{font-size:16px}
}
'''
rep('</head>', '<style id="fd-gar">' + CSS + '</style></head>')
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Гарантия у Герта</i>'
    '<button type="button" data-g="gr" data-v="1" aria-pressed="true">1 · Гарантия + номера</button>'
    '<button type="button" data-g="gr" data-v="2" aria-pressed="false">2 · Обещание Герта</button>'
    '<button type="button" data-g="gr" data-v="3" aria-pressed="false">3 · Помощь + гарантия</button>'
    '<button type="button" data-g="gr" data-v="4" aria-pressed="false">4 · Только гарантия</button></div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} gr-1">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Гарантия у Герта</title>', 1)
(D / 'fd-gar.html').write_text(s)
print('ok', len(s))
