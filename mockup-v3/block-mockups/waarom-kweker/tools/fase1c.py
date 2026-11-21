# Mockup tool (not site code): phase 1, step C as approved by the owner (17-18 Nov), applied by tools/finalize_main.py.
# The reviewed version with all options is tools/fase1c_review.py (fase1c.html, fase1c-fable.html).
#   Links (the same addresses as the live site, gadzhaprod/rhododendrons):
#     logo -> /, Planten -> /assortiment, "De kweker" becomes "Over ons" -> Waarom wij, Advies -> /plantgids,
#     Groothandel (menu and hero) -> /groothandel, Contact (new, desktop menu) -> the guarantee block with Gert and both numbers,
#     Bestellen -> /assortiment, "Bekijk de planten" -> the seven varieties below,
#     the cards -> /assortiment/<variety>, "Alle maten en prijzen" -> /assortiment, "Lees de voorwaarden" -> garantie.html (the guarantee page,
#     tools/build_garantie4.py; on the live site /garantie).
#     In the mockup a link to a page that is not here shows a short note (data-page) instead of leading nowhere.
#   Header: no phone number on desktop (owner and Fable, 18 Nov: it loads the header and cannot be called from a browser),
#     "Contact" in the menu instead; "Bestellen" appears once the hero's "Bekijk de planten" has scrolled away;
#     the cart icon always. Phone: call + menu; the cart is a row in the menu, and its count shows on the menu button.
#   1.8 the cart drawer (empty state) and a working phone menu (Bellen / WhatsApp).
#   1.9 a skip link, the hero photo described, the page title, click targets of at least 24 px.
import re, pathlib
T = pathlib.Path(__file__).parent

CART = ('<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/>'
        '<path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>')
PHONE = ('<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 '
         '19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27'
         'a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>')
CHAT = ('<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>')
CLOSE = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M18 6 6 18M6 6l12 12"/></svg>'
WA = 'href="https://wa.me/31620297849" target="_blank" rel="noopener noreferrer"'
SLUG = {'Nova Zembla': 'nova-zembla', 'Catawbiense Grandiflorum': 'catawbiense-grandiflorum', "Cunningham&#x27;s White": 'cunninghams-white',
        'Catawbiense Boursault': 'catawbiense-boursault', 'Roseum Elegans': 'roseum-elegans', 'Ponticum': 'ponticum', 'Ponticum Roseum': 'ponticum-roseum'}

MENU = ('<div class="mm-bg" hidden></div>'
        '<div class="mm" id="mobile-menu" hidden><nav class="mm-nav" aria-label="Menu">'
        '<a href="/assortiment" data-page="Assortiment">Planten</a><a href="#waarom">Over ons</a>'
        '<a href="/plantgids" data-page="Plantgids">Advies</a><a href="/groothandel" data-page="Groothandel">Groothandel</a>'
        '<button type="button" class="mm-cart" data-cart>Winkelwagen<span>' + CART + '<i class="mm-cn">leeg</i></span></button></nav>'
        '<div class="mm-acts"><a class="mm-cta" href="/assortiment" data-page="Assortiment">Bestellen</a>'
        '<a href="tel:+31620104312">' + PHONE + 'Bellen</a><a ' + WA + '>' + CHAT + 'WhatsApp</a></div></div>')

DRAWER = ('<div class="cd" id="winkelwagen" role="dialog" aria-modal="true" aria-labelledby="cd-h" hidden>'
          '<div class="cd-bg" data-close></div><div class="cd-p">'
          '<div class="cd-hd"><h2 id="cd-h">Winkelwagen</h2><button type="button" class="cd-x" aria-label="Sluiten" data-close>' + CLOSE + '</button></div>'
          '<div class="cd-e"><span class="cd-ic">' + CART + '</span><p class="cd-t">Uw winkelwagen is nog leeg</p>'
          '<p>Kies een soort en een maat. U&nbsp;bestelt vanaf 1&nbsp;plant.</p>'
          '<a class="cd-btn" href="#assortiment" data-close>Bekijk de planten<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a></div>'
          '<div class="cd-ft"><p>Liever persoonlijk bestellen? Bel of app de kwekerij.</p><div>'
          '<a href="tel:+31620104312">' + PHONE + 'Bellen</a><a ' + WA + '>' + CHAT + 'WhatsApp</a></div></div>'
          '</div></div>')


