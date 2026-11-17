# Mockup tool (not site code): fonts-fable.html = the main mockup with extra typeface states from the independent type
# review (17 Nov). Same mechanism as build_fonts.py (html.ff-N classes + the review bar); existing files are untouched.
#   html.ff-0  Manrope (now), reference
#   html.ff-1  Fraunces 480 / SOFT 50 + Manrope, exactly as in fonts.html, reference
#   html.ff-5  Newsreader + Manrope: the calm editorial serif of ff-2, but the approved text font stays (2 families)
#   html.ff-6  Source Serif 4 + Manrope: a sturdier, more neutral serif with a real display optical size
#   html.ff-7  Fraunces + Manrope, retuned: lighter (430), SOFT 30, tighter tracking; not a new pairing, a setting of ff-1
# Unlike build_fonts.py the H1 and the H2 get their own weight and letter-spacing, and the guarantee's lead line goes back
# to the text font (a serif at 20px next to 15px sans text reads as a third voice).
# Usage: python3 tools/build_fonts_fable.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

GF = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
      'family=Fraunces:opsz,wght,SOFT@9..144,300..700,0..100'
      '&family=Newsreader:opsz,wght@6..72,300..700'
      '&family=Source+Serif+4:opsz,wght@8..60,300..700&display=swap">')
CSS = r'''
/* ===== typeface candidates, independent review (17 Nov) ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
html{--ffb:'Manrope',system-ui,sans-serif;--fvs:normal}
html.ff-1{--ffd:'Fraunces',Georgia,serif;--w1:480;--w2:480;--ls1:-.012em;--ls2:-.012em;--fvs:'SOFT' 50}
html.ff-5{--ffd:'Newsreader',Georgia,serif;--w1:500;--w2:500;--ls1:-.018em;--ls2:-.014em}
html.ff-6{--ffd:'Source Serif 4',Georgia,serif;--w1:500;--w2:500;--ls1:-.022em;--ls2:-.018em}
html.ff-7{--ffd:'Fraunces',Georgia,serif;--w1:430;--w2:430;--ls1:-.022em;--ls2:-.018em;--fvs:'SOFT' 30}
html:not(.ff-0){--font-display:var(--ffd)}
html:not(.ff-0) :is(h1,h1 *,h2,h2 *,.wh2-facts b){font-family:var(--ffd)!important;font-variation-settings:var(--fvs);
  font-optical-sizing:auto;font-variant-numeric:lining-nums}
html:not(.ff-0) :is(h1,h1 *){font-weight:var(--w1)!important;letter-spacing:var(--ls1)!important}
html:not(.ff-0) :is(h2,h2 *,.wh2-facts b){font-weight:var(--w2)!important;letter-spacing:var(--ls2)!important}
/* ff-1 is the reference from fonts.html: there the guarantee's lead line is in the heading font too */
html.ff-1 #kweker .fp-txt b{font-family:var(--ffd)!important;font-weight:480!important;letter-spacing:-.012em!important;font-variation-settings:var(--fvs)}
/* the review bar keeps its own font */
.rv,.rv *{font-family:system-ui,sans-serif!important}
'''
rep('</head>', GF + '<style id="fonts">' + CSS + '</style></head>')
B = lambda v, t, on: f'<button type="button" data-g="ff" data-v="{v}" aria-pressed="{"true" if on else "false"}">{t}</button>'
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Шрифт</i>'
    + B('0', '0 · Manrope (сейчас)', 0) + B('1', '1 · Fraunces + Manrope (как было)', 0)
    + B('5', '5 · Newsreader + Manrope', 1) + B('6', '6 · Source Serif 4 + Manrope', 0)
    + B('7', '7 · Fraunces 430 / SOFT 30 + Manrope', 0) + '</div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} ff-5">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Шрифт · выбор (Fable)</title>', 1)
(D / 'fonts-fable.html').write_text(s)
print('ok', len(s))
