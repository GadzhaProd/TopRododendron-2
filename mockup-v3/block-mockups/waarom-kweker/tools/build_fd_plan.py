# Mockup tool (not site code): fd-plan.html = the main mockup with a plan for the founder card (owner, 13 Nov: "is it
# overloaded, is it needed, which block does it go in?"). Reads index.html, writes fd-plan.html; nothing else is touched.
#   html.fp2-0  как сейчас: the card last on the page, with the quote, the invitation and the 2 × 2 contact grid
#   html.fp2-1  помощник (recommended): the card moves right after the assortment and becomes a helper with one action:
#               who he is (small), one headline, one sentence, phone and WhatsApp as text links, the hours. No quote, no grid.
#               The address and the full visiting details go to a footer sketch; the Waarom wij reason loses its numbers.
#   html.fp2-2  на месте, легче: the card stays last as the portrait of the grower; the quote is replaced by the walk-in
#               invitation with one contact line, and the footer sketch follows right under it.
# The approved portrait treatments (desktop extended shoulder, phone «Подпись») are used unchanged. No buttons or pills.
# New Dutch copy is a DRAFT for the owner to confirm; all data is real (address, numbers, hours, walk-in, since 2001).
# Usage: python3 tools/build_fd_plan.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

T1 = '<a href="tel:+31620104312">06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</a>'
T2 = '<a href="tel:+31620297849">06&nbsp;20&nbsp;29&nbsp;78&nbsp;49</a>'
WA2 = '<a href="https://wa.me/31620297849">06&nbsp;20&nbsp;29&nbsp;78&nbsp;49</a>'
WA = '<a href="https://wa.me/31620297849">WhatsApp</a>'
MAPS = 'https://www.google.com/maps/search/Esserbroekweg+2+Otterlo'

# --- the founder section as it is now; the two new versions keep its figure and replace the text panel
i = s.index('<section class="fd" id="kweker"'); j = s.index('</section>', i) + len('</section>')
cur = s[i:j]
m = re.search(r'<div class="fd-pn">.*</div>(?=</div></div></section>$)', cur, re.S)
assert m
def variant(n, panel):
    v = cur[:m.start()] + '<div class="fd-pn">' + panel + '</div>' + cur[m.end():]
    v = v.replace('<section class="fd" id="kweker" aria-labelledby="h-kweker">', f'<section class="fd fp fp-{n}" id="kweker-{n}" aria-labelledby="h-kweker-{n}">')
    assert f'fp-{n}' in v
    return v

P1 = ('<p class="fp-who"><b>Gert Top</b><span>Oprichter en kweker</span></p>'
      '<h2 id="h-kweker-1" class="fp-h"><span>Twijfelt u welke soort past?</span> <span>Gert denkt met u mee.</span></h2>'
      '<p class="fp-txt">Eén gewas, sinds 2001: daardoor weten wij wat een rhododendron nodig heeft. Bel of app met uw vraag, '
      'of kom langs in Otterlo. <span class="nb">Dat kan zonder afspraak.</span></p>'
      '<div class="fp-act"><dl><div><dt>Bellen</dt><dd>' + T1 + '</dd></div><div><dt>WhatsApp</dt><dd>' + WA2 + '</dd></div></dl>'
      '<p class="fp-hrs">Ma–vr 08:00–17:00, za 09:00–13:00</p></div>')
P2 = ('<div class="fd-name"><h2 id="h-kweker-2">Gert Top</h2><p class="fd-role">Oprichter en kweker</p></div>'
      '<p class="fd-txt">Eén gewas; daardoor weten wij wat een rhododendron nodig heeft.</p>'
      '<div class="fp-inv"><p class="fp-big">Kom gerust langs, <span class="nb">ook zonder afspraak.</span></p>'
      '<p class="fp-sub">Rondkijken, advies vragen of direct meenemen. Liever eerst overleggen? Bel ' + T1 + ' of stuur een ' + WA + '.</p></div>')

FOOT = ('<footer class="ft"><div class="in"><div class="ft-g">'
        '<div class="ft-b"><b>Top Rhododendrons</b><p>Familiekwekerij in Otterlo, sinds 2001.</p></div>'
        '<div><h3>Bezoek</h3><p><a href="' + MAPS + '">Esserbroekweg&nbsp;2<br>6731&nbsp;DB Otterlo</a></p>'
        '<p>Ma–vr 08:00–17:00<br>Za 09:00–13:00</p><p>Zonder afspraak welkom</p></div>'
        '<div><h3>Contact</h3><p><span>Bellen</span>' + T1 + '<br>' + T2 + '</p><p><span>WhatsApp</span>' + WA2 + '</p></div>'
        '</div><p class="ft-note">Эскиз футера: только чтобы показать, куда уезжают адрес и часы. Дизайн футера отдельно.</p></div></footer>')

