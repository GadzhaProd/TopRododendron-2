# The site footer (plan item 2.3), three designs for review. footer_html(n, home) returns the markup of design n;
# apply(html, n, home) replaces the stub footer of a built page with it and adds tools/footer.css.
#   1 "Тёмный": dark, full width, a rounded top; the two phone lines are the largest thing in it
#   2 "Светлый": the page does not turn dark: a soft sage-butter light at its foot, three calm columns
#   3 "Карточка": one moss card set into the page, a list of contacts on hairlines; the small links under it
#   4 "Большое имя": dark; the name as one very large word across the foot · 5 "Карточка с именем": a moss card with the
#   motto, a way back up and the large name inside · 6 "Контур": light; the name in outline, drawn in when it comes into view
# home = '' on the homepage; 'index.html' on other pages (so "#waarom" becomes "index.html#waarom").
# Facts only from the brief of 22 Nov; no BTW number yet (it is left out, no placeholder).
import pathlib

# (owner, 23 Nov: the search link opened the office; a route to the exact pin of the field instead)
MAP_FIELD = 'https://www.google.com/maps/dir/?api=1&amp;destination=52.0914891%2C5.7283254'
MAP_OFFICE = 'https://www.google.com/maps/search/?api=1&amp;query=Esserbroekweg%202%2C%206731%20DB%20Otterlo'
EXT = ' target="_blank" rel="noopener noreferrer"'
MARK = ('<svg class="fz-mark" viewBox="0 0 40 40" aria-hidden="true" focusable="false"><rect x="1" y="1" width="38" height="38" rx="11" fill="currentColor"/>'
        '<path class="fz-mk" d="M12 13h16M20 13v15" fill="none" stroke-width="2.6" stroke-linecap="round"/><path class="fz-mf" d="M20 28c0-6 3.5-9.5 9-9.5 0 6-3.5 9.5-9 9.5Z"/></svg>')
IG = ('<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r=".6"/></svg>')
TEL = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
WA = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>'


# Paying: eight icons, no visible text, each with its name for screen readers and as a tooltip. The five brands are the
# real marks (img/pay/*.svg, see img/pay/CREDITS.md; referenced as files, not changed). The other three have no brand: our
# own icons in the same 38 x 24 white card, drawn filled and in colour like the brand symbols (owner, 23 Nov: the line icons
# in one colour looked foreign next to the coloured marks): a bank with a gold roof, green banknotes, an invoice with an
# orange euro badge. The cards stay light on every footer.
def _card(label, inner):
    return (f'<li><svg viewBox="0 0 38 24" role="img" aria-label="{label}"><title>{label}</title>'
            '<path fill="#000" opacity=".07" d="M35 0H3C1.3 0 0 1.3 0 3v18c0 1.7 1.4 3 3 3h32c1.7 0 3-1.3 3-3V3c0-1.7-1.4-3-3-3Z"/>'
            '<path fill="#fff" d="M35 1c1.1 0 2 .9 2 2v18c0 1.1-.9 2-2 2H3c-1.1 0-2-.9-2-2V3c0-1.1.9-2 2-2h32Z"/>'
            f'{inner}</svg></li>')
def _mark(name, label):
    return f'<li title="{label}"><img src="img/pay/{name}.svg" alt="{label}" width="38" height="24" loading="lazy"></li>'
EURO = 'font-family="Manrope,system-ui,sans-serif" font-weight="800" text-anchor="middle"'
BANK = ('<path fill="#d9a62e" d="M10.6 9.5 19 4.6l8.4 4.9Z"/><circle cx="19" cy="7.7" r=".95" fill="#fff"/>'
        '<rect x="10.6" y="9.5" width="16.8" height="1.5" rx=".3" fill="#3f4a37"/>'
        '<rect x="12.9" y="11.6" width="1.8" height="4.6" rx=".3" fill="#3f4a37"/><rect x="18.1" y="11.6" width="1.8" height="4.6" rx=".3" fill="#3f4a37"/>'
        '<rect x="23.3" y="11.6" width="1.8" height="4.6" rx=".3" fill="#3f4a37"/>'
        '<rect x="10.6" y="16.7" width="16.8" height="1.5" rx=".3" fill="#3f4a37"/><rect x="9.6" y="18.7" width="18.8" height="1.5" rx=".4" fill="#3f4a37"/>')
CASH = ('<rect x="11.6" y="4.4" width="17.6" height="10" rx="1.3" fill="#2f6f3a"/>'
        '<rect x="8.8" y="8.2" width="17.6" height="10.6" rx="1.3" fill="#5aa152"/>'
        '<rect x="10" y="9.4" width="15.2" height="8.2" rx=".8" fill="none" stroke="#9fd18f" stroke-width=".6"/>'
        '<circle cx="17.6" cy="13.5" r="2.9" fill="#eaf6e2"/>'
        f'<text x="17.6" y="15.1" font-size="4.4" fill="#2f6f3a" {EURO}>€</text>')
