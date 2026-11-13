# Mockup tool (not site code): fd-name-fable.html = the main mockup with two more places for Gert's name and role in the
# founder helper card (designer's proposals, 13 Nov). The headline always comes first (owner: "first the headline, then the
# rest; the name first does not fit"). Companion to fd-name.html (signature after the text / at the end / name in the text).
#   html.nf-0  как сейчас: name and role on top, then the headline
#   html.nf-1  строка под заголовком: headline · one byline "Gert Top, oprichter en kweker" · paragraph · contacts.
#              The headline says "Gert"; the line right under it answers "which Gert?" before the reader moves on.
#   html.nf-2  в списке контактов: headline · paragraph · the label | value list opens with "Kweker | Gert Top, oprichter".
#              The name stands where it is needed: next to the numbers, as on a business card. No separate byline at all.
# Copy: the role line is shortened to fit each place (draft for the owner); nothing else changes. Portraits untouched.
# No caption on the photo, no eyebrow over the headline, no buttons or pills. The desktop card gets lower, never taller.
# Usage: python3 tools/build_fd_name_fable.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

# 1 · the byline, right after the headline
rep('<span>Gert denkt met u mee.</span></h2>',
    '<span>Gert denkt met u mee.</span></h2><p class="fp-by"><b>Gert Top</b>, oprichter en kweker</p>')
# 2 · the name as the first row of the contact list
rep('<div class="fp-act"><dl><div><dt>Bellen</dt>',
    '<div class="fp-act"><dl><div class="fp-nmr"><dt>Kweker</dt><dd class="fp-nm"><b>Gert Top</b><span>, oprichter</span></dd></div>'
    '<div><dt>Bellen</dt>')

CSS = r'''
/* ===== founder helper card · where the name goes, designer's proposals (review, 13 Nov) ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
.fp-by,.fp-act dl > .fp-nmr{display:none}
html:is(.nf-1,.nf-2) .fp-who{display:none}

/* 1 · one line under the headline: the name in ink, the role in the body grey, at the size of the old role line */
html.nf-1 .fp-by{display:block;font-size:15.5px;line-height:1.4;color:#3d3c37}
.fp-by b{font-weight:600;color:#141413}

/* 2 · the first row of the list: the name at the size of the numbers (it is not a link, so no underline), the role small */
html.nf-2 .fp-act dl > .fp-nmr{display:contents}
.fp-nm{font-size:clamp(21px,1.75vw,25px);line-height:1.25;letter-spacing:-.02em;color:#141413}
.fp-nm b{font-weight:600}
.fp-nm span{font-size:15px;letter-spacing:0;color:#3d3c37}

@media (min-width:861px){
  html:is(.nf-1,.nf-2) .fp-h{margin-top:0!important}
  html.nf-1 .fp-by{margin-top:clamp(12px,1.1vw,16px)}
  html.nf-1 .fp-txt{margin-top:clamp(18px,1.7vw,24px)!important}
}
@media (min-width:861px) and (max-width:1199px){
  .fp-nm{font-size:20px}
  .fp-nm span,html.nf-1 .fp-by{font-size:14.5px}
}
@media (max-width:860px){
  html:is(.nf-1,.nf-2).fd-podpis .fp-h{padding-top:28px}
  html.nf-1.fd-podpis .fp-by{order:2;padding:10px 22px 0;font-size:15px}
  .fp-nm{font-size:clamp(19px,5.4vw,22px)}
  .fp-nm span{font-size:14.5px}
}
'''
rep('</head>', '<style id="fd-name-fable">' + CSS + '</style></head>')
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Имя Герта</i>'
    '<button type="button" data-g="nf" data-v="0" aria-pressed="false">0 · Сейчас</button>'
    '<button type="button" data-g="nf" data-v="1" aria-pressed="true">1 · Под заголовком</button>'
    '<button type="button" data-g="nf" data-v="2" aria-pressed="false">2 · В контактах</button></div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} nf-1">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Gert Top · где имя (2)</title>', 1)
(D / 'fd-name-fable.html').write_text(s)
print('ok', len(s))
