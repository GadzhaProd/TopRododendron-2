# Mockup tool (not site code): garantie4.html = the guarantee page after the owner's choice (20 Nov) on garantie-fable3.html:
# the plant label of gb-3 ("Бирка на шнурке") with the seal. Round 2 (owner, 20 Nov): the cord must really go through the
# hole, so the label has a metal eyelet and the cord runs into it at the top and on behind the label (the lower part of the
# hole stays empty); the subtitle sits under the heading as on the other pages; no step numbers; on the phone the page is the
# label with the main points and the pdf, the contacts, and the full conditions behind one "Lees alle voorwaarden" button.
# Desktop (>= 900 px): the label hangs beside the sheet (how it works in four steps, the conditions in short, a tear-off
# contact strip) and stays in view while the sheet scrolls.
# Copy: shortened from the Dutch draft of tools/build_garantie.py (which keeps the full text), no new facts. DRAFT: the owner
# confirms it and a lawyer checks it (plan 3.12). Header, cart, phone menu and footer come from the main mockup (index.html).
# The seal is Fable's (tools/build_garantie_fable3.py). Usage: python3 tools/build_garantie4.py [dir]
import math, re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
i = s.index('<main id="main"'); j = s.index('</main>') + len('</main>')
head, tail = s[:i], s[j:]

WA = 'href="https://wa.me/31620297849" target="_blank" rel="noopener noreferrer"'
FIELD = 'https://www.google.com/maps/search/?api=1&amp;query=52.0914891%2C5.7283254'
A_WA = '<a ' + WA + '>06&nbsp;20&nbsp;29&nbsp;78&nbsp;49</a>'
A_TEL = '<a href="tel:+31620104312">06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</a>'
A_MAIL = '<a href="mailto:info@toprhododendrons.nl">info@toprhododendrons.nl</a>'
A_FIELD = '<a href="' + FIELD + '" target="_blank" rel="noopener noreferrer">Apeldoornseweg, Wekerom</a>'
PDFA = ('<a class="gt-pdfa" href="#" data-page="Aangroeigarantie (pdf)">Alle voorwaarden als pdf<svg viewBox="0 0 16 16" aria-hidden="true">'
        '<path d="M8 2v9M4 8l4 4 4-4M3 14h10"/></svg></a>')


def seal(uid, cls=''):
    # Fable's stamp: a scalloped edge, two rings, the name over the top, the place under it, the term in the middle; worn ink;
    # no dashes beside "maanden" (owner, 20 Nov)
    n, R, r = 40, 114, 9.6
    pts = [(120 + R * math.cos(2 * math.pi * k / n - math.pi / 2), 120 + R * math.sin(2 * math.pi * k / n - math.pi / 2)) for k in range(n)]
    edge = 'M%.2f %.2f' % pts[0] + ''.join('A%.1f %.1f 0 0 1 %.2f %.2f' % (r, r, x, y) for x, y in pts[1:] + pts[:1]) + 'Z'
    ticks = ''.join('<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"/>' % (120 + 68 * math.cos(t), 120 + 68 * math.sin(t), 120 + 72 * math.cos(t), 120 + 72 * math.sin(t))
                    for t in [2 * math.pi * k / 60 for k in range(60)])
    return ('<svg class="gt-seal %s" viewBox="0 0 240 240" role="img" aria-label="Zegel: Top Rhododendrons, Otterlo, sinds 2001. 3 maanden aangroeigarantie">'
            '<defs><path id="%s-t" d="M36 120a84 84 0 0 1 168 0"/><path id="%s-b" d="M24 120a96 96 0 0 0 192 0"/>'
            '<filter id="%s-ink" x="-5%%" y="-5%%" width="110%%" height="110%%"><feTurbulence type="fractalNoise" baseFrequency="1.05" numOctaves="2" seed="11" result="n"/>'
            '<feColorMatrix in="n" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -3 2.95" result="m"/><feComposite in="SourceGraphic" in2="m" operator="in"/></filter></defs>'
            '<g filter="url(#%s-ink)" fill="none" stroke="currentColor">'
            '<path d="%s" stroke-width="2.2"/><circle cx="120" cy="120" r="104" stroke-width="1"/>'
            '<circle cx="120" cy="120" r="62" stroke-width="1.6"/><g stroke-width="1">%s</g>'
            '<g fill="currentColor" stroke="none"><circle cx="30" cy="120" r="2.6"/><circle cx="210" cy="120" r="2.6"/>'
            '<text font-family="Manrope,system-ui,sans-serif" font-size="15" font-weight="700" letter-spacing="3.1"><textPath href="#%s-t" startOffset="50%%" text-anchor="middle">TOP RHODODENDRONS</textPath></text>'
            '<text font-family="Manrope,system-ui,sans-serif" font-size="13.5" font-weight="700" letter-spacing="3"><textPath href="#%s-b" startOffset="50%%" text-anchor="middle">OTTERLO · SINDS 2001</textPath></text>'
            '<text x="120" y="130" text-anchor="middle" font-family="Newsreader,Georgia,serif" font-size="66" font-weight="500">3</text>'
            '<text x="120" y="154" text-anchor="middle" font-family="Newsreader,Georgia,serif" font-size="20" font-weight="500">maanden</text>'
            '</g></g></svg>') % (cls, uid, uid, uid, uid, edge, ticks, uid, uid)