INVOICE = ('<path d="M12.4 4.2h8.2l3.9 3.9v11.7h-12.1Z" fill="#fff" stroke="#3f4a37" stroke-width="1.1" stroke-linejoin="round"/>'
           '<path d="M20.6 4.2v3.9h3.9" fill="#dee4d1" stroke="#3f4a37" stroke-width="1.1" stroke-linejoin="round"/>'
           '<rect x="14.4" y="10.4" width="6.6" height="1.2" rx=".6" fill="#3f4a37"/><rect x="14.4" y="12.8" width="5.2" height="1.2" rx=".6" fill="#3f4a37"/>'
           '<rect x="14.4" y="15.2" width="3.6" height="1.2" rx=".6" fill="#3f4a37"/>'
           '<circle cx="25" cy="16.9" r="3.9" fill="#e07b2a"/>'
           f'<text x="25" y="18.6" font-size="4.8" fill="#fff" {EURO}>€</text>')
PAY = ('<ul class="fz-pays">' + _mark('ideal', 'iDEAL') + _mark('visa', 'Visa') + _mark('mastercard', 'Mastercard') + _mark('maestro', 'Maestro') + _mark('vpay', 'V PAY')
       + _card('Overschrijving', BANK) + _card('Contant bij ontvangst', CASH) + _card('Zakelijk op factuur', INVOICE)
       + '</ul>')
# the name as one very large word across the footer (decoration: the name is already there as text)
def wordmark(cls=''):
    # the viewBox leaves room for the descender of "p" (owner, 23 Nov: the p of "Top" was cut, the word read as something else).
    # At font-size 105 the word in Newsreader 500 is 1000 units wide by itself, so textLength only evens out rounding and the
    # letters keep their own proportions (at 124 it was squeezed by 15 %; independent review, 23 Nov)
    return (f'<div class="fz-word {cls}" aria-hidden="true"><svg class="fz-w1" viewBox="0 0 1000 122" preserveAspectRatio="xMidYMid meet">'
            '<text x="0" y="89" textLength="1000" lengthAdjust="spacingAndGlyphs" font-family="Newsreader,Georgia,serif" font-weight="500" font-size="105">Top Rhododendrons</text></svg>'
            # on the phone in two lines, "Rhododendrons" across the full width (134 is its natural size for 1000 units), so the
            # name stays large (owner, 23 Nov; at 390 px in one line it was about 45 px high)
            '<svg class="fz-w2" viewBox="0 0 1000 280" preserveAspectRatio="xMidYMid meet">'
            '<text font-family="Newsreader,Georgia,serif" font-weight="500" font-size="134"><tspan x="0" y="104">Top</tspan>'
            '<tspan x="0" y="240" textLength="1000" lengthAdjust="spacingAndGlyphs">Rhododendrons</tspan></text></svg></div>')
TOP = ('<a class="fz-up" href="#root" aria-label="Terug naar boven" title="Terug naar boven"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 13V3M4 7l4-4 4 4"/></svg></a>')
# the large name comes into view calmly; without scripting or with reduced motion it is simply there
SCRIPT = ('<script>(function(){var w=[].slice.call(document.querySelectorAll(".fz-word"));if(!w.length)return;'
          'if(!("IntersectionObserver" in window)){return}document.documentElement.classList.add("fz-js");'
          'var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("is-in")}})},{threshold:.35});'
          'w.forEach(function(x){io.observe(x)})})();</script>')