# 1 · the helper stands right after the assortment, before Hoe het werkt
rep('</section></div><div class="between">', '</section></div>' + variant(1, P1) + '<div class="between">')
# 2 · the lighter card stands where the card is now
s = s[:s.index('<section class="fd" id="kweker"')] + cur + variant(2, P2) + s[s.index('<section class="fd" id="kweker"') + len(cur):]
rep('<div style="height:96px;background:#f1efea"></div></main>', '<div class="fp-tail" style="height:96px;background:#f1efea"></div></main>' + FOOT)
# Hoe het werkt placeholder: says where the pick-up address goes
rep('<span>… hier volgt Hoe het werkt …</span>',
    '<span class="fp-n0">… hier volgt Hoe het werkt …</span><span class="fp-n1">… hier volgt Hoe het werkt: bij de stap «afhalen» staan het adres en de openingstijden …</span>')
# Waarom wij, third reason: without the numbers in 1 and 2 (they are in the header above and with Gert below)
k = s.index('<p class="wh-ct">'); k2 = s.index('</p>', k) + 4
s = s[:k] + s[k:k2].replace('<p class="wh-ct">', '<p class="wh-ct fp-r0">') + \
    '<p class="fp-r1">Twijfelt u over soort of maat? U spreekt de kweker zelf: per telefoon, WhatsApp of op de kwekerij.</p>' + s[k2:]

