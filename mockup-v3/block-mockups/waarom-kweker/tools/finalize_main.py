# Mockup tool (not site code): builds the main mockup index.html from varianten.html with only the approved
# Waarom wij K (lead under the heading) between the hero and the founder block; review bar removed.
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'varianten.html').read_text()
def cut_section(s, sid):
    i = s.index(f'id="{sid}"'); i = s.rfind('<section', 0, i); j = s.index('</section>', i) + len('</section>')
    return s[:i] + s[j:]
for sid in ['waarom', 'waarom-b', 'waarom-c', 'waarom-p', 'waarom-r']:
    s = cut_section(s, sid)
s = s.replace('id="waarom-k"', 'id="waarom"').replace('id="h-waarom-k"', 'id="h-waarom"').replace('aria-labelledby="h-waarom-k"', 'aria-labelledby="h-waarom"')
# variant switching and review bar are no longer needed
s = s.replace('#waarom,#waarom-k,#waarom-b,#waarom-c,#waarom-p,#waarom-r{display:none}\n', '')
s = s.replace('.d-o #waarom,.d-k #waarom-k,.d-b #waarom-b,.d-c #waarom-c,.d-p #waarom-p,.d-r #waarom-r{display:block}\n', '')
s = s.replace('.rv .rv-gg,.rv .rv-lp{display:none}.d-o .rv .rv-gg,.d-k .rv .rv-lp{display:flex}\n', '')
s = s.replace('body{padding-top:48px}\nheader.fixed{top:48px}\n#hero{min-height:calc(100svh - 48px)}\n', '')
i = s.index('<div class="rv" role="group"'); j = s.index('<div id="root">')
s = s[:i] + s[j:]
s = re.sub(r'<html lang="nl" class="[^"]*">', '<html lang="nl" class="m-n3 t-0 d-k lp-u">', s, count=1)
s = s.replace('<title>Waarom wij · eerdere varianten</title>', '<title>Waarom wij · De kweker</title>', 1)
assert s.count('<section') == 3, s.count('<section')
# approved card colours ("Veld", 9 Nov): appended after the page CSS so they override the baseline card
card = (D / 'tools' / 'card-veld.css').read_text()
s = s.replace('</head>', '<style>' + card + '</style></head>', 1)
(D / 'index.html').write_text(s)
print('ok', len(s))
