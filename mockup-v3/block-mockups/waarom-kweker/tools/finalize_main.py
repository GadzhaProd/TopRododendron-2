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
# Founder block, phone: "Подпись" (approved 10 Nov; reviewed as 4 on fd-fable.html). Desktop unchanged.
rep('<img class="ph-m" src="img/owner-portrait-m.webp" alt="Gert Top, oprichter en kweker van Top Rhododendrons" width="1200" height="1628" loading="lazy">',
    '<img class="ph-m" src="img/fd-podpis-bust.webp" alt="Gert Top, oprichter en kweker van Top Rhododendrons" width="1440" height="1718" loading="lazy">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} fd-podpis">', s, count=1)
fp = (D / 'tools' / 'fd-podpis.css').read_text()
s = s.replace('</head>', '<style id="fd-podpis">' + fp + '</style></head>', 1)
# the quote's second sentence starts its own line on phones; a span in the markup would shift the desktop glyphs by a fraction of
# a pixel, so it is added by script on phone widths only (for the code transfer: render the span in the phone layout only)
rep('</body>', "<script>(function(){var p=document.querySelector('#kweker .fd-q p'),m=matchMedia('(max-width:860px)');if(!p)return;"
    "function f(){var t=p.textContent,i=t.indexOf('. ');if(m.matches&&i>0){p.textContent=t.slice(0,i+2);var s=document.createElement('span');"
    "s.className='q2';s.textContent=t.slice(i+2);p.appendChild(s)}else{p.textContent=t}}f();m.addEventListener('change',f)})();</script></body>")
# Assortiment «Сад» on the «Дымка, нежнее» field (approved 11 Nov; reviewed as iz-d fp-7 on assortiment-4.html).
# Markup from tools/as3-sad.html (written by tools/build_as3_sad.py from content.ts) plus the field layer; CSS in tools/assortiment.css.
sad = (D / 'tools' / 'as3-sad.html').read_text().replace('<section id="as3-1" class="sd"', '<section class="sd"', 1)
sad = sad.replace('<div class="in">', '<div class="in"><div class="sd-field" aria-hidden="true"><span class="sd-fbg"></span>'
                  '<span class="wh-grain"></span></div>', 1)
assert 'sd-field' in sad and 'as3-1' not in sad
rep('<div class="between"><div class="in"><span>… hier volgen Assortiment en Hoe het werkt …</span></div></div>',
    '<div id="assortiment">' + sad + '</div><div class="between"><div class="in"><span>… hier volgt Hoe het werkt …</span></div></div>')
s = s.replace('</head>', '<style id="assortiment-css">' + (D / 'tools' / 'assortiment.css').read_text() + '</style></head>', 1)
# Contact with the grower (audit item 1, 12 Nov): real numbers and hours from the live site, hours confirmed by the owner.
PHONE = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 '
         '19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6'
         'l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>')
rep('<div class="flex items-center gap-3"><div class="hidden lg:block">',
    '<div class="flex items-center gap-3"><a class="hc-tel" href="tel:+31620104312" aria-label="Bel de kweker: 06 20 10 43 12">' + PHONE +
    '<span>06 20 10 43 12</span></a><div class="hidden lg:block">')
rep('<li><div><h3>Persoonlijk advies van de kweker</h3><p>De kweker helpt u persoonlijk, <span class="nb">ma–za 09:00–17:00</span>.</p></div></li>',
    '<li><div><h3>Persoonlijk advies van de kweker</h3><p class="wh-ct">Bel <a href="tel:+31620104312">06 20 10 43 12</a> of '
    '<a href="tel:+31620297849">06 20 29 78 49</a>, of stuur een <a href="https://wa.me/31620297849">WhatsApp</a>.'
    '<span class="wh-hours">Ma–vr 08:00–17:00, za 09:00–13:00.</span></p></div></li>')
s = s.replace('</head>', '<style id="contact-css">' + (D / 'tools' / 'contact.css').read_text() + '</style></head>', 1)
# Founder block: walk-in invitation and contact (variant C, approved 12 Nov; reviewed on fd-contact.html). Real data:
# both numbers, WhatsApp on the second, hours Mon–Fri 08:00–17:00 and Sat 09:00–13:00, walk-in welcome (owner, 12 Nov).
FC = ('<div class="fd-ct"><p class="fd-inv">Kom gerust langs, ook zonder afspraak: rondkijken, advies vragen of direct meenemen.</p>'
      '<dl class="fd-dl">'
      '<div class="fd-adr"><dt>Adres</dt><dd><a href="https://www.google.com/maps/search/Esserbroekweg+2+Otterlo">Esserbroekweg&nbsp;2, Otterlo</a></dd></div>'
      '<div class="fd-open"><dt>Open</dt><dd><span class="nb">ma–vr 08:00–17:00</span><span class="fd-sep"> · </span><span class="nb">za 09:00–13:00</span></dd></div>'
      '<div class="fd-tel"><dt>Bellen</dt><dd><a href="tel:+31620104312">06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</a><span class="fd-sep"> · </span>'
      '<a href="tel:+31620297849">06&nbsp;20&nbsp;29&nbsp;78&nbsp;49</a></dd></div>'
      '<div class="fd-wa"><dt>WhatsApp</dt><dd><a href="https://wa.me/31620297849">06&nbsp;20&nbsp;29&nbsp;78&nbsp;49</a></dd></div>'
      '</dl></div>')
rep('</blockquote></div></div></div></div></section>', '</blockquote></div>' + FC + '</div></div></div></section>')
s = s.replace('</head>', '<style id="founder-contact-css">' + (D / 'tools' / 'founder-contact.css').read_text() + '</style></head>', 1)
# Founder card, desktop only (861 px and up): the text panel re-set with more air (owner, 13 Nov). Phones unchanged.
s = s.replace('</head>', '<style id="founder-desktop-css">' + (D / 'tools' / 'founder-desktop.css').read_text() + '</style></head>', 1)
(D / 'index.html').write_text(s)
print('ok', len(s))