def apply(s):
    def rep(a, b, n=1):
        nonlocal s
        assert s.count(a) == n, (s.count(a), a[:80]); s = s.replace(a, b)

    # 1.9 the skip link, the main landmark focusable, the page title (the live site's), the hero photo described
    rep('<body>', '<body><a class="skip" href="#main">Naar de inhoud</a>')
    rep('<main id="main">', '<main id="main" tabindex="-1">')
    s = re.sub(r'<title>[^<]*</title>', '<title>Top Rhododendrons | Kwekerij in Otterlo, sinds 2001</title>', s, count=1)
    rep('<img src="img/hero-field.jpg" alt="" aria-hidden="true"', '<img src="img/hero-field.jpg" alt="Ons rhododendronveld in Otterlo, in bloei"')

    # the header: logo, menu items, then phone · Bestellen (a slot that can open) · cart · menu button
    rep('<a href="#" aria-label="Top Rhododendrons, naar de homepage"', '<a href="/" data-home aria-label="Top Rhododendrons, naar de homepage"')
    N = 'class="text-[14px] tracking-[0.01em] transition-colors text-fg-2 hover:text-fg"'
    rep(f'<a href="#planten" {N}>Planten</a>', f'<a href="/assortiment" data-page="Assortiment" {N}>Planten</a>')
    rep(f'<a href="#kweker" {N}>De kweker</a>', f'<a href="#waarom" {N}>Over ons</a>')
    rep(f'<a href="#advies" {N}>Advies</a>', f'<a href="/plantgids" data-page="Plantgids" {N}>Advies</a>')
    rep(f'<a href="#" {N}>Groothandel</a>', f'<a href="/groothandel" data-page="Groothandel" {N}>Groothandel</a>'
        f'<a href="#kweker" {N}>Contact</a>')
    B = ('class="inline-flex items-center justify-center gap-2 whitespace-nowrap font-medium transition-all duration-300 disabled:opacity-60 '
         'disabled:pointer-events-none select-none bg-accent text-accent-fg hover:opacity-90 h-10 px-4 text-[13px] rounded-ui group/btn"')
    rep(f'<div class="hidden lg:block"><a {B} href="#planten">Bestellen</a></div>',
        f'<div class="hb-slot"><div class="hb-in"><a {B} href="/assortiment" data-page="Assortiment">Bestellen</a></div></div>'
        '<button type="button" class="hc-cart" data-cart aria-haspopup="dialog" aria-controls="winkelwagen" aria-label="Winkelwagen, leeg">'
        + CART + '<span class="hc-n" hidden>0</span></button>')
    rep('translate-y-[3px]"></span></button></div></div></div></header>',
        'translate-y-[3px]"></span><b class="hc-n mm-n" hidden>0</b></button></div></div></div>' + MENU + '</header>')
    rep('</main>', '</main>' + DRAWER)

    # the hero
    rep('split:h-14 split:px-8 split:text-[15px]" href="#planten">Bekijk de planten', 'split:h-14 split:px-8 split:text-[15px]" href="#assortiment">Bekijk de planten')
    rep('<a class="hero-link" href="#">', '<a class="hero-link" href="/groothandel" data-page="Groothandel">')

    # the assortment cards and the conditions link
    for name, slug in SLUG.items():
        rep(f'<a href="#assortiment" aria-label="{name}, vanaf', f'<a href="/assortiment/{slug}" data-page="{name.replace("&#x27;", "’")}" aria-label="{name}, vanaf')
    rep('<a class="sd-more" href="#assortiment">', '<a class="sd-more" href="/assortiment" data-page="Assortiment">')
    rep('<a class="fp-more" href="#garantievoorwaarden">', '<a class="fp-more" href="garantie.html">')

    # WhatsApp opens in a new tab
    rep('href="https://wa.me/31620297849">', WA + '>', 2)
    # (the footer's map link, now to the field, carries target and rel in finalize_main.py)

    s = s.replace('</head>', '<style id="fase1c-css">' + (T / 'fase1c.css').read_text() + '</style></head>', 1)
    s = s.replace('</body>', '<script id="fase1c-js">' + (T / 'fase1c.js').read_text() + '</script></body>', 1)
    return s
