# Mockup tool (not site code), kept for the record: built k-tekst.html (the 10 Nov review page) from the main mockup as it
# was before that copy was approved. The approved copy now lives in finalize_main.py + k-tekst.css, so re-running this
# against the current index.html stops at the first assert; k-tekst.html stays as the review snapshot.
import pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)
rep('<h2 id="h-waarom" class="wh2-h">Wij kweken rhododendrons. <span class="nb">Niet meer, niet minder.</span></h2>',
    '<h2 id="h-waarom" class="wh2-h">Wij kweken alleen rhododendrons. <span class="nb">Dat merkt u aan elke plant.</span></h2>')
rep('<p class="wh2-lead">Onze planten groeien in de volle grond op veenrijke bodem en ontwikkelen daar een sterk wortelstelsel. Gerooid met kluit, direct van het veld naar uw tuin.</p>', '')
rep('<li><div><h3>Aangroeigarantie op elke plant</h3><p>Niet aangeslagen in het eerste seizoen? Wij vervangen kosteloos.</p></div></li>',
    '<li class="kt-hl"><div><h3>Aangroeigarantie op elke plant</h3><p>Slaat een plant in het eerste seizoen <span class="nb">niet aan?</span> Dan vervangen wij hem kosteloos.</p></div></li>')
rep('<p>Wij stemmen bezorging of afhaal af op uw planning en rooien uw planten pas vlak daarvoor.</p>',
    '<p>Wij stemmen bezorging of afhaal af op uw planning en rooien uw planten pas vlak daarvoor, met kluit.</p>')
CSS = '''
/* K + new copy (10 Nov): no lead, so the list follows the H2 directly; the guarantee leads by size; phones: reasons before the card */
.wh2 .wh2-grid{grid-template-areas:"h card" "list card";grid-template-rows:auto 1fr}
.wh2 .wh2-list{margin-top:clamp(40px,4.5vw,64px);align-self:start}
.wh2 .kt-hl h3{font-size:clamp(26px,2.6vw,36px);letter-spacing:-.025em}
.wh2 .kt-hl p{font-size:clamp(16px,1.2vw,17.5px);color:#2f2e2a}
@media (max-width:860px){
  .wh2 .wh2-grid{grid-template-areas:"h" "list" "card"}
  .wh2 .wh2-list{margin-top:28px}
  .wh2 .wh2-h .nb{white-space:normal;display:block}
  .wh2 .wh2-card{margin-top:32px}
}
'''
s = s.replace('</head>', '<style id="k-tekst">' + CSS + '</style></head>', 1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Waarom wij · K met nieuwe tekst</title>', 1)
(D / 'k-tekst.html').write_text(s)
print('ok')
