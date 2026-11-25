/* The plant calculator (tools/calc3.py, tools/calc3.css). It reads the controls marked data-c and writes the results into
   the elements marked data-o inside each ".sx" block.
   Norms (a guideline, docs/normen-haag.md): plants per metre in one row, or per square metre, by size; one 40 L bag of
   substrate per plant. */
(function () {
  var PER_M = [2, 2, 1.5, 1, 1];                    // a hedge: 40–50, 50–60, 60–80, 80–100, 100–120 cm
  var PER_M2 = [3, 3, 2, 1, 1];                     // a group or border
  var LOWS = [40, 50, 60, 80, 100], TOPS = [50, 60, 80, 100, 120];   // the five size slots; a variety is not sold in every one
  var BAG = 16.5, MIN = 1, TOP = { len: 200, bd: 50, bl: 50, bw: 50 };
  var eur = new Intl.NumberFormat('nl-NL', { style: 'currency', currency: 'EUR' });
  var num = new Intl.NumberFormat('nl-NL', { maximumFractionDigits: 1 });
  var inCart = 0;

  function each(list, fn) { Array.prototype.forEach.call(list, fn); }
  // a typed measure: digits with one optional decimal (comma or point); a point before three digits is a thousands mark;
  // anything after that is ignored, so "1e2" is 1 and never 100
  function parse(text) {
    var m = /^\d+(?:[.,]\d*)?/.exec(String(text).replace(/\s/g, '').replace(/\.(?=\d{3}(?:\D|$))/g, ''));
    return m ? parseFloat(m[0].replace(',', '.')) : NaN;
  }

  function setup(root) {
    var data = JSON.parse(root.getAttribute('data-soorten'));
    var status = root.querySelector('[data-o="status"]'), said = root.querySelector('[data-o="said"]'), add = root.querySelector('[data-add]');
    var addText = add.textContent, first = true, timer, addTimer;

    function pick(name) { var el = root.querySelector('input[data-c="' + name + '"]:checked'); return el ? el.value : ''; }
    function field(key) { return root.querySelector('input[data-c="' + key + '"]'); }
    function value(key) {
      var v = parse(field(key).value);
      if (isNaN(v)) v = MIN;
      return Math.min(TOP[key], Math.max(MIN, Math.round(v * 2) / 2));
    }
    function put(key, text) { each(root.querySelectorAll('[data-o="' + key + '"]'), function (el) { el.textContent = text; }); }
    function words(n, one, many) { return n + ' ' + (n === 1 ? one : many); }

    // two measures side by side where they fit, one under the other where they do not
    function stack() {
      each(root.querySelectorAll('.sx-meas'), function (el) { el.classList.remove('is-stack'); if (el.scrollWidth > el.clientWidth) el.classList.add('is-stack'); });
    }

    // typing: the text in the field is left as typed (only the sums follow); it is tidied when the field is left
    function update(typing) {
      var bed = pick('mode') === 'border', shape = pick('shape'), round = shape !== 'recht', vi = parseInt(pick('var'), 10), si = parseInt(pick('size'), 10);
      var len = value('len'), D = value('bd'), L = value('bl'), W = value('bw'), v = data[vi], subOn = pick('sub') !== '0';
      // the size slots of this variety: one it is not sold in is hidden; the chosen slot stays when the variety changes,
      // and where the new variety lacks it the choice falls back to 50–60 cm
      if (v.p[si] == null) si = 1;
      var shown = 0;
      each(root.querySelectorAll('input[data-c="size"]'), function (el) {
        var k = parseInt(el.value, 10), has = v.p[k] != null;
        el.parentNode.hidden = !has; el.checked = k === si; if (has) shown++;
      });
      root.querySelector('.sx-sizes').setAttribute('data-n', shown);
      // the bed: a round group by its diameter (an oval one by the mean of its length and width, the hint says so; about 2 %
      // more than the oval for usual shapes) or a straight border by length and width (owner, 24 Nov: two shapes, not three)
      var area = shape === 'rond' ? Math.PI * D * D / 4 : L * W;
      var d = bed ? PER_M2[si] : PER_M[si], n = Math.ceil((bed ? area : len) * d - 1e-9);
      var price = v.p[si], plants = n * price, bags = subOn ? n : 0, bagSum = bags * BAG, total = plants + bagSum;
      each(['len', 'bd', 'bl', 'bw'], function (k) {
        var el = field(k);
        if (!typing) el.value = num.format(value(k));
        el.style.width = Math.max(1, el.value.length) + 'ch';     // the field is as wide as its figure, in every browser
      });
      each(root.querySelectorAll('[data-mode]'), function (el) { el.hidden = el.getAttribute('data-mode') !== (bed ? 'border' : 'haag'); });
      each(root.querySelectorAll('[data-shape]'), function (el) { el.hidden = el.getAttribute('data-shape').split(' ').indexOf(shape) < 0; });
      stack();
      var bedName = shape === 'rond' ? 'ronde groep' : 'border', kind = bed ? (round ? 'groep' : 'border') : 'haag';
      var lo = LOWS[si], hi = TOPS[si], size = lo + '–' + hi + ' cm';
      put('area', num.format(area)); put('h2', kind);
      put('title', bed ? 'Uw ' + bedName + ' van ' + num.format(area) + ' m²' : 'Uw haag van ' + num.format(len) + ' meter');
      put('var', v.n); put('size', size);
      put('sizenote', 'U krijgt planten van ' + lo + ' tot ' + hi + ' cm hoog, gemeten vanaf de bovenkant van de kluit.');
      put('permlead', bed ? (round ? 'Richtlijn voor een groep' : 'Richtlijn voor een border') : 'Richtlijn voor één rij');
      // the spacing, rounded to 5 cm; left out for one plant per metre in a row, where it would say the same twice
      var apart = Math.round(100 / (bed ? Math.sqrt(d) : d) / 5) * 5;
      put('perm', num.format(d) + (d === 1 ? ' plant' : ' planten') + (bed ? ' per m²' : ' per meter')
        + (d === 1 && !bed ? '' : ', ongeveer ' + (apart === 100 ? '1 meter' : apart + ' cm') + ' uit elkaar'));
      put('dense', 'Dichter geplant groeit de ' + kind + ' sneller dicht.');
      put('max', v.m); each(root.querySelectorAll('[data-row="big"]'), function (el) { el.hidden = v.m <= TOPS[TOPS.length - 1]; });
      put('n', n); put('nword', n === 1 ? 'plant' : 'planten'); put('each', eur.format(price)); put('plants', eur.format(plants));
      put('bags', bags); put('bword', bags === 1 ? 'zak' : 'zakken'); put('bagsum', eur.format(bagSum)); put('total', eur.format(total));
      each(root.querySelectorAll('[data-p]'), function (el) { var pr = v.p[parseInt(el.getAttribute('data-p'), 10)]; el.textContent = pr == null ? '' : eur.format(pr); });
      each(root.querySelectorAll('[data-row="sub"]'), function (el) { el.hidden = !subOn; });
      root._calc = { n: n, bags: bags };
      status.textContent = '';
      // for a screen reader: the result in one sentence, a moment after the last change; silent when the page loads
      clearTimeout(timer);
      if (first) { first = false; return; }
      timer = setTimeout(function () {
        said.textContent = words(n, 'plant', 'planten') + ' ' + v.n + ', ' + lo + ' tot ' + hi + ' centimeter, voor '
          + (bed ? 'een ' + bedName + ' van ' + num.format(area) + ' vierkante meter' : 'een haag van ' + num.format(len) + ' meter')
          + (subOn ? ', met ' + words(bags, 'zak', 'zakken') + ' substraat' : ', zonder substraat') + ', samen ' + eur.format(total) + '.';
      }, 600);
    }

    each(['len', 'bd', 'bl', 'bw'], function (k) {
      field(k).addEventListener('input', function () { update(true); });
      field(k).addEventListener('blur', function () { update(false); });
    });
    each(root.querySelectorAll('[data-step]'), function (b) {
      b.addEventListener('click', function () { var k = b.getAttribute('data-for'); field(k).value = String(value(k) + parseFloat(b.getAttribute('data-step'))); update(false); });
    });
    each(root.querySelectorAll('input[type="radio"][data-c]'), function (el) { el.addEventListener('change', function () { update(false); }); });

    // into the cart: the button answers each time, and the line under it says what was added (owner, 23 Nov: no running
    // total, the bags would make it read 36 for 18 plants; the header cart shows the count). The line is emptied first so a
    // screen reader announces the same words again on a second tap.
    add.addEventListener('click', function () {
      var c = root._calc; inCart += c.n + c.bags;
      if (typeof window.tbCart === 'function') window.tbCart(inCart);
      var said = words(c.n, 'plant', 'planten') + (c.bags ? ' en ' + words(c.bags, 'zak', 'zakken') + ' substraat' : '') + ' toegevoegd aan uw winkelwagen.';
      status.textContent = '';
      setTimeout(function () { status.textContent = said; }, 60);
      add.textContent = 'Toegevoegd ✓'; add.classList.add('is-done');
      clearTimeout(addTimer);
      addTimer = setTimeout(function () { add.textContent = addText; add.classList.remove('is-done'); }, 2000);
    });

    // phone: a small bar with the total, only while the questions fill the upper part of the screen and the sheet is not in view
    var bar = root.querySelector('.sx-mini'), ask = root.querySelector('.sx-ask'), res = root.querySelector('[data-res]');
    if (bar && 'IntersectionObserver' in window) {
      var seen = { ask: false, res: false };
      var watch = function (el, key, margin) {
        new IntersectionObserver(function (es) { seen[key] = es[es.length - 1].isIntersecting; bar.classList.toggle('is-on', seen.ask && !seen.res); }, { rootMargin: margin }).observe(el);
      };
      watch(ask, 'ask', '-96px 0px -45% 0px'); watch(res, 'res', '0px 0px -10px 0px');
    }
    // a new width (the phone turned) only re-fits the measures; nothing typed is touched
    if ('ResizeObserver' in window) new ResizeObserver(stack).observe(root.querySelector('.sx-ask'));
    update(false);
  }
  each(document.querySelectorAll('.sx'), setup);
})();
