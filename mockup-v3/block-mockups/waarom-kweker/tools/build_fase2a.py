# Mockup tool (not site code): fase2a.html = the main mockup with "Hoe het werkt" (phase 2, item 2.1) in three layouts
# instead of the placeholder between the guarantee and the footer (review round 3, 18 Nov). Review bar:
#   hw-d Van veld naar tuin (field photo melting into a garden photo, a route of four verbs) · hw-e Woorden (the route alone)
# Round 1 (icons, "STAP" labels, chips, white cards) was not the page's style; round 2 reused our own blocks (nothing new).
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

STEPS = [  # (verb, text, meta)
    ('Kiezen', 'Soort, maat en aantal. Bij elke soort staan alle maten met hun prijs.', ''),
    ('Bestellen', 'Online of per telefoon. U&nbsp;betaalt met iDEAL, per overschrijving of bij ontvangst; zakelijk op factuur.', ''),
    ('Afspreken', 'Samen kiezen we de dag van bezorgen of afhalen, wanneer het u&nbsp;uitkomt.', ''),
    ('Ontvangen', 'Bezorgd of afgehaald. De bezorgkosten hangen af van afstand en aantal; u&nbsp;ziet ze vóór u&nbsp;betaalt.',
     '<p class="hw-m">Afhalen: Esserbroekweg&nbsp;2, Otterlo. <span class="nb">Ma–vr 08:00–17:00,</span> <span class="nb">za 09:00–13:00.</span></p>'),
]
H2 = lambda i: f'<h2 id="h-hw-{i}" class="hw-h"><span>Van ons veld naar uw tuin,</span> <span>in vier stappen.</span></h2>'
sec = lambda v, body: f'<section class="hw hw-{v}" aria-labelledby="h-hw-{v}"><div class="in">{body}</div></section>'
ROUTE = '<ol class="hw-route">' + ''.join(f'<li><h3>{v}</h3><p>{p}</p>{x}</li>' for v, p, x in STEPS) + '</ol>'
VD = (H2('d') + '<div class="hwd"><div class="hwd-pan">'
     '<img class="hwd-veld" src="img/hw-veld.webp" alt="Ons rhododendronveld in Otterlo" loading="lazy">'
     '<img class="hwd-tuin" src="img/hw-tuin.webp" alt="Een Cunningham&#x27;s White in een tuin" loading="lazy">'
     '</div>' + ROUTE + '</div>')
VE = H2('e') + ROUTE

PH = '<div class="between"><div class="in"><span>… hier volgt Hoe het werkt: bij de stap «afhalen» staan het adres en de openingstijden …</span></div></div>'
rep(PH, sec('d', VD) + sec('e', VE))
rep('</head>', '<style id="hoe-werkt-css">' + (D / 'tools' / 'hoe-werkt.css').read_text() + '</style>'
    '<style id="fase2a-rv">body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}</style></head>')
Bt = lambda g, v, t, on: f'<button type="button" data-g="{g}" data-v="{v}" aria-pressed="{"true" if on else "false"}">{t}</button>'
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Hoe het werkt</i>'
    + Bt('hw', 'd', 'D · С поля в сад', 1) + Bt('hw', 'e', 'E · Слова', 0) + '</div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} hw-d">', s, count=1)
s = re.sub(r'<title>[^<]*</title>', '<title>Этап 2 · Hoe het werkt</title>', s, count=1)
(D / 'fase2a.html').write_text(s)
print('ok', len(s))
