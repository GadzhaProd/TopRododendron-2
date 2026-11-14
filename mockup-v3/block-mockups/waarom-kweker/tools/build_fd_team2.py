# Mockup tool (not site code): fd-team2.html = the main mockup with ways to tie Gert's name to something, instead of a
# lone name line (owner, 14 Nov: "the name must be attached to something, not just a name and guess what it is about").
# All share the headline "Twijfelt u welke soort past? Wij denken met u mee." (Gert and the team). New Dutch copy = draft.
#   html.ft-0  как сейчас (approved state: "Gert denkt met u mee." + byline under the headline)
#   html.ft-1  Fable: a line right above the numbers, "Gert Top, oprichter en kweker, en zijn team"
#   html.ft-2  имя в призыве: the name is part of the sentence that leads into the numbers:
#              "Bel of app met Gert Top, oprichter en kweker, of met zijn team:"; the paragraph keeps the walk-in
#   html.ft-3  слова Герта: the paragraph becomes Gert's own words on a moss rule, signed "Gert Top, oprichter en kweker"
# Usage: python3 tools/build_fd_team2.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

rep('<span>Gert denkt met u mee.</span></h2>',
    '<span class="h-0">Gert denkt met u mee.</span><span class="h-w">Wij denken met u mee.</span></h2>')
txt = re.search(r'<p class="fp-txt">.*?</p>', s, re.S).group(0)
rep(txt, '<p class="fp-txt"><span>Eén gewas, sinds 2001: daardoor weten wij wat een rhododendron nodig heeft. </span>'
         '<span class="t-call">Bel of app met uw vraag, of kom langs in Otterlo. <span class="nb">Dat kan zonder afspraak.</span></span>'
         '<span class="t-visit">Kom gerust langs in Otterlo, <span class="nb">ook zonder afspraak.</span></span></p>'
         '<p class="ft-attr">Gert Top, oprichter en kweker</p>')
rep('<div class="fp-act"><dl>',
    '<p class="ft-line ft-l1"><b>Gert Top</b>, oprichter en kweker, en zijn team</p>'
    '<p class="ft-line ft-l2">Bel of app met <b>Gert Top</b>, oprichter en kweker, <span class="nb">of met zijn team:</span></p>'
    '<div class="fp-act"><dl>')

CSS = r'''
/* ===== founder helper card · where the name belongs (review, 14 Nov) ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
.fp-h .h-w,.t-visit,.ft-attr,.ft-line{display:none}
html:not(.ft-0) .fp-h .h-0{display:none}
html:not(.ft-0) .fp-h .h-w{display:block}
html:not(.ft-0) .fp-by{display:none}
html.ft-2 .t-call{display:none}
html.ft-2 .t-visit{display:inline}
html.ft-1 .ft-l1,html.ft-2 .ft-l2{display:block}
.ft-line{font-size:15.5px;line-height:1.45;color:#3d3c37;text-wrap:pretty}
.ft-line b{font-weight:600;color:#141413}
.ft-l2{font-size:16px;color:#2f2e2a}

/* 3 · Gert's own words: the paragraph and its signature share one moss rule (the line style approved for his quote) */
html.ft-3 .fp-txt{border-left:2px solid var(--moss);padding-left:18px;color:#2f2e2a}
html.ft-3 .ft-attr{display:block;border-left:2px solid var(--moss);padding:8px 0 2px 18px;font-size:14.5px;line-height:1.4;font-weight:600;color:#141413}

@media (min-width:861px){
  .fp .ft-line{margin-top:clamp(24px,2.4vw,34px)}
  html:is(.ft-1,.ft-2) .fp-act{margin-top:clamp(12px,1.2vw,16px)}
  html.ft-3 .fp-act{margin-top:clamp(24px,2.4vw,34px)}
}
@media (min-width:861px) and (max-width:1199px){.ft-line{font-size:14.5px}.ft-l2{font-size:15px}}
@media (max-width:860px){
  html.fd-podpis .ft-line{order:2;padding:22px 22px 0;font-size:15px}
  html.fd-podpis .ft-l2{font-size:15.5px}
  html:is(.ft-1,.ft-2).fd-podpis .fp-act{padding-top:12px}
  /* the rule starts at the text, not in the gap under the headline */
  html.ft-3.fd-podpis .fp-txt{margin:18px 0 0 22px;padding:0 22px 0 16px}
  html.ft-3.fd-podpis .ft-attr{order:2;margin-left:22px;padding-left:16px}
}
'''
rep('</head>', '<style id="fd-team2">' + CSS + '</style></head>')
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Имя Герта</i>'
    '<button type="button" data-g="ft" data-v="0" aria-pressed="false">0 · Сейчас</button>'
    '<button type="button" data-g="ft" data-v="1" aria-pressed="false">1 · Fable</button>'
    '<button type="button" data-g="ft" data-v="2" aria-pressed="true">2 · Имя в призыве</button>'
    '<button type="button" data-g="ft" data-v="3" aria-pressed="false">3 · Слова Герта</button></div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} ft-2">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Gert Top · имя к чему</title>', 1)
(D / 'fd-team2.html').write_text(s)
print('ok', len(s))
