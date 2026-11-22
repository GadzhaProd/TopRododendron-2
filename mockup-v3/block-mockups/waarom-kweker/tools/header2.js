/* The header: a pill after scrolling (see tools/header2.css). Sets on <html>:
   hp-pill  the page has moved more than 24 px
   hp-menu  the phone menu is open
   hp-away  the page is moving down (more than 8 px since the last turn), not near the top, the menu is closed and the
            keyboard focus is not in the header; any move up removes it */
(function () {
  var root = document.documentElement;
  var head = document.querySelector('header.fixed');
  if (!head) return;
  var menuBtn = head.querySelector('[aria-controls="mobile-menu"]');
  var lastY = window.pageYOffset, turnY = lastY, waiting = false;

  function menuIsOpen() { return !!menuBtn && menuBtn.getAttribute('aria-expanded') === 'true'; }
  // keyboard focus only: after a tap the button keeps the focus, and that must not pin the header
  function focusInside() { try { return !!head.querySelector(':focus-visible'); } catch (e) { return head.contains(document.activeElement); } }

  function apply() {
    waiting = false;
    var y = window.pageYOffset;
    root.classList.toggle('hp-pill', y > 24);
    if (y < lastY) { turnY = y; root.classList.remove('hp-away'); }           // any move up: the header is back
    else if (y > lastY) {
      if (root.classList.contains('hp-away')) turnY = y;
      else if (y - turnY > 8 && y > 160 && !menuIsOpen() && !focusInside()) root.classList.add('hp-away');
    }
    lastY = y;
  }
  window.addEventListener('scroll', function () {
    if (!waiting) { waiting = true; window.requestAnimationFrame(apply); }
  }, { passive: true });

  head.addEventListener('focusin', function () { if (focusInside()) { root.classList.remove('hp-away'); turnY = window.pageYOffset; } });
  if (menuBtn && 'MutationObserver' in window) {
    new MutationObserver(function () {
      var open = menuIsOpen();
      root.classList.toggle('hp-menu', open);
      if (open) root.classList.remove('hp-away');
      turnY = window.pageYOffset;
    }).observe(menuBtn, { attributes: true, attributeFilter: ['aria-expanded'] });
  }
  apply();
})();
