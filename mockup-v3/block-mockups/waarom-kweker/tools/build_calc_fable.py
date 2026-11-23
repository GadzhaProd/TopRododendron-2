# Mockup tool (not site code): calc-fable.html = the homepage (index.html) with three designs of the hedge calculator for
# review (tools/calc.py, tools/calc.css, tools/calc.js). kc-1 the quote (refined) · kc-2 the rule with a slider · kc-3 the photo and the answer.
# Usage: python3 tools/build_calc_fable.py [dir]
import re, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import calc
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
blocks = ''.join(calc.calc_html(n).replace('id="haag"', f'id="haag-{n}"').replace('h-haag', f'h-haag-{n}') for n in (1, 2, 3))
s = calc.place(s, blocks)
REVIEW = '''body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
@media (max-width:520px){ .rv{justify-content:flex-start} }
.hc{display:none;--hc-top:140px}
html.kc-1 .hc1,html.kc-2 .hc2,html.kc-3 .hc3{display:block}
'''
mh = re.search(r'<html lang="nl" class="([^"]*)">', s); assert mh and not any(c.startswith(('kc-', 'ct-')) for c in mh.group(1).split())
s = s.replace(mh.group(0), '<html lang="nl" class="' + mh.group(1) + ' kc-1 ct-a">', 1)
def btn(v, name, on=False):
    return f'<button type="button" data-g="kc" data-v="{v}" aria-pressed="{"true" if on else "false"}">{v}<span class="l"> · {name}</span></button>'
BAR = '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Калькулятор</i>' + btn(1, 'Смета', True) + btn(2, 'Линейка') + btn(3, 'Фото и итог') + '</div><span class="sep"></span><div class="rv-g"><i>Цвет</i>' + ''.join(f'<button type="button" data-g="ct" data-v="{v}" aria-pressed="{"true" if v == "a" else "false"}">{t}</button>' for v, t in (('0', 'Тёмный (было)'), ('a', 'A · Шалфей'), ('b', 'B · Масло'), ('c', 'C · Контур'))) + '</div></div>'
assert '<div class="rv"' not in s and s.count('<div id="root">') == 1 and s.count('</head>') == 1 and s.count('</body>') == 1
s = s.replace('<div id="root">', BAR + '<div id="root">')
s = s.replace('</head>', '<style id="calc-css">' + calc.css() + '</style><style id="calc-review">' + REVIEW + '</style></head>')
s = s.replace('</body>', '<script>' + calc.js() + '</script></body>')
(D / 'calc-fable.html').write_text(s)
print('ok', len(s))
