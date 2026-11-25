/* The page of a variety (tools/soort.py, tools/soort.css): only the buying. The texts and photos are in the markup; the
   prices of this variety, the size slots and the bag price come from the build (data-so, written from tools/calc3.py). */
(function () {
  var main = document.querySelector('[data-so]');
  if (!main) return;
  var d = JSON.parse(main.getAttribute('data-so')), MAXQ = 999;
  var eur = new Intl.NumberFormat('nl-NL', { style: 'currency', currency: 'EUR' });
  var qty = main.querySelector('[data-c="qty"]'), said = main.querySelector('[data-o="said"]'), status = main.querySelector('[data-o="status"]');
  var bar = main.querySelector('[data-bar]'), real = main.querySelector('.so-buy [data-add]'), oth = main.querySelector('[data-oth]');
  var st = { s: parseInt(main.querySelector('[data-c="size"]:checked').value, 10), q: 1, sub: false }, first = true, timer;

  function put(key, text) { Array.prototype.forEach.call(main.querySelectorAll('[data-o="' + key + '"]'), function (el) { el.textContent = text; }); }
  function words(n, one, many) { return n + ' ' + (n === 1 ? one : many); }
  function clamp(n) { return Math.min(MAXQ, Math.max(1, n)); }
  // a typed number: the digits before the first other character ("2,5" is 2, "1e3" is 1)
  function parseQ(text) { var m = /^\s*(\d+)/.exec(text); return m ? clamp(parseInt(m[1], 10)) : 1; }
  function size() { return d.lows[st.s] + '–' + d.tops[st.s] + ' cm'; }

  function update(typing) {
    var n = st.q, bags = st.sub ? n : 0, total = n * d.p[st.s] + bags * d.bag;
    if (!typing) qty.value = String(n);
    qty.style.width = Math.max(1, qty.value.length) + 'ch';
    qty.setAttribute('aria-valuenow', n);
    main.querySelector('[data-step="-1"]').disabled = n <= 1;
    main.querySelector('[data-step="1"]').disabled = n >= MAXQ;
    put('total', eur.format(total));
    put('barline', n + ' × ' + size() + (st.sub ? ' + substraat' : ''));
    clearTimeout(timer);
    if (first) { first = false; return; }
    // for a screen reader: the result in one sentence, a moment after the last change
    timer = setTimeout(function () {
      said.textContent = words(n, 'plant', 'planten') + ' ' + d.name + ', ' + d.lows[st.s] + ' tot ' + d.tops[st.s] + ' centimeter'
        + (st.sub ? ', met ' + words(bags, 'zak', 'zakken') + ' substraat' : ', zonder substraat') + ', samen ' + eur.format(total) + '.';
    }, 600);
  }

  main.addEventListener('change', function (e) {
    var c = e.target.getAttribute('data-c');
    if (c === 'size') { st.s = parseInt(e.target.value, 10); update(false); }
    else if (c === 'sub') { st.sub = e.target.value === '1'; update(false); }
  });
  qty.addEventListener('input', function () { st.q = parseQ(qty.value); update(true); });
  qty.addEventListener('blur', function () { update(false); });
  qty.addEventListener('keydown', function (e) {
    var step = e.key === 'ArrowUp' ? 1 : e.key === 'ArrowDown' ? -1 : 0;
    if (step) { e.preventDefault(); st.q = clamp(st.q + step); update(false); }
  });
  main.addEventListener('click', function (e) {
    var b = e.target.closest('button');
    if (!b) return;
    if (b.hasAttribute('data-step')) { st.q = clamp(st.q + parseInt(b.getAttribute('data-step'), 10)); update(false); }
    else if (b.hasAttribute('data-add')) add(b);
  });

  // into the cart (tools/fase1c.js): the button answers, a screen reader hears what was added, the header counts the plants
  function add(b) {
    var n = st.q, bags = st.sub ? n : 0;
    if (typeof window.tbCartAdd === 'function') window.tbCartAdd({ name: d.name, size: size(), qty: n, price: d.p[st.s], bags: bags, bagPrice: d.bag });
    status.textContent = '';
    setTimeout(function () { status.textContent = words(n, 'plant', 'planten') + (bags ? ' en ' + words(bags, 'zak', 'zakken') + ' substraat' : '') + ' toegevoegd aan uw winkelwagen.'; }, 60);
    if (!b._text) b._text = b.textContent;
    b.textContent = 'Toegevoegd ✓';
    clearTimeout(b._timer);
    b._timer = setTimeout(function () { b.textContent = b._text; }, 2000);
  }

  // phone: the small bar is on show once the real cart button has gone up out of view, until the other varieties begin
  var tick = false;
  function bars() {
    tick = false;
    bar.classList.toggle('is-on', real.getBoundingClientRect().bottom < 0 && oth.getBoundingClientRect().top > window.innerHeight - 80);
  }
  function ask() { if (!tick) { tick = true; requestAnimationFrame(bars); } }
  window.addEventListener('scroll', ask, { passive: true });
  window.addEventListener('resize', ask);

  // the gallery (layout "galerij"): the row of photos slides by itself under a finger; the arrows, the thumbnails or dots
  // and the arrow keys move it one photo at a time. No auto-play.
  var gal = main.querySelector('[data-gal]');
  if (gal) {
    var track = gal.querySelector('[data-track]'), slides = track.children, gos = gal.querySelectorAll('[data-go]'), at = 0, gt = false;
    var calm = matchMedia('(prefers-reduced-motion: reduce)');
    var go = function (i) {
      i = Math.min(slides.length - 1, Math.max(0, i));
      track.scrollTo({ left: slides[i].offsetLeft - slides[0].offsetLeft, behavior: calm.matches ? 'auto' : 'smooth' });
    };
    var mark = function () {
      gt = false;
      var x = track.scrollLeft + slides[0].offsetLeft, best = 0;
      for (var i = 1; i < slides.length; i++) if (Math.abs(slides[i].offsetLeft - x) < Math.abs(slides[best].offsetLeft - x)) best = i;
      at = best;
      Array.prototype.forEach.call(gos, function (b, i) { if (i === at) b.setAttribute('aria-current', 'true'); else b.removeAttribute('aria-current'); });
      gal.querySelector('[data-dir="-1"]').disabled = at === 0;
      gal.querySelector('[data-dir="1"]').disabled = at === slides.length - 1;
    };
    track.addEventListener('scroll', function () { if (!gt) { gt = true; requestAnimationFrame(mark); } }, { passive: true });
    gal.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      if (b.hasAttribute('data-go')) go(parseInt(b.getAttribute('data-go'), 10));
      else if (b.hasAttribute('data-dir')) { var to = at + parseInt(b.getAttribute('data-dir'), 10); go(to); if (b.disabled || to <= 0 || to >= slides.length - 1) track.focus({ preventScroll: true }); }
    });
    track.addEventListener('keydown', function (e) {
      var step = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (step) { e.preventDefault(); go(at + step); }
    });
    mark();
  }

  // a page that comes back from the browser's memory starts fresh: one plant, no substrate, the first size
  window.addEventListener('pageshow', function (e) {
    if (!e.persisted) return;
    st.q = 1; st.sub = false; main.querySelector('[data-c="sub"][value="0"]').checked = true;
    var one = main.querySelector('[data-c="size"]'); one.checked = true; st.s = parseInt(one.value, 10);
    update(false);
  });
  // (a reload may bring back the form's old choices: read them once, so the sum always matches what is shown)
  var r = main.querySelector('[data-c="size"]:checked'); st.s = parseInt(r.value, 10);
  st.sub = main.querySelector('[data-c="sub"]:checked').value === '1'; st.q = parseQ(qty.value);
  update(false); ask();
})();
