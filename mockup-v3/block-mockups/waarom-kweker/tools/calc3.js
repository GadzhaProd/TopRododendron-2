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
  var inCart = 0, uid = 0;

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

    // The planting, drawn. A class on the block picks the treatment: sx-k1 discs · sx-k2 drawn shrubs · sx-k3 one hedge;
    // for reference sx-kflat (two plain circles) and sx-kglow (blurred spots, rejected by the owner as "soapy").
    // All of 1–3 are crisp shapes in pale sage tones; the flower's colour is a clear dot, outlined when it is as pale as the sheet.
    // view: 'side' (a hedge on the ground line y = 70) or 'top' (a bed); pts: the plants' centres; r: a plant's radius; g: the room.
    function planting(view, pts, r, colour, g) {
      var m = root.className.match(/sx-k(\w+)/), kind = m ? m[1] : '3', id = 'sxg' + (++uid), out = '', top = view === 'top';
      var rgb = [1, 3, 5].map(function (k) { return parseInt(colour.substr(k, 2), 16); }), pale = (rgb[0] * .299 + rgb[1] * .587 + rgb[2] * .114) > 215;
      var edge = pale ? ' stroke="#8a9a78" stroke-width="1" vector-effect="non-scaling-stroke"' : '';
      function f(v) { return v.toFixed(1); }
      function dot(x, y, q) {     // a blossom: one crisp dot of the flower's colour
        return '<circle cx="' + f(x) + '" cy="' + f(y) + '" r="' + f(q) + '" fill="' + colour + '"' + edge + '/>';
      }
      if (kind === 'flat') {
        pts.forEach(function (p) { var y = top ? p[1] : 70 - r * .9; out += '<circle cx="' + f(p[0]) + '" cy="' + f(y) + '" r="' + f(r) + '" class="sx-bush"/><circle cx="' + f(p[0]) + '" cy="' + f(y) + '" r="' + f(r * .3) + '" fill="' + colour + '" class="sx-bloom"/>'; });
        return out;
      }
      if (kind === 'glow') {
        pts.forEach(function (p) { var y = top ? p[1] : 70 - r * .9; out += '<circle cx="' + f(p[0]) + '" cy="' + f(y) + '" r="' + f(r * 1.7) + '" fill="url(#' + id + 'a)"/><circle cx="' + f(p[0]) + '" cy="' + f(y) + '" r="' + f(r * .7) + '" fill="url(#' + id + 'b)"/>'; });
        return '<defs><radialGradient id="' + id + 'a"><stop offset="0" stop-color="#8da578" stop-opacity=".95"/><stop offset=".48" stop-color="#a3b78c" stop-opacity=".72"/><stop offset="1" stop-color="#b9c8a0" stop-opacity="0"/></radialGradient>'
          + '<radialGradient id="' + id + 'b"><stop offset="0" stop-color="' + colour + '" stop-opacity=".88"/><stop offset=".42" stop-color="' + colour + '" stop-opacity=".52"/><stop offset="1" stop-color="' + colour + '" stop-opacity="0"/></radialGradient>'
          + '<clipPath id="' + id + 'c">' + (top ? '<rect x="0" y="0" width="' + g.w + '" height="' + g.h + '" rx="10"/>' : '<rect x="-60" y="-60" width="' + (g.w + 120) + '" height="130"/>') + '</clipPath></defs>'
          + '<g clip-path="url(#' + id + 'c)">' + out + '</g>';
      }
      if (kind === '1') {
        // discs: a crisp sage disc, lighter towards the upper left, and the flower in its middle
        pts.forEach(function (p) { var y = top ? p[1] : 70 - r; out += '<circle cx="' + f(p[0]) + '" cy="' + f(y) + '" r="' + f(r) + '" fill="url(#' + id + 'd)"/>' + dot(p[0], y, r * .34); });
        return '<defs><radialGradient id="' + id + 'd" cx=".34" cy=".3" r=".8"><stop offset="0" stop-color="#d9e1c9"/><stop offset="1" stop-color="#b3c29b"/></radialGradient></defs>' + out;
      }
      if (kind === '3') {
        // one planting: a hedge with a gently bumpy top (a bed: one planted field), a blossom or three per plant, and each plant marked
        if (top) {
          var q = Math.min(9, g.s * .17), x0 = pts[0][0] - g.s / 2, y0 = pts[0][1] - g.s / 2, x1 = pts[pts.length - 1][0] + g.s / 2, y1 = pts[pts.length - 1][1] + g.s / 2;
          out = '<rect x="' + f(x0) + '" y="' + f(y0) + '" width="' + f(x1 - x0) + '" height="' + f(y1 - y0) + '" rx="' + f(Math.min(22, g.s * .4)) + '" fill="#c6d2b1"/>';
          pts.forEach(function (p) { out += '<circle cx="' + f(p[0]) + '" cy="' + f(p[1]) + '" r="' + f(g.s * .36) + '" fill="#b1c099"/>' + dot(p[0], p[1], q); });
          return out;
        }
        var h = Math.min(50, Math.max(34, r * 1.8)), half = g.gap / 2, peak = 70 - h, dip = 70 - h * .76, a = pts[0][0] - half, b = pts[pts.length - 1][0] + half, d = 'M' + f(a) + ',70 L' + f(a) + ',' + f(dip + 8) + ' Q' + f(a) + ',' + f(dip) + ' ' + f(a + Math.min(8, half * .4)) + ',' + f(dip - 1);
        pts.forEach(function (p, k) {
          var l = k === 0 ? a + Math.min(8, half * .4) : p[0] - half, e = k === pts.length - 1 ? b - Math.min(8, half * .4) : p[0] + half;
          d += ' C' + f(l + (p[0] - l) * .4) + ',' + f(peak) + ' ' + f(p[0] - (p[0] - l) * .35) + ',' + f(peak) + ' ' + f(p[0]) + ',' + f(peak)
            + ' C' + f(p[0] + (e - p[0]) * .35) + ',' + f(peak) + ' ' + f(e - (e - p[0]) * .4) + ',' + f(peak) + ' ' + f(e) + ',' + f(k === pts.length - 1 ? dip - 1 : dip);
        });
        d += ' Q' + f(b) + ',' + f(dip) + ' ' + f(b) + ',' + f(dip + 8) + ' L' + f(b) + ',70 Z';
        out = '<path d="' + d + '" fill="url(#' + id + 'h)"/>';
        var q3 = Math.min(5, half * .18);
        pts.forEach(function (p, pk) {
          var o = pk % 2 ? [[-.5, .36], [-.02, .7], [.44, .5]] : [[-.44, .54], [.1, .76], [.52, .32]];
          out += dot(p[0] + half * o[0][0], 70 - h * o[0][1], q3) + dot(p[0] + half * o[1][0], 70 - h * o[1][1], q3) + dot(p[0] + half * o[2][0], 70 - h * o[2][1], q3)
            + '<circle cx="' + f(p[0]) + '" cy="70" r="2.6" fill="#3f4a37"/>';
        });
        return '<defs><linearGradient id="' + id + 'h" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#bfcca9"/><stop offset="1" stop-color="#a2b58a"/></linearGradient></defs>' + out;
      }
      // 2 · a drawn shrub, defined once and placed per plant: from the side a rounded mound in three sage tones with a few trusses;
      // from above a rosette of leaves with one truss in the middle
      var sym;
      if (top) {
        var leaves = '', k2;
        for (k2 = 0; k2 < 8; k2++) leaves += '<ellipse cx="0" cy="-27" rx="10.5" ry="20" fill="' + (k2 % 2 ? '#c9d5b6' : '#bac8a3') + '" transform="rotate(' + (k2 * 45) + ')"/>';
        sym = '<circle r="44" fill="#a9bb90"/>' + leaves + '<circle r="15" fill="' + colour + '"' + edge + '/>';
        pts.forEach(function (p) { out += '<use href="#' + id + 's" x="' + f(p[0] - r) + '" y="' + f(p[1] - r) + '" width="' + f(r * 2) + '" height="' + f(r * 2) + '"/>'; });
        return '<defs><symbol id="' + id + 's" viewBox="-50 -50 100 100">' + sym + '</symbol></defs>' + out;
      }
      var tr = [[-26, -26], [-4, -50], [20, -38], [32, -15], [-2, -20]], blooms = '';
      tr.forEach(function (t) { blooms += '<circle cx="' + t[0] + '" cy="' + t[1] + '" r="7.4" fill="' + colour + '"' + edge + '/>'; });
      sym = '<path d="M-52,0 C-56,-30 -40,-54 -20,-58 C-8,-74 16,-74 26,-56 C44,-50 56,-28 52,0 Z" fill="#b6c59e"/>'
        + '<path d="M-52,0 C-56,-30 -40,-54 -20,-58 C-8,-74 16,-74 26,-56 C8,-60 -14,-52 -24,-34 C-32,-20 -34,-8 -32,0 Z" fill="#c9d5b6"/>' + blooms;
      var bw = Math.min(g.gap * .98, r * 2.4), bh = bw * .7;
      pts.forEach(function (p) { out += '<use href="#' + id + 's" x="' + f(p[0] - bw / 2) + '" y="' + f(70 - bh) + '" width="' + f(bw) + '" height="' + f(bh) + '"/>'; });
      return '<defs><symbol id="' + id + 's" viewBox="-54 -76 108 76" preserveAspectRatio="none">' + sym + '</symbol></defs>' + out;
    }

    // a border seen from above: the plants on a grid at the guideline's spacing (up to 8 by 6 metres)
    function drawBed(box, perM2, colour, L, W) {
      var l = Math.min(L, 8), w = Math.min(W, 6), u = 100, s = 1 / Math.sqrt(perM2), r = Math.min(27, s * u * .4), out = '';
      var fs = Math.ceil((l * u + 60) / Math.max(box.clientWidth, 1) * 14);
      var pts = [];
      // whole rows and columns only, centred in the bed
      var nx = Math.max(1, Math.floor(l / s + 1e-9)), ny = Math.max(1, Math.floor(w / s + 1e-9)), ox = (l - nx * s) / 2, oy = (w - ny * s) / 2;
      for (var iy = 0; iy < ny; iy++) for (var ix = 0; ix < nx; ix++) {
        var x = ox + s / 2 + ix * s, y = oy + s / 2 + iy * s;
        pts.push([x * u, y * u]);
      }
      out += planting('top', pts, r, colour, { w: l * u, h: w * u, s: s * u }) + '<rect x="0" y="0" width="' + l * u + '" height="' + w * u + '" rx="10" class="sx-bed"/><text x="' + l * u / 2 + '" y="' + (w * u + fs * 1.5) + '" text-anchor="middle" font-size="' + fs + '" class="sx-m">' + num.format(l) + ' m</text>'
        + '<text x="' + (l * u + fs * .6) + '" y="' + (w * u / 2 + fs * .35) + '" font-size="' + fs + '" class="sx-m">' + num.format(w) + ' m</text>';
      box.innerHTML = '<svg viewBox="-2 -2 ' + (l * u + fs * 3.4) + ' ' + (w * u + fs * 2.2) + '" aria-hidden="true" focusable="false" class="is-bed">' + out + '</svg>';
      put('shown', (L > l || W > w) ? 'De tekening toont een deel van ' + num.format(l) + ' bij ' + num.format(w) + ' meter.' : '');
    }
    function put(key, text) { each(root.querySelectorAll('[data-o="' + key + '"]'), function (el) { el.textContent = text; }); }

    // the hedge to scale: the plants along a metre rule. data-draw="fit" shows the whole hedge (up to 12 m), otherwise the first metres
    function draw(box, perM, colour, len) {
      var fit = box.getAttribute('data-draw') === 'fit';
      var span = fit ? Math.min(12, Math.max(4, Math.ceil(len))) : (box.clientWidth < 520 ? 4 : 6);
      if (fit && box.clientWidth < 520) span = Math.min(span, 6);
      var metres = Math.min(len, span), mw = 100, w = span * mw, s = '', fs = Math.ceil(w / Math.max(box.clientWidth, 1) * 14);
      for (var m = 0; m <= span; m++) {
        s += '<line x1="' + (m * mw) + '" y1="70" x2="' + (m * mw) + '" y2="' + (m <= metres ? 80 : 75) + '" class="sx-tick"/>';
        if (m <= metres) s += '<text x="' + (m * mw + (m === 0 ? 1 : m === span ? -1 : 0)) + '" y="' + (82 + fs) + '" text-anchor="' + (m === 0 ? 'start' : m === span ? 'end' : 'middle') + '" font-size="' + fs + '" class="sx-m">' + m + ' m</text>';
      }
      s += '<line x1="0" y1="70" x2="' + w + '" y2="70" class="sx-ground"/>';
      var gap = mw / perM, r = Math.min(27, gap * .46), count = Math.ceil(metres * perM - 1e-9), pts = [];
      for (var k = 0; k < count; k++) {
        var x = gap / 2 + k * gap;
        if (x > metres * mw + .01) break;
        pts.push([x, 70]);
      }
      box.innerHTML = '<svg viewBox="-2 0 ' + (w + 4) + ' ' + (86 + fs) + '" aria-hidden="true" focusable="false">' + planting('side', pts, r, colour, { w: w, gap: gap }) + s + '</svg>';
      put('shown', len > span ? 'De tekening toont de eerste ' + span + ' meter.' : '');
    }

    function update(fromInput) {
      var bed = mode() === 'border', len = length(), L = value('bl', 50), W = value('bw', 50), area = L * W, v = data[pick('var')], si = pick('size');
      var subBox = root.querySelector('[data-c="sub"]'), subOn = !subBox || subBox.checked;
      var n = Math.ceil((bed ? area * PER_M2[si] : len * PER_M[si]) - 1e-9), price = v.p[si], plants = n * price, bags = subOn ? n : 0, bagSum = bags * BAG, total = plants + bagSum;
      if (!fromInput) { lenInput.value = num.format(len); field('bl').value = num.format(L); field('bw').value = num.format(W); }
      if (range) { range.value = Math.min(len, parseFloat(range.max)); range.style.setProperty('--sx-fill', ((range.value - range.min) / (range.max - range.min) * 100) + '%'); }
      each(root.querySelectorAll('[data-mode]'), function (el) { el.hidden = el.getAttribute('data-mode') !== (bed ? 'border' : 'haag'); });
      var what = bed ? num.format(area) + '\u00a0m²' : num.format(len) + '\u00a0meter';
      put('area', num.format(area)); put('h2', bed ? 'border' : 'haag'); put('what', what); put('title', (bed ? 'Uw border van ' : 'Uw haag van ') + what);
      put('len', num.format(len)); put('n', n); put('each', eur.format(price)); put('plants', eur.format(plants));
      put('bags', bags); put('bagsum', eur.format(bagSum)); put('total', eur.format(total));
      var b = SIZES[si].replace(' cm', '').split('–');
      put('sizenote', 'U krijgt planten tussen ' + b[0] + ' en ' + b[1] + '\u00a0cm hoog, gemeten vanaf de kluit; de kluit telt niet mee.');
      put('var', v.n); put('size', SIZES[si]); put('nword', n === 1 ? 'plant' : 'planten'); put('bword', bags === 1 ? 'zak' : 'zakken');
      var d = bed ? PER_M2[si] : PER_M[si];
      put('permlead', bed ? 'Richtlijn voor een border' : 'Richtlijn voor één rij');
      put('perm', num.format(d) + (d === 1 ? ' plant' : ' planten') + (bed ? ' per m²' : ' per meter') + ', om de ' + Math.round(100 / (bed ? Math.sqrt(d) : d)) + ' cm');
      each(root.querySelectorAll('[data-p]'), function (el) { el.textContent = eur.format(v.p[parseInt(el.getAttribute('data-p'), 10)]); });
      each(root.querySelectorAll('[data-row="sub"]'), function (el) { el.hidden = !subOn; });
      each(root.querySelectorAll('[data-draw]'), function (box) { if (bed) drawBed(box, PER_M2[si], v.c, L, W); else draw(box, PER_M[si], v.c, len); });
      root._calc = { n: n, bags: bags };
      if (status) status.textContent = '';
      clearTimeout(timer);
      timer = setTimeout(function () {
        if (said) said.textContent = n + (n === 1 ? ' plant' : ' planten') + ' ' + v.n + ' ' + SIZES[si] + ' voor ' + (bed ? 'een border van ' + num.format(area) + ' vierkante meter' : 'een haag van ' + num.format(len) + ' meter') + ', samen ' + eur.format(total) + '.';
      }, 600);
    }

    lenInput.addEventListener('input', function () { update(true); });
    lenInput.addEventListener('blur', function () { update(false); });
    each(['bl', 'bw'], function (k) { field(k).addEventListener('input', function () { update(true); }); field(k).addEventListener('blur', function () { update(false); }); });
    if (range) range.addEventListener('input', function () { lenInput.value = range.value; update(false); });
    each(root.querySelectorAll('[data-step]'), function (b) {
      b.addEventListener('click', function () { var k = b.getAttribute('data-for') || 'len'; field(k).value = String(value(k, k === 'len' ? MAX : 50) + parseFloat(b.getAttribute('data-step'))); update(false); });
    });
    each(root.querySelectorAll('[data-c="var"],[data-c="size"],[data-c="sub"],[data-c="mode"]'), function (el) { el.addEventListener('change', function () { update(false); }); });
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
