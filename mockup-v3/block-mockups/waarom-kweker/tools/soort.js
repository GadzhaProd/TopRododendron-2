/* The product page of a variety (tools/soort.py, tools/soort.css). The variety comes from the hash (#ponticum); the
   choices (size, number, substrate) are one state shared by the directions on the review page. The script reads the
   controls marked data-c and writes into the slots marked data-o, as the calculator does. */
(function () {
  var main = document.querySelector('[data-so]');
  if (!main) return;
  var data = JSON.parse(main.getAttribute('data-soorten'));
  var LOWS = [40, 50, 60, 80, 100], TOPS = [50, 60, 80, 100, 120], BAG = 16.5, MAXQ = 999;   // the five size slots, as in the calculator
  var eur = new Intl.NumberFormat('nl-NL', { style: 'currency', currency: 'EUR' });
  var st = { v: 0, s: 0, q: 1, sub: false }, inCart = 0, first = true, timer;
  var said = main.querySelector('[data-o="said"]'), oth = main.querySelector('[data-oth]');
  var roots = main.querySelectorAll('.so');

  function each(list, fn) { Array.prototype.forEach.call(list, fn); }
  function all(sel) { return main.querySelectorAll(sel); }
  function put(key, text) { each(all('[data-o="' + key + '"]'), function (el) { el.textContent = text; }); }
  function words(n, one, many) { return n + ' ' + (n === 1 ? one : many); }
  function parseQ(text) { var n = parseInt(String(text).replace(/\D/g, ''), 10); return isNaN(n) ? 1 : Math.min(MAXQ, Math.max(1, n)); }
  function current() {
    var d = /\bsrt-(a2|a|b|c)\b/.exec(document.documentElement.className);
    return main.querySelector('.so[data-d="' + (d ? d[1] : 'a2') + '"]') || roots[0];
  }

  // the variety: its texts, photos and the list of the other varieties
  function variety() {
    var v = data[st.v];
    main.style.setProperty('--g', v.g);
    st.s = 0; while (v.p[st.s] == null) st.s++;       // the page of a variety opens on its first size, the "vanaf" price
    put('name', v.n);
    each(all('[data-o="facts"]'), function (el) {
      el.textContent = '';
      v.f.forEach(function (t) { var sp = document.createElement('span'); sp.textContent = t; el.appendChild(sp); });
    }); put('desc', v.d); put('from', v.v); put('over', v.o); put('over2', v.o2);
    each(all('[data-k]'), function (el) { el.textContent = v.k[parseInt(el.getAttribute('data-k'), 10)]; });
    each(all('[data-k2]'), function (el) { el.textContent = v.k2[parseInt(el.getAttribute('data-k2'), 10)]; });
    each(all('img[data-img]'), function (im) {
      var n = im.getAttribute('data-img'), base = 'img/' + v.slug + (n === '2' ? '-2' : ''), w = v.w[n === '2' ? 1 : 0];
      im.srcset = base + '-sm.webp ' + w[0] + 'w, ' + base + '-lg.webp ' + w[1] + 'w';
      im.src = base + '-sm.webp';
      if (!im.closest('button')) im.alt = v.n + (n === '2' ? ', bloeiende struik' : ', bloem van dichtbij');
      im.style.objectPosition = n === '2' ? v.pos : '';
    });
    each(all('[data-slug]'), function (el) { el.hidden = el.getAttribute('data-slug') === v.slug; });
    each(all('[data-show]'), function (el) { show(el, '2'); });
    document.title = v.n + ' | Top Rhododendrons';
    if (typeof window.soVar === 'function') window.soVar(v.slug);
  }

  function update(typing) {
    var v = data[st.v], si = st.s, n = st.q, price = v.p[si], plants = n * price, bags = st.sub ? n : 0, bagSum = bags * BAG, total = plants + bagSum;
    var lo = LOWS[si], hi = TOPS[si], size = lo + '–' + hi + ' cm', shown = 0;
    each(all('[data-s]'), function (el) { var k = parseInt(el.getAttribute('data-s'), 10); el.textContent = LOWS[k] + '–' + TOPS[k] + ' cm'; });
    each(all('[data-p]'), function (el) { var pr = v.p[parseInt(el.getAttribute('data-p'), 10)]; el.textContent = pr == null ? '' : eur.format(pr); });
    // a size the variety is not sold in is not shown
    each(all('input[data-c="size"]'), function (el) { var k = parseInt(el.value, 10); el.checked = k === si; el.parentNode.hidden = v.p[k] == null; });
    for (var k = 0; k < v.p.length; k++) if (v.p[k] != null) shown++;
    each(all('.so-sizes'), function (el) { el.setAttribute('data-n', shown); });
    each(all('input[data-c="sub"]'), function (el) { el.checked = (el.value === '1') === st.sub; });
    each(all('input[data-c="qty"]'), function (el) {
      if (!(typing && el === document.activeElement)) el.value = String(n);
      el.style.width = Math.max(1, el.value.length) + 'ch';
    });
    each(all('[data-step="-1"]'), function (b) { b.disabled = n <= 1; });
    each(all('[data-step="1"]'), function (b) { b.disabled = n >= MAXQ; });
    put('size', size);
    put('sizenote', 'U krijgt planten van ' + lo + ' tot ' + hi + ' cm hoog, gemeten vanaf de bovenkant van de kluit.');
    put('max', v.m);
    var big = v.m > TOPS[TOPS.length - 1];
    each(all('[data-row="big"]'), function (el) { el.hidden = !big; });
    each(all('[data-row="ask"]'), function (el) { el.hidden = big; });
    each(all('[data-row="sub"]'), function (el) { el.hidden = !st.sub; });
    put('n', n); put('nword', n === 1 ? 'plant' : 'planten'); put('each', eur.format(price)); put('plants', eur.format(plants));
    put('bags', bags); put('bword', bags === 1 ? 'zak' : 'zakken'); put('bagsum', eur.format(bagSum)); put('total', eur.format(total));
    each(all('[data-o="sumline"]'), function (el) {
      el.textContent = '';
      [words(n, 'plant', 'planten') + ' van ' + size].concat(st.sub ? [words(bags, 'zak', 'zakken') + ' substraat'] : []).forEach(function (t) {
        var sp = document.createElement('span'); sp.textContent = t; el.appendChild(sp);
      });
    });
    put('barline', n + ' × ' + size + (st.sub ? ' + substraat' : ''));
    put('status', '');
    clearTimeout(timer);
    if (first) { first = false; return; }
    timer = setTimeout(function () {
      said.textContent = words(n, 'plant', 'planten') + ' ' + v.n + ', ' + lo + ' tot ' + hi + ' centimeter'
        + (st.sub ? ', met ' + words(bags, 'zak', 'zakken') + ' substraat' : ', zonder substraat') + ', samen ' + eur.format(total) + '.';
    }, 600);
  }

  // the photo of the card (direction c): the bush or the flower
  function show(box, n) {
    box.setAttribute('data-show', n);
    each(box.querySelectorAll('[data-pic]'), function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-pic') === n ? 'true' : 'false'); });
  }

  main.addEventListener('change', function (e) {
    var el = e.target, c = el.getAttribute && el.getAttribute('data-c');
    if (c === 'size') { st.s = parseInt(el.value, 10); update(false); }
    else if (c === 'sub') { st.sub = el.value === '1'; update(false); }
  });
  main.addEventListener('input', function (e) {
    if (e.target.getAttribute('data-c') === 'qty') { st.q = parseQ(e.target.value); update(true); }
  });
  main.addEventListener('focusout', function (e) {
    if (e.target.getAttribute && e.target.getAttribute('data-c') === 'qty') { e.target.value = String(st.q); e.target.style.width = e.target.value.length + 'ch'; }
  });
  main.addEventListener('click', function (e) {
    var b = e.target.closest('button');
    if (!b || !main.contains(b)) return;
    if (b.hasAttribute('data-step')) { st.q = Math.min(MAXQ, Math.max(1, st.q + parseInt(b.getAttribute('data-step'), 10))); update(false); }
    else if (b.hasAttribute('data-pic')) show(b.closest('[data-show]'), b.getAttribute('data-pic'));
    else if (b.hasAttribute('data-add')) add(b);
  });

  // into the cart: the button answers, the line under the real button says what was added, the header cart counts
  function add(b) {
    var n = st.q, bags = st.sub ? n : 0;
    inCart += n + bags;
    if (typeof window.tbCart === 'function') window.tbCart(inCart);
    var text = words(n, 'plant', 'planten') + (bags ? ' en ' + words(bags, 'zak', 'zakken') + ' substraat' : '') + ' toegevoegd aan uw winkelwagen.';
    put('status', '');
    setTimeout(function () { put('status', text); }, 60);
    if (!b._text) b._text = b.textContent;
    b.textContent = 'Toegevoegd ✓';
    clearTimeout(b._timer);
    b._timer = setTimeout(function () { b.textContent = b._text; }, 2000);
  }

  // phone: the small bar is on show while the real cart button is out of view, and gone once the other varieties begin
  var tick = false;
  function bars() {
    tick = false;
    var root = current(), bar = root.querySelector('[data-bar]');
    if (!bar) return;
    var mark = root.querySelector('[data-res]') || root.querySelector('.so-buy [data-add]'), r = mark.getBoundingClientRect(), h = window.innerHeight;
    var seen = r.top < h - 10 && r.bottom > 0, past = oth.getBoundingClientRect().top < h - 80;
    bar.classList.toggle('is-on', !seen && !past);
  }
  function ask() { if (!tick) { tick = true; requestAnimationFrame(bars); } }
  window.addEventListener('scroll', ask, { passive: true });
  window.addEventListener('resize', ask);

  // the direction on show (the review page): the others are taken out of the page for assistive technology too
  window.soDir = function () {
    var cur = current();
    each(roots, function (r) { r.hidden = r !== cur; });
    ask();
  };

  function fromHash() {
    var h = decodeURIComponent(location.hash.slice(1));
    for (var i = 0; i < data.length; i++) if (data[i].slug === h) { st.v = i; return true; }
    return false;
  }
  window.addEventListener('hashchange', function () {
    if (!fromHash()) return;
    variety(); update(false);
    window.scrollTo(0, 0);
    var h1 = current().querySelector('h1');
    if (h1) h1.focus({ preventScroll: true });
  });

  fromHash(); variety(); window.soDir(); update(false);
})();
