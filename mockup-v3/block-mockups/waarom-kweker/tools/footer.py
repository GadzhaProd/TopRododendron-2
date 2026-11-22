# The site footer (plan item 2.3), three designs for review. footer_html(n, home) returns the markup of design n;
# apply(html, n, home) replaces the stub footer of a built page with it and adds tools/footer.css.
#   1 "Тёмный": dark, full width, a rounded top; the two phone lines are the largest thing in it
#   2 "Светлый": the page does not turn dark: a soft sage-butter light at its foot, three calm columns
#   3 "Карточка": one moss card set into the page, a list of contacts on hairlines; the small links under it
# home = '' on the homepage; 'index.html' on other pages (so "#waarom" becomes "index.html#waarom").
# Facts only from the brief of 22 Nov; no BTW number yet (it is left out, no placeholder).
import pathlib

MAP_FIELD = 'https://www.google.com/maps/search/?api=1&amp;query=52.0914891%2C5.7283254'
MAP_OFFICE = 'https://www.google.com/maps/search/?api=1&amp;query=Esserbroekweg%202%2C%206731%20DB%20Otterlo'
EXT = ' target="_blank" rel="noopener noreferrer"'
MARK = ('<svg class="fz-mark" viewBox="0 0 40 40" aria-hidden="true" focusable="false"><rect x="1" y="1" width="38" height="38" rx="11" fill="currentColor"/>'
        '<path class="fz-mk" d="M12 13h16M20 13v15" fill="none" stroke-width="2.6" stroke-linecap="round"/><path class="fz-mf" d="M20 28c0-6 3.5-9.5 9-9.5 0 6-3.5 9.5-9 9.5Z"/></svg>')
IG = ('<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r=".6"/></svg>')
TEL = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
WA = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>'


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
    visit = ('<div class="fz-visit"><h3>Bezoek de kwekerij</h3><p><a href="' + MAP_FIELD + '"' + EXT + '>Apeldoornseweg, Wekerom</a></p>'
             '<dl class="fz-hours"><div><dt>Ma–vr</dt><dd>08:00–17:00</dd></div><div><dt>Za</dt><dd>09:00–13:00</dd></div></dl>'
             '<p class="fz-free">Zonder afspraak welkom</p></div>')
    calls = ('<ul class="fz-calls"><li><a href="tel:+31620104312">' + TEL + '<span><i>Bellen</i><b>06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</b></span></a></li>'
             '<li><a href="https://wa.me/31620297849"' + EXT + '>' + WA + '<span><i>WhatsApp</i><b>06&nbsp;20&nbsp;29&nbsp;78&nbsp;49</b></span></a></li></ul>')
    more = ('<dl class="fz-more"><div><dt>E-mail</dt><dd><a href="mailto:info@toprhododendrons.nl">info@toprhododendrons.nl</a></dd></div>'
            '<div><dt>Kantoor</dt><dd><a href="' + MAP_OFFICE + '"' + EXT + '>Esserbroekweg&nbsp;2, 6731&nbsp;DB Otterlo</a></dd></div></dl>')
    contact = '<div class="fz-contact"><h3>Contact</h3>' + calls + more + '</div>'
    pay = ('<div class="fz-pay"><h3>Betalen</h3><ul><li>iDEAL</li><li>Overschrijving</li><li>Bij ontvangst</li><li>Zakelijk op factuur</li></ul></div>')
    legal = '<p class="fz-legal">© 2026 Top Rhododendrons · KvK&nbsp;82480273</p>'
    return brand, menu, service, visit, contact, pay, legal


def footer_html(n, home=''):
    brand, menu, service, visit, contact, pay, legal = parts(home)
    if n == 1:      # dark: contact first and large; the visit beside it; the links and the small print in a quiet band below
        body = ('<div class="fz-top">' + brand + contact + visit + '</div><div class="fz-low">' + menu + service + pay + '</div>' + legal)
    elif n == 2:    # light: brand on the left, three calm columns, the small print on a hairline
        body = ('<div class="fz-top">' + brand + visit + contact + '<div class="fz-links">' + menu + service + '</div></div><div class="fz-low">' + pay + legal + '</div>')
    else:           # a moss card: the brand and the visit on the left, the contacts as a list on the right; small links under the card
        body = ('<div class="fz-card"><div class="fz-left">' + brand + visit + '</div>' + contact + '</div><div class="fz-low">' + menu + service + pay + '</div>' + legal)
    return f'<footer class="fz fz{n}"><div class="in">{body}</div></footer>'


def css():
    return (pathlib.Path(__file__).parent / 'footer.css').read_text()


def apply(html, n=1, home=''):
    i = html.index('<footer class="ft"'); j = html.index('</footer>', i) + len('</footer>')
    html = html[:i] + footer_html(n, home) + html[j:]
    assert html.count('</head>') == 1
    return html.replace('</head>', '<style id="footer-css">' + css() + '</style></head>')
