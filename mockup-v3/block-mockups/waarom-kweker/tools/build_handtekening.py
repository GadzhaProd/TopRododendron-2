# Mockup tool (not site code): Gert's signature in the founder block for review, each variant built by the real
# tools/handtekening.py apply() on index.html, so the page shows exactly what the main build would:
#   handtekening.html    E  the contact part first with its own heading ("Advies van de kwekerij."), the guarantee,
#                           the signature and "Gert Top, oprichter en kweker" under it (owner, 26 Nov)
#   handtekening-d.html  D  as E without the heading ("Vragen over een soort of de garantie? Bel of app de kwekerij:")
#   handtekening-c.html  C  the contact line with Gert's name first, the guarantee and the signature last
# (A and B, the signature under the guarantee or under the numbers in the old order, are left out: the owner moved on to
# the new order.) A small black bar links the three; each page opens on the founder block.
# Usage: python3 tools/build_handtekening.py [dir]
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import handtekening as h
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
base = (D / 'index.html').read_text()
assert 'class="fd-sig"' not in base
PAGES = [('e', 'handtekening.html', 'E · с заголовком'), ('d', 'handtekening-d.html', 'D · имя под подписью'), ('c', 'handtekening-c.html', 'C · гарантия внизу')]
REVIEW = '''body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
.rvh{position:fixed;z-index:1000;left:0;right:0;top:0;height:48px;display:flex;align-items:center;justify-content:center;gap:6px;padding:0 10px;background:#111;color:#fff;font:500 13px/1 Manrope,system-ui,sans-serif;white-space:nowrap}
.rvh i{font-style:normal;color:#b9b9b4;margin-right:4px}
.rvh a{display:inline-flex;align-items:center;height:32px;padding:0 12px;border:1px solid #555;border-radius:999px;color:#fff;text-decoration:none}
.rvh a[aria-current]{background:#fff;border-color:#fff;color:#111}
@media (max-width:480px){ .rvh i{display:none} .rvh a{padding:0 9px} }
'''
JS = ('<script>(function(){if(!location.hash){var k=document.getElementById("kweker");if(k)setTimeout(function(){k.scrollIntoView()},60)}})();</script>')
for v, name, label in PAGES:
    bar = '<div class="rvh" role="group" aria-label="Подпись Герта"><i>Подпись</i>' + ''.join(
        f'<a href="{n}"{" aria-current=" + chr(34) + "page" + chr(34) if n == name else ""}>{l}</a>' for _, n, l in PAGES) + '</div>'
    s = h.apply(base, v)
    s = s.replace('</head>', '<style id="handtekening-review">' + REVIEW + '</style></head>', 1)
    s = s.replace('<div id="root">', bar + '<div id="root">', 1).replace('</body>', JS + '</body>', 1)
    (D / name).write_text(s)
    print(name, len(s))
