# Mockup tool (not site code): fd-team.html = the main mockup with three ways to say that Gert AND his team answer
# (owner, 13 Nov: not only Gert takes the calls; the byline under the headline feels foreign, maybe after the text, before
# the numbers). All new Dutch copy is a DRAFT for the owner; the facts (team, numbers, hours, walk-in) are his.
#   html.fe-0  как сейчас: "Gert denkt met u mee." + byline under the headline
#   html.fe-1  «Wij» + подпись у номеров: headline "Wij denken met u mee."; after the paragraph, right above the numbers,
#              one quiet line "Gert Top en het team van de kwekerij"
#   html.fe-2  «Gert en het team» + фраза у номеров: headline "Gert en het team denken met u mee."; above the numbers the
#              sentence "U spreekt Gert Top, oprichter en kweker, of iemand van zijn team."
#   html.fe-3  имя в тексте: headline "Wij denken met u mee."; the paragraph says "Gert Top, oprichter en kweker, en zijn
#              team helpen u graag."; no separate line
# Usage: python3 tools/build_fd_team.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

rep('<span>Gert denkt met u mee.</span></h2>',
    '<span class="fe-h0">Gert denkt met u mee.</span><span class="fe-h1">Wij denken met u mee.</span>'
    '<span class="fe-h2">Gert en het team denken met u mee.</span></h2>')
rep('Bel of app met uw vraag, of kom langs in Otterlo.',
    '<span class="fe-t3">Gert Top, oprichter en kweker, en zijn team helpen u graag. </span>Bel of app met uw vraag, of kom langs in Otterlo.')
rep('<div class="fp-act"><dl>',
    '<p class="fe-sig fe-s1"><b>Gert Top</b> en het team van de kwekerij</p>'
    '<p class="fe-sig fe-s2">U spreekt <b>Gert Top</b>, oprichter en kweker, of iemand van zijn team.</p>'
    '<div class="fp-act"><dl>')

CSS = r'''
/* ===== founder helper card · Gert and the team (review, 13 Nov) ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
.fp-h .fe-h1,.fp-h .fe-h2,.fe-t3,.fe-sig{display:none}
html:is(.fe-1,.fe-3) .fp-h .fe-h0,html.fe-2 .fp-h .fe-h0{display:none}
html:is(.fe-1,.fe-3) .fp-h .fe-h1{display:block}
html.fe-2 .fp-h .fe-h2{display:block}
html:not(.fe-0) .fp-by{display:none}
html.fe-3 .fe-t3{display:inline}
html.fe-1 .fe-s1,html.fe-2 .fe-s2{display:block}
.fe-sig{font-size:15.5px;line-height:1.45;color:#3d3c37;text-wrap:pretty}
.fe-sig b{font-weight:600;color:#141413}
@media (min-width:861px){
  /* the line opens the contact group: close to the numbers, clearly after the paragraph */
  .fp .fe-sig{margin-top:clamp(24px,2.4vw,34px)}
  html:is(.fe-1,.fe-2) .fp-act{margin-top:clamp(12px,1.2vw,16px)}
}
@media (min-width:861px) and (max-width:1199px){.fe-sig{font-size:14.5px}}
@media (max-width:860px){
  html.fd-podpis .fe-sig{order:2;padding:22px 22px 0;font-size:15px}
  html:is(.fe-1,.fe-2).fd-podpis .fp-act{padding-top:12px}
}
'''
rep('</head>', '<style id="fd-team">' + CSS + '</style></head>')
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Герт и команда</i>'
    '<button type="button" data-g="fe" data-v="0" aria-pressed="false">0 · Сейчас</button>'
    '<button type="button" data-g="fe" data-v="1" aria-pressed="true">1 · «Wij» + подпись</button>'
    '<button type="button" data-g="fe" data-v="2" aria-pressed="false">2 · Герт и команда</button>'
    '<button type="button" data-g="fe" data-v="3" aria-pressed="false">3 · Имя в тексте</button></div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} fe-1">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Gert Top · Герт и команда</title>', 1)
(D / 'fd-team.html').write_text(s)
print('ok', len(s))
