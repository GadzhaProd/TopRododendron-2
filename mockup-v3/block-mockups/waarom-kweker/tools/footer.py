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

MAP_FIELD = 'https://www.google.com/maps/search/?api=1&amp;query=52.0914891%2C5.7283254'
MAP_OFFICE = 'https://www.google.com/maps/search/?api=1&amp;query=Esserbroekweg%202%2C%206731%20DB%20Otterlo'
EXT = ' target="_blank" rel="noopener noreferrer"'
MARK = ('<svg class="fz-mark" viewBox="0 0 40 40" aria-hidden="true" focusable="false"><rect x="1" y="1" width="38" height="38" rx="11" fill="currentColor"/>'
        '<path class="fz-mk" d="M12 13h16M20 13v15" fill="none" stroke-width="2.6" stroke-linecap="round"/><path class="fz-mf" d="M20 28c0-6 3.5-9.5 9-9.5 0 6-3.5 9.5-9 9.5Z"/></svg>')
IG = ('<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r=".6"/></svg>')
TEL = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
WA = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>'


# Paying: eight icons, no visible text, each with its name for screen readers and as a tooltip. The five brands are the
# real marks (img/pay/*.svg, see img/pay/CREDITS.md; referenced as files, not changed). The other three have no brand: our own line icons in moss,
# in the same 38 x 24 card frame, so the row reads as one set. The cards stay light on every footer.
def _card(label, inner):
    return (f'<li><svg viewBox="0 0 38 24" role="img" aria-label="{label}"><title>{label}</title>'
            '<path fill="#000" opacity=".07" d="M35 0H3C1.3 0 0 1.3 0 3v18c0 1.7 1.4 3 3 3h32c1.7 0 3-1.3 3-3V3c0-1.7-1.4-3-3-3Z"/>'
            '<path fill="#fff" d="M35 1c1.1 0 2 .9 2 2v18c0 1.1-.9 2-2 2H3c-1.1 0-2-.9-2-2V3c0-1.1.9-2 2-2h32Z"/>'
            f'<g fill="none" stroke="#3f4a37" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round">{inner}</g></svg></li>')
def _mark(name, label):
    return f'<li><img src="img/pay/{name}.svg" alt="{label}" title="{label}" width="38" height="24" loading="lazy"></li>'
PAY = ('<ul class="fz-pays">' + _mark('ideal', 'iDEAL') + _mark('visa', 'Visa') + _mark('mastercard', 'Mastercard') + _mark('maestro', 'Maestro') + _mark('vpay', 'V PAY')
       + _card('Overschrijving', '<path d="M11 9.6 19 5.2l8 4.4Z"/><path d="M13.4 11.6v4.6M19 11.6v4.6M24.6 11.6v4.6M11.4 16.6h15.2M10.4 18.8h17.2"/>')
       + _card('Contant bij ontvangst', '<rect x="10.5" y="5.6" width="17" height="8.6" rx="1.2"/><circle cx="19" cy="9.9" r="2"/><path d="M13 8v3.8M25 8v3.8"/>'
                                        '<path d="M8.6 18.4h3.2l3.4 1.5h6.2l5.8-2.9"/>')
       + _card('Zakelijk op factuur', '<path d="M14.2 4.8h6.6l3 3v11.4h-9.6Z"/><path d="M20.8 4.8v3h3"/><path d="M16.4 11.2h5.2M16.4 13.6h5.2M16.4 16h3"/>')
       + '</ul>')
# the name as one very large word across the footer (decoration: the name is already there as text)
def wordmark(cls=''):
    return (f'<div class="fz-word {cls}" aria-hidden="true"><svg viewBox="0 0 1000 132" preserveAspectRatio="xMidYMid meet">'
            '<text x="0" y="104" textLength="1000" lengthAdjust="spacingAndGlyphs" font-family="Newsreader,Georgia,serif" font-weight="500" font-size="124">Top Rhododendrons</text></svg></div>')
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
    visit = ('<div class="fz-visit"><h3>Bezoek de kwekerij</h3><p><a href="' + MAP_FIELD + '"' + EXT + '>Apeldoornseweg, Wekerom</a></p>'
             '<dl class="fz-hours"><div><dt>Ma–vr</dt><dd>08:00–17:00</dd></div><div><dt>Za</dt><dd>09:00–13:00</dd></div></dl>'
             '<p class="fz-free">Zonder afspraak welkom</p></div>')
    calls = ('<ul class="fz-calls"><li><a href="tel:+31620104312">' + TEL + '<span><i>Bellen</i><b>06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</b></span></a></li>'
             '<li><a href="https://wa.me/31620297849"' + EXT + '>' + WA + '<span><i>WhatsApp</i><b>06&nbsp;20&nbsp;29&nbsp;78&nbsp;49</b></span></a></li></ul>')
    more = ('<dl class="fz-more"><div><dt>E-mail</dt><dd><a href="mailto:info@toprhododendrons.nl">info@toprhododendrons.nl</a></dd></div>'
            '<div><dt>Kantoor</dt><dd><a href="' + MAP_OFFICE + '"' + EXT + '>Esserbroekweg&nbsp;2, 6731&nbsp;DB Otterlo</a></dd></div></dl>')
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
        body = ('<div class="fz-grid">' + contact + visit + menu + service + '</div><div class="fz-low">' + brand + pay + legal + '</div>' + wordmark())
    elif n == 5:    # a moss card with the name: the motto and a way back up, the columns, the name inside the card
        motto = '<div class="fz-head"><p class="fz-motto">Familiekwekerij in Otterlo, sinds&nbsp;2001.</p>' + TOP + '</div>'
        body = ('<div class="fz-card">' + motto + '<div class="fz-grid">' + contact + visit + menu + service + '</div><div class="fz-low">' + pay
                + '<p class="fz-ig"><a href="https://www.instagram.com/toprhododendrons"' + EXT + '>' + IG + '@toprhododendrons</a></p></div>' + wordmark() + '</div>' + legal)
    elif n == 6:    # the outline: light; the name drawn in line as a watermark, the columns under it
        body = (wordmark('is-line') + '<div class="fz-grid">' + contact + visit + menu + service + '</div><div class="fz-low">' + brand + pay + legal + '</div>')
    else:           # a moss card: the brand and the visit on the left, the contacts as a list on the right; small links under the card
        body = ('<div class="fz-card"><div class="fz-left">' + brand + visit + '</div>' + contact + '</div><div class="fz-low">' + menu + service + pay + '</div>' + legal)
    return f'<footer class="fz fz{n}"><div class="in">{body}</div></footer>'


def css():
    return (pathlib.Path(__file__).parent / 'footer.css').read_text()


def apply(html, n=1, home=''):
    i = html.index('<footer class="ft"'); j = html.index('</footer>', i) + len('</footer>')
    html = html[:i] + footer_html(n, home) + html[j:]
    assert html.count('</head>') == 1
    html = html.replace('</body>', SCRIPT + '</body>') if n >= 4 else html
    return html.replace('</head>', '<style id="footer-css">' + css() + '</style></head>')
