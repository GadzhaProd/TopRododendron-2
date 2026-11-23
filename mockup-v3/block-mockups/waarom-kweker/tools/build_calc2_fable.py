# Mockup tool (not site code): calc2-fable.html = the homepage (index.html) with two new directions of the plant calculator
# for review (tools/calc2.py, tools/calc2.css, tools/calc2.js). k2-a the sentence · k2-b the variety and the rows.
# Usage: python3 tools/build_calc2_fable.py [dir]
import re, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import calc2
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
blocks = ''.join(calc2.calc_html(d).replace('id="rekenhulp"', f'id="rekenhulp-{d}"').replace('h-rekenhulp', f'h-rekenhulp-{d}') for d in ('a', 'b'))
s = calc2.place(s, blocks)
REVIEW = '''body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
@media (max-width:520px){ .rv{justify-content:flex-start} .rv .l{display:inline} }
.pc{display:none}
html.k2-a .pc-a,html.k2-b .pc-b{display:block}
'''
mh = re.search(r'<html lang="nl" class="([^"]*)">', s); assert mh and not any(c.startswith('k2-') for c in mh.group(1).split())
s = s.replace(mh.group(0), '<html lang="nl" class="' + mh.group(1) + ' k2-a">', 1)
def btn(v, name, on=False):
    return f'<button type="button" data-g="k2" data-v="{v}" aria-pressed="{"true" if on else "false"}">{v.upper()}<span class="l"> · {name}</span></button>'
BAR = '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Калькулятор</i>' + btn('a', 'Фраза', True) + btn('b', 'Сорт и строки') + '</div></div>'
assert '<div class="rv"' not in s and s.count('<div id="root">') == 1 and s.count('</head>') == 1 and s.count('</body>') == 1
s = s.replace('<div id="root">', BAR + '<div id="root">')
s = s.replace('</head>', '<style id="calc2-css">' + calc2.css() + '</style><style id="calc2-review">' + REVIEW + '</style></head>')
s = s.replace('</body>', '<script>' + calc2.js() + '</script></body>')
(D / 'calc2-fable.html').write_text(s)
print('ok', len(s))
