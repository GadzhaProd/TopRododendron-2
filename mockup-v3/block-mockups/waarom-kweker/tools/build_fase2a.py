# Mockup tool (not site code): fase2a.html = the main mockup with "Hoe het werkt" (phase 2, item 2.1) in three layouts
# instead of the placeholder between the guarantee and the footer. Review bar: hw-a Lijn · hw-b Kaarten · hw-c Tijdlijn.
# Facts (owner, 13 and 16 Nov): only the Netherlands; the day by agreement; payment iDEAL, bank transfer, on delivery,
# invoice for businesses; delivery cost by distance and quantity (provisional wording, the founder confirms it).
# The steps say what happens and when; the reasons (fresh dug, own transport) stay in Waarom wij. All Dutch copy is a draft.
# Usage: python3 tools/build_fase2a.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

I = {  # lucide: sprout, credit-card, calendar-days, truck
    'sprout': '<path d="M7 20h10"/><path d="M10 20c5.5-2.5.8-6.4 3-10"/><path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5.4-4.8-.3-1.2-.6-2.3-1.9-3-4.2 2.8-.5 4.4 0 5.5.8z"/><path d="M14.1 6a7 7 0 0 0-1.1 4c1.9-.1 3.3-.6 4.3-1.4 1-1 1.6-2.3 1.7-4.6-2.7.1-4 1-4.9 2z"/>',
    'card': '<rect width="20" height="14" x="2" y="5" rx="2"/><path d="M2 10h20"/>',
    'cal': '<path d="M8 2v4"/><path d="M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/><path d="M8 14h.01"/><path d="M12 14h.01"/><path d="M16 14h.01"/><path d="M8 18h.01"/><path d="M12 18h.01"/>',
    'truck': '<path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2"/><path d="M15 18H9"/><path d="M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.624l-3.48-4.35A1 1 0 0 0 17.52 8H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/>',
}
svg = lambda k: f'<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">{I[k]}</svg>'
PAY = '<p class="hw-pay" aria-label="Betaalwijzen"><span>iDEAL</span><span>Overschrijving</span><span>Bij ontvangst</span><span>Zakelijk op factuur</span></p>'
STEPS = [
    ('sprout', 'Kies soort en maat', 'Bij elke soort staan alle maten met hun prijs. Kies er het aantal bij.', ''),
    ('card', 'Bestel online of telefonisch', 'Via de webshop of per telefoon. U&nbsp;betaalt zoals u&nbsp;wilt:', PAY),
    ('cal', 'Spreek de dag af', 'Samen kiezen we de dag van bezorgen of afhalen, wanneer het u uitkomt.', ''),
    ('truck', 'Bezorgen of afhalen', 'Bezorgkosten hangen af van afstand en aantal; u ziet ze vóór u betaalt.',
     '<p class="hw-m"><b>Afhalen</b> Esserbroekweg&nbsp;2, Otterlo<br>Ma–vr 08:00–17:00 · Za 09:00–13:00</p>'),
]
H2 = lambda i: f'<h2 id="h-hw-{i}" class="hw-h"><span>Van ons veld naar uw tuin,</span> <span>in vier stappen.</span></h2>'
sec = lambda v, body: f'<section class="hw hw-{v}" aria-labelledby="h-hw-{v}"><div class="in">{body}</div></section>'

A = H2('a') + '<ol class="hwa-l">' + ''.join(
    f'<li><span class="hwa-n" aria-hidden="true">{n}</span><h3>{t}</h3><p>{p}</p>{x}</li>' for n, (_, t, p, x) in enumerate(STEPS, 1)) + '</ol>'
B = H2('b') + '<ol class="hwb-l">' + ''.join(
    f'<li><span class="hwb-i">{svg(k)}</span><span class="hw-s">Stap {n}</span><h3>{t}</h3><p>{p}</p>{x}</li>' for n, (k, t, p, x) in enumerate(STEPS, 1)) + '</ol>'
C = ('<div class="hwc-g"><div class="hwc-hd">' + H2('c') + '<p>U kiest en bestelt, de rest stemmen we met&nbsp;u&nbsp;af.</p></div><ol class="hwc-l">' + ''.join(
    f'<li><span class="hwc-i">{svg(k)}</span><div><span class="hw-s">Stap {n}</span><h3>{t}</h3><p>{p}</p>{x}</div></li>' for n, (k, t, p, x) in enumerate(STEPS, 1))
     + '</ol></div>')

PH = '<div class="between"><div class="in"><span>… hier volgt Hoe het werkt: bij de stap «afhalen» staan het adres en de openingstijden …</span></div></div>'
rep(PH, sec('a', A) + sec('b', B) + sec('c', C))
rep('</head>', '<style id="hoe-werkt-css">' + (D / 'tools' / 'hoe-werkt.css').read_text() + '</style>'
    '<style id="fase2a-rv">body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}</style></head>')
Bt = lambda g, v, t, on: f'<button type="button" data-g="{g}" data-v="{v}" aria-pressed="{"true" if on else "false"}">{t}</button>'
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Hoe het werkt</i>'
    + Bt('hw', 'a', 'A · Линия', 1) + Bt('hw', 'b', 'B · Карточки', 0) + Bt('hw', 'c', 'C · Тайм-лайн', 0) + '</div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} hw-a">', s, count=1)
s = re.sub(r'<title>[^<]*</title>', '<title>Этап 2 · Hoe het werkt</title>', s, count=1)
(D / 'fase2a.html').write_text(s)
print('ok', len(s))
