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
for slug in soort.SLUGS:
    h = re.sub(r'<title>[^<]*</title>', '<title>' + html.escape(soort.title(slug)) + '</title><meta name="description" content="'
               + html.escape(soort.description(slug), quote=True) + '">', head, count=1)
    h = h.replace('</head>', '<style id="soort-css">' + soort.css() + '</style></head>')
    page = h + soort.main_html(slug) + tail
    (D / f'soort-{slug}.html').write_text(page)
    print(f'soort-{slug}.html', len(page))
