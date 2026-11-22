# FROZEN (22 Nov): the owner chose version 2; it is in the main mockup now (tools/header_pill.py), so index.html carries the
# classes this script asserts are absent. Do not rebuild; header2.html stays as the record of the review.
# Mockup tool (not site code): header2.html = the homepage (index.html) with the new header for review: a full-width bar
# at the top, a pill after scrolling (tools/header2.css, tools/header2.js). Two phone versions on the review bar:
#   ph-0 the header as it is now · ph-1 the pill, on the phone always in view · ph-2 the pill, on the phone it slides away
#   on the way down and comes back on the way up. Desktop is the same in 1 and 2.
# For the review the opt-in classes of header2.css are mapped to the bar: "hp" = not ph-0, "hp-hide" = ph-2.
# In the main build: add class "hp" (and "hp-hide" for version 2) to <html> and include the two files as they are.
# Usage: python3 tools/build_header2.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
css = (D / 'tools' / 'header2.css').read_text()
assert css.count('html.hp.hp-hide') == 2
css = css.replace('html.hp.hp-hide', 'html.ph-2').replace('html.hp', 'html:not(.ph-0)')
REVIEW = '''body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
@media (max-width:520px){ .rv{justify-content:flex-start} }
'''
mh = re.search(r'<html lang="nl" class="([^"]*)">', s); assert mh and not any(c.startswith(('ph-', 'hp')) for c in mh.group(1).split())
s = s.replace(mh.group(0), '<html lang="nl" class="' + mh.group(1) + ' ph-1">', 1)
def btn(v, name, on=False):
    return f'<button type="button" data-g="ph" data-v="{v}" aria-pressed="{"true" if on else "false"}">{v}<span class="l"> · {name}</span></button>'
BAR = ('<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Шапка</i>' + btn(0, 'Сейчас') + btn(1, 'Телефон: всегда видна', True)
       + btn(2, 'Телефон: прячется при прокрутке вниз') + '</div></div>')
assert '<div class="rv"' not in s and s.count('<div id="root">') == 1 and s.count('</head>') == 1 and s.count('</body>') == 1
s = s.replace('<div id="root">', BAR + '<div id="root">')
s = s.replace('</head>', '<style id="header2-css">' + css + '</style><style id="header2-review">' + REVIEW + '</style></head>')
s = s.replace('</body>', '<script>' + (D / 'tools' / 'header2.js').read_text() + '</script></body>')
(D / 'header2.html').write_text(s)
print('ok', len(s))
