# Mockup tool (not site code): fd-contact.html = the main mockup with three quiet ways to put the grower's contact and the
# walk-in visit into the founder block (audit item 1, 12 Nov). No buttons or pills: the owner removed those on 6 Nov.
# Facts (owner, 12 Nov): both numbers (06 20 10 43 12, 06 20 29 78 49, WhatsApp on the second); hours Mon–Fri 08:00–17:00,
# Sat 09:00–13:00; visitors are welcome without an appointment: to look round, to talk, or to buy and take plants home.
# Address from the live site: Esserbroekweg 2, 6731 DB Otterlo.
#   html.fc-0  как сейчас
#   html.fc-a  две тихие строки под цитатой: "Bel of app Gert …" and "Kom langs …"
#   html.fc-b  визитка: a hairline, then two short columns "Bellen of appen" | "Langskomen" (address, hours, walk-in)
#   html.fc-c  приглашение: one sentence of invitation, then the address and hours, then the numbers
# Usage: python3 tools/build_fd_contact.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

T1 = '<a href="tel:+31620104312">06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</a>'
T2 = '<a href="tel:+31620297849">06&nbsp;20&nbsp;29&nbsp;78&nbsp;49</a>'
WA = '<a href="https://wa.me/31620297849">WhatsApp</a>'
MAPS = 'https://www.google.com/maps/search/Esserbroekweg+2+Otterlo'

A = ('<div class="fd-ct fd-ct-a">'
     '<p><span class="fd-k">Bel of app Gert</span> ' + T1 + ' · <span class="nb">' + T2 + ' · ' + WA + '</span></p>'
     '<p><span class="fd-k">Kom langs</span> <a href="' + MAPS + '">Esserbroekweg&nbsp;2, Otterlo</a> · '
     '<span class="nb">ma–vr 08–17</span>, <span class="nb">za 09–13</span>, zonder afspraak</p></div>')
B = ('<div class="fd-ct fd-ct-b">'
     '<div><h3>Bellen of appen</h3><p>' + T1 + '<br>' + T2 + ' · ' + WA + '</p></div>'
     '<div><h3>Langskomen</h3><p><a href="' + MAPS + '">Esserbroekweg&nbsp;2<br>6731&nbsp;DB Otterlo</a></p>'
     '<p>Ma–vr 08:00–17:00<br>Za 09:00–13:00<br>Zonder afspraak welkom</p></div></div>')
C = ('<div class="fd-ct fd-ct-c">'
     '<p class="fd-inv">Kom gerust langs, ook zonder afspraak: rondkijken, advies vragen of direct meenemen.</p>'
     '<p><a href="' + MAPS + '">Esserbroekweg&nbsp;2, Otterlo</a> · <span class="nb">ma–vr 08:00–17:00</span>, <span class="nb">za 09:00–13:00</span></p>'
     '<p>Bel ' + T1 + ' of <span class="nb">' + T2 + ' · ' + WA + '</span></p></div>')
rep('</blockquote></div></div></div></div></section>', '</blockquote></div>' + A + B + C + '</div></div></div></section>')

CSS = r'''
/* ===== founder block · contact and walk-in (review, 12 Nov) ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
.fd-ct{display:none;font-size:15px;line-height:1.55;color:#3d3c37}
html.fc-a .fd-ct-a,html.fc-c .fd-ct-c{display:block}
html.fc-b .fd-ct-b{display:grid}
.fd-ct p{margin:0}
.fd-ct a{color:var(--moss);font-weight:600;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:4px;
  text-decoration-color:rgba(63,74,55,.4)}
.fd-ct a:hover{text-decoration-color:var(--moss)}
.fd-ct a:focus-visible{outline:2px solid var(--moss);outline-offset:3px;border-radius:3px}

/* A · two quiet lines under the quote */
.fd-ct-a{margin-top:clamp(22px,2.2vw,32px)}
.fd-ct-a p+p{margin-top:6px}
.fd-ct-a .fd-k{color:#141413;font-weight:600;margin-right:4px}

/* B · a card-like footer: a hairline, two short columns */
.fd-ct-b{grid-template-columns:repeat(2,minmax(0,1fr));column-gap:clamp(20px,2.4vw,40px);margin-top:clamp(24px,2.4vw,36px);
  padding-top:clamp(18px,1.8vw,24px);border-top:1px solid rgba(20,20,19,.16)}
.fd-ct-b h3{margin:0 0 6px;font-size:13.5px;line-height:1.3;font-weight:600;letter-spacing:.01em;color:#141413}
.fd-ct-b p+p{margin-top:6px}

/* C · an invitation, then the details */
.fd-ct-c{margin-top:clamp(22px,2.2vw,32px)}
.fd-ct-c .fd-inv{font-size:16.5px;line-height:1.5;color:#141413;max-width:40ch;margin-bottom:10px;text-wrap:pretty}
.fd-ct-c p+p{margin-top:4px}

/* desktop: the contact takes the panel's bottom padding, so the card (and the approved portrait crop) keeps its height */
@media (min-width:861px){
  html:is(.fc-a,.fc-b,.fc-c) .fd-pn{padding-bottom:clamp(32px,4vw,64px)}
  html:is(.fc-a,.fc-b,.fc-c) .fd-qw{padding-top:clamp(24px,2.4vw,40px)}
}
/* phone («Подпись»): the contact sits after the quote, before the portrait */
@media (max-width:860px){
  html.fd-podpis .fd-ct{order:3;margin-inline:22px}
  .fd-ct-b{grid-template-columns:1fr;row-gap:14px}
}
'''
rep('</head>', '<style id="fd-contact">' + CSS + '</style></head>')
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Контакт в блоке Герта</i>'
    '<button type="button" data-g="fc" data-v="0" aria-pressed="false">0 · Как сейчас</button>'
    '<button type="button" data-g="fc" data-v="a" aria-pressed="true">A · Две строки</button>'
    '<button type="button" data-g="fc" data-v="b" aria-pressed="false">B · Визитка</button>'
    '<button type="button" data-g="fc" data-v="c" aria-pressed="false">C · Приглашение</button></div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} fc-a">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Gert Top · contact</title>', 1)
(D / 'fd-contact.html').write_text(s)
print('ok', len(s))
