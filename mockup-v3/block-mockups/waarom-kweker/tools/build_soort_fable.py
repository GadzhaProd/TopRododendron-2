# Mockup tool (not site code): soort-fable.html = the product page of a variety in for review
# (tools/soort.py, tools/soort.css, tools/soort.js). Built like garantie.html (tools/build_garantie4.py): the header, the
# cart, the phone menu and the footer come from the main mockup (index.html), <main> is replaced, the homepage anchors
# become links to index.html, and the calculator's style and script are dropped.
# The variety is chosen by the hash (soort-fable.html#ponticum); the direction with the black review bar (or ?d=a2|a).
# Since 24 Nov the page shows a2 ("Легче", the default) beside a; b and c stay in tools/soort.py but are not built.
# Usage: python3 tools/build_soort_fable.py [dir]
import re, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import soort
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
i = s.index('<main id="main"'); j = s.index('</main>') + len('</main>')
head, tail = s[:i], s[j:]
head, n1 = re.subn(r'<style id="calc3-css">.*?</style>', '', head, count=1, flags=re.S)
tail, n2 = re.subn(r'<script id="calc3-js">.*?</script>', '', tail, count=1, flags=re.S)
assert n1 == 1 and n2 == 1
s = head + soort.main_html() + tail

# the homepage anchors become real links to the homepage, the logo goes home (only in the markup, not in the scripts)
parts = re.split(r'(<script\b.*?</script>)', s, flags=re.S)
for k in range(0, len(parts), 2):
    for a in ['#waarom', '#kweker', '#assortiment', '#hoe']:
        parts[k] = re.sub(r'href="' + a + r'"(?![^>]*data-page)', f'href="index.html{a}"', parts[k])
    parts[k] = parts[k].replace('<a href="/" data-home ', '<a href="index.html" ')
s = ''.join(parts)

# the review bar: black, fixed, 48 px; "srt-a2|a" on <html> is the direction on show
REVIEW = '''html{--so-rv:48px}body{padding-top:48px}header.fixed{top:48px}
.rvs{position:fixed;z-index:1000;left:0;right:0;top:0;height:48px;display:flex;align-items:center;justify-content:center;gap:6px;padding:0 10px;background:#111;color:#fff;
  font:500 13px/1 Manrope,system-ui,sans-serif;overflow-x:auto;white-space:nowrap}
.rvs i{font-style:normal;color:#b9b9b4;margin-right:4px}
.rvs button,.rvs select{flex:none;height:32px;padding:0 12px;border:1px solid #555;border-radius:999px;background:none;color:#fff;font:inherit;cursor:pointer}
.rvs select{margin-left:8px;padding-right:8px;background:#111}
.rvs button[aria-pressed="true"]{background:#fff;border-color:#fff;color:#111}
.rvs :is(button,select):focus-visible{outline:2px solid #fff;outline-offset:2px}
@media (max-width:1100px){ .rvs{justify-content:flex-start} }
@media (max-width:760px){ .rvs .l{display:none} }
'''
BAR = ('<div class="rvs" role="group" aria-label="Варианты страницы сорта"><i>Страница сорта</i>'
       + ''.join(f'<button type="button" data-srt="{v}" aria-pressed="{"true" if v == "a2" else "false"}">{v.upper()}<span class="l"> · {n}</span></button>'
                 for v, n in [('a2', 'Легче'), ('a', 'Тихая страница')])
       + '<i style="margin-left:10px">Значки</i>' + ''.join(f'<button type="button" data-sic="{v}" aria-pressed="{"true" if v == "0" else "false"}">{n}</button>'
                 for v, n in [('0', 'Без значков'), ('1', '1 · В строке'), ('2', '2 · Ячейки'), ('3', '3 · Полоса')])
       + '<select data-srt-var aria-label="Сорт">' + ''.join(f'<option value="{x["slug"]}">{x["n"]}</option>' for x in soort.SOORTEN) + '</select></div>')
RJS = '''(function(){var h=document.documentElement,m=/[?&]d=(a2|a)\\b/.exec(location.search),d=m?m[1]:null;
try{d=d||sessionStorage.getItem('srt')}catch(e){}if(d!=='a'&&d!=='a2')d=null;
function set(v){h.className=h.className.replace(/\\bsrt-\\w+/,'srt-'+v);try{sessionStorage.setItem('srt',v)}catch(e){}
[].forEach.call(document.querySelectorAll('[data-srt]'),function(b){b.setAttribute('aria-pressed',b.getAttribute('data-srt')===v?'true':'false')});
if(window.soDir)window.soDir(v)}
document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('[data-srt]');if(b)set(b.getAttribute('data-srt'))});
var sel=document.querySelector('[data-srt-var]');sel.addEventListener('change',function(){location.hash=sel.value});
var mi=/[?&]ic=([0-3])/.exec(location.search),ic=mi?mi[1]:null;try{ic=ic||sessionStorage.getItem('sic')}catch(e){}
function seti(v){h.className=h.className.replace(/ ?\\bsic-\\d/,'')+' sic-'+v;try{sessionStorage.setItem('sic',v)}catch(e){}
[].forEach.call(document.querySelectorAll('[data-sic]'),function(b){b.setAttribute('aria-pressed',b.getAttribute('data-sic')===v?'true':'false')})}
document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('[data-sic]');if(b)seti(b.getAttribute('data-sic'))});
if(/^[1-3]$/.test(ic||''))seti(ic);
window.soVar=function(slug){sel.value=slug};if(d&&d!=='a2')set(d)})();'''
mh = re.search(r'<html lang="nl" class="([^"]*)">', s); assert mh and 'srt-' not in mh.group(1)
s = s.replace(mh.group(0), '<html lang="nl" class="' + mh.group(1) + ' srt-a2">', 1)
assert s.count('<div id="root">') == 1 and s.count('</head>') == 1 and s.count('</body>') == 1 and 'class="rvs"' not in s
s = s.replace('<div id="root">', BAR + '<div id="root">')
s = s.replace('</head>', '<style id="soort-css">' + soort.css() + '</style><style id="soort-review">' + REVIEW + '</style></head>')
s = s.replace('</body>', '<script id="soort-review-js">' + RJS + '</script><script id="soort-js">' + soort.js() + '</script></body>')
s = re.sub(r'<title>[^<]*</title>', '<title>Nova Zembla | Top Rhododendrons</title>', s, count=1)
(D / 'soort-fable.html').write_text(s)
print('ok', len(s))
