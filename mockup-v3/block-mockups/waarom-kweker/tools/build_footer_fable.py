# Mockup tool (not site code): footer-fable.html = the homepage (index.html) with three designs of the footer for review
# (tools/footer.py, tools/footer.css). fo-0 the footer as it is now · fo-1 dark · fo-2 light · fo-3 a moss card.
# Usage: python3 tools/build_footer_fable.py [dir]
import re, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import footer
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
i = s.index('<footer class="ft"'); j = s.index('</footer>', i) + len('</footer>')
s = s[:j] + ''.join(footer.footer_html(n) for n in (1, 2, 3)) + s[j:]
REVIEW = '''body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
@media (max-width:520px){ .rv{justify-content:flex-start} }
html:not(.fo-0) footer.ft,.fz{display:none}
html.fo-1 .fz1,html.fo-2 .fz2,html.fo-3 .fz3{display:block}
'''
mh = re.search(r'<html lang="nl" class="([^"]*)">', s); assert mh and not any(c.startswith('fo-') for c in mh.group(1).split())
s = s.replace(mh.group(0), '<html lang="nl" class="' + mh.group(1) + ' fo-1">', 1)
def btn(v, name, on=False):
    return f'<button type="button" data-g="fo" data-v="{v}" aria-pressed="{"true" if on else "false"}">{v}<span class="l"> · {name}</span></button>'
BAR = '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Подвал</i>' + btn(0, 'Сейчас') + btn(1, 'Тёмный', True) + btn(2, 'Светлый') + btn(3, 'Карточка') + '</div></div>'
assert '<div class="rv"' not in s and s.count('<div id="root">') == 1 and s.count('</head>') == 1
s = s.replace('<div id="root">', BAR + '<div id="root">').replace('</head>', '<style id="footer-css">' + footer.css() + '</style><style id="footer-review">' + REVIEW + '</style></head>')
(D / 'footer-fable.html').write_text(s)
print('ok', len(s))
