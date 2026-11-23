/* The hedge calculator (tools/calc.py, tools/calc.css). One script serves every design: it reads the controls marked
   data-c and writes the results into the elements marked data-o inside each ".hc" block.
   Norms (a guideline, docs/normen-haag.md): plants per metre in one row by size; one 40 L bag of substrate per plant. */
(function () {
  var PER_M = [2, 1.5, 1, 1];                       // 40–60, 60–80, 80–100, 100–120 cm
  var SIZES = ['40–60 cm', '60–80 cm', '80–100 cm', '100–120 cm'];
  var BAG = 14.95, MIN = 1, MAX = 200;
  var eur = new Intl.NumberFormat('nl-NL', { style: 'currency', currency: 'EUR' });
  var num = new Intl.NumberFormat('nl-NL', { maximumFractionDigits: 1 });
  var inCart = 0;

  function each(list, fn) { Array.prototype.forEach.call(list, fn); }

  function setup(root) {
    var data = JSON.parse(root.getAttribute('data-soorten'));
    var lenInput = root.querySelector('[data-c="len"]');
    var range = root.querySelector('[data-c="range"]');
    var status = root.querySelector('[data-o="status"]');
    var said = root.querySelector('[data-o="said"]');
    var timer;

    function pick(name) {
      var el = root.querySelector('input[data-c="' + name + '"]:checked');
      return el ? parseInt(el.value, 10) : 0;
    }
    function length() {
      var v = parseFloat(String(lenInput.value).replace(',', '.'));
      if (isNaN(v)) v = MIN;
      return Math.min(MAX, Math.max(MIN, Math.round(v * 2) / 2));
    }
    function put(key, text) { each(root.querySelectorAll('[data-o="' + key + '"]'), function (el) { el.textContent = text; }); }

    // the hedge to scale: the plants along a metre rule. data-draw="fit" shows the whole hedge (up to 12 m), otherwise the first metres
    function draw(box, perM, colour, len) {
      var fit = box.getAttribute('data-draw') === 'fit';
      var span = fit ? Math.min(12, Math.max(4, Math.ceil(len))) : (box.clientWidth < 520 ? 4 : 6);
      if (fit && box.clientWidth < 520) span = Math.min(span, 6);
      var metres = Math.min(len, span), mw = 100, w = span * mw, s = '', fs = Math.round(w / Math.max(box.clientWidth, 1) * 12);
      for (var m = 0; m <= span; m++) {
        s += '<line x1="' + (m * mw) + '" y1="70" x2="' + (m * mw) + '" y2="' + (m <= metres ? 80 : 75) + '" class="hc-tick"/>';
        if (m <= metres) s += '<text x="' + (m * mw + (m === 0 ? 1 : m === span ? -1 : 0)) + '" y="' + (82 + fs) + '" text-anchor="' + (m === 0 ? 'start' : m === span ? 'end' : 'middle') + '" font-size="' + fs + '" class="hc-m">' + m + ' m</text>';
      }
      s += '<line x1="0" y1="70" x2="' + w + '" y2="70" class="hc-ground"/>';
      var gap = mw / perM, r = Math.min(27, gap * .46), count = Math.ceil(metres * perM - 1e-9);
      for (var k = 0; k < count; k++) {
        var x = gap / 2 + k * gap;
        if (x > metres * mw + .01) break;
        s += '<circle cx="' + x.toFixed(1) + '" cy="' + (70 - r * .9).toFixed(1) + '" r="' + r.toFixed(1) + '" class="hc-bush"/>'
          + '<circle cx="' + x.toFixed(1) + '" cy="' + (70 - r * .9).toFixed(1) + '" r="' + (r * .3).toFixed(1) + '" fill="' + colour + '" class="hc-bloom"/>';
      }
      box.innerHTML = '<svg viewBox="-2 0 ' + (w + 4) + ' ' + (86 + fs) + '" aria-hidden="true" focusable="false">' + s + '</svg>';
      put('shown', len > span ? 'De tekening toont de eerste ' + span + ' meter.' : '');
    }

    function update(fromInput) {
      var len = length(), v = data[pick('var')], si = pick('size');
      var subBox = root.querySelector('[data-c="sub"]'), subOn = !subBox || subBox.checked;
      var n = Math.ceil(len * PER_M[si] - 1e-9), price = v.p[si], plants = n * price, bags = subOn ? n : 0, bagSum = bags * BAG, total = plants + bagSum;
      if (!fromInput) lenInput.value = num.format(len);
      if (range) { range.value = Math.min(len, parseFloat(range.max)); range.style.setProperty('--hc-fill', ((range.value - range.min) / (range.max - range.min) * 100) + '%'); }
      put('len', num.format(len)); put('n', n); put('each', eur.format(price)); put('plants', eur.format(plants));
      put('bags', bags); put('bagsum', eur.format(bagSum)); put('total', eur.format(total));
      var b = SIZES[si].replace(' cm', '').split('–');
      put('sizenote', 'U krijgt planten tussen ' + b[0] + ' en ' + b[1] + '\u00a0cm hoog, gemeten vanaf de kluit; de kluit telt niet mee.');
      put('var', v.n); put('size', SIZES[si]); put('nword', n === 1 ? 'plant' : 'planten'); put('bword', bags === 1 ? 'zak' : 'zakken');
      put('perm', num.format(PER_M[si]) + (PER_M[si] === 1 ? ' plant' : ' planten') + ' per meter, om de ' + Math.round(100 / PER_M[si]) + ' cm');
      each(root.querySelectorAll('[data-p]'), function (el) { el.textContent = eur.format(v.p[parseInt(el.getAttribute('data-p'), 10)]); });
      each(root.querySelectorAll('[data-row="sub"]'), function (el) { el.hidden = !subOn; });
      each(root.querySelectorAll('[data-draw]'), function (box) { draw(box, PER_M[si], v.c, len); });
      root._calc = { n: n, bags: bags };
      if (status) status.textContent = '';
      clearTimeout(timer);
      timer = setTimeout(function () {
        if (said) said.textContent = n + (n === 1 ? ' plant' : ' planten') + ' ' + v.n + ' ' + SIZES[si] + ' voor ' + num.format(len) + ' meter, samen ' + eur.format(total) + '.';
      }, 600);
    }

    lenInput.addEventListener('input', function () { update(true); });
    lenInput.addEventListener('blur', function () { update(false); });
    if (range) range.addEventListener('input', function () { lenInput.value = range.value; update(false); });
    each(root.querySelectorAll('[data-step]'), function (b) {
      b.addEventListener('click', function () { lenInput.value = String(length() + parseFloat(b.getAttribute('data-step'))); update(false); });
    });
    each(root.querySelectorAll('[data-c="var"],[data-c="size"],[data-c="sub"]'), function (el) { el.addEventListener('change', function () { update(false); }); });
    var add = root.querySelector('[data-add]');
    if (add) add.addEventListener('click', function () {
      var c = root._calc; inCart += c.n + c.bags;
      if (typeof window.tbCart === 'function') window.tbCart(inCart);
      if (status) status.textContent = c.n + (c.n === 1 ? ' plant' : ' planten') + (c.bags ? ' en ' + c.bags + (c.bags === 1 ? ' zak' : ' zakken') + ' substraat' : '') + ' in uw winkelwagen.';
    });
    // phone: a small bar with the total while the questions are on screen and the answer is not
    var bar = root.querySelector('.hc-mini'), res = root.querySelector('[data-res]');
    if (bar && res && 'IntersectionObserver' in window) {
      var seen = { root: false, res: false };
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (e) { seen[e.target === res ? 'res' : 'root'] = e.isIntersecting; });
        bar.classList.toggle('is-on', seen.root && !seen.res);
      }, { rootMargin: '-80px 0px -40px 0px' });
      io.observe(root); io.observe(res);
    }
    window.addEventListener('resize', function () { update(false); });
    update(false);
  }
  each(document.querySelectorAll('.hc'), setup);
})();
