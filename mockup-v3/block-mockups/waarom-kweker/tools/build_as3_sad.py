# Mockup tool (not site code): writes tools/as3-sad.html, variant 1 · Сад of the homepage Assortiment block, round 3 (11 Nov).
# The page itself (assortiment-3.html) is built by tools/build_assortiment3.py, which inserts this fragment and tools/as3-sad.css.
# Variant 1 is round 2's «Сад» corrected on professional grounds:
#   - all seven varieties at once, in an aligned grid: no stagger, so names and prices can be compared along a line;
#   - one photo frame for all (4:5), each photo positioned so the bush stays whole;
#   - name, colour, bloom and price sit on shared rows (CSS subgrid), whatever the name length;
#   - the price always carries its size and "met kluit"; the whole card links to the variety;
#   - the grid closes without orphans: desktop 4 columns = heading + 7; tablet 3 columns = heading + 7 + link tile;
#     phone 2 columns = 7 + link tile, with the heading above.
# Plant data is read from mockup-v3/src/data/content.ts (mirror of the live site's lib/products.ts).
# Usage: python3 tools/build_as3_sad.py [dir]
import re, pathlib, sys, html

D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
ts = (D.parent.parent / 'src' / 'data' / 'content.ts').read_text()
vblock = ts[ts.index('export const varieties'):ts.index('export const bySlug')]


def field(o, k):
    m = re.search(k + r""": (?:'((?:[^'\\]|\\.)*)'|"((?:[^"\\]|\\.)*)")""", o)
    assert m, k
    return (m.group(1) if m.group(1) is not None else m.group(2)).replace("\\'", "'")


V = [dict(slug=field(o, 'slug'), name=field(o, 'name'), color=field(o, 'color'), hex=field(o, 'hex'), bloei=field(o, 'bloei'), frm=field(o, 'from'))
     for o in re.findall(r"\{\s*slug: .*?\n  \},", vblock, re.S)]
assert [v['frm'] for v in V] == ['29', '25', '27', '27', '29', '22', '22'], [v['frm'] for v in V]
assert len(V) == 7

# where each bush sits in its photo, so the 4:5 frame keeps it whole (checked on the renders)
POS = {'roseum-elegans': '50% 60%', 'nova-zembla': '50% 70%', 'cunninghams-white': '50% 40%'}
e = html.escape
ARW = '<svg class="sd-arw" viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'

items = ''
for v in V:
    light = v['hex'].lower() in ('#f1ece3',)
    items += ('<article class="sd-it"><a href="#assortiment" aria-label="' + e(v['name']) + ', vanaf € ' + v['frm'] + ' voor 40–60 cm">'
              '<div class="sd-ph"><img src="img/' + v['slug'] + '-2-sm.webp" alt="' + e(v['name']) + ', bloeiende struik" loading="lazy"'
              + (' style="object-position:' + POS[v['slug']] + '"' if v['slug'] in POS else '') + '></div>'
              '<h3>' + e(v['name']) + '</h3>'
              '<p class="sd-c"><i' + (' class="lt"' if light else '') + ' style="background:' + v['hex'] + '" aria-hidden="true"></i>' + e(v['color']) + '</p>'
              '<p class="sd-b">Bloeit ' + e(v['bloei'].lower()) + '</p>'
              '<p class="sd-pr"><span class="sd-v">vanaf</span><b>€&nbsp;' + v['frm'] + '</b><span class="sd-s">40–60&nbsp;cm, met kluit</span></p>'
              '</a></article>')

ALL = '<a class="sd-all" href="#assortiment">Bekijk alle planten' + ARW + '</a>'
out = ('<section id="as3-1" class="sd" aria-labelledby="h-sd"><div class="in"><div class="sd-grid">'
       '<div class="sd-hd"><h2 id="h-sd">Zeven soorten uit eigen kweek.</h2>'
       '<p class="sd-lead">Elke soort is er in vier maten, van 40 tot 120&nbsp;cm. U bestelt vanaf 1&nbsp;plant.</p>' + ALL + '</div>'
       + items +
       '<a class="sd-tile" href="#assortiment"><span>Alle zeven soorten, maten en prijzen</span><b>Bekijk alle <span class="nw">planten' + ARW + '</span></b></a>'
       '</div></div></section>')
(D / 'tools' / 'as3-sad.html').write_text(out)
print('as3-sad.html', len(out))
