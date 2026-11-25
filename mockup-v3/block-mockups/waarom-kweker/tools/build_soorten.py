# Mockup tool (not site code): the seven variety pages, soort-<slug>.html next to index.html (tools/soort.py, soort.css,
# soort.js). Built from the finished index.html like garantie.html (tools/build_garantie4.py): the header, the cart, the
# phone menu and the footer are kept, <main> is replaced, the homepage anchors become links to index.html, and the
# calculator's style and script are dropped. Each page has its own <title> and meta description.
# Run after tools/finalize_main.py. Usage: python3 tools/build_soorten.py [dir]
import re, pathlib, sys, html
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import soort
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
i = s.index('<main id="main"'); j = s.index('</main>') + len('</main>')
head, tail = s[:i], s[j:]
head, n1 = re.subn(r'<style id="calc3-css">.*?</style>', '', head, count=1, flags=re.S)
tail, n2 = re.subn(r'<script id="calc3-js">.*?</script>', '', tail, count=1, flags=re.S)
assert n1 == 1 and n2 == 1
assert head.count('</head>') == 1 and tail.count('</body>') == 1 and 'name="description"' not in head


def links(t):
    # the homepage anchors become real links to the homepage, the logo goes home (only in the markup, not in the scripts)
    parts = re.split(r'(<script\b.*?</script>)', t, flags=re.S)
    for k in range(0, len(parts), 2):
        for a in ['#waarom', '#kweker', '#assortiment', '#hoe']:
            parts[k] = re.sub(r'href="' + a + r'"(?![^>]*data-page)', f'href="index.html{a}"', parts[k])
        parts[k] = parts[k].replace('<a href="/" data-home ', '<a href="index.html" ')
    return ''.join(parts)


head, tail = links(head), links(tail)
tail = tail.replace('</body>', '<script id="soort-js">' + soort.js() + '</script></body>')
# While the owner compares the two layouts (25 Nov): soort-<slug>.html is "Галерея" (the default; the homepage cards open
# it), soort-<slug>-nu.html is the page as it was. A small black review bar switches between them. When he has chosen:
# keep one layout, drop REVIEW, the bar and the "-nu" files.
REVIEW = '''body{padding-top:48px}header.fixed{top:48px}
.rvs{position:fixed;z-index:1000;left:0;right:0;top:0;height:48px;display:flex;align-items:center;justify-content:center;gap:6px;padding:0 10px;background:#111;color:#fff;font:500 13px/1 Manrope,system-ui,sans-serif;white-space:nowrap}
.rvs i{font-style:normal;color:#b9b9b4;margin-right:4px}
.rvs a{display:inline-flex;align-items:center;height:32px;padding:0 14px;border:1px solid #555;border-radius:999px;color:#fff;text-decoration:none}
.rvs a[aria-current]{background:#fff;border-color:#fff;color:#111}
.rvs a:focus-visible{outline:2px solid #fff;outline-offset:2px}
@media (max-width:480px){ .rvs i{display:none} }
'''
assert tail.count('<div id="root">') + head.count('<div id="root">') == 1
for slug in soort.SLUGS:
    for layout, sfx in (('galerij', ''), ('nu', '-nu')):
        bar = ('<div class="rvs" role="group" aria-label="Варианты страницы сорта"><i>Страница сорта</i>'
               f'<a href="soort-{slug}-nu.html"{" aria-current=" + chr(34) + "page" + chr(34) if sfx else ""}>Сейчас</a>'
               f'<a href="soort-{slug}.html"{"" if sfx else " aria-current=" + chr(34) + "page" + chr(34)}>Галерея</a></div>')
        h = re.sub(r'<title>[^<]*</title>', '<title>' + html.escape(soort.title(slug)) + '</title><meta name="description" content="'
                   + html.escape(soort.description(slug), quote=True) + '">', head, count=1)
        h = h.replace('</head>', '<style id="soort-css">' + soort.css() + '</style><style id="soort-review">' + REVIEW + '</style></head>')
        page = (h + soort.main_html(slug, layout, sfx) + tail).replace('<div id="root">', bar + '<div id="root">')
        (D / f'soort-{slug}{sfx}.html').write_text(page)
        print(f'soort-{slug}{sfx}.html', len(page))
