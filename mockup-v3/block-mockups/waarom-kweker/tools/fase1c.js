/* Phase 1, step C (approved 17-18 Nov): in-page scrolling, the "Bestellen" reveal, the cart drawer, the phone menu,
   the cart count, and a short note for links to pages that are not in this mockup. */
(function () {
  var root = document.documentElement;
  var reduce = matchMedia('(prefers-reduced-motion: reduce)');
  var header = document.querySelector('header.fixed');
  var headerH = function () { return header ? header.getBoundingClientRect().bottom : 0; };
  var go = function (y) { window.scrollTo({ top: Math.max(0, y), behavior: reduce.matches ? 'auto' : 'smooth' }); };

  /* links to pages that come later: a note instead of a dead click */
  var toast, tt;
  function note(name, path) {
    if (!toast) {
      toast = document.createElement('div'); toast.className = 'pg-toast'; toast.setAttribute('role', 'status');
      document.body.appendChild(toast);
    }
    toast.innerHTML = '<b></b><span></span>';
    toast.firstChild.textContent = name + ': deze pagina volgt';
    toast.lastChild.textContent = path;
    toast.classList.add('on'); clearTimeout(tt);
    tt = setTimeout(function () { toast.classList.remove('on'); }, 2600);
  }

  /* in-page links land with the heading just under the fixed header, and move focus there */
  function scrollToId(id) {
    var t = document.getElementById(id); if (!t) return false;
    var h = t.querySelector('h2') || t;
    go(h.getBoundingClientRect().top + scrollY - headerH() - (innerWidth < 768 ? 24 : 40));
    if (!t.hasAttribute('tabindex')) t.setAttribute('tabindex', '-1');
    t.focus({ preventScroll: true });
    return true;
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest('a'); if (!a) return;
    if (a.hasAttribute('data-home')) { e.preventDefault(); closeMenu(); closeCart(); go(0); return; }
    if (a.hasAttribute('data-page')) { e.preventDefault(); closeMenu(); note(a.getAttribute('data-page'), a.getAttribute('href')); return; }
    var href = a.getAttribute('href') || '';
    if (href.length > 1 && href[0] === '#' && href !== '#main') {
      var id = href.slice(1);
      if (document.getElementById(id)) { e.preventDefault(); closeMenu(); closeCart(); scrollToId(id); }
    }
  });

  /* "Bestellen" appears once the hero's own button has gone under the header (html.hb-on) */
  var cta = document.querySelector('#hero a[href="#assortiment"]');
  if (cta && 'IntersectionObserver' in window) {
    var io;
    var watch = function () {
      if (io) io.disconnect();
      io = new IntersectionObserver(function (es) {
        es.forEach(function (en) {
          root.classList.toggle('hb-on', !en.isIntersecting && en.boundingClientRect.top < headerH());
        });
      }, { rootMargin: '-' + Math.round(headerH()) + 'px 0px 0px 0px' });
      io.observe(cta);
    };
    watch(); addEventListener('resize', watch);
  } else { root.classList.add('hb-on'); }

  /* focus stays inside an open dialog or menu */
  function trap(box, e) {
    var f = [].filter.call(box.querySelectorAll('a[href],button:not([disabled])'), function (x) { return x.offsetParent !== null; });
    if (!f.length) return;
    var first = f[0], last = f[f.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  }

  /* the cart drawer */
  var cd = document.getElementById('winkelwagen'), opener = null;
  function openCart(from) {
    if (!cd) return; closeMenu(); opener = from || document.activeElement;
    cd.hidden = false; void cd.offsetWidth; cd.classList.add('open'); root.classList.add('cd-open');
    cd.querySelector('.cd-x').focus();
  }
  function closeCart() {
    if (!cd || cd.hidden) return;
    cd.classList.remove('open'); root.classList.remove('cd-open');
    setTimeout(function () { cd.hidden = true; }, reduce.matches ? 0 : 450);
    if (opener && opener.focus) opener.focus({ preventScroll: true });
  }
  document.querySelectorAll('[data-cart]').forEach(function (b) { b.addEventListener('click', function () { openCart(b); }); });
  if (cd) {
    /* the backdrop and the close button; the empty cart's "Bekijk de planten" is an in-page link, handled above */
    cd.addEventListener('click', function (e) { var c = e.target.closest('[data-close]'); if (c && c.tagName !== 'A') closeCart(); });
    cd.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeCart(); if (e.key === 'Tab') trap(cd.querySelector('.cd-p'), e); });
  }

  /* the cart count: the header cart (desktop), the menu button and the menu row (phone). The mockup's cart is empty;
     window.tbCart(n) shows how a count looks. */
  function setCount(n) {
    document.querySelectorAll('.hc-n').forEach(function (b) { b.textContent = n > 9 ? '9+' : String(n); b.hidden = !n; });
    var c = document.querySelector('header .hc-cart'); if (c) c.setAttribute('aria-label', n ? 'Winkelwagen, ' + n + (n === 1 ? ' artikel' : ' artikelen') : 'Winkelwagen, leeg');
    var r = document.querySelector('.mm-cn'); if (r) r.textContent = n ? n + (n === 1 ? ' artikel' : ' artikelen') : 'leeg';
    root.setAttribute('data-cart', n);
    var m = document.querySelector('header button[aria-controls="mobile-menu"]');
    if (m && m.getAttribute('aria-expanded') !== 'true') m.setAttribute('aria-label', 'Menu openen' + (n ? ', ' + n + ' in winkelwagen' : ''));
  }
  window.tbCart = setCount;

  /* the phone menu */
  var mb = document.querySelector('header button[aria-controls="mobile-menu"]');
  var mm = document.getElementById('mobile-menu'), mbg = document.querySelector('.mm-bg');
  function openMenu() {
    if (!mm) return; mm.hidden = false; if (mbg) mbg.hidden = false; void mm.offsetWidth;
    root.classList.add('mm-open'); mb.setAttribute('aria-expanded', 'true'); mb.setAttribute('aria-label', 'Menu sluiten');
  }
  function closeMenu() {
    if (!mm || mm.hidden) return;
    root.classList.remove('mm-open'); mb.setAttribute('aria-expanded', 'false'); var n = +root.getAttribute('data-cart') || 0; mb.setAttribute('aria-label', 'Menu openen' + (n ? ', ' + n + ' in winkelwagen' : ''));
    setTimeout(function () { if (!root.classList.contains('mm-open')) { mm.hidden = true; if (mbg) mbg.hidden = true; } }, reduce.matches ? 0 : 350);
  }
  if (mb && mm) {
    mb.addEventListener('click', function () { mm.hidden ? openMenu() : closeMenu(); });
    if (mbg) mbg.addEventListener('click', closeMenu);
    document.addEventListener('keydown', function (e) {
      if (mm.hidden) return;
      if (e.key === 'Escape') { closeMenu(); mb.focus(); }
      if (e.key === 'Tab') trap(header, e);
    });
    addEventListener('resize', function () { if (innerWidth >= 1024) closeMenu(); });
  }
})();
