# Mockup tool (not site code): the «Voor professionals» block (plan 2.6) for review, each variant built by the real
# tools/pro.py apply() on the finished index.html, so the page shows exactly what the main build would:
#   pro.html    A · Строки  open, the facts as hairline rows beside the heading
#   pro-b.html  B · Карточка  the same in a card in the guarantee card's light
# A small black bar links the two; each page opens on the block.
# Usage: python3 tools/build_pro.py [dir]
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import pro
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
base = (D / 'index.html').read_text()
PAGES = [('a', 'pro.html', 'A · Строки'), ('b', 'pro-b.html', 'B · Карточка')]
REVIEW = '''body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
.rvh{position:fixed;z-index:1000;left:0;right:0;top:0;height:48px;display:flex;align-items:center;justify-content:center;gap:6px;padding:0 10px;background:#111;color:#fff;font:500 13px/1 Manrope,system-ui,sans-serif;white-space:nowrap}
.rvh i{font-style:normal;color:#b9b9b4;margin-right:4px}
.rvh a{display:inline-flex;align-items:center;height:32px;padding:0 12px;border:1px solid #555;border-radius:999px;color:#fff;text-decoration:none}
.rvh a[aria-current]{background:#fff;border-color:#fff;color:#111}
@media (max-width:480px){ .rvh i{display:none} .rvh a{padding:0 9px} }
'''
JS = ('<script>(function(){if(!location.hash){var k=document.getElementById("professionals");if(k)setTimeout(function(){k.scrollIntoView()},60)}})();</script>')
for v, name, label in PAGES:
    bar = '<div class="rvh" role="group" aria-label="Voor professionals"><i>Для профи</i>' + ''.join(
        f'<a href="{n}"{" aria-current=" + chr(34) + "page" + chr(34) if n == name else ""}>{l}</a>' for _, n, l in PAGES) + '</div>'
    s = pro.apply(base, v)
    s = s.replace('</head>', '<style id="pro-review">' + REVIEW + '</style></head>', 1)
    s = s.replace('<div id="root">', bar + '<div id="root">', 1).replace('</body>', JS + '</body>', 1)
    (D / name).write_text(s)
    print(name, len(s))
