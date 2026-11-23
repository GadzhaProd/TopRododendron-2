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

    // ---- colour: the chips' flow (tools/calc3.css, --sx-on of a variety): from the variety's soft colour through a light
    // cream into the sage, eased and mixed in OKLab so no grey middle appears. The same stops, as SVG gradient stops.
    function lab(hex) {
      var c = [1, 3, 5].map(function (k) { var v = parseInt(hex.substr(k, 2), 16) / 255; return v <= .04045 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); });
      var l = Math.cbrt(.4122214708 * c[0] + .5363325363 * c[1] + .0514459929 * c[2]), m = Math.cbrt(.2119034982 * c[0] + .6806995451 * c[1] + .1073969566 * c[2]), q = Math.cbrt(.0883024619 * c[0] + .2817188376 * c[1] + .6299787005 * c[2]);
      return [.2104542553 * l + .793617785 * m - .0040720468 * q, 1.9779984951 * l - 2.428592205 * m + .4505937099 * q, .0259040371 * l + .7827717662 * m - .808675766 * q];
    }
    function hex(o) {
      var l = Math.pow(o[0] + .3963377774 * o[1] + .2158037573 * o[2], 3), m = Math.pow(o[0] - .1055613458 * o[1] - .0638541728 * o[2], 3), q = Math.pow(o[0] - .0894841775 * o[1] - 1.291485548 * o[2], 3);
      return '#' + [4.0767416621 * l - 3.3077115913 * m + .2309699292 * q, -1.2684380046 * l + 2.6097574011 * m - .3413193965 * q, -.0041960863 * l - .7034186147 * m + 1.707614701 * q].map(function (v) {
        v = v <= .0031308 ? 12.92 * v : 1.055 * Math.pow(v, 1 / 2.4) - .055; return ('0' + Math.round(Math.min(1, Math.max(0, v)) * 255).toString(16)).slice(-2);
      }).join('');
    }
    function flow(glow) {
      var W = [1, 1, .98, .86, .63, .37, .14, .02, 0], a = lab(glow), b = lab('#f1ead4'), c = lab('#c9d4b5'), out = '';
      function mix(x, y, w) { return hex([x[0] * w + y[0] * (1 - w), x[1] * w + y[1] * (1 - w), x[2] * w + y[2] * (1 - w)]); }
      W.forEach(function (w, k) { out += '<stop offset="' + (.22 + k * .055).toFixed(2) + '" stop-color="' + mix(a, b, w) + '"/>'; });
      W.forEach(function (w, k) { if (k > 1) out += '<stop offset="' + (.56 + k * .055).toFixed(2) + '" stop-color="' + mix(b, c, w) + '"/>'; });
      return out;
    }

    // ---- the plants, drawn. A class on the block picks the drawing; every plant is one <use> of a symbol defined once.
    //   sx-k1 the chips' flow: a crisp mound (from the side) or circle (from above), the variety's soft colour flowing into the sage
    //   sx-k2 a planting plan: fine lines as on a garden architect's drawing, a scalloped outline tinted with the variety's colour
    //   sx-k3 our own photo of the variety, cut to a mound or a circle
    //   sx-kflat two plain circles (the first version, kept for comparison in the review)
    // view: 'side' (a hedge on the ground line y = 70) or 'top' (a bed); pts: the plants' centres; r: a plant's radius; v: the variety.
    function planting(view, pts, r, v, gap) {
      var m = root.className.match(/sx-k(\w+)/), kind = m ? m[1] : '3', id = 'sxg' + (++uid), top = view === 'top', sym, box, defs = '', out = '';
      var rgb = [1, 3, 5].map(function (k) { return parseInt(v.c.substr(k, 2), 16); }), pale = (rgb[0] * .299 + rgb[1] * .587 + rgb[2] * .114) > 215;
      var edge = ' stroke="#3f4a37" stroke-opacity="' + (pale ? '.7' : '0') + '" stroke-width="1" vector-effect="non-scaling-stroke"';
      var DOME = 'M-50,0 C-50,-36 -31,-70 0,-70 C31,-70 50,-36 50,0 Z';
      function f(x) { return x.toFixed(1); }
      if (kind === 'flat') {
        pts.forEach(function (p) { var y = top ? p[1] : 70 - r * .9; out += '<circle cx="' + f(p[0]) + '" cy="' + f(y) + '" r="' + f(r) + '" class="sx-bush"/><circle cx="' + f(p[0]) + '" cy="' + f(y) + '" r="' + f(r * .3) + '" fill="' + v.c + '" class="sx-bloom"/>'; });
        return out;
      }
      if (kind === '2') {
        // fine lines, as on a garden architect's planting plan: from above a scalloped ring with its centre marked, from the
        // side a plain mound with the trusses along its crown; the inside faintly tinted with the variety's colour
        var d = '', k, a, x, y, px, py, q, line = ' stroke="#3f4a37" stroke-opacity=".62" stroke-width="1" stroke-linejoin="round" vector-effect="non-scaling-stroke"';
        if (top) {
          for (k = 0; k <= 11; k++) {
            a = k / 11 * 2 * Math.PI; x = Math.cos(a) * 44; y = Math.sin(a) * 44;
            if (k) { q = Math.hypot(x - px, y - py) * .62; d += ' A' + f(q) + ' ' + f(q) + ' 0 0 1 ' + f(x) + ' ' + f(y); } else d = 'M' + f(x) + ' ' + f(y);
            px = x; py = y;
          }
          sym = '<path d="' + d + ' Z" fill="' + v.g + '" fill-opacity=".38"' + line + '/><circle r="7.5" fill="' + v.c + '"' + edge + '/>';
        } else {
          sym = '<path d="' + DOME + '" fill="' + v.g + '" fill-opacity=".3"' + line + '/>';
          [[-36, -31], [-21, -55], [0, -62], [21, -55], [36, -31]].forEach(function (t) { sym += '<circle cx="' + t[0] + '" cy="' + t[1] + '" r="3.8" fill="' + v.c + '"' + edge + '/>'; });
        }
      } else if (kind === '3') {
        // the variety's photo (already on the page for the assortment card), cut crisply. From the side the shrub's crown, a little
        // wider than the mound; from above the middle of its crown in a circle. Three cuts in turn, one mirrored,
        // so a row is not one stamp
        var bx = v.b, sw = bx[2] - bx[0], w = (top ? 150 : 134) / sw, h = w * 900 / 672, cut = top ? '<circle r="48"/>' : '<path d="' + DOME + '"/>', syms = '';
        var ix0 = -(bx[0] + sw / 2) * w, iy0 = top ? -(bx[1] + (bx[3] - bx[1]) * .42) * h : -73 - (bx[1] + (bx[3] - bx[1]) * .05) * h;
        [[-13, 0, 1], [11, -5, -1], [2, 4, 1]].forEach(function (t, k) {
          syms += '<symbol id="' + id + 's' + k + '" viewBox="' + (top ? '-50 -50 100 100' : '-52 -72 104 72') + '" preserveAspectRatio="none"><g clip-path="url(#' + id + 'c)">'
            + '<image href="img/' + v.f + '-2-sm.webp" x="' + f(ix0 + t[0]) + '" y="' + f(iy0 + t[1] * (top ? 3 : 1)) + '" width="' + f(w) + '" height="' + f(h) + '" preserveAspectRatio="none"'
            + (t[2] < 0 ? ' transform="translate(' + f(2 * (ix0 + t[0]) + w) + ' 0) scale(-1 1)"' : '') + '/></g></symbol>';
        });
        defs = '<clipPath id="' + id + 'c">' + cut + '</clipPath>' + syms;
        sym = null;
      } else {
        defs = (top ? '<radialGradient id="' + id + 'f" cx=".5" cy=".5" r=".5">' : '<radialGradient id="' + id + 'f" gradientUnits="userSpaceOnUse" cx="0" cy="-76" r="82" gradientTransform="translate(0 -76) scale(1.5 1) translate(0 76)">') + flow(v.g) + '</radialGradient>';
        sym = (top ? '<circle r="48"' : '<path d="' + DOME + '"') + ' fill="url(#' + id + 'f)"/>';
      }
      box = top ? '-50 -50 100 100' : '-52 -72 104 72';
      var bw = top ? r * 2 : Math.min(gap * .96, r * 2.3), bh = top ? r * 2 : bw * .74;
      pts.forEach(function (p, k) { out += '<use href="#' + id + 's' + (sym ? '' : k % 3) + '" x="' + f(p[0] - bw / 2) + '" y="' + f(top ? p[1] - r : 70 - bh) + '" width="' + f(bw) + '" height="' + f(bh) + '"/>'; });
      return '<defs>' + defs + (sym ? '<symbol id="' + id + 's" viewBox="' + box + '" preserveAspectRatio="none" overflow="visible">' + sym + '</symbol>' : '') + '</defs>' + out;
    }

    // a bed seen from above, with exactly n plants spread evenly inside its outline: a round or oval group on a sunflower
    // spiral (Vogel), a straight border in rows. Up to 8 by 6 metres is drawn; of a larger bed, that part with its own count.
    function drawBed(box, perM2, v, shape, L, W, n) {
      var round = shape !== 'recht', l = Math.min(L, 8), w = Math.min(W, shape === 'rond' ? 8 : 6), u = 100, part = L > l || W > w;
      var area = round ? Math.PI * l * w / 4 : l * w, cnt = part ? Math.ceil(area * perM2 - 1e-9) : n, r = Math.min(27, Math.sqrt(area / cnt) * u * .4), pts = [], k;
      // the labels: 14 px on screen, whether the drawing is held by the sheet's width or by its own greatest height (230 px)
      var fs = Math.ceil(14.8 * Math.max((l * u + 60) / Math.max(box.clientWidth, 1), (w * u + 40) / 230));
      if (round && cnt <= 36) {
        // a small group is planted in rings: one plant in the middle (from seven plants on) and rings around it, each ring with
        // plants in proportion to its length; the rings fill the outline
        var unit = [], dmin = 2, i2, j2, mid = cnt >= 7 ? 1 : 0, rings = 1, left = cnt - mid, ri, got = 0, sum;
        while (mid && 1 + 3 * rings * (rings + 1) < cnt) rings++;
        sum = rings * (rings + 1) / 2;
        if (mid || cnt === 1) unit.push([0, 0]);
        for (ri = 1; ri <= rings && cnt > 1; ri++) {
          var c2 = Math.max(0, ri === rings ? left - got : Math.round(left * ri / sum)), rho = mid ? ri / rings : cnt === 2 ? .5 : cnt < 5 ? .6 : .72, a0 = -Math.PI / 2 + (ri % 2 ? 0 : Math.PI / c2);
          got += c2;
          for (k = 0; k < c2; k++) unit.push([rho * Math.cos(a0 + k / c2 * 2 * Math.PI), rho * Math.sin(a0 + k / c2 * 2 * Math.PI)]);
        }
        for (i2 = 0; i2 < cnt; i2++) for (j2 = i2 + 1; j2 < cnt; j2++) dmin = Math.min(dmin, Math.hypot((unit[i2][0] - unit[j2][0]) * l, (unit[i2][1] - unit[j2][1]) * w) / Math.min(l, w));
        // a plant's radius: just under half the smallest distance between two plants, after leaving room for it at the rim
        var half = Math.min(l, w) * u / 2; r = Math.min(27, cnt === 1 ? half * .5 : .47 * dmin * half / (1 + .47 * dmin));
        unit.forEach(function (p) { pts.push([l * u / 2 + (l * u / 2 - r * 1.15) * p[0], w * u / 2 + (w * u / 2 - r * 1.15) * p[1]]); });
      } else if (round) {
        // planted in a triangle pattern (driehoeksverband), the most even spacing: of a triangular grid, the cnt plants nearest
        // the middle of the group, then the whole set fitted inside the outline with room for the outermost plants
        var step = Math.sqrt(area / cnt * 2 / Math.sqrt(3)), span = Math.ceil(Math.max(l, w) / step) + 2, all, far = 0, best = 9e9, ix2, iy2;
        // the grid may have a plant, the middle of a triangle or the middle of a side in the centre: the set that sits most
        // evenly round the middle wins (its centre of gravity first, then how compact it is)
        [[0, 0], [.5, Math.sqrt(3) / 6], [.5, 0]].forEach(function (o) {
          var set = [], reach = 0;
          for (iy2 = -span; iy2 <= span; iy2++) for (ix2 = -span; ix2 <= span; ix2++) {
            var gx = (ix2 + (iy2 % 2 ? .5 : 0) - o[0]) * step, gy = (iy2 * Math.sqrt(3) / 2 - o[1]) * step;
            set.push([gx, gy, Math.round((Math.pow(gx / (l / 2), 2) + Math.pow(gy / (w / 2), 2)) * 1e6)]);
          }
          set.sort(function (p, q) { return p[2] - q[2] || p[1] - q[1] || p[0] - q[0]; });
          var mx = 0, my = 0;
          set = set.slice(0, cnt); set.forEach(function (p) { reach = Math.max(reach, Math.sqrt(p[2] / 1e6)); mx += p[0] / cnt; my += p[1] / cnt; });
          var score = Math.hypot(mx, my) / step * 12 + reach * Math.min(l, w) / 2 / step;
          if (score < best - 1e-6) { best = score; far = reach; all = set; }
        });
        // the plants keep their true spacing when the group is full; they move inwards only as far as the outline asks
        r = Math.min(27, step * u * .44);
        var kx = far ? (l * u / 2 - r * 1.2) / (far * l * u / 2) : 1, ky = far ? (w * u / 2 - r * 1.2) / (far * w * u / 2) : 1;
        kx = Math.min(kx, 1.12); ky = Math.min(ky, 1.12);      // a nearly full outer row is drawn out to the outline, never squeezed past it
        r = Math.min(r, step * u * .44 * Math.min(kx, ky));
        all.forEach(function (p) { pts.push([l * u / 2 + p[0] * u * kx, w * u / 2 + p[1] * u * ky]); });
      } else {
        var ny = Math.max(1, Math.min(cnt, Math.round(Math.sqrt(cnt * w / l)))), base = Math.floor(cnt / ny), extra = cnt - base * ny, iy, ix, c;
        for (iy = 0; iy < ny; iy++) { c = base + (iy < extra ? 1 : 0); for (ix = 0; ix < c; ix++) pts.push([(ix + .5) * l * u / c, (iy + .5) * w * u / ny]); }
        r = Math.min(27, .46 * Math.min(l * u / (base + (extra ? 1 : 0)), w * u / ny));     // a plant fits its own cell
      }
      var line = round ? '<ellipse cx="' + l * u / 2 + '" cy="' + w * u / 2 + '" rx="' + l * u / 2 + '" ry="' + w * u / 2 + '" class="sx-bed"/>' : '<rect x="0" y="0" width="' + l * u + '" height="' + w * u + '" rx="10" class="sx-bed"/>';
      var out = planting('top', pts, r, v) + line + '<text x="' + l * u / 2 + '" y="' + (w * u + fs * 1.5) + '" text-anchor="middle" font-size="' + fs + '" class="sx-m">' + (shape === 'rond' ? '⌀ ' : '') + num.format(l) + ' m</text>'
        + (shape === 'rond' ? '' : '<text x="' + (l * u + fs * .6) + '" y="' + (w * u / 2 + fs * .35) + '" font-size="' + fs + '" class="sx-m">' + num.format(w) + ' m</text>');
      box.innerHTML = '<svg viewBox="-2 -2 ' + (l * u + (shape === 'rond' ? 4 : fs * 3.4)) + ' ' + (w * u + fs * 2.2) + '" aria-hidden="true" focusable="false" class="is-bed" data-n="' + pts.length + '">' + out + '</svg>';
      put('shown', !part ? '' : shape === 'rond' ? 'De tekening toont een deel van ' + num.format(l) + ' meter doorsnede.' : 'De tekening toont een deel van ' + num.format(l) + ' bij ' + num.format(w) + ' meter.');
    }
    function put(key, text) { each(root.querySelectorAll('[data-o="' + key + '"]'), function (el) { el.textContent = text; }); }

    // the hedge to scale: the plants along a metre rule. data-draw="fit" shows the whole hedge (up to 12 m), otherwise the first metres
    function draw(box, perM, v, len) {
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
      box.innerHTML = '<svg viewBox="-2 0 ' + (w + 4) + ' ' + (86 + fs) + '" aria-hidden="true" focusable="false" data-n="' + pts.length + '">' + planting('side', pts, r, v, gap) + s + '</svg>';
      put('shown', len > span ? 'De tekening toont de eerste ' + span + ' meter.' : '');
    }

    function update(fromInput) {
      var bed = mode() === 'border', len = length(), D = value('bd', 50), L = value('bl', 50), W = value('bw', 50), v = data[pick('var')], si = pick('size');
      // the bed's shape: a round group by its diameter, an oval one or a straight border by length and width
      var sh = root.querySelector('input[data-c="shape"]:checked'), shape = sh ? sh.value : 'recht', round = shape !== 'recht';
      var area = shape === 'rond' ? Math.PI * D * D / 4 : shape === 'ovaal' ? Math.PI * L * W / 4 : L * W;
      var subBox = root.querySelector('[data-c="sub"]'), subOn = !subBox || subBox.checked;
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
      each(root.querySelectorAll('[data-draw]'), function (box) { if (bed) drawBed(box, PER_M2[si], v, shape, shape === 'rond' ? D : L, shape === 'rond' ? D : W, n); else draw(box, PER_M[si], v, len); });
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
