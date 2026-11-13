# Mockup tool (not site code): fd-name.html = the main mockup with three places for Gert's name and role in the founder
# helper card, the headline always first (owner, 13 Nov: "first the headline, then the rest; the name first does not fit").
#   html.nm-0  как сейчас: name and role on top, then the headline
#   html.nm-1  подпись после текста: headline · paragraph · name and role (as a signature) · contacts
#   html.nm-2  подпись в конце: headline · paragraph · contacts · name and role closing the card
#   html.nm-3  имя в тексте: no separate byline; the paragraph opens with "Gert Top is oprichter en kweker." (draft copy)
# Only the order and the spacing change; sizes, copy (except the draft sentence in 3) and the portraits stay as they are.
# Usage: python3 tools/build_fd_name.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

rep('<p class="fp-txt">Eén gewas, sinds 2001:',
    '<p class="fp-txt"><span class="fp-intro"><b>Gert Top</b> is oprichter en kweker. </span>Eén gewas, sinds 2001:')

CSS = r'''
/* ===== founder helper card · where the name goes (review, 13 Nov) ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
.fp-intro{display:none}
.fp-intro b{font-weight:600;color:#141413}
html.nm-3 .fp-intro{display:inline}
html.nm-3 .fp-who{display:none}

@media (min-width:861px){
  html:is(.nm-1,.nm-2,.nm-3) .fp-h{order:1;margin-top:0!important}
  html:is(.nm-1,.nm-2,.nm-3) .fp-txt{order:2}
  html.nm-3 .fp-act{order:3}
  /* 1 · the signature closes the text, the contacts follow */
  html.nm-1 .fp-who{order:3;margin-top:clamp(18px,1.8vw,24px)}
  html.nm-1 .fp-act{order:4;margin-top:clamp(22px,2.2vw,32px)}
  /* 2 · the contacts follow the text, the signature closes the card */
  html.nm-2 .fp-act{order:3}
  html.nm-2 .fp-who{order:4;margin-top:clamp(22px,2.2vw,32px)}
}
@media (max-width:860px){
  html:is(.nm-1,.nm-2,.nm-3).fd-podpis .fp-h{order:1;padding-top:28px}
  html.nm-1.fd-podpis .fp-who{order:3;padding-top:20px}
  html.nm-1.fd-podpis .fp-act{order:3}
  html.nm-2.fd-podpis .fp-act{order:3}
  html.nm-2.fd-podpis .fp-who{order:4;padding-top:22px}
  html.nm-2.fd-podpis .fd-ph{order:5}
}
'''
rep('</head>', '<style id="fd-name">' + CSS + '</style></head>')
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Имя Герта</i>'
    '<button type="button" data-g="nm" data-v="0" aria-pressed="false">0 · Сейчас</button>'
    '<button type="button" data-g="nm" data-v="1" aria-pressed="true">1 · Подпись после текста</button>'
    '<button type="button" data-g="nm" data-v="2" aria-pressed="false">2 · Подпись в конце</button>'
    '<button type="button" data-g="nm" data-v="3" aria-pressed="false">3 · Имя в тексте</button></div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} nm-1">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Gert Top · где имя</title>', 1)
(D / 'fd-name.html').write_text(s)
print('ok', len(s))
