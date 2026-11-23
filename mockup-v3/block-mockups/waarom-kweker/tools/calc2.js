/* The plant calculator, second take (tools/calc2.py, tools/calc2.css). One script serves both directions: it reads the
   controls marked data-c and writes the results into the elements marked data-o inside each ".pc" block.
   Norms (a guideline, docs/normen-haag.md): plants per metre in one row, or per square metre, by size;
   one 40 L bag of substrate per plant. */
(function () {
  var PER_M = [2, 1.5, 1, 1];                       // a hedge: 40–60, 60–80, 80–100, 100–120 cm
  var PER_M2 = [3, 2, 1, 1];                        // a group or border
  var SIZES = ['40–60 cm', '60–80 cm', '80–100 cm', '100–120 cm'];
  var BAG = 14.95, MIN = 1, TOP = { len: 200, bl: 50, bw: 50 };
  var TIP = 'Kies een onderstreept woord om het aan te passen.';
  var eur = new Intl.NumberFormat('nl-NL', { style: 'currency', currency: 'EUR' });
  var num = new Intl.NumberFormat('nl-NL', { maximumFractionDigits: 1 });
  var inCart = 0;

  function each(list, fn) { Array.prototype.forEach.call(list, fn); }

  function setup(root) {
    var data = JSON.parse(root.getAttribute('data-soorten'));
    var status = root.querySelector('[data-o="status"]'), said = root.querySelector('[data-o="said"]');
    var photo = root.querySelector('[data-photo]'), timer;

    function field(key) { return root.querySelector('input[data-c="' + key + '"]'); }
    function pick(name) {
      var el = root.querySelector('select[data-c="' + name + '"]') || root.querySelector('input[data-c="' + name + '"]:checked');
      return el ? el.value : '';
    }
    function value(key) {
      var v = parseFloat(String(field(key).value).replace(',', '.'));
      if (isNaN(v)) v = MIN;
      return Math.min(TOP[key], Math.max(MIN, Math.round(v * 2) / 2));
    }
    function put(key, text) { each(root.querySelectorAll('[data-o="' + key + '"]'), function (el) { if (el.textContent !== text) el.textContent = text; }); }
    function fit(el) { el.style.width = Math.max(1, String(el.value).length) + 'ch'; }

    function update(typing) {
      var bed = pick('mode') === 'border', len = value('len'), L = value('bl'), W = value('bw'), area = L * W;
      var vi = parseInt(pick('var'), 10) || 0, si = parseInt(pick('size'), 10) || 0, v = data[vi];
      var subBox = root.querySelector('[data-c="sub"]'), subOn = !subBox || subBox.checked;
      var d = bed ? PER_M2[si] : PER_M[si];
      var n = Math.ceil((bed ? area : len) * d - 1e-9), price = v.p[si], plants = n * price, bags = subOn ? n : 0, bagSum = bags * BAG, total = plants + bagSum;
      if (!typing) { field('len').value = num.format(len); field('bl').value = num.format(L); field('bw').value = num.format(W); }
      each(['len', 'bl', 'bw'], function (k) { fit(field(k)); });
      each(root.querySelectorAll('[data-mode]'), function (el) { el.hidden = el.getAttribute('data-mode') !== (bed ? 'border' : 'haag'); });
      put('modeword', bed ? 'groep of border' : 'haag');
      put('n', String(n)); put('nword', n === 1 ? 'plant' : 'planten');
      put('var', v.n); put('size', SIZES[si]); put('each', eur.format(price)); put('plants', eur.format(plants));
      put('bagsum', subOn ? eur.format(bagSum) : '–'); put('total', eur.format(total));
      put('perm', num.format(d) + (d === 1 ? ' plant' : ' planten') + (bed ? ' per m²' : ' per meter') + ', om de ' + Math.round(100 / (bed ? Math.sqrt(d) : d)) + ' cm');
      var b = SIZES[si].replace(' cm', '').split('–');
      put('sizenote', 'U krijgt planten tussen ' + b[0] + ' en ' + b[1] + ' cm hoog, gemeten vanaf de kluit; de kluit telt niet mee.');
      each(root.querySelectorAll('[data-p]'), function (el) { el.textContent = eur.format(v.p[parseInt(el.getAttribute('data-p'), 10)]); });
      each(root.querySelectorAll('[data-dot]'), function (el) { el.style.background = v.c; });
      if (photo && photo.getAttribute('data-f') !== v.f) { photo.setAttribute('data-f', v.f); photo.src = 'img/' + v.f + '-2-sm.webp'; photo.style.objectPosition = v.o; }
      root._calc = { n: n, bags: bags };
      if (status) status.textContent = '';
      clearTimeout(timer);
      timer = setTimeout(function () {
        if (said) said.textContent = n + (n === 1 ? ' plant ' : ' planten ') + v.n + ' ' + SIZES[si] + ' voor ' + (bed ? 'een groep of border van ' + num.format(area) + ' vierkante meter' : 'een haag van ' + num.format(len) + ' meter') + ', samen ' + eur.format(total) + '.';
      }, 600);
    }

    // the sentence: an underlined word opens its choices under the sentence; one set at a time
    var words = root.querySelectorAll('[data-open]');
    function panel(key) { return root.querySelector('[data-panel="' + key + '"]'); }
    function open(key, focus) {
      each(words, function (w) {
        var on = w.getAttribute('data-open') === key && w.getAttribute('aria-expanded') !== 'true';
        w.setAttribute('aria-expanded', on ? 'true' : 'false'); panel(w.getAttribute('data-open')).hidden = !on;
        if (on && focus) { var c = panel(key).querySelector('input:checked') || panel(key).querySelector('input'); if (c) c.focus(); }
      });
    }
    function closeAll(back) {
      each(words, function (w) {
        if (w.getAttribute('aria-expanded') === 'true') { w.setAttribute('aria-expanded', 'false'); panel(w.getAttribute('data-open')).hidden = true; if (back) w.focus(); }
      });
    }
    each(words, function (w) { w.addEventListener('click', function () { open(w.getAttribute('data-open'), true); }); });
    each(root.querySelectorAll('[data-panel]'), function (p) {
      // a choice made with the pointer closes the set; with the arrow keys it stays open until Enter or Escape
      p.addEventListener('click', function (e) { if (e.detail > 0 && e.target.closest('label')) setTimeout(function () { closeAll(true); }, 0); });
      p.addEventListener('keydown', function (e) { if (e.key === 'Escape' || e.key === 'Enter') { e.preventDefault(); closeAll(true); } });
    });

    each(['len', 'bl', 'bw'], function (k) {
      var el = field(k);
      el.addEventListener('input', function () { update(true); });
      el.addEventListener('blur', function () { update(false); put('tip', TIP); });
      el.addEventListener('focus', function () { el.select(); if (words.length) { closeAll(false); put('tip', 'Van 1 tot ' + TOP[k] + ' meter, ook halve meters.'); } });
      el.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowUp' || e.key === 'ArrowDown') { e.preventDefault(); el.value = String(value(k) + (e.key === 'ArrowUp' ? 1 : -1)); update(false); }
        if (e.key === 'Enter') el.blur();
      });
    });
    each(root.querySelectorAll('[data-step]'), function (b) {
      b.addEventListener('click', function () { var k = b.getAttribute('data-for'); field(k).value = String(value(k) + parseFloat(b.getAttribute('data-step'))); update(false); });
    });
    each(root.querySelectorAll('[data-c="var"],[data-c="size"],[data-c="sub"],[data-c="mode"]'), function (el) { el.addEventListener('change', function () { update(false); }); });
    var add = root.querySelector('[data-add]');
    if (add) add.addEventListener('click', function () {
      var c = root._calc; inCart += c.n + c.bags;
      if (typeof window.tbCart === 'function') window.tbCart(inCart);
      if (status) status.textContent = c.n + (c.n === 1 ? ' plant' : ' planten') + (c.bags ? ' en ' + c.bags + (c.bags === 1 ? ' zak' : ' zakken') + ' substraat' : '') + ' in uw winkelwagen.';
    });
    update(false);
  }
  each(document.querySelectorAll('.pc'), setup);
})();
