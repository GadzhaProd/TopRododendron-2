# Mockup tool (not site code): the header as the owner approved it on 22 Nov (header2.html, version 2): a full-width bar at
# the top of the page, a centred pill after scrolling, and on the phone the pill slides away on the way down and comes back
# on the way up. Applied by tools/finalize_main.py after the other steps; the styles and the script are tools/header2.css
# and tools/header2.js, the page opts in with the classes "hp hp-hide" on <html>.
import re, pathlib
T = pathlib.Path(__file__).parent


def apply(s):
    m = re.search(r'<html lang="nl" class="([^"]*)">', s)
    assert m and 'hp' not in m.group(1).split(), m and m.group(1)
    s = s.replace(m.group(0), '<html lang="nl" class="' + m.group(1) + ' hp hp-hide">', 1)
    assert s.count('</head>') == 1 and s.count('</body>') == 1
    s = s.replace('</head>', '<style id="header-pill-css">' + (T / 'header2.css').read_text() + '</style></head>', 1)
    return s.replace('</body>', '<script id="header-pill-js">' + (T / 'header2.js').read_text() + '</script></body>', 1)
