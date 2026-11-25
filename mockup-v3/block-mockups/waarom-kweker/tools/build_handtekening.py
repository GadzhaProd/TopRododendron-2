# Mockup tool (not site code): handtekening.html = the homepage (index.html) with Gert's signature in the founder block in
# two places for review (tools/handtekening.py): A under the guarantee text, B under the two numbers. A small black bar
# switches them (class hs-a / hs-b on <html>); the page opens on the founder block.
# Usage: python3 tools/build_handtekening.py [dir]
import re, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import handtekening as h
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
assert 'class="fd-sig"' not in s
start = s.index('id="kweker"')
ia = s.index('</p>', s.index('class="fp-txt"', start)) + len('</p>')
ib = s.index('</dl></div>', s.index('class="fp-act"', start)) + len('</dl></div>')
A = h.IMG.replace('class="fd-sig"', 'class="fd-sig hs-ia"'); B = h.IMG.replace('class="fd-sig"', 'class="fd-sig hs-ib"')
s = s[:ia] + A + s[ia:ib] + B + s[ib:]
REVIEW = '''body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
html.hs-a .hs-ib,html.hs-b .hs-ia{display:none!important}
.rvh{position:fixed;z-index:1000;left:0;right:0;top:0;height:48px;display:flex;align-items:center;justify-content:center;gap:6px;padding:0 10px;background:#111;color:#fff;font:500 13px/1 Manrope,system-ui,sans-serif;white-space:nowrap}
.rvh i{font-style:normal;color:#b9b9b4;margin-right:4px}
.rvh button{height:32px;padding:0 14px;border:1px solid #555;border-radius:999px;background:none;color:#fff;font:inherit;cursor:pointer}
.rvh button[aria-pressed="true"]{background:#fff;border-color:#fff;color:#111}
@media (max-width:480px){ .rvh i{display:none} }
'''
BAR = ('<div class="rvh" role="group" aria-label="Подпись Герта"><i>Подпись</i>'
       '<button type="button" data-hs="a" aria-pressed="true">A · под гарантией</button>'
       '<button type="button" data-hs="b" aria-pressed="false">B · под телефонами</button></div>')
JS = ('<script>(function(){var h=document.documentElement;[].forEach.call(document.querySelectorAll(".rvh button"),function(b){'
      'b.addEventListener("click",function(){h.classList.remove("hs-a","hs-b");h.classList.add("hs-"+b.dataset.hs);'
      '[].forEach.call(document.querySelectorAll(".rvh button"),function(x){x.setAttribute("aria-pressed",x===b?"true":"false")})})});'
      'if(!location.hash){var k=document.getElementById("kweker");if(k)setTimeout(function(){k.scrollIntoView()},60)}})();</script>')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} hs-a">', s, count=1)
s = s.replace('</head>', '<style id="handtekening-css">' + h.CSS + '</style><style id="handtekening-review">' + REVIEW + '</style></head>', 1)
s = s.replace('<div id="root">', BAR + '<div id="root">', 1).replace('</body>', JS + '</body>', 1)
(D / 'handtekening.html').write_text(s)
print('ok', len(s))