# (owner, 20 Nov: the two dashes either side of "maanden" are gone: on the phone, from a distance, they read as a strike-through)


# The cord (owner chose "2б", 21 Nov; designed in the cord rounds, tools/build_garantie4_fable.py, now frozen): a closed loop of
# moss cord over a small pin, two taut strands in a narrow V. The left strand runs down the front of the paper into a plain
# metal eyelet (just the ring and the dark hole) and darkens as it goes in; the right strand goes behind the top edge
# (CORD_B is painted before the label, so the paper covers it). SVG 120 x 180: the label's top edge at y 128, the eyelet
# at 60,160, the pin at 60,40 (the point the label turns around). The markup is the generated result, kept as it is.
CORD = '<svg class="gt-cord" viewBox="0 0 120 180" aria-hidden="true"><defs><filter id="gt-bl" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="1.3"/></filter><filter id="gt-bs" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation=".8"/></filter><linearGradient id="gt-hol" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4c4b42"/><stop offset=".6" stop-color="#6b695e"/><stop offset="1" stop-color="#85837a"/></linearGradient><radialGradient id="gt-pin" cx=".36" cy=".3" r=".8"><stop offset="0" stop-color="#b7c3a8"/><stop offset=".55" stop-color="#6f8062"/><stop offset="1" stop-color="#3f4a37"/></radialGradient><linearGradient id="gt-met" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f4f1e6"/><stop offset=".5" stop-color="#c3c1ad"/><stop offset="1" stop-color="#85846f"/></linearGradient><clipPath id="gt-pap"><rect x="0" y="128.4" width="120" height="60"/></clipPath></defs><g fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="61" cy="161.4" r="14" fill="rgba(38,44,32,.3)" filter="url(#gt-bl)"/><circle cx="60" cy="160" r="13.4" fill="url(#gt-met)" stroke="rgba(52,58,44,.5)" stroke-width=".8"/><circle cx="60" cy="160" r="8.8" fill="url(#gt-hol)"/><path d="M52.0 158.2A8.200000000000001 8.200000000000001 0 0 1 68.0 158.2A11.0 10.0 0 0 0 52.0 158.2Z" fill="rgba(28,33,24,.5)" filter="url(#gt-bs)"/><circle cx="60" cy="160" r="8.8" stroke="rgba(52,58,44,.55)" stroke-width=".9"/><g clip-path="url(#gt-pap)"><path d="M58.9 157C58.8 146 58.6 136 58.2 128C57.2 100 55.6 70 54.4 47C53.8 40 56.4 35.6 60 35.6" stroke="rgba(38,44,32,.42)" stroke-width="4.0" filter="url(#gt-bl)" transform="translate(1.7 2.3)"/></g><g opacity="1.0" stroke-linecap="round"><path d="M58.9 157C58.8 146 58.6 136 58.2 128C57.2 100 55.6 70 54.4 47C53.8 40 56.4 35.6 60 35.6" stroke="#333c2d" stroke-width="5.3"/><path d="M58.9 157C58.8 146 58.6 136 58.2 128C57.2 100 55.6 70 54.4 47C53.8 40 56.4 35.6 60 35.6" stroke="#6f8062" stroke-width="4.0"/><path d="M58.9 157C58.8 146 58.6 136 58.2 128C57.2 100 55.6 70 54.4 47C53.8 40 56.4 35.6 60 35.6" stroke="#414c38" stroke-width="4.0" stroke-dasharray=".9 2.1" stroke-linecap="butt" opacity=".34"/><path d="M58.9 157C58.8 146 58.6 136 58.2 128C57.2 100 55.6 70 54.4 47C53.8 40 56.4 35.6 60 35.6" stroke="#a9b89b" stroke-width="1.0" opacity=".7" transform="translate(-0.80 -0.32)"/></g><ellipse cx="58.9" cy="158.6" rx="3.6" ry="2.7" fill="#3d4337" filter="url(#gt-bs)"/><ellipse cx="62.2" cy="43.6" rx="6.4" ry="5.6" fill="rgba(38,44,32,.4)" filter="url(#gt-bl)"/><circle cx="60" cy="40" r="5.8" fill="url(#gt-pin)" stroke="#333c2d" stroke-width=".9"/><ellipse cx="58.1" cy="37.9" rx="2.1" ry="1.5" fill="#fff" opacity=".55"/></g></svg>'
CORD_B = '<svg class="gt-cord gt-cord-b" viewBox="0 0 120 180" aria-hidden="true"><g fill="none" stroke-linecap="round" stroke-linejoin="round"><g opacity="1.0" stroke-linecap="round"><path d="M60 35.6C63.6 35.6 66.2 40 65.6 47C64.6 70 63.4 100 62.9 128C62.9 132 63 137 63 142" stroke="#333c2d" stroke-width="5.3"/><path d="M60 35.6C63.6 35.6 66.2 40 65.6 47C64.6 70 63.4 100 62.9 128C62.9 132 63 137 63 142" stroke="#6f8062" stroke-width="4.0"/><path d="M60 35.6C63.6 35.6 66.2 40 65.6 47C64.6 70 63.4 100 62.9 128C62.9 132 63 137 63 142" stroke="#414c38" stroke-width="4.0" stroke-dasharray=".9 2.1" stroke-linecap="butt" opacity=".34"/><path d="M60 35.6C63.6 35.6 66.2 40 65.6 47C64.6 70 63.4 100 62.9 128C62.9 132 63 137 63 142" stroke="#a9b89b" stroke-width="1.0" opacity=".7" transform="translate(-0.80 -0.32)"/></g></g></svg>'

