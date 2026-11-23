# Mockup tool (not site code): calc3-fable.html = the homepage (index.html) with the «Смета» calculator in three control
# treatments for review (tools/calc3.py, tools/calc3.css, tools/calc3.js) and, for comparison, the old Смета in colour A
# (tools/calc.py, unchanged). kn-1 pills · kn-2 rows · kn-3 tiles · kn-0 the old one;
# kb-0..3 the cart button (moss, olive, sage, glow) · gl-1/gl-0 the cards' glow or flat.
# Usage: python3 tools/build_calc3_fable.py [dir]
import re, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import calc, calc3
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
old = calc.calc_html(1).replace('id="haag"', 'id="haag-0"').replace('h-haag', 'h-haag-0')
s = calc3.place(s, calc3.calc_html(3, 1, True) + old)
REVIEW = '''body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
@media (max-width:520px){ .rv{justify-content:flex-start} }
@media (max-width:760px){ .rv .l{display:inline} }
.hc,.sx{--hc-top:140px;--sx-top:140px}
.hc{display:none}
html.kn-0 .hc1{display:block}
html.kn-0 .sx{display:none}
'''
# the bar switches classes on <html> (the page's own review script); this copies the choice to the block and redraws
SWITCH = '''(function(){var sx=document.querySelector('.sx'),h=document.documentElement;function get(g,d){var m=h.className.match(new RegExp('(?:^| )'+g+'-(\\\\w)'));return m?m[1]:d}
[].forEach.call(document.querySelectorAll('.rv button'),function(b){b.addEventListener('click',function(){setTimeout(function(){
var kn=get('kn','1');if(kn!=='0')sx.className='sx sx-t'+kn+' sx-b'+get('kb','1')+(get('gl','1')==='0'?' sx-flat':'');else sx.className=sx.className.replace(/sx-b\\d/,'sx-b'+get('kb','1'));
window.dispatchEvent(new Event('resize'))},0)})})})();'''
mh = re.search(r'<html lang="nl" class="([^"]*)">', s); assert mh and not any(c.startswith(('kn-', 'ct-')) for c in mh.group(1).split())
s = s.replace(mh.group(0), '<html lang="nl" class="' + mh.group(1) + ' kn-3 kb-1 gl-1 ct-a">', 1)   # ct-a: the old block's colour A
def btn(v, name, on=False, g='kn'):
    return f'<button type="button" data-g="{g}" data-v="{v}" aria-pressed="{"true" if on else "false"}">{name}</button>'
BAR = ('<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Кнопки</i>' + btn(1, '1 · Пилюли') + btn(2, '2 · Строки') + btn(3, '3 · Плитки', True) + btn(0, 'Было')
       + '</div><span class="sep"></span><div class="rv-g"><i>Кнопка корзины</i>' + btn(0, 'Мох (было)', g='kb') + btn(1, 'A · Олива', True, g='kb') + btn(2, 'B · Шалфей', g='kb') + btn(3, 'C · Свечение', g='kb')
       + '</div><span class="sep"></span><div class="rv-g"><i>Свечение</i>' + btn(1, 'Свечение: да', True, g='gl') + btn(0, 'нет', g='gl') + '</div></div>')
assert '<div class="rv"' not in s and s.count('<div id="root">') == 1 and s.count('</head>') == 1 and s.count('</body>') == 1
s = s.replace('<div id="root">', BAR + '<div id="root">')
s = s.replace('</head>', '<style id="calc-css">' + calc.css() + '</style><style id="calc3-css">' + calc3.css() + '</style><style id="calc3-review">' + REVIEW + '</style></head>')
s = s.replace('</body>', '<script>' + calc.js() + '</script><script>' + calc3.js() + '</script><script>' + SWITCH + '</script></body>')
(D / 'calc3-fable.html').write_text(s)
print('ok', len(s))
