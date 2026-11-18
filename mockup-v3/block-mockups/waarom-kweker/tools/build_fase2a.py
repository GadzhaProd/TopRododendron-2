# Mockup tool (not site code): fase2a.html = the main mockup with "Hoe het werkt" (phase 2, item 2.1) in three layouts
# instead of the placeholder between the guarantee and the footer (review round 2, 18 Nov). Review bar:
#   hw-a Rijen (the Waarom wij list) · hw-b Kolommen (the facts card's figures) · hw-c Veld (the columns in one woven panel)
# Round 1 (icons, "STAP" labels, chips, white cards) was rejected by the owner: not the page's style.
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

STEPS = [
    ('Kies soort en maat', 'Bij elke soort staan alle maten met hun prijs. Kies er het aantal bij.', ''),
    ('Bestel online of telefonisch', 'Via de webshop of per telefoon. U&nbsp;betaalt met iDEAL, per overschrijving of bij ontvangst; zakelijk op factuur.', ''),
    ('Spreek de dag af', 'Samen kiezen we de dag van bezorgen of afhalen, wanneer het u&nbsp;uitkomt.', ''),
    ('Bezorgen of afhalen', 'Bezorgkosten hangen af van afstand en aantal; u&nbsp;ziet ze vóór u&nbsp;betaalt.',
     '<p class="hw-m">Afhalen: Esserbroekweg&nbsp;2, Otterlo. <span class="nb">Ma–vr 08:00–17:00,</span> <span class="nb">za 09:00–13:00.</span></p>'),
]
H2 = lambda i: f'<h2 id="h-hw-{i}" class="hw-h"><span>Van ons veld naar uw tuin,</span> <span>in vier stappen.</span></h2>'
sec = lambda v, body: f'<section class="hw hw-{v}" aria-labelledby="h-hw-{v}"><div class="in">{body}</div></section>'
N = lambda n: f'<span class="hw-n" aria-hidden="true">{n}</span>'

A = H2('a') + '<ol class="hwa-l">' + ''.join(
    f'<li>{N(n)}<h3>{t}</h3><div><p>{p}</p>{x}</div></li>' for n, (t, p, x) in enumerate(STEPS, 1)) + '</ol>'
cols = lambda cls: f'<ol class="{cls}">' + ''.join(
    f'<li>{N(n)}<div><h3>{t}</h3><p>{p}</p>{x}</div></li>' for n, (t, p, x) in enumerate(STEPS, 1)) + '</ol>'
B = H2('b') + cols('hwb-l')
C = H2('c') + '<div class="hwc-p">' + cols('hwc-l') + '</div>'

PH = '<div class="between"><div class="in"><span>… hier volgt Hoe het werkt: bij de stap «afhalen» staan het adres en de openingstijden …</span></div></div>'
rep(PH, sec('a', A) + sec('b', B) + sec('c', C))
rep('</head>', '<style id="hoe-werkt-css">' + (D / 'tools' / 'hoe-werkt.css').read_text() + '</style>'
    '<style id="fase2a-rv">body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}</style></head>')
Bt = lambda g, v, t, on: f'<button type="button" data-g="{g}" data-v="{v}" aria-pressed="{"true" if on else "false"}">{t}</button>'
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Hoe het werkt</i>'
    + Bt('hw', 'a', 'A · Ряды', 1) + Bt('hw', 'b', 'B · Колонки', 0) + Bt('hw', 'c', 'C · Поле', 0) + '</div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} hw-a">', s, count=1)
s = re.sub(r'<title>[^<]*</title>', '<title>Этап 2 · Hoe het werkt</title>', s, count=1)
(D / 'fase2a.html').write_text(s)
print('ok', len(s))