SHORT = ('<ul class="gt-short" aria-label="De garantie in het kort"><li><b>3 maanden</b> na levering</li><li><b>Zelfde soort en maat</b> als vervanging</li>'
         '<li><b>Kosteloos</b> bezorgd of klaargezet</li><li><b>Foto’s volstaan</b>, u hoeft niets aan te tonen</li></ul>')
HEAD = ('<div class="gt-head"><nav class="gt-crumb" aria-label="Kruimelpad"><a href="index.html" data-page="Home">Home</a><span aria-hidden="true">/</span><span>Aangroeigarantie</span></nav>'
        '<h1><span>Slaat een plant niet aan?</span> <span>Dan krijgt u een nieuwe.</span></h1>'
        '<div class="gt-intro"><p class="gt-lead"><b>3 maanden aangroeigarantie na levering</b>, bovenop uw wettelijke rechten. '
        'Dezelfde soort en maat, kosteloos bezorgd of voor u klaargezet. De oorzaak hoeft u niet aan te tonen: een paar foto’s volstaan.</p>'
        '<p class="gt-draft">Concepttekst: de eigenaar en een jurist controleren deze voorwaarden nog.</p></div></div>')
LABEL = ('<div class="gt-lab">' + CORD_B + CORD + '<div class="gt-tag"><p class="gt-lbrand">Top Rhododendrons</p>' + seal('s1')
         + '<p class="gt-lname">Aangroeigarantie</p>' + SHORT + '<p class="gt-lpdf">' + PDFA + '</p></div></div>')

