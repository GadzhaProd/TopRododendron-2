# Mockup tool (not site code): builds the main mockup index.html from varianten.html with only the approved
# Waarom wij K between the hero and the founder block; review bar removed. Since 10 Nov K carries the approved new copy:
# benefit-led H2, no lead under it, the guarantee first and larger, root ball in the fresh-dug line, phones: reasons before the card.
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
# hero text block in the bottom-left corner on desktop + landscape tablets (approved 9 Nov); phones / portrait tablets unchanged
hero = (D / 'tools' / 'hero-bottom-left.css').read_text()
s = s.replace('</head>', '<style id="hero-bottom-left">' + hero + '</style></head>', 1)
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)
# Waarom wij K, new copy (approved 10 Nov; reviewed as k-tekst.html)
rep('<h2 id="h-waarom" class="wh2-h">Wij kweken rhododendrons. <span class="nb">Niet meer, niet minder.</span></h2>',
    '<h2 id="h-waarom" class="wh2-h">Wij kweken alleen rhododendrons. <span class="nb">Dat merkt u aan elke plant.</span></h2>')
rep('<p class="wh2-lead">Onze planten groeien in de volle grond op veenrijke bodem en ontwikkelen daar een sterk wortelstelsel. Gerooid met kluit, direct van het veld naar uw tuin.</p>', '')
rep('<li><div><h3>Aangroeigarantie op elke plant</h3><p>Niet aangeslagen in het eerste seizoen? Wij vervangen kosteloos.</p></div></li>',
    '<li class="kt-hl"><div><h3>Aangroeigarantie op elke plant</h3><p>Slaat een plant in het eerste seizoen <span class="nb">niet aan?</span> Dan vervangen wij hem kosteloos.</p></div></li>')
rep('<p>Wij stemmen bezorging of afhaal af op uw planning en rooien uw planten pas vlak daarvoor.</p>',
    '<p>Wij stemmen bezorging of afhaal af op uw planning en rooien uw planten pas vlak daarvoor, met kluit.</p>')
kt = (D / 'tools' / 'k-tekst.css').read_text()
s = s.replace('</head>', '<style id="k-tekst">' + kt + '</style></head>', 1)
(D / 'index.html').write_text(s)
print('ok', len(s))