CSS = r'''
/* ===== founder card · plan (review, 13 Nov) ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
.fp,.ft,.fp-r1,.fp-n1{display:none}
html.fp2-1 .fp-1,html.fp2-2 .fp-2,html:is(.fp2-1,.fp2-2) .ft{display:block}
html:is(.fp2-1,.fp2-2) :is(#kweker,.fp-tail,.fp-r0,.fp-n0){display:none}
html:is(.fp2-1,.fp2-2) .fp-r1{display:block}
html:is(.fp2-1,.fp2-2) .fp-n1{display:inline}

.fp a{color:#141413;font-weight:600;text-decoration:underline;text-decoration-thickness:1.5px;text-underline-offset:5px;text-decoration-color:rgba(63,74,55,.55)}
.fp a:hover{text-decoration-color:var(--moss)}
.fp a:focus-visible{outline:2px solid var(--moss);outline-offset:3px;border-radius:3px}
.fp p,.fp dl,.fp dd,.fp h2{margin:0}

/* 1 · helper: who (small) · headline · one sentence · the action */
.fp-1 > .in{padding-top:clamp(20px,2.6vw,40px);padding-bottom:clamp(56px,6vw,96px)}
.fp-who{display:flex;flex-wrap:wrap;align-items:baseline;column-gap:12px;row-gap:2px}
.fp-who b{font-size:19px;line-height:1.3;font-weight:600;letter-spacing:-.015em;color:#141413}
.fp-who span{font-size:15px;line-height:1.4;color:#3d3c37}
.fp-h{font-size:clamp(30px,3.1vw,44px);line-height:1.06;font-weight:600;letter-spacing:-.035em;color:#141413;text-wrap:balance}
.fp-h span{display:block}.fp .nb{white-space:nowrap}
.fp-txt{font-size:16.5px;line-height:1.55;color:#3d3c37;text-wrap:pretty}
.fp-act dl{display:flex;flex-wrap:wrap;column-gap:clamp(28px,3.6vw,56px);row-gap:14px}
.fp-act dt{font-size:13.5px;line-height:1.4;font-weight:500;color:#45443f;margin-bottom:3px}
.fp-act dd{font-size:clamp(21px,1.75vw,25px);line-height:1.25;letter-spacing:-.02em}
.fp-hrs{margin-top:14px!important;font-size:14.5px;line-height:1.5;color:#3d3c37}

/* 2 · the portrait of the grower, lighter: the invitation takes the quote's place */
.fp-big{font-size:clamp(25px,2.3vw,33px);line-height:1.15;font-weight:500;letter-spacing:-.03em;color:#141413;text-wrap:balance}
.fp-sub{margin-top:14px!important;font-size:16.5px;line-height:1.55;color:#3d3c37;text-wrap:pretty}
.fp-2 > .in{padding-bottom:clamp(56px,6vw,96px)}

@media (min-width:861px){
  /* the text is one group, centred in the panel's height: the same air above and below, and its lower left corner stays
     well above the shoulder; it runs to the panel's right margin */
  .fd.fp .fd-card .fd-pn{justify-content:center;padding-top:var(--fd-top);padding-bottom:var(--fd-bot)}
  .fp-h{margin-top:clamp(18px,1.8vw,26px)!important}
  .fp-txt{margin-top:clamp(16px,1.5vw,22px)!important;max-width:54ch}
  .fp-act{margin-top:clamp(26px,2.6vw,40px)}
  .fd.fp-2 .fd-card .fd-txt{max-width:none}
  .fp-inv{margin-top:clamp(30px,3.2vw,48px);padding-top:clamp(26px,2.8vw,42px);border-top:1px solid rgba(63,74,55,.24)}
  .fp-sub{max-width:50ch}
}
@media (min-width:861px) and (max-width:1199px){
  .fp-h{font-size:clamp(27px,3vw,34px)}
  .fp-txt,.fp-sub{font-size:15.5px;line-height:1.5}
  .fp-act dd{font-size:20px}
  .fp-act dl{column-gap:24px}
}
/* phone («Подпись»): the same light card, the texts first, the portrait rising from the bottom */
@media (max-width:860px){
  html.fd-podpis .fp-who{order:1;padding:28px 22px 0}
  html.fd-podpis .fp-h{order:2;padding:12px 22px 0;font-size:clamp(25px,7.1vw,34px);line-height:1.06}
  html.fd-podpis .fp-txt{order:2;padding:16px 22px 0;font-size:16px;line-height:1.5}
  html.fd-podpis .fp-act{order:3;padding:24px 22px 0}
  .fp-act dl{column-gap:22px}
  .fp-act dd{font-size:clamp(19px,5.4vw,22px)}
  html.fd-podpis .fp-inv{order:3;padding:26px 22px 0}
  html.fd-podpis .fp-big{font-size:clamp(25px,7.1vw,32px);line-height:1.1;font-weight:600;letter-spacing:-.035em}
  .fp-sub{font-size:16px;line-height:1.5}
  .fp-1 > .in{padding-top:8px}
}

/* footer sketch: where the address and the full visiting details live */
.ft{background:#1e231b;color:#e9e8e2;font-size:15px;line-height:1.6}
.ft > .in{padding-top:clamp(44px,5vw,72px);padding-bottom:clamp(28px,3vw,40px)}
.ft-g{display:grid;grid-template-columns:minmax(0,1.6fr) minmax(0,1fr) minmax(0,1fr);gap:32px clamp(28px,5vw,80px)}
.ft p{margin:0}.ft p+p{margin-top:10px}
.ft-b b{display:block;font-size:19px;font-weight:600;letter-spacing:-.02em;color:#fff;margin-bottom:8px}
.ft h3{margin:0 0 10px;font-size:13.5px;line-height:1.4;font-weight:600;color:#b9c4ab}
.ft a{color:#fff;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:4px;text-decoration-color:rgba(255,255,255,.4)}
.ft a:hover{text-decoration-color:#fff}
.ft a:focus-visible{outline:2px solid #fff;outline-offset:3px;border-radius:3px}
.ft p > span{display:block;font-size:13px;color:#b9c4ab}
.ft-note{margin-top:clamp(32px,4vw,56px)!important;padding-top:16px;border-top:1px dashed rgba(255,255,255,.22);font-size:13px;color:#b9c4ab}
@media (max-width:700px){.ft-g{grid-template-columns:minmax(0,1fr)}}
'''
rep('</head>', '<style id="fd-plan">' + CSS + '</style></head>')
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Карточка Герта</i>'
    '<button type="button" data-g="fp2" data-v="0" aria-pressed="false">0 · Сейчас</button>'
    '<button type="button" data-g="fp2" data-v="1" aria-pressed="true">1 · Помощник</button>'
    '<button type="button" data-g="fp2" data-v="2" aria-pressed="false">2 · На месте</button></div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} fp2-1">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Gert Top · план карточки</title>', 1)
(D / 'fd-plan.html').write_text(s)
print('ok', len(s))
