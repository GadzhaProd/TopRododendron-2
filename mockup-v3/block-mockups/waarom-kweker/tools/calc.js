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
    var status = root.querySelector('[data-o="status"]');
    var said = root.querySelector('[data-o="said"]');
    var timer;

    function pick(name) {
      var el = root.querySelector('select[data-c="' + name + '"]') || root.querySelector('input[data-c="' + name + '"]:checked');
      return el ? parseInt(el.value, 10) : 0;
    }
    function length() {
      var v = parseFloat(String(lenInput.value).replace(',', '.'));
      if (isNaN(v)) v = MIN;
      return Math.min(MAX, Math.max(MIN, Math.round(v * 2) / 2));
    }
    function put(key, text) { each(root.querySelectorAll('[data-o="' + key + '"]'), function (el) { el.textContent = text; }); }

    function draw(perM, colour, len) {
      var box = root.querySelector('[data-draw]');
      if (!box) return;
      var span = box.clientWidth < 520 ? 3 : 6;                // the phone shows three metres, so the figures stay readable
      var metres = Math.min(len, span), w = span === 3 ? 300 : 600, h = 96, mw = w / span, s = '';
      for (var m = 0; m <= span; m++) {
        s += '<line x1="' + (m * mw + .5) + '" y1="70" x2="' + (m * mw + .5) + '" y2="' + (m <= metres ? 82 : 76) + '" class="hc-tick"/>';
        if (m <= metres) s += '<text x="' + (m * mw + (m === 0 ? 2 : m === span ? -2 : 0)) + '" y="95" text-anchor="' + (m === 0 ? 'start' : m === span ? 'end' : 'middle') + '" class="hc-m">' + m + ' m</text>';
      }
      s += '<line x1="0" y1="70" x2="' + w + '" y2="70" class="hc-ground"/>';
      var count = Math.ceil(metres * perM), gap = mw / perM, r = Math.min(26, gap * .46);
      for (var k = 0; k < count; k++) {
        var x = gap / 2 + k * gap;
        if (x > metres * mw) break;
        s += '<circle cx="' + x.toFixed(1) + '" cy="' + (70 - r * .92).toFixed(1) + '" r="' + r.toFixed(1) + '" class="hc-bush"/>'
          + '<circle cx="' + x.toFixed(1) + '" cy="' + (70 - r * .92).toFixed(1) + '" r="' + (r * .3).toFixed(1) + '" fill="' + colour + '" class="hc-bloom"/>';
      }
      box.innerHTML = '<svg viewBox="0 0 ' + w + ' ' + h + '" aria-hidden="true" focusable="false">' + s + '</svg>';
    }

    function update(fromInput) {
      var len = length(), v = data[pick('var')], si = pick('size');
      var subOn = !root.querySelector('[data-c="sub"]') || root.querySelector('[data-c="sub"]').checked;
      var n = Math.ceil(len * PER_M[si] - 1e-9), price = v.p[si], plants = n * price, bags = subOn ? n : 0, bagSum = bags * BAG, total = plants + bagSum;
      if (!fromInput) lenInput.value = num.format(len);
      put('len', num.format(len)); put('n', n); put('each', eur.format(price)); put('plants', eur.format(plants));
      put('bags', bags); put('bagsum', eur.format(bagSum)); put('total', eur.format(total));
      put('var', v.n); put('size', SIZES[si]); put('nword', n === 1 ? 'plant' : 'planten'); put('bword', bags === 1 ? 'zak' : 'zakken');
      put('perm', num.format(PER_M[si]) + (PER_M[si] === 1 ? ' plant' : ' planten') + ' per meter, om de ' + Math.round(100 / PER_M[si]) + ' cm');
      each(root.querySelectorAll('[data-p]'), function (el) { el.textContent = eur.format(v.p[parseInt(el.getAttribute('data-p'), 10)]).replace(',00', ''); });
      each(root.querySelectorAll('[data-row="sub"]'), function (el) { el.hidden = !subOn; });
      root.style.setProperty('--hc-dot', v.c);
      draw(PER_M[si], v.c, len);
      root._calc = { n: n, bags: bags };
      if (status) status.textContent = '';
      clearTimeout(timer);
      timer = setTimeout(function () {
        if (said) said.textContent = n + (n === 1 ? ' plant' : ' planten') + ' ' + v.n + ' ' + SIZES[si] + ' voor ' + num.format(len) + ' meter, samen ' + eur.format(total) + '.';
      }, 600);
    }

    lenInput.addEventListener('input', function () { update(true); });
    lenInput.addEventListener('blur', function () { update(false); });
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
    update(false);
    window.addEventListener('resize', function () { update(false); });
  }
  each(document.querySelectorAll('.hc'), setup);
})();
