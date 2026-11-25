# Mockup tool (not site code): writes tools/as3-sad.html, variant 1 · Сад of the homepage Assortiment block, round 3 (11 Nov).
# The page itself (assortiment-3.html) is built by tools/build_assortiment3.py, which inserts this fragment and tools/as3-sad.css.
# Variant 1 is round 2's «Сад» corrected on professional grounds:
#   - all seven varieties at once, in an aligned grid: no stagger, so names and prices can be compared along a line;
#   - one photo frame for all (4:5), each photo positioned so the bush stays whole;
#   - name, bloom and price sit on shared rows (CSS subgrid), whatever the name length (the colour line was removed
#     on 11 Nov at the owner's request: the photo shows the colour);
#   - the price always carries its size and "met kluit"; the whole card links to the variety;
#   - the heading row sits above the grid with a text link to all plants (12 Nov); just the seven cards: one row from
#     1280 px, 4 + 3 centred below, 2 columns with the 7th centred on phone (chosen by a blind review).
# Plant data is read from mockup-v3/src/data/content.ts (mirror of the live site's lib/products.ts).
# Usage: python3 tools/build_as3_sad.py [dir]
import re, pathlib, sys, html
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import calc3   # the prices per size (owner, 25 Nov): "vanaf" is the variety's lowest price there, not content.ts's "from"

D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
ts = (D.parent.parent / 'src' / 'data' / 'content.ts').read_text()
vblock = ts[ts.index('export const varieties'):ts.index('export const bySlug')]


def field(o, k):
    m = re.search(k + r""": (?:'((?:[^'\\]|\\.)*)'|"((?:[^"\\]|\\.)*)")""", o)
    assert m, k
    return (m.group(1) if m.group(1) is not None else m.group(2)).replace("\\'", "'")


V = [dict(slug=field(o, 'slug'), name=field(o, 'name'), color=field(o, 'color'), hex=field(o, 'hex'), bloei=field(o, 'bloei'), frm=field(o, 'from'))
     for o in re.findall(r"\{\s*slug: .*?\n  \},", vblock, re.S)]
assert len(V) == 7

# where each bush sits in its photo, so the 4:5 frame keeps it whole (checked on the renders)
POS = {'roseum-elegans': '50% 60%', 'nova-zembla': '50% 70%', 'cunninghams-white': '50% 40%'}
e = html.escape
ARW = '<svg class="sd-arw" viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'

# card order (owner and the blind review, 12 Nov): distinct flower colours alternate, so the four lilac and purple varieties
# never stand side by side: red, pale lilac, white, deep purple, hot pink, violet, light pink-lilac
ORDER = ['nova-zembla', 'catawbiense-grandiflorum', 'cunninghams-white', 'catawbiense-boursault', 'roseum-elegans', 'ponticum', 'ponticum-roseum']
assert sorted(ORDER) == sorted(v['slug'] for v in V)
V = sorted(V, key=lambda v: ORDER.index(v['slug']))

# each variety's own size range (owner, 16 Nov: the sizes on the reseller's site are Top's own; docs/maten-per-soort.md).
# The price is "vanaf": the variety's lowest price per plant in tools/calc3.py (owner, 25 Nov).
RANGE = {'nova-zembla': (50, 180), 'catawbiense-grandiflorum': (50, 225), 'cunninghams-white': (50, 225),
         'catawbiense-boursault': (40, 180), 'roseum-elegans': (50, 225), 'ponticum': (50, 120), 'ponticum-roseum': (40, 160)}
assert sorted(RANGE) == sorted(ORDER)
# calc3.SOORTEN stands in the order of the cards; its ranges must be the cards' ranges
assert len(calc3.SOORTEN) == 7 and [r for n, p, r in calc3.SOORTEN] == [RANGE[k] for k in ORDER]
for v, (n, p, r) in zip(V, calc3.SOORTEN):
    assert v['name'].replace("'", '’') == n, (v['name'], n)
    v['frm'] = ('%.2f' % calc3.vanaf(p)).replace('.', ',')   # "19,50"
items = ''
for v in V:
    lo, hi = RANGE[v['slug']]
    items += ('<article class="sd-it"><a href="#assortiment" aria-label="' + e(v['name']) + ', vanaf € ' + v['frm'] + ', van ' + str(lo) + ' tot ' + str(hi) + ' cm">'
              '<div class="sd-ph"><img src="img/' + v['slug'] + '-2-sm.webp" alt="' + e(v['name']) + ', bloeiende struik" loading="lazy"'
              + (' style="object-position:' + POS[v['slug']] + '"' if v['slug'] in POS else '') + '></div>'
              '<h3>' + e(v['name']) + '</h3>'
              '<p class="sd-b">Bloeit ' + e(v['bloei'].lower().replace(' – ', '–')) + '</p>'
              '<p class="sd-pr"><span class="sd-v">vanaf</span><b>€&nbsp;' + v['frm'] + '</b><span class="sd-s">' + str(lo) + ' tot ' + str(hi) + '&nbsp;cm, met kluit</span></p>'
              '</a></article>')

out = ('<section id="as3-1" class="sd" aria-labelledby="h-sd"><div class="in">'
       # the lead sits under the heading (owner, 16 Nov: as elsewhere on the page)
       '<div class="sd-hd"><div class="sd-hl"><h2 id="h-sd">Zeven soorten uit eigen kweek.</h2>'
       # sizes from 40 to 225 cm (owner, 16 Nov: the sizes on the reseller's site are Top's own; docs/maten-per-soort.md)
       '<p class="sd-lead"><span>Van 40 tot 225&nbsp;cm, afhankelijk van de soort.</span> <span>U&nbsp;bestelt vanaf 1&nbsp;plant.</span></p></div></div>'
       '<div class="sd-grid">' + items + '</div>'
       # the way on to all plants closes the block: a pill in the bottom right corner, under the cards (owner, 16 Nov)
       # the cards show the smallest size only; the pill leads to every size and price (owner, 16 Nov: "all plants" made no
       # sense with all seven varieties already in view)
       '<div class="sd-ft"><a class="sd-more" href="#assortiment">Alle maten en prijzen' + ARW + '</a></div>'
       '</div></section>')
(D / 'tools' / 'as3-sad.html').write_text(out)
print('as3-sad.html', len(out))