def parts(home):
    h = home
    brand = ('<div class="fz-brand"><p class="fz-name">' + MARK + '<span>Top Rhododendrons</span></p><p class="fz-tag">Familiekwekerij in Otterlo, sinds 2001.</p>'
             '<p class="fz-ig"><a href="https://www.instagram.com/toprhododendrons"' + EXT + '>' + IG + '@toprhododendrons</a></p></div>')
    menu = ('<nav class="fz-menu" aria-label="Menu in de voettekst"><h3>Menu</h3><ul>'
            '<li><a href="/assortiment" data-page="Assortiment">Planten</a></li>'
            f'<li><a href="{h}#waarom">Over ons</a></li>'
            '<li><a href="/plantgids" data-page="Plantgids">Advies</a></li>'
            '<li><a href="/groothandel" data-page="Groothandel">Groothandel</a></li>'
            f'<li><a href="{h}#kweker">Contact</a></li></ul></nav>')
    service = ('<nav class="fz-serv" aria-label="Service"><h3>Service</h3><ul>'
               '<li><a href="garantie.html">Aangroeigarantie</a></li>'
               f'<li><a href="{h}#hoe">Hoe bestellen</a></li>'
               '<li><a href="/voorwaarden" data-page="Algemene voorwaarden">Algemene voorwaarden</a></li>'
               '<li><a href="/privacy" data-page="Privacy">Privacy</a></li></ul></nav>')
    # both places together (owner, 23 Nov: the field and the office were in two columns, one at the top, one at the bottom):
    # the field (visits and pick-up) and the office, then the field's hours
    visit = ('<div class="fz-visit"><h3>Adressen</h3><dl class="fz-more fz-addr">'
             '<div><dt>Kwekerij · bezoek en afhalen</dt><dd><a href="' + MAP_FIELD + '"' + EXT + '>Apeldoornseweg, Wekerom</a></dd></div>'
             '<div><dt>Kantoor</dt><dd><a href="' + MAP_OFFICE + '"' + EXT + '>Esserbroekweg&nbsp;2, 6731&nbsp;DB Otterlo</a></dd></div></dl>'
             '<p class="fz-sub">Openingstijden kwekerij</p>'
             # every day written out (owner, 23 Nov); "Zondag gesloten" is on the live site
             '<dl class="fz-hours">' + ''.join(f'<div><dt>{d}</dt><dd>{t}</dd></div>' for d, t in [
                 ('Maandag', '08:00–17:00'), ('Dinsdag', '08:00–17:00'), ('Woensdag', '08:00–17:00'), ('Donderdag', '08:00–17:00'),
                 ('Vrijdag', '08:00–17:00'), ('Zaterdag', '09:00–13:00'), ('Zondag', 'Gesloten')]) + '</dl>'
             '<p class="fz-free">Zonder afspraak welkom</p></div>')
    calls = ('<ul class="fz-calls"><li><a href="tel:+31620104312">' + TEL + '<span><i>Bellen</i><b>06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</b></span></a></li>'
             '<li><a href="https://wa.me/31620297849"' + EXT + '>' + WA + '<span><i>WhatsApp</i><b>06&nbsp;20&nbsp;29&nbsp;78&nbsp;49</b></span></a></li></ul>')
    more = '<dl class="fz-more"><div><dt>E-mail</dt><dd><a href="mailto:info@toprhododendrons.nl">info@toprhododendrons.nl</a></dd></div></dl>'
    contact = '<div class="fz-contact"><h3>Contact</h3>' + calls + more + '</div>'
    pay = '<div class="fz-pay"><h3>Betalen</h3>' + PAY + '</div>'
    legal = '<p class="fz-legal">© 2026 Top Rhododendrons · KvK&nbsp;82480273</p>'
    return brand, menu, service, visit, contact, pay, legal


def footer_html(n, home=''):
    brand, menu, service, visit, contact, pay, legal = parts(home)
    if n == 1:      # dark: contact first and large; the visit beside it; the links and the small print in a quiet band below
        body = ('<div class="fz-top">' + brand + contact + visit + '</div><div class="fz-low">' + menu + service + pay + '</div>' + legal)
    elif n == 2:    # light: brand on the left, three calm columns, the small print on a hairline
        body = ('<div class="fz-top">' + brand + visit + contact + '<div class="fz-links">' + menu + service + '</div></div><div class="fz-low">' + pay + legal + '</div>')
    elif n == 4:    # the large name: dark; the columns, then the name across the whole width at the very foot
        # (owner, 23 Nov: the name only, no tagline; Instagram and the KvK line under the name, not in one long row)
        side = ('<div class="fz-brand"><p class="fz-name">' + MARK + '<span>Top Rhododendrons</span></p>'
                '<p class="fz-ig"><a href="https://www.instagram.com/toprhododendrons"' + EXT + '>' + IG + '@toprhododendrons</a></p>'
                '<p class="fz-legal">© 2026 · KvK&nbsp;82480273</p></div>')
        body = ('<div class="fz-grid">' + contact + visit + menu + service + '</div><div class="fz-low">' + side + pay + '</div>' + wordmark())
    elif n == 5:    # a moss card with the name: the motto and a way back up, the columns, the name inside the card
        motto = '<div class="fz-head"><p class="fz-motto">Familiekwekerij in Otterlo, sinds&nbsp;2001.</p>' + TOP + '</div>'
        body = ('<div class="fz-card">' + motto + '<div class="fz-grid">' + contact + visit + menu + service + '</div><div class="fz-low">' + pay
                + '<p class="fz-ig"><a href="https://www.instagram.com/toprhododendrons"' + EXT + '>' + IG + '@toprhododendrons</a></p></div>' + wordmark() + '</div>' + legal)
    elif n == 6:    # the outline: light; the name drawn in line as a watermark, the columns under it
        body = (wordmark('is-line') + '<div class="fz-grid">' + contact + visit + menu + service + '</div><div class="fz-low">' + brand + pay + legal + '</div>')
    else:           # a moss card: the brand and the visit on the left, the contacts as a list on the right; small links under the card
        body = ('<div class="fz-card"><div class="fz-left">' + brand + visit + '</div>' + contact + '</div><div class="fz-low">' + menu + service + pay + '</div>' + legal)
    return f'<footer class="fz fz{n}"><h2 class="fz-sr">Contact en praktische informatie</h2><div class="in">{body}</div></footer>'


def css():
    return (pathlib.Path(__file__).parent / 'footer.css').read_text()


def apply(html, n=1, home=''):
    i = html.index('<footer class="ft"'); j = html.index('</footer>', i) + len('</footer>')
    html = html[:i] + footer_html(n, home) + html[j:]
    assert html.count('</head>') == 1
    html = html.replace('</body>', SCRIPT + '</body>') if n >= 4 else html
    return html.replace('</head>', '<style id="footer-css">' + css() + '</style></head>')