# ---- the sheet: how it works in four steps, then the conditions in short ----
STEPS = [
 ('Planten', 'Plant binnen <b>14&nbsp;dagen</b> na levering, in kalkvrije, zure grond en niet dieper dan de kluit. Geef water in droge periodes.'),
 ('Melden', 'Slaat een plant binnen <b>3&nbsp;maanden</b> niet aan? Stuur twee of drie foto’s met uw ordernummer, per WhatsApp of <span class="nb">e-mail</span>. '
            'De oorzaak hoeft u niet aan te tonen.'),
 ('Antwoord', 'Binnen <b>twee werkdagen</b> hoort u van ons, binnen 14&nbsp;dagen volgt ons besluit. Twijfelen wij, dan komen wij kijken. Dat kost u niets.'),
 ('Nieuwe plant', 'U krijgt een plant van <b>dezelfde soort en maat</b>, in het eerstvolgende plantseizoen kosteloos bezorgd of klaargezet op de kwekerij, '
                  + A_FIELD + '. De oude hoeft niet terug.'),
]
TERMS = [
 ('Voor welke planten', 'Alle rhododendrons die u als particulier bij ons koopt en in de volle grond plant, bezorgd in Nederland of afgehaald. '
                        'Niet aangeslagen betekent: afgestorven, of in het groeiseizoen niet meer uitgelopen.'),
 ('Niet meer leverbaar', 'Dan kiest u: een andere soort in dezelfde maat, of uw geld terug.'),
 ('Wanneer wij niet vervangen', 'Als vaststaat dat de oorzaak vorst is die strenger is dan de vermelde winterhardheid, langdurig staand water, '
                                'vraat door dieren, mechanische schade of vandalisme, verplanten, of kalkhoudende grond.'),
 ('Uw wettelijke rechten', 'Deze garantie komt bovenop uw wettelijke rechten en beperkt ze niet. Voldoet een plant bij levering niet aan wat u mocht '
                           'verwachten, dan heeft u kosteloos recht op vervanging, en anders op prijsvermindering of ontbinding.'),
 ('Wie geeft de garantie', '<span class="gt-ph">[juridische naam]</span>, handelend onder de naam Top Rhododendrons. KvK&nbsp;82480273. '
                           'Esserbroekweg&nbsp;2, 6731&nbsp;DB Otterlo.'),
]
WAYS = '<dl><div><dt>WhatsApp</dt><dd>' + A_WA + '</dd></div><div><dt>Bellen</dt><dd>' + A_TEL + '</dd></div><div><dt>E-mail</dt><dd>' + A_MAIL + '</dd></div></dl>'
DOC = ('<article class="gt-doc" aria-labelledby="h-doc">' +
       '<header class="gt-top"><p class="gt-brand">Top Rhododendrons · familiekwekerij in Otterlo</p>'
       '<h2 id="h-doc">Aangroeigarantie</h2><p class="gt-sub">3 maanden na levering, bovenop uw wettelijke rechten.</p></header>'
       '<section class="gt-how" aria-labelledby="h-how"><h3 class="gt-lbl" id="h-how">Zo werkt het</h3><ol class="gt-steps">'
       + ''.join(f'<li><h4>{t}</h4><p>{p}</p></li>' for t, p in STEPS) +
       '</ol></section>'
       '<section class="gt-terms" aria-labelledby="h-terms"><h3 class="gt-lbl" id="h-terms">Goed om te weten</h3><dl>'
       + ''.join(f'<div><dt>{t}</dt><dd>{p}</dd></div>' for t, p in TERMS) +
       '</dl></section>'
       '<div class="gt-tear" aria-hidden="true"></div>'
       '<footer class="gt-strip"><h3>Gaat een plant achteruit?</h3><p>Meld het zo snel mogelijk, dan kijken we eerst samen of hij te redden is. '
       'U spreekt met Gert Top, oprichter en kweker, of met zijn team.</p>'
       + WAYS + '</footer></article>')
# below 900 px: the contacts under the label, and the full conditions behind one button
HELP = ('<div class="gt-help"><h2>Gaat een plant achteruit?</h2><p>Stuur ons een paar foto’s. U spreekt met Gert Top, oprichter en kweker, of met zijn team.</p>'
        + WAYS + '</div>')
MORE = ('<button class="gt-more" type="button" aria-expanded="false" aria-controls="voorwaarden"><span>Lees alle voorwaarden</span>'
        '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6l4 4 4-4"/></svg></button>')
JS = ('<script>(function(){var b=document.querySelector(".gt-more"),g=document.querySelector(".gt");if(!b||!g)return;'
      'b.addEventListener("click",function(){var o=g.classList.toggle("is-open");b.setAttribute("aria-expanded",o);'
      'b.querySelector("span").textContent=o?"Verberg de voorwaarden":"Lees alle voorwaarden";});})();</script>')
MAIN = ('<main id="main" tabindex="-1" class="gtm"><div class="in gt">' + HEAD + LABEL + HELP + MORE
        + '<div class="gt-stage" id="voorwaarden"><div class="gt-air" aria-hidden="true"></div>' + DOC + '</div></div>' + JS + '</main>')
s = head + MAIN + tail


def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:70]); s = s.replace(a, b)


# on this page the homepage anchors become links to the homepage (only in the markup, not in the scripts)
parts = re.split(r'(<script\b.*?</script>)', s, flags=re.S)
for k in range(0, len(parts), 2):
    for a, label in [('#waarom', 'Over ons (homepage)'), ('#kweker', 'Contact (homepage)'), ('#assortiment', 'Planten (homepage)')]:
        parts[k] = re.sub(r'href="' + a + r'"(?![^>]*data-page)', f'href="index.html{a}" data-page="{label}"', parts[k])
s = ''.join(parts)
rep('</head>', '<style id="garantie4-css">' + (D / 'tools' / 'garantie4.css').read_text() + '</style></head>')
s = re.sub(r'<title>[^<]*</title>', '<title>Aangroeigarantie | Top Rhododendrons</title>', s, count=1)
(D / 'garantie4.html').write_text(s)
print('ok', len(s))
