/* The hedge calculator, «Смета» restyled (tools/calc3.py, tools/calc3.css; the logic of tools/calc.js). It reads the controls marked
   data-c and writes the results into the elements marked data-o inside each ".sx" block.
   Norms (a guideline, docs/normen-haag.md): plants per metre in one row by size; one 40 L bag of substrate per plant. */
(function () {
  var PER_M2 = [3, 2, 1, 1];                        // a group or border: plants per square metre
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
    function field(key) { return root.querySelector('input[data-c="' + key + '"]'); }
    function value(key, max) {
      var v = parseFloat(String(field(key).value).replace(',', '.'));
      if (isNaN(v)) v = MIN;
      return Math.min(max, Math.max(MIN, Math.round(v * 2) / 2));
    }
    function length() { return value('len', MAX); }
    function mode() { var el = root.querySelector('input[data-c="mode"]:checked'); return el ? el.value : 'haag'; }

    function put(key, text) { each(root.querySelectorAll('[data-o="' + key + '"]'), function (el) { el.textContent = text; }); }

    function update(fromInput) {
      var bed = mode() === 'border', len = length(), D = value('bd', 50), L = value('bl', 50), W = value('bw', 50), v = data[pick('var')], si = pick('size');
      // the bed's shape: a round group by its diameter, an oval one or a straight border by length and width
      var sh = root.querySelector('input[data-c="shape"]:checked'), shape = sh ? sh.value : 'recht', round = shape !== 'recht';
      var area = shape === 'rond' ? Math.PI * D * D / 4 : shape === 'ovaal' ? Math.PI * L * W / 4 : L * W;
      var subEl = root.querySelector('input[data-c="sub"]:checked'), subOn = !subEl || subEl.value !== '0';
      var n = Math.ceil((bed ? area * PER_M2[si] : len * PER_M[si]) - 1e-9), price = v.p[si], plants = n * price, bags = subOn ? n : 0, bagSum = bags * BAG, total = plants + bagSum;
      if (!fromInput) { lenInput.value = num.format(len); field('bd').value = num.format(D); field('bl').value = num.format(L); field('bw').value = num.format(W); }
      if (range) { range.value = Math.min(len, parseFloat(range.max)); range.style.setProperty('--sx-fill', ((range.value - range.min) / (range.max - range.min) * 100) + '%'); }
      each(root.querySelectorAll('[data-mode]'), function (el) { el.hidden = el.getAttribute('data-mode') !== (bed ? 'border' : 'haag'); });
      each(root.querySelectorAll('[data-shape]'), function (el) { el.hidden = el.getAttribute('data-shape').split(' ').indexOf(shape) < 0; });
      var bedName = shape === 'rond' ? 'ronde groep' : shape === 'ovaal' ? 'ovale groep' : 'border';
      var what = bed ? num.format(area) + '\u00a0m²' : num.format(len) + '\u00a0meter';
      put('area', num.format(area)); put('h2', bed ? (round ? 'groep' : 'border') : 'haag'); put('what', what); put('title', (bed ? 'Uw ' + bedName + ' van ' : 'Uw haag van ') + what);
      put('len', num.format(len)); put('n', n); put('each', eur.format(price)); put('plants', eur.format(plants));
      put('bags', bags); put('bagsum', eur.format(bagSum)); put('total', eur.format(total));
      var b = SIZES[si].replace(' cm', '').split('–');
      put('sizenote', 'U krijgt planten tussen ' + b[0] + ' en ' + b[1] + '\u00a0cm hoog, gemeten vanaf de kluit; de kluit telt niet mee.');
      put('var', v.n); put('size', SIZES[si]); put('nword', n === 1 ? 'plant' : 'planten'); put('bword', bags === 1 ? 'zak' : 'zakken');
      var d = bed ? PER_M2[si] : PER_M[si];
      put('permlead', bed ? (round ? 'Richtlijn voor een groep' : 'Richtlijn voor een border') : 'Richtlijn voor één rij');
      put('perm', num.format(d) + (d === 1 ? ' plant' : ' planten') + (bed ? ' per m²' : ' per meter') + ', om de ' + Math.round(100 / (bed ? Math.sqrt(d) : d)) + ' cm');
      each(root.querySelectorAll('[data-p]'), function (el) { el.textContent = eur.format(v.p[parseInt(el.getAttribute('data-p'), 10)]); });
      each(root.querySelectorAll('[data-row="sub"]'), function (el) { el.hidden = !subOn; });
      root._calc = { n: n, bags: bags };
      if (status) status.textContent = '';
      clearTimeout(timer);
      timer = setTimeout(function () {
        if (said) said.textContent = n + (n === 1 ? ' plant' : ' planten') + ' ' + v.n + ' ' + SIZES[si] + ' voor ' + (bed ? 'een ' + bedName + ' van ' + num.format(area) + ' vierkante meter' : 'een haag van ' + num.format(len) + ' meter') + ', samen ' + eur.format(total) + '.';
      }, 600);
    }

    lenInput.addEventListener('input', function () { update(true); });
    lenInput.addEventListener('blur', function () { update(false); });
    each(['bd', 'bl', 'bw'], function (k) { field(k).addEventListener('input', function () { update(true); }); field(k).addEventListener('blur', function () { update(false); }); });
    if (range) range.addEventListener('input', function () { lenInput.value = range.value; update(false); });
    each(root.querySelectorAll('[data-step]'), function (b) {
      b.addEventListener('click', function () { var k = b.getAttribute('data-for') || 'len'; field(k).value = String(value(k, k === 'len' ? MAX : 50) + parseFloat(b.getAttribute('data-step'))); update(false); });
    });
    each(root.querySelectorAll('[data-c="var"],[data-c="size"],[data-c="sub"],[data-c="mode"],[data-c="shape"]'), function (el) { el.addEventListener('change', function () { update(false); }); });
    var add = root.querySelector('[data-add]');
    if (add) add.addEventListener('click', function () {
      var c = root._calc; inCart += c.n + c.bags;
      if (typeof window.tbCart === 'function') window.tbCart(inCart);
      if (status) status.textContent = c.n + (c.n === 1 ? ' plant' : ' planten') + (c.bags ? ' en ' + c.bags + (c.bags === 1 ? ' zak' : ' zakken') + ' substraat' : '') + ' in uw winkelwagen.';
    });
    // phone: a small bar with the total while the questions are on screen and the answer is not
    var bar = root.querySelector('.sx-mini'), res = root.querySelector('[data-res]');
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
  each(document.querySelectorAll('.sx'), setup);
})();
