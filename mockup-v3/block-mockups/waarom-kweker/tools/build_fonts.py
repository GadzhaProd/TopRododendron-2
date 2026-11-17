# Mockup tool (not site code): fonts.html = the main mockup with a typeface switch, to choose the site's fonts before the
# type scale is consolidated (owner, 17 Nov: "first approve the font, then phase 1"). All candidates are Google Fonts.
#   html.ff-0  Manrope (now): one sans for everything
#   html.ff-1  Fraunces (soft serif, headings) + Manrope (text): warm, organic, a garden character
#   html.ff-2  Newsreader (editorial serif, headings) + Inter (text): calm, trustworthy, journal-like
#   html.ff-3  Instrument Serif (headings) + Instrument Sans (text): slender, elegant, the most premium
#   html.ff-4  Hanken Grotesk (one sans): like now, but crisper and more restrained than Manrope
# The heading font goes to the H1, the section H2s, the big facts numbers and the guarantee's lead line; card names,
# reasons, prices and body text use the text font. Sizes stay as they are; only the family, the heading weight and the
# heading letter-spacing change per candidate (serifs need less negative tracking than Manrope).
# Usage: python3 tools/build_fonts.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

GF = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
      'family=Fraunces:opsz,wght,SOFT@9..144,300..700,50'
      '&family=Newsreader:opsz,wght@6..72,300..700'
      '&family=Inter:wght@400..700'
      '&family=Instrument+Serif&family=Instrument+Sans:wght@400..700'
      '&family=Hanken+Grotesk:wght@400..700&display=swap">')
CSS = r'''
/* ===== typeface candidates (review, 17 Nov) ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
html.ff-1{--ffb:'Manrope',system-ui,sans-serif;--ffd:'Fraunces',Georgia,serif;--fdw:480;--fdls:-.012em}
html.ff-2{--ffb:'Inter',system-ui,sans-serif;--ffd:'Newsreader',Georgia,serif;--fdw:500;--fdls:-.01em}
html.ff-3{--ffb:'Instrument Sans',system-ui,sans-serif;--ffd:'Instrument Serif',Georgia,serif;--fdw:400;--fdls:-.005em}
html.ff-4{--ffb:'Hanken Grotesk',system-ui,sans-serif;--ffd:'Hanken Grotesk',system-ui,sans-serif;--fdw:600;--fdls:-.03em}
html:not(.ff-0){--font-sans:var(--ffb);--font-display:var(--ffd)}
html:not(.ff-0) body,html:not(.ff-0) :is(button,input,select,a,p,li,dt,dd,span,h3,b){font-family:var(--ffb)}
html:not(.ff-0) :is(h1,h1 *,h2,h2 *,.wh2-facts b,#kweker .fp-txt b){font-family:var(--ffd)!important;font-weight:var(--fdw)!important;letter-spacing:var(--fdls)!important}
/* the review bar keeps its own font */
.rv,.rv *{font-family:system-ui,sans-serif!important}
'''
rep('</head>', GF + '<style id="fonts">' + CSS + '</style></head>')
B = lambda v, t, on: f'<button type="button" data-g="ff" data-v="{v}" aria-pressed="{"true" if on else "false"}">{t}</button>'
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Шрифт</i>'
    + B('0', '0 · Manrope (сейчас)', 1) + B('1', '1 · Fraunces + Manrope', 0) + B('2', '2 · Newsreader + Inter', 0)
    + B('3', '3 · Instrument Serif + Sans', 0) + B('4', '4 · Hanken Grotesk', 0) + '</div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} ff-0">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Шрифт · выбор</title>', 1)
(D / 'fonts.html').write_text(s)
print('ok', len(s))
