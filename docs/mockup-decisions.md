# Approved mockup decisions (to carry into the site code later)

Work goes block by block as mockups; the site code (`mockup-v3/src`) is changed only after a block is approved.

## Hero (first screen)

- Photo: the real white field photo `mockup-v3/src/assets/hero-field.jpg`, static, no video, no Ken Burns.
- Copy: H1 "Rhododendrons die aanslaan. Met aangroeigarantie.", the text and the two buttons. The eyebrow "Familiekwekerij · Otterlo, Veluwe · sinds 2001" is removed (owner, 6 Nov): "sinds 2001" lives in the trust bar.
- No dissolve of the photo into the next block.
- Scrim: variant 1 "Lichter" from `mockup-v3/block-mockups/hero-licht/` (shadow only behind the text, cleaner photo centre). AA measured on the photo at 360–1440 px.

```css
/* text column right edge: gutter + 36rem */
:root { --tc: calc(clamp(20px, 4vw, 64px) + 36rem); }

/* desktop and landscape tablets (replaces .hero-scrim-photo) */
.hero-scrim-photo {
  background:
    linear-gradient(to right, rgb(12 14 11 / .84) 0, rgb(12 14 11 / .74) calc(var(--tc) - 200px),
      rgb(12 14 11 / .56) var(--tc), rgb(12 14 11 / .2) calc(var(--tc) + 170px), transparent calc(var(--tc) + 320px)),
    linear-gradient(to top, rgb(12 14 11 / .22) 0%, transparent 24%);
}

/* phones: drop the full-screen 10% veil; dark base only behind the text block */
@media (max-width: 639px), (orientation: landscape) { /* the bg-black/10 veil */ background: transparent; }
/* phone bottom gradient (replaces h-[68%] from-black/90 via-black/72) */
height: 500px; max-height: 78%;
background: linear-gradient(to top, rgb(0 0 0 / .88) 0, rgb(0 0 0 / .76) 280px, rgb(0 0 0 / .62) 360px,
  rgb(0 0 0 / .28) 430px, transparent 500px);

/* tablets in portrait (replaces h-[62%] from-black/80 via-black/45) */
height: 62%;
background: linear-gradient(to bottom, rgb(0 0 0 / .82) 0%, rgb(0 0 0 / .6) 52%, rgb(0 0 0 / .25) 78%, transparent 100%);
```

## Trust bar under the hero — in progress

- Mockup: `mockup-v3/block-mockups/trustbar-linen/` (variants Lente / Туман / Карточка; owner leans to the light versions).
- Colours: 21st theme Linen Stone, light: bg #e9e4d8, card #f4efe4, text #2e2e2e, muted #5e5a52, line #d2cbbb; the bar itself dissolves into the page colour #f1efea (the photo is not faded).
- Icons: 21st "Animated Icon" library (Cojeev, id 37504), duotone treatment (stroke #2e2e2e 1.6, accent wash #8b9a7c at 30 %), organic leaf; package, calendar-days, leaf, circle-check.
- Facts: 10.000 planten op voorraad · Kwekerij sinds 2001 · 7 soorten, 4 maten · Vanaf 1 plant, geen minimumbestelling.
- Open: which of the three variants.

## Founder block "De kweker" — desktop approved (6 Nov)

- Mockup: `mockup-v3/block-mockups/waarom-kweker/` (lower block). Placed after "Hoe het werkt", separate from "Waarom wij".
- Approved by the owner on 6 Nov ("это мне уже нравится, зафиксируем"): commit cc5a1fc. Desktop and tablet (861 px and up) are fixed exactly as in that commit; asset `img/owner-portrait-ext.webp` (alpha baked in) is the source of truth for the code transfer.
- Base = the first glass version the owner liked: card columns .9fr / 1.1fr, radius 28px; card gradient #e0e1e3 → #d4d8cc → #c5cab2 → #aab696 with a pink glow rgba(224,198,209,.42) at 44% 96%; panel veil rgba(240,241,238,0 → .5 → .82).
- Owner's idea "дорисовать плечо": `img/owner-portrait-ext.webp` (1580×1418) = the original portrait plus 380 px drawn on at the right: backdrop continued, jacket/shoulder continued down to the bottom edge. Face and everything left of x≈1130 untouched. Used from 861 px up (`<picture>`); the phone keeps the original.
- Frame (6 Nov, owner: "чуть ниже, больше места подбородку и шее"): the original 1200 px part is 93.5 % of the card height wide, top cropped 3 % (just above the hair), bottom at 93.5 % of the image: chin, neck and collar have room. Card min-height = photo column width × 1.05.
- Shoulder (6 Nov, owner: "уголок на стыке", then "плечи как у дистрофика"): from x 1150 the jacket edge is one smooth curve that continues the original slope (0.35, easing to 0.5 at x 1400). This matches his left shoulder in the photo, which runs almost straight (~0.4) to the frame edge. The shoulder now leaves the card bottom at x ≈ 1488 of 1580 instead of dropping into the arm right after the old edge.
- Room for the shoulder under the buttons: panel padding-bottom = photo column × .17 (desktop), × .22 (1024–1199), × .30 (861–1023). Gap from button to shoulder is 35–63 px. On tablet the photo shifts left (×.75 of the overflow, never more than 12 % of its width, so the hair stays in frame).
- Dissolve: baked into the WebP alpha, no CSS mask: same fade as the first version (opaque to the original 78 % point, transparent by 84 % of the extended canvas), while the jacket keeps full opacity along its exact outline, so no wedge of backdrop is left above the shoulder. Panel veil starts after the shoulder tip so it stays dark: 0 until 20 % → .5 at 40 % → .82 (desktop); 34 % / 56 % (1024–1199); 44 % / 64 % (861–1023). Text contrast ≥ 6.2:1 on the darkest pixels.
- Copy (owner chose option A, 6 Nov): quote "Een gezonde plant is geen toeval. Dat is onze standaard."; H2 "Gert Top"; role "Oprichter van Top Rhododendrons"; text "Eén gewas; daardoor weten wij wat een rhododendron nodig heeft." (7 Nov: "sinds 2001" removed here to avoid repeating the Waarom wij facts row; the old site's own construction). Source: old site's groothandel page ("Familiebedrijf sinds 2001. Eén gewas; daardoor weten wij wat u nodig heeft.") and the photo alt ("oprichter"). Rejected: "Op ons eigen veld … rechtstreeks met Gert" (repeats Waarom wij). No role caption on the photo.
- Order in the panel (owner, 7 Nov): name "Gert Top" + role + text at the top, the quote at the bottom. The big "66" quote glyph is removed. Quote style approved (7 Nov): 2px moss rule on the left of the quote. Quote contrast ≥ 10.4:1.
- Phone tidy-up (7 Nov): the pink glow inside the phone panel ended in a hard edge under the photo; removed.
- Open: the owner saw a white strip, "криво обрезана", at the bottom left of the card in the DESKTOP version (not reproduced in Chromium: the photo reaches the card edge). The owner will re-check once the block is in the full mockup; fix then if it is still there.
- Phone, APPROVED 7 Nov: variant "Синяя" = the card in the jacket's navy (tones sampled from the portrait: lit #2f3a56, highlight #3f4d6c, shadow #0f1522; card #2c3653 → #232c45 → #1a2135). Photo full-bleed on top, the original photo (no extension). Only its last 10 % fades into the card (eased: 90 % opaque → 100 % transparent), well below the chin. Text starts 18 px below the photo. Rejected 7 Nov: drawing the photo on downward. The mirrored skin texture made the neck look reflected ("шея отзеркаливается, это баг"). The owner wants only a light transition. Three navy variants to compare in the review bar (7 Nov): 1 = first version (fade from 86 %, text pulled up 14 px); 2 = fade from 90 %, text 18 px below; 3 = phone portrait `img/owner-portrait-m.webp` (1200×1665, built by `tools/phone_portrait.py`, everything baked in, no CSS mask). Owner, 7 Nov, "на таком же уровне осветлить шею": the neck fades at the same level as the jacket. Owner, 7 Nov, "у шеи и воротника что-то рябит": the cause was the sharp, wrinkled neck texture meeting a perfectly smooth haze within ~30 px, plus light-blue collar bands running down. Fix: below the chin (from 88.5 %) the photo goes progressively soft (blur 0 → 12 px at the bottom edge, 17 px in the tail). Then each column's colour continues for 72 css px and fades into the card: the jacket smoothed wide, the collar strips replaced by the jacket, the neck muted (55 % skin / 45 % navy) and shorter. The lit chest in the last 5 % is calmed toward the same muted tone. Colour and blur only; no texture is copied, so nothing looks mirrored. Rejected 7 Nov: the neck arc keep-zone. The flat navy under the arc read as a blue spot next to the soft jacket, and the joins at the collars looked patched ("костыльно, не премиально"). APPROVED 7 Nov (owner reviewed both and chose v4: "нормально смотрится, берём её"): v4, one even treatment across the full width. Below the chin the photo goes progressively soft (0 → 8 px) and fades out from 89 % (smoothstep) over a broad gradient in the jacket's own tones (the bottom row with collar/neck replaced by the jacket, σ 160 px: lit left #2f3a57 → shadow right #141827). The gradient then fades into the card over 61 css px. Source: commit a17eb54, `img/owner-portrait-m.webp`, `tools/phone_portrait.py`. Tried and dropped: v5, the neck and collars kept whole down to an arc (commit 2622162). Owner, 7 Nov: "мало воздуха между текстом и портретом": the text block (name, role, text, quote) starts 56 px below the photo (was 18 px) and the card bottom padding is 34 px; the card is longer. Contrast ≥ 7.9:1 in all three. Light text: name #f5f2ea, role/text #c9cfdb, quote rule #a9b894. Contrast ≥ 8.2:1. The light card with the inset photo was the alternative; dropped.
- No buttons in this block (owner, 6 Nov: "пилюли тут не нужны"): "Bel Gert" and "WhatsApp" removed. Gap from the last text line to the shoulder: 53–77 px.
- If a cleaner extension is ever needed: redo the right 380 px with Photoshop Generative Expand on the original file.

## De kwekerij (block 2) — in progress

- Scheme C: text left, Gert's portrait right, quote card overlapping only the lower part of the photo (face never covered), no eyebrow, no "eigenaar", no CTA buttons.
- Copy: `mockup-v3/block-mockups/kweker-final/` (trimmed old-site copy).
- Open: background colour (21st palettes rejected), and whether the facts (10.000 planten · 7 soorten · vanaf 1 plant) return inside the block or are dropped.

## Rejected (do not offer again)

- 21st.dev colour themes for the block; the Royal Blue store skill (owner: work on our own concept C instead); the dissolve transition of the photo; the dark (charcoal) trust bar.

## Waarom wij — variant A chosen (7 Nov); final design = K (see the end of this file)

- Mockup: `mockup-v3/block-mockups/waarom-kweker/` (upper block). Owner chose A "Список" (numbered rows 01–04 on hairlines). B "Преимущества" (icon grid) is dropped, and so is the review bar. The owner will say how A should be designed.
- Copy: H2 "Wij kweken rhododendrons. Niet meer, niet minder."; lead "Onze planten groeien in de volle grond op veenrijke bodem en ontwikkelen daar een sterk wortelstelsel. Gerooid met kluit, direct van het veld naar uw tuin."; facts row 10.000 planten op voorraad / Sinds 2001 familiekwekerij in Otterlo / 7 soorten in 4 maten, 40 tot 120 cm / Vanaf 1 plant geen minimumbestelling.
- Rows: 01 Aangroeigarantie op elke plant; 02 Vers gerooid voor uw levering; 03 Persoonlijk advies van de kweker; 04 Eigen transport of afhalen.
- Row 03 text, for now (owner, 7 Nov): the old site's "De kweker helpt u persoonlijk, ma–za 09:00–17:00." (note "Ma–za 09:00–17:00"), replacing "U spreekt rechtstreeks met Gert, van vraag tot levering", which the owner disliked. May be rewritten later.
- "Sinds 2001" lives only here, in the facts row (removed from the founder text).
- Design, in review (8 Nov). Owner: no gradient over the whole block, only a separate card for the facts. Heading, lead and rows 01–04 stay on the page background (as variant A). The facts row (10.000 / Sinds 2001 / 7 soorten / Vanaf 1 plant) sits in its own gradient card: radius 24 px (20 on phone), 4 columns with hairline dividers (2×2 on phone).
  - Background: the `bs-soft-gradient-deck` skill technique, i.e. pastel radial blobs over a pale paper plus an SVG feTurbulence grain (opacity .38, overlay). Blob shapes are adapted to a wide, low card (tall ellipses at the corners, so they don't flatten into stripes); on phones there are corner ellipses.
  - 1 · Шалфей: paper #edefe6; blobs sage #b9c8a0, pink #e9c6d1, sage #c6d3b0, linen #eadabd.
  - 2 · Цветение: paper #f3eee5; blobs rhododendron pink #ecbcc9, lilac #d3c4e4, peach-linen #ecd0b2, sage #c6d3b3.
  - 3 · Мох (lighter and softer, owner 8 Nov): paper #3c4834; blobs #4f5e43 / #566449 / #46543d / #536148; light text #f8f6f0 / #e1e4d8; grain .22 soft-light.
  - Contrast measured on the pixels under each text: ≥ 6.3:1 in 1 and 2, ≥ 5.5:1 in 3. Against the pure blob colour at its peak (worst theoretical case): small labels 4.9:1 in 1 (#4c4b45 on #b9c8a0) and 4.9:1 in 3 (#e1e4d8 on #566449). That is still AA.
  - F · Бумага (independent design review, 8 Nov). The card is in the site's own card colour (#fbfaf8 on the #f1efea page) with a hairline border, one quiet sage wash bottom-right and a faint linen wash top-left, and light grain (.16, multiply). Values are in moss #3f4a37 at 26–38 px, a step below the H2 so the heading stays the lead. The right-hand notes on rows 01–04 are dropped (they repeated the row text). On phones the 2×2 grid becomes a ledger (value left, label right, hairlines; a 5th fact just adds a row). Contrast: moss values ≥ 6.9:1, labels ≥ 6.5:1.
  - Review points: the facts card at 44 px competed with the H2; palette 2's lilac/peach is foreign to the site palette; palette 3 repeats the rejected dark trust bar and makes a third dark block on phones (hero → moss → navy founder card); notes 01–04 duplicate the row text; phone wraps "40 tot 120 / cm" and "Vanaf 1 / plant" are now fixed with non-breaking spaces in all variants. Reviewer recommends hero 0 (full width) and F, else 1 without the pink corner.
  - M · Средний (owner, 8 Nov: "собери средний путь"): F's structure (moss values 26–38 px with tabular figures, row notes dropped, ledger rows on phones) on the Шалфей gradient without the pink corner. Paper #edefe6; blobs sage #b9c8a0, pale linen-sage #e3e3cc, sage #c6d3b0, linen #eadabd; grain .3 overlay. Contrast under the text ≥ 6.1:1 (pure blob peak: moss 5.3:1, labels 4.9:1). Default in the review bar; F, 1, 2 and 3 kept for comparison.
- Hero: stays full width as before (owner: "работаем так, как есть"). The option "A · Карточка" (hero as a rounded card of the same width) is still in the review bar for comparison. The full-block sheet option was dropped together with the full-block card.
- K · "Kaart naast de lijst" (design by the reviewer, 8 Nov; owner asked for 21st components + the soft-gradient skill). Split layout: rows 01–04 down the left under the H2; ONE portrait facts card on the right under the lead, as tall as the list. A tall card lets the skill's `.bg-warm` geometry (blobs at 8% 8% / 92% 12% / 20% 95% / 85% 90%) stay blobs. Palette: paper #eef0e8, sage #b9c8a0, linen #eadabd, pale sage #c6d3b0, the founder card's pink glow #e9cfd6; grain .32 overlay. Values moss 32–44 px, labels 15 px #3d3c37; numbers 01–04 in moss 12.5 px with letter-spacing; row notes dropped. ≤ 860 px: H2, lead, the card as a ledger, then the list. The page then alternates: facts card on the right, founder photo on the left.
  - 21st components: Editorial service list (37530), Split Feature Section (29418), Bold Stats (18908), Stats Section with Text (1195).
  - Contrast on real pixels: moss values ≥ 5.3:1, labels ≥ 6.3:1, list text ≥ 5.7:1. No horizontal scroll at 360/390/768/1024/1440.
  - Notes: the phone ledger uses subgrid (with a fallback). With a 5th fact the card would grow taller than the list on desktop.
  - In the mockup: review bar "Блок": K (default) or O (ours, with the gradient choices M/F/1/2/3). Section markup kept verbatim in `tools/waarom-kaart-section.html`.
- Owner, 8 Nov: the K facts card goes into work. The numbers 01–04 are removed ("не нужны, однозначно"). Lead placement is open, so the review bar has "Текст": R = on the right above the card (as designed); U = under the H2, with the card spanning the full height of the block on the right (desktop/tablet only; phones are stacked anyway). The owner also asked the reviewer to design the whole block, not only the card ("схитрил: задизайнил карточку и поменял местами"); in progress.
- B · "Bento met de kaart als anker" (the reviewer's whole-block design, 8 Nov). One composition on a 3-column lattice: two equal columns plus the card column (452 px), 20 px gaps. Top tier: H2 over the two tile columns, lead over the card column, aligned to the bottom. Bottom tier: the four reasons as 2×2 flat paper tiles (#fbfaf8, hairline border, radius 24) with a duotone icon on top (check = guarantee, leaf = freshly lifted, speech = advice, van = transport) and the text at the bottom. The K facts card is unchanged and spans both rows as the anchor tile; it is the only coloured, grainy object.
  - Lead stays on the right (it leads into the figures, and it gives the top tier the same columns as the bottom tier). Rhythm: flat tiles + warm card here, warm founder card below.
  - ≤ 860 px: H2, lead, card as a ledger, then the tiles (2×2 at 600–860, one column with the icon on the left on phones). No horizontal scroll at 360–1440.
  - 21st: Bento Feature Grid (26901), Feature Bento (18898), Feature Grid Spotlight Cards (26797), Animated Icon / Cojeev (37504) for the icon style; the card keeps Split Feature Section (29418) and Bold Stats (18908).
  - Contrast: card values ≥ 5.3:1, labels ≥ 6.3:1; tile titles 17.7:1, tile text 6.2:1, icons 17.7:1. Icons are hand-drawn inline SVG in the Lucide/Cojeev geometry; they can be swapped for library icons in code.
  - Note: earlier (6 Nov) the owner asked for no cards in Waarom wij and chose the list over the icon grid; B brings tiles and icons back on purpose, as a whole-block proposal.
  - In the mockup: review bar "Блок": B (default) / K / O. Section markup kept verbatim in `tools/waarom-bento-section.html`.
- 9 Nov, owner: "Fable поленился". The bento B redesigned only the tiles, reused the K card unchanged, and named 21st components without comparing any. New round: 16 searches on 21st.dev, 130 components reviewed on contact sheets (`scratchpad/c21/wy/review-*.jpg`). Three whole-block directions built, each a different composition; all share the eyebrow "Waarom wij" (soft-gradient skill), the K facts card as the single gradient/grain object, the site's duotone icons from the 21st Cojeev set (37504) for the reasons, and no numbers:
  - C · Центр, after 21st "About Us section" (2749). Centred eyebrow, H2 and lead. Below, three columns: two reasons on the left (right-aligned toward the card), the tall facts card in the middle, two reasons on the right, rows aligned. 861–1023 px: card on top as a ledger, reasons 2 + 2 below. Phone: head, card as a ledger, reasons as a list with icons.
  - P · Фото, after 21st "About Section" (6289), "Split Feature Section" (29418) and "Editorial service list" (37530). Left: eyebrow, H2, lead, then the reasons as a list with icons on hairlines. Right: a tall rounded photo of Cunningham's White (real product photo), with the facts card as a compact ledger overlapping its lower-left corner (soft shadow). Phone: head, photo with the card overlapping it, list.
  - R · Колонки, after 21st "Features" (10445) and "Feature Section with hover effects" (1521). Top: eyebrow, H2 and lead on the left; the facts card on the right as a 2×2 grid with hairlines (wider than tall, but blobs still read). Below: the four reasons in four open columns divided by vertical hairlines, icon on top (2 × 2 at ≤ 1100, list on phones).
  - No horizontal scroll at 360/390/1024/1440. Review bar "Блок": C (default) / P / R / B / K / O. Builder kept in `tools/waarom-three-directions.py`.

## Waarom wij — fresh redesign, 3 concepts (9 Nov)

The owner was lost among the variants. In his words, "the colour card is cool but lonely, not connected to anything", and "something is missing". A new designer (fresh reviewer, no prior variants) redesigned the block from scratch. The mockup page now shows ONLY these three concepts (review bar "Концепт"); all earlier variants (O/M/F/1–3, K, B, C, P, R) are removed from the page and remain in git history (commit 730b9ed and earlier). The header, hero and approved founder block are unchanged (verified identical).
- Starting question: right after the hero the visitor should feel "a field and the people who grow it, not a shop" and see why the guarantee is credible (open ground → roots → root ball).
- 1 · Veldkaart: left, eyebrow, H2, lead, and the four reasons as rows on hairlines (title | one line), no icons or numbers. Right, one tall card: a field photo (B2BHERO) that fades downward into the sage/linen grain gradient, with the four facts standing in that "soil". Same language as the founder glass card, so hero (full photo) → field card → founder (portrait in glass). Contrast ≥ 5.7:1. 21st: 37530, 19077. Reviewer's recommendation.
- 2 · Grondboek: typographic, no gradient, no photo. Four columns on hairlines; each column = a big moss figure plus one reason (10.000 → Vers gerooid; Sinds 2001 → Persoonlijk advies; 7 soorten → Aangroeigarantie; Vanaf 1 plant → Eigen transport). The reasons are reordered to match the figures. Contrast ≥ 5.7:1. 21st: 18908.
  - Caution: the figure-to-reason pairing is rhetorical, not factual (e.g. "7 soorten" does not prove the guarantee); keep the pairs visually independent or regroup before using.
- 3 · Drie in de rij: three equal tall panels in a row: Cunningham's White photo, the facts on the gradient, Nova Zembla photo (variety chips). Below, the four reasons in four columns on one hairline. The gradient takes its colours from the neighbouring photos. Contrast ≥ 5.5:1. 21st: 1195, 26797.
- All: no horizontal scroll at 360/390/1024/1440, static (no animation), real facts and photos only. Builder: `tools/waarom-fresh-build.py`.

## Waarom wij — bold sketches (9 Nov)

Owner on the three fresh concepts: "none surprised me, simple as doors, nothing catches the eye, looks like AI slop". Diagnosis: every round was assembled from SaaS component blocks and a slide skill around the same skeleton (H2, lead, 4 facts, 4 reasons) in beige on beige; nothing belonged only to this nursery. New rule: the eye-catcher must be something only Top Rhododendrons has (the colours of its 7 varieties, field, peat soil, root ball, Gert).
Mockup: `mockup-v3/block-mockups/waarom-schetsen/` (standalone sketches, one per section; phone-checked, not yet in the site page):
- 1 · Zeven soorten: the 7 real varieties as 7 tall arch-topped close-ups in a row (Cunningham's White, Nova Zembla, Catawbiense Boursault, Catawbiense Grandiflorum, Ponticum, Ponticum Roseum, Roseum Elegans; photos from the old site's images), headed "7 soorten in 4 maten, 40 tot 120 cm". Other facts in one quiet line, the 4 reasons in columns below. On phones the arches are a swipeable row.
- 2 · Boven en onder de grond: one wide plate. Above the ground line, the real Cunningham's White photo; below it, peat soil (the old site's tuinturf photo) with a drawn root ball (kluit) and roots. Callouts: Aangroeigarantie, 7 soorten in 4 maten, Volle grond / veenrijke bodem, Sterk wortelstelsel, Gerooid met kluit vlak voor uw levering. Shows why the guarantee holds. The roots are a generated line drawing; a real photo or an illustrator would be better for production.
- 3 · 10.000: the number set huge across the full width with the field photo inside the letters (background-clip), then "planten op voorraad, in de volle grond in Otterlo…", then H2 + lead and the reasons list. The number is decorative (aria-hidden); the same fact is in the text below.

## Waarom wij K — lead placement (9 Nov, readability review)

Recommendation: U (lead under the H2, the card on the right spanning the whole block), with fixes. Reasons:
- After the hero the eye enters top-left and reads H2 → lead → list (F pattern). In R the lead sits about 180 px away from the H2 and reads as a caption to the card.
- R line length breaks down at 1280/1024 (4 lines, 33–41 chars at 1024).
- In U, text changes only lengthen the left column; in R a 3-line H2 or a longer lead breaks the top alignment.

Fixes applied in `waarom-kweker/varianten.html` (K + U are now the default there):
- `.lp-u .wh2-lead{margin-top:24px;max-width:44ch}`: 3 lines of about 57/56/40 chars at 1440, 1280 and 1024, no orphan.
- `.lp-u .wh2-list{margin-top:clamp(44px,5vw,72px)}`.
- `.lp-u .wh2-facts{justify-content:center}`, `li{flex:0 0 auto;padding:clamp(26px,2.8vw,40px) 0}`, `b{font-size:clamp(36px,3.4vw,48px)}`: facts as a compact centred group instead of spread out.
- The card keeps the full height, from the top of the H2 to the last hairline of the list.

## Waarom wij — APPROVED: K with the lead under the heading (9 Nov)

Owner: "да, берём K, переноси в основной макет".
- Main mockup `mockup-v3/block-mockups/waarom-kweker/index.html` = header, hero (full width), Waarom wij K (lead under the H2, readability fixes above), placeholder for Assortiment / Hoe het werkt, founder block. No review bar. Built from `varianten.html` by `tools/finalize_main.py`.
- K, final: the H2 and, under it, the lead (max 44ch); then the four reasons as rows on hairlines (title + one line, no numbers, no icons). On the right, the soft-gradient facts card (paper #eef0e8; blobs sage #b9c8a0, linen #eadabd, pale sage #c6d3b0, pink glow #e9cfd6; grain .32 overlay), as tall as the whole block, facts grouped in the middle, values in moss clamp(36px,3.4vw,48px). Phones: H2, lead, card as a ledger, list.
- Checks: no horizontal scroll at 360/390/768/1024/1440. Contrast on real pixels: card values ≥ 6.1:1, labels ≥ 8.0:1, list text 5.7:1, lead 8.5:1.
- Kept for reference: `varianten.html` (all earlier variants, K + U as default) and `concepten.html` (the three fresh concepts). `waarom-schetsen/` holds the bold sketches.
- For the code transfer: the page CSS still carries rules for the earlier variants (O/M/F/1–3, bento, C/P/R) that this page no longer uses; transfer only the K rules (`.wh2-*`, `.wh-grain`, `.lp-u`).

## Waarom wij K — colour treatments for the facts card (9 Nov): «Поле» approved

Owner: the block is approved, but he wants to work further on the card's colours and blur in a separate mockup (not the main one). Separate page: `waarom-kweker/kaart.html` (copy of the main mockup; only the card CSS differs; review bar: 0–3, class `k-0…k-3`). All values stay moss #3f4a37; contrast is measured on real pixels.
- 0 · Сейчас: the approved card (sage, linen, pale sage, pink glow). Min contrast 6.07 / 5.90 (1440 / 390).
- 1 · Поле: colours sampled from the hero photo and laid out like it: flower light at the top, foliage on the left, the sandy path along the bottom, a faint bud blush. Paper #ebece3; foliage #adbb98 / #c2cca9; light #f1f0e8; sand #d9cbb0 → #c7b893; blush #ecd6d2; base #e8e3d4; grain .32 overlay. Min 5.61 / 5.43. The reviewer's recommendation: it ties the card to the hero photo.
- 2 · Стекло: the founder card's language, so the two cards read as a pair: a vertical grey-sage gradient (#e6e7e8 → #dcdfd5 → #d0d5c1 → #c4ccb1), a pink glow at the bottom, a white highlight top-left, a 1 px white inner edge, two blur depths; grain .20 soft-light. Min 6.20 / 5.92.
- 3 · Цветение: the seven varieties' colours, lightened, gathered into a soft bloom at the bottom right, with foliage holding the left. Paper #ecefe6; foliage #b3c19f / #c3ceac; white #eff0ea; pink #e7ccd5; Nova Zembla core #e2bec8; lilac #dfd2e0; lavender #dcd8e6; grain .30. Min 5.57 / 5.89. The reviewer notes it is the closest to the lilac gradients rejected earlier.
- APPROVED (owner, 9 Nov: "берём Поле, переноси в основной макет"): 1 · Поле is now the card in the main mockup. Its CSS is in `tools/card-veld.css`; `tools/finalize_main.py` appends it to the page. The main card renders pixel-identical to variant 1 on `kaart.html` at 1440/1024/390/360. No horizontal scroll. Contrast min 5.61:1 (desktop) / 5.43:1 (phone).

## Hero — text block bottom-left (9 Nov): APPROVED

Owner: move the hero text block (H1, paragraph, buttons) lower, toward the bottom-left corner, but not stuck to it; the designer decides the exact layout. Approved: "да, переноси в основной макет".
- Desktop and landscape tablets (`split`): `justify-content:flex-end`; left edge on the container gutter as before; bottom padding = max(48px, gutter × 1.25): 51 px at 1024, 64 at 1280, 68 at 1366, 72 at 1440, 80 at 1920. Top padding 7rem as a safety margin under the header. At least 280 px to the header even at 1366×768.
- Why: the top of the photo (forest, far rows) stays clean; the big flower cluster stays the focal point; the eye runs forest → cluster → H1 → buttons → next section.
- Scrim: the same text-column gradient, now masked to the bottom (full in the lower 54 %, gone by 94 %). Edges .80 / .72 / .62 at `--tc`, bottom band .24 → 26 %.
- Contrast on real pixels: paragraph 5.45–5.80:1, H1 5.45–5.65:1. Before the change the paragraph dipped to 4.18–4.52:1 on a few pixels at 1024–1440.
- Phones and portrait tablets unchanged: on phones the text was already at the bottom; on portrait tablets it stays at the top on the dark forest band (moving it down would mean darkening the big white cluster).
- CSS: `waarom-kweker/tools/hero-bottom-left.css`, appended by `tools/finalize_main.py`. Main mockup renders pixel-identical to the preview `hero-onder.html` at 360–1920. For the code transfer: replace `split:justify-center` with `split:justify-end` and set the padding instead of the override.
- H1 on wide screens (owner, 9 Nov: "3 строки"): from about 1600 px the H1 (72 px) wrapped to 4 lines in the 36rem column. At ≥ 1600 px the H1 column is now 40rem and the scrim's text-column edge `--tc` moves with it (in `tools/hero-bottom-left.css`). Result: 3 lines at every width checked, 1024–2560 ("Rhododendrons / die aanslaan. Met / aangroeigarantie."; up to 1366 "Rhododendrons die / aanslaan. Met / aangroeigarantie."). The paragraph width is unchanged, there is no horizontal scroll, and contrast stays above AA.

## Waarom wij — critic round (9 Nov), in review

An outside critic said the approved K "reads more like an information section than an explanation of why a buyer should choose Top Rhododendrons" and sent a mock (eyebrow "Waarom Top Rhododendrons", H2 "Rechtstreeks van de kweker. Sterk vanaf de wortel.", a root-ball photo with a tractor, three icon cards, a facts row). An independent review (Fable) and my own review agree on the diagnosis:
- the H2 is about us, not the buyer;
- the lead repeats the hero;
- the facts card takes the strongest spot;
- the guarantee is not emphasised;
- on phones the reasons come after the facts.

Not usable as is:
- the critic's photo is very likely generated (a perfectly round ball with thick woody roots; rhododendrons have fine, shallow roots), which breaks the real-photos rule;
- it repeats the hero even more;
- it drops personal advice and own transport;
- it overstates the facts: "10.000+", and the guarantee without "first season" / "kosteloos";
- "Rechtstreeks" hints at "no middlemen";
- its icons are generic.

Variants on a separate page `waarom-kweker/kritiek.html` (built by `tools/build_kritiek.py` from the main mockup; review bar 0–4). Shared new copy in 1–4 (draft):
- eyebrow "Waarom Top Rhododendrons";
- H2 "Wij kweken alleen rhododendrons. Dat merkt u aan elke plant.";
- lead "Een familiekwekerij in Otterlo, gericht op één gewas. Voor uw tuin of uw project kiest u uit eigen kweek, met advies van de kweker zelf." (no hero repeat);
- the guarantee first and emphasised; all four real reasons and exact wording kept.

The variants:
- 0 · Сейчас: the approved K.
- 1 · Текст: K layout and the field card kept; new copy; the guarantee row gets a duotone check and moss title; on phones the reasons come before the card.
- 2 · Фото: the critic's structure with a real photo. Head left, the Cunningham's White bush right (img/cw-bush.webp, from the old site); four soft tiles (the guarantee tile on the field gradient + grain); a facts strip at the bottom.
- 3 · Герт: as 2 with Gert's portrait and his quote in the head. The separate founder block is hidden in this variant (could be dropped if chosen).
- 4 · Карточка Герта: the approved founder card placed inside this block, between the head and the tiles; the separate founder block is hidden.

Checks: no horizontal scroll at 360/390/1024/1440. Contrast on real pixels ≥ 5.6:1, guarantee tile title 6.0:1.
- 5 · Герт + преимущества (owner's idea, 9 Nov): the approved founder card keeps only the name and role ("Gert Top", "Oprichter van Top Rhododendrons"); the four reasons sit inside the same card on hairlines (the guarantee first, with a check, in moss), and the facts strip is below. Quote and the "Eén gewas" line are dropped. The separate founder block is hidden. The phone uses the navy card with light reasons. The card grows to 681 px at 1440. Text-to-shoulder clearance is ≥ 34 px at 900–1440. Contrast on real pixels: reason text ≥ 5.9:1, titles ≥ 6.5:1.
  - 5, revised (owner, 9 Nov): the check icon is removed (the guarantee title stays moss); the lead moves under the H2 (nothing top-right, max 44ch); at ≥ 1200 px the card text starts further left (panel padding-left clamp(8px,1vw,20px)) and the reason lines may run wider, because the right half of the panel was empty. The card is now 636 px at 1440. Shoulder clearance is ≥ 32 px.
  - 5, review point 1 (owner, 9 Nov): Gert's quote "Een gezonde plant is geen toeval. Dat is onze standaard." returns under the role, before the reasons (19–22 px, moss rule), linking portrait and list. The name steps down to clamp(32px,2.8vw,40px) (30 px on phones), so the card no longer reads as a business card. More bottom room in the panel keeps the last reason clear of the shoulder (≥ 33 px at 900–1440): padding-bottom colw × .21 (≥ 1200), .32 (1024–1199), .44 (861–1023). The card is 716 px at 1440. Contrast: quote ≥ 10.5:1, reason text ≥ 5.4:1.
  - 5, review point 2 (owner, 9 Nov: "подключаем 21st и Impeccable как дизайнеров"): three ways to lead with the guarantee without an icon (review bar "Гарантия"). The guarantee title is now ink instead of moss, which read paler than its neighbours.
    - A · Шрифт: Impeccable's rule that emphasis comes from size, weight and rhythm. Title clamp(20px,1.7vw,24px), its line 15–16.5 px #2f2e2a, more air after the row.
    - B · Полоса: after the 21st component 27506 "Feature List Showcase" (the active row on a soft tint). The guarantee row sits on a light wash in the field colours, radius 14 px.
    - C · Линия: the reviewer's 2 px moss rule on the left. Impeccable lists coloured side rules above 1 px as a category default.
    - More bottom room keeps every option ≥ 40 px from the shoulder: padding-bottom colw × .24 (≥ 1200), .32 (1024–1199), .54 (861–1023). The card is now about 735–757 px at 1440. Contrast: guarantee title ≥ 8.8:1, its line ≥ 6.2:1.
    - Impeccable's other flags, not acted on and left for the owner: it bans eyebrows above headings ("Waarom Top Rhododendrons"), and it lists "big number + small label" fact strips as a category default.
    - Impeccable is installed as a Claude Code skill (`~/.claude/skills/impeccable`, v4.8.2, from github.com/pbakaus/impeccable). Its engine binary (detector, context loader) was not run: it downloads code, and auto mode blocked that. The skill's playbooks (layout, craft-floor) were used directly.
  - 5, quote one step quieter (owner, 9 Nov): the quote is now clamp(17px,1.25vw,19px), weight 400, #2f2e2a (#eef0f4 on the phone's navy card). Order of weight: name, guarantee title, quote, other reasons. Contrast ≥ 9.6:1. Shoulder clearance ≥ 41 px.
  - 5, quote on one line (owner, 9 Nov): at ≥ 1200 px the quote runs on one line (nowrap, max-width none; it fits at 1200–1920); below 1200 it wraps to two lines as before.
  - 5, shorter copy (owner, 9 Nov, after the density review: "сократи текст и сразу убирай «Waarom Top Rhododendrons»"):
    - eyebrow removed;
    - lead cut to "Voor uw tuin of uw project kiest u uit eigen kweek.";
    - reason lines shortened, facts unchanged: Vers gerooid → "Wij rooien pas vlak voor uw levering."; Persoonlijk advies → "Ma–za 09:00–17:00."; Eigen transport of afhalen → "Bezorgd door heel Nederland.";
    - guarantee line, name, role ("Oprichter van Top Rhododendrons", kept because the eyebrow is gone), quote and facts strip unchanged.

    About 100 words instead of 140. Panel padding-bottom at ≥ 1200 px is colw × .20. Card 702 px at 1440 (was 726); on phones 979 px (was 1063). Shoulder clearance ≥ 32 px. The face is still about 85–90 % of the card height (the next step per the review: draw on a soft background above the head).
  - 5, review points 1–2 (owner, 10 Nov: "делай пункты 1 и 2, цитату средний вариант"):
    - Portrait: at ≥ 1200 px the photo column is about 36 % (grid .72fr / 1.28fr). The portrait is 72 % of the card height (--w:72cqh), anchored to the bottom with the same chin and neck crop, and its top fades into the card (mask 0 → 16 %), whose top colour matches the portrait backdrop. The head is about 66 % of the card height, with about 200 px of air above the hair. Tablets keep a wider column so the face is never cropped: 1024–1199 .9fr / 1.1fr; 861–1023 1fr / 1fr with --w 66cqh. Card 696 px at 1440, 635 at 1024. Shoulder clearance ≥ 33 px. The phone portrait is unchanged.
    - Text: reason titles clamp(17px,1.4vw,20px); lines clamp(15px,1.12vw,16px) #2f2e2a; guarantee title (A) clamp(22px,1.95vw,28px), its line up to 17 px. Quote (the middle option): clamp(18px,1.4vw,20px), #262521, one line on desktop. Contrast ≥ 7.2:1.
    - Copy: guarantee "Slaat een plant in het eerste seizoen niet aan? Dan vervangen wij hem kosteloos." Transport line restored: "Bezorgd door heel Nederland, of af te halen in Otterlo."
  - 5, hair (owner, 10 Nov: "убрать дымку с волос, на макушке она залазит на волосы"): the top fade is now an inline alpha mask (395×354, data URI). It fades the photo's top over 18 % but keeps the head fully opaque; the matte is taken from the portrait itself (pixels darker than the backdrop), dilated about 12 px and feathered. The backdrop dissolves around the crown, not over it. Hair pixels vs the unmasked photo: 99th percentile difference 6.7/255, i.e. visually identical. (A plain short fade ending at 3 % also cleared the hair but left a visible light band above the head; a mask loaded from a separate file did not render from file://, hence the inline data URI.)
  - 5, desktop text layout by the reviewer (10 Nov; owner: "в веб версии что-то не то"). Diagnosis:
    - the text column sat right against the face, with empty space on its right (the rules ran 770 px, the longest text 625 px);
    - the column hung at the top (58 px above, 95 px below, the list ending on a floating rule);
    - blurred type steps (quote = reason titles; fact numbers 37 vs name 40; the lead at 17.5 under a 58 H2);
    - spacing without a scale.

    Fix (`tools/fable-layout.css`, applied under html.fl-y; the review bar "Текст": Fable / Было):
    - The text column starts at 5/12 of the container (610 px at 1440) with 64 px insets on top, right and bottom, and is vertically centred.
    - The list ends on text (no last rule).
    - Type scale 58 / 40 / 28 / 20 / 16: the lead, quote and reason titles are 20; all small text is 16; fact numbers are 28.
    - Spacing scale 8 · 16 · 24 · 32 · 64: lead 24 px under the H2, card 64 px lower, facts 40 px under the card.
    - Bottom inset 80 px at 1200–1365 px. Tablets 861–1199: 48 px insets, same scale.

    Card 651 px at 1440 (was 696). Shoulder clearance ≥ 38 px. Worst contrast 5.66:1. Phone unchanged (pixel-identical). Optional html.fl-l1 puts the first fact under the portrait and the others on the text line (not recommended). The comparison page renders pixel-identical to the reviewer's copy at 390–1440.
  - APPROVED (owner, 10 Nov: "расстановку утверждаем"): the reviewer's desktop text layout (fl-y) for variant 5.
  - Guarantee emphasis, final round, on the approved layout: A · Шрифт (title 28 px step, no decoration) vs B · Полоса (the same title on a soft field-colour band; band inset 24 px with −24 px margins so the text stays on the column line; radius 16; line 16 px). B: shoulder ≥ 33 px, contrast ≥ 6.6:1. The reviewer is asked to pick the stronger one, or propose another.
  - Reviewer's pick (10 Nov): A · Шрифт. The guarantee leads through hierarchy, not decoration; the list keeps its rhythm; the glass stays the only coloured surface; it works the same at every width and the phone hierarchy is stronger than with B. B reads as a promo "plate within a plate", the band's second gradient looks muddy over the glass, it comes closer to the portrait at 1024, and its contrast depends on the gradient. Checks on A (lightest pixels): reason lines ≥ 9.1:1, role ≥ 7.7:1, fact labels 5.66:1.
  - Guarantee line wrapping: it now breaks after the question below 1280 px ("…seizoen niet aan? / Dan vervangen wij hem kosteloos."), never inside "niet aan" (nb span + a br shown at ≤ 1279 px). It stays on one line at ≥ 1280.
  - Quote on the band (owner, 10 Nov: "как B, только цитату взять в эту карточку"): html.q-b puts Gert's quote on the soft field-colour band (radius 16, 20/24 px inset, −24 px margins so the text stays on the column line; on the phone a light 9 % wash on the navy) instead of the moss rule. The guarantee keeps A. Review bar "Цитата": Линия / Карточка (default Карточка for review). Shoulder clearance ≥ 31 px, no horizontal scroll.
  - Reviewer's pick for the quote (10 Nov): Линия (the 2 px moss rule). The hierarchy reads name → quote → guarantee → reasons; the quote stays Gert's voice rather than a block; there is a single surface (the glass). The band made the quote the loudest spot (against the owner's "quieter quote"), repeated the rejected "plate within a plate", added a second gradient and a second alignment axis, made the card about 32 px taller, and looked like a chat bubble on the phone. Default on the page is back to Линия. Optional polish noted by the reviewer (not applied): a lighter rule, or a hanging rule so the quote text sits on the column line (check shoulder clearance).
  - Quote polish applied (owner, 10 Nov; html.qp-y; review bar "Правки": До / После). At ≥ 861 px the rule is site sage #8b9a7c (was dark moss #3f4a37) and hangs 22 px into the margin (2 px, rounded), so the quote text sits on the same column line as the name and the reasons (552 px at 1440; it was 26 px further right). The card height and shoulder clearance are unchanged. The phone keeps its light rule.
  - Reviewer on the polish (10 Nov): "После" is better. Before, the quote created a second left edge (26 px in) and the eye tripped on it. After, every line of text sits on one edge, and the rule hangs in the margin like hanging punctuation or list markers; the eye aligns on the text mass, not the thin mark. The site-sage rule was too faint (the quote read as a third line under the role), so the rule is now #6b7a5e, between the dark moss and the sage; 2 px, 22 px hang unchanged.
Next best asset: a real photo of a lifted rhododendron with its root ball, shot at the nursery.

## Waarom wij — APPROVED: K with new copy (10 Nov)

The owner's UX friend (senior) preferred the main mockup's K: "reads easily, bright card, accented numbers". The outside critic's point (reads like information, not "why us") is addressed with copy and order only, keeping K's layout, the field card and its large numbers.
- Owner: "Да, давай утверждаем" (10 Nov). Now in the main mockup `waarom-kweker/index.html`: `tools/finalize_main.py` applies the copy changes, and `tools/k-tekst.css` holds the layout rules. Review page kept as `waarom-kweker/k-tekst.html` (snapshot; `tools/build_k_tekst.py` only rebuilds it from the pre-approval index).
- H2 "Wij kweken alleen rhododendrons. Dat merkt u aan elke plant."
- The lead is removed: it repeated the hero. The list follows the H2 directly.
- Second review fixes (Fable, approved): "Vers gerooid" line ends "…en rooien uw planten pas vlak daarvoor, met kluit." (the root ball was only in the removed lead; the hero has veenrijke bodem and sterk wortelstelsel). Phones: the second H2 sentence starts on its own line (`.nb{display:block}` ≤860 px), 4 lines at 360/390; desktop stays at 3 lines.
- Guarantee first and larger: title clamp(26px,2.6vw,36px), line "Slaat een plant in het eerste seizoen niet aan? Dan vervangen wij hem kosteloos." at 16–17.5 px #2f2e2a. The other reasons are unchanged.
- Phones: the reasons come before the facts card.
- The founder block stays separate below, as approved. Variant 5 (Gert inside this block) remains on `kritiek.html`.
- No horizontal scroll at 360/390/1024/1440/1920.
- For the code transfer: the lead rule `.wh2-lead` is no longer used by K.

## Founder block, phone — new card treatments (10 Nov), in review

Owner: the navy phone card was made before the soft-gradient card style existed; redo the part the photo melts into, and as a second variant show the photo and the card as two separate parts. Desktop unchanged (pixel-identical).
- Page: `waarom-kweker/fd-telefoon.html`, built from `index.html` by `tools/build_fd_telefoon.py`. Review bar: 0 · Сейчас (approved navy v4), 1 · Накладка, 2 · Две части; colour Синий / Поле.
- 1 · Накладка: the same v4 phone photo melts into a navy soft-gradient card with grain (lit dusty blue under the photo, moss glow bottom-left, heather glow right; grain .26 overlay, not on the photo). Navy only: a light card under the dark jacket was tried and dropped, the jacket fades into it only through a grey haze band.
- 2 · Две части: the original photo (1200×1418, no fade) with 22 px corners, a 10 px gap, then the text card with the same corners. Синий = navy soft gradient; Поле = the Waarom wij facts card palette.
- Contrast on real pixels at 360/390: every text ≥ 6.1:1. No horizontal scroll.
- Fable's own phone designs (10 Nov), on `waarom-kweker/fd-fable.html`, built by `tools/build_fd_fable.py` (also builds `img/fd-fable-portrait-top.webp` and `img/fd-fable-portrait-bust.webp` from the real portrait: only the photo's own plain background is extended upward). Review bar: 0 · Сейчас, 1 · Обложка, 2 · Разворот, 3 · Подпись.
  - 1 · Обложка: one card, light at the top and navy at the bottom; the name (64 px) sits above the head on the extended photo background; the jacket melts into navy as in v4; the quote is at the bottom on navy. Lowest contrast 8.4:1.
  - 2 · Разворот: the name in two lines on the left with the portrait as a tile in the top-right corner, then the line and a large quote full width; the sage card as on desktop; about 460 px tall instead of 765. Original photo, no fades. Lowest contrast 7.4:1.
  - 3 · Подпись: an all-light card; text and quote first, then Gert rising from the bottom edge, the jacket cut by the card edge as on desktop. Lowest contrast 7.8:1.
  - In all three the quote's second sentence starts on a new line (added by a small phone-only script, so the desktop DOM stays as in index.html). Desktop pixel-identical at 1440/1200/1024/861; no horizontal scroll at 360/390/430/768.
- Owner's reaction (10 Nov): picked Fable 3 · Подпись — "всё вместе, нет разрыва", the light top "лёгкая, в ней воздух есть, цвета перемешанные". The navy variants feel fake ("фальшь… нижняя часть прям грубецкая"): the dark part under the chin is painted, not photographed (the original has almost nothing below the chin). Navy is dropped on the phone unless a real half-length photo turns up.
- 4 · Подпись, правки (on `fd-fable.html`): 3 with the name leading by size as on desktop (clamp(48px,14.4vw,64px), 56 px at 390) and a wider bust from the desktop's approved extended portrait (first 1440 px of `owner-portrait-ext.webp` + the backdrop continued upward = `img/fd-podpis-bust.webp`), so the right shoulder slopes out of the frame; same air above the hair (photo margin-top -9%). Lowest contrast 8.0:1 at 360/390/430; no horizontal scroll; desktop diff 0.
- Fable's rework of «2 · Две части · Поле», on `fd-dve.html` (built by `tools/build_fd_dve.py`; the original photo as is, no derived images): 0 · Было (pixel-identical to fd-telefoon fm-2 fc-v), 1 · Лист (the text sheet lies over the last 22 px of the photo, one silhouette, the jacket shows in its rounded top corners; sheet colours taken from the photo's backdrop; lowest contrast 8.1:1), 2 · Оттиск (the photo as a print laid on the Поле card, its top 30 % above the card edge, soft shadow; lowest contrast 8.4:1). Desktop diff 0; no horizontal scroll at 360/390/430/768.

## Founder block, phone — APPROVED: «Подпись» (10 Nov)

Owner: "Берём 4". The phone founder block in the main mockup is now 4 · Подпись, правки; the navy card (v4) is retired on the phone.
- One light card. Name "Gert Top" (clamp(48px,14.4vw,64px)), role, line and the quote (26–34 px semibold, moss rule, second sentence on its own line) first, on the photo's own backdrop continued upward; Gert rises from the bottom edge, the jacket is cut by the card edge as on desktop. Nothing is painted below the chin. Card colours: #e6e8e5 with a sage glow top-left and a blush glow right, grain .26 soft-light.
- Photo: `img/fd-podpis-bust.webp` (1440×1718) = the desktop's approved extended portrait (right shoulder) cut at 1440 px plus the backdrop continued upward; built by `tools/build_fd_fable.py`.
- Main mockup: `tools/finalize_main.py` swaps the phone `<img class="ph-m">` to that file, adds `html.fd-podpis`, appends `tools/fd-podpis.css` and the phone-only script that puts the quote's second sentence on its own line. Phone render is pixel-identical to the review page at 360/390/430/768; desktop pixel-identical to before at 1440/1200/1024/861.
- For the code transfer: render the quote's second-sentence span in the phone layout only; `img/owner-portrait-m.webp` and the `.m-n*` rules are no longer used by the main mockup.
- Review pages (`fd-telefoon.html`, `fd-fable.html`, `fd-dve.html`) stay as snapshots; their build scripts start from `index.html`, so re-running them now starts from the approved Подпись.

## Assortiment — three designs by Fable (10 Nov), in review

Page `waarom-kweker/assortiment.html`, built from `index.html` by `tools/build_assortiment.py` (reads varieties, sizes and prices from `mockup-v3/src/data/content.ts`, which mirrors the live site's `lib/products.ts`; vanaf = the 40–60 cm price). The block replaces the placeholder between Waarom wij and the founder block. Real photos: `img/<slug>-sm.webp` and `<slug>-2-sm.webp` copied from `mockup-v3/src/assets/img/`. Review bar: 1 · Ряд, 2 · Палитра, 3 · Подбор.
- 1 · Ряд: the seven bushes in a row "as on the field"; the hovered one widens and shows a card with colour, bloom, stand, height and the four sizes with prices; narrow panels carry name + vanaf. Phones and touch screens up to 1200 px: a swipe row of full cards (photo, facts, prices 2×2), the next card peeks. About 800 px tall on desktop. 21st: the "Hover Expand Gallery" principle (27010). Lowest contrast 7.5:1.
- 2 · Палитра: one large Поле soft-gradient card; seven round flower close-ups with name and vanaf; below, the chosen variety large (bush photo, one line from the site data, four facts, four large moss prices, a button). Phone: the circles scroll inside the card, one variety at a time. Lowest contrast 6.5:1. Open: the line for Nova Zembla ("de meest populaire rhododendron van Nederland") is the site's own claim; keep or drop.
- 3 · Подбор: left, a tall gradient card with the three questions (zon, hoogte, kleur) and a large counter ("7 soorten" → "4 van 7"); right, all seven varieties on hairlines with flower photo, facts and the vanaf price with size and "met kluit". The picker really filters by standplaatsFilter / hoogteFilter / kleurFilter; non-matching varieties drop to quiet rows under "Past niet bij uw keuze"; an empty result says so and offers to clear an answer. Phone: the question card first (44 px buttons), then seven rows; about 1700 px. 21st: "Index List Image Gallery" (36226). Lowest contrast 5.66:1. Fable's pick (matches the plan "7 сортов без фильтров плюс подбор за 3 вопроса").
- Headings are new copy: "Kies uw rhododendron." (1, 2) and "Welke rhododendron past in uw tuin?" (3); links are placeholders.
- Checks: no horizontal scroll at 360/390/768/1024/1440/1920 in all three; header, hero, Waarom wij and the founder block have identical sizes and computed styles to index.html at 390 and 1440 (pixel diffs only from the fractional vertical offset).
- Owner on round 1 (10 Nov): 3 · Подбор plays well with Waarom wij on desktop (mirrored card), but the three questions are useless with 7 varieties (the choice is made on the product card). 1 · Ряд crops the flowers in narrow panels ("вообще не катит"). 2 · Палитра "более-менее, но что-то не то". Photos should be relatively large with the whole flower or plant visible. Later: the mirrored composition is optional.

## Assortiment — round 2 by Fable (10 Nov), in review

Page `waarom-kweker/assortiment-2.html`, built by `tools/build_assortiment2.py`. No picker. Every photo frame takes the file's own proportion (bushes mostly 3:4, Roseum Elegans square, Ponticum flower 2:3), so nothing is cropped. Review bar: 1 · Полка, 2 · Сад, 3 · Сорт.
- 1 · Полка: left, a tall Поле card with the four sizes in large figures and the price range of each (€ 22–29, 35–45, 50–65, 70–89); the chosen size changes the price under all seven plants (it filters nothing). Right, a row of the seven flowers with arrows. Mirrors Waarom wij. 21st: Product Carousel 8297, Product Card 28199, Sneaker Product Page Hero 44658 (size drives price). About 705 px on desktop, 930 px on phone. Lowest contrast 5.66:1.
- 2 · Сад: all seven bushes at once in a staggered grid, the heading in the first cell; name, colour, bloom and vanaf under each photo. 21st: Team Showcase 10098 (staggered columns), Gallery Grid with Captions 26909. 4 columns on desktop (photos 313×417 at 1440, about 1270 px), 3 on tablet, 2 staggered on phone (about 1800 px). Lowest contrast 5.66:1. Fable's pick.
- 3 · Сорт: one variety large on a wide Поле card: the seven names with colour dots on the left, bush and flower photos together in the middle, facts, four prices and a button on the right. 21st: Featured Product Showcase 29291, Feature List Showcase 27506, Editorial Collage Hero 19074. About 685 px on desktop; phone: names as a swipe row of chips, the bush full width, about 1310 px. Lowest contrast 6.98:1.
- New Dutch copy: "Zeven soorten, elk in vier maten.", "Zeven soorten uit eigen kweek.", "Kies uw rhododendron.", "Welke maat wilt u?", "Hoogte van de plant bij levering." ("bij levering" to be confirmed by the owner).
- Checks: no horizontal scroll at 360–1920 in all three; header, hero, Waarom wij and the founder block identical in sizes and computed styles to index.html; touch targets ≥ 44 px; no "most popular" claim.
- Owner (11 Nov): judge on professional design grounds, not on his wishes. Take Сад as the base and add two independent professional variants.

## Assortiment — round 3 (11 Nov), in review

Page `waarom-kweker/assortiment-3.html`, built by `tools/build_assortiment3.py` (Fable), which inserts variant 1 from `tools/as3-sad.html` (written by `tools/build_as3_sad.py`) and `tools/as3-sad.css`. Review bar: 1 · Сад, 2 · Прайс, 3 · Ряд.
- 1 · Сад (round 2's garden grid corrected): all seven at once in an aligned grid, no stagger; one 4:5 photo frame; name, colour (dot + name), bloom and "vanaf € … · 40–60 cm, met kluit" on shared rows via CSS subgrid, so prices compare along a line; the whole card links to the variety. The grid closes without orphans: desktop 4 columns = heading cell + 7 (the heading cell's link sits on the price row); tablet 3 columns = heading + 7 + a Поле link tile; phone 2 columns = 7 + tile, heading above, bloom hidden. Heights: about 1257 px at 1440, 1623 px at 390. Lowest contrast 5.66:1.
- 2 · Прайс (Fable): a price list, one row per variety: flower and bush thumbnails, name and colour, bloom, stand, height, then four price columns by size under "Prijs per plant, met kluit"; the whole row is a link. Fact columns drop as the width narrows; photo, name and the four prices always stay. Phone: one price per row with a four-size segmented control above (48 px buttons, arrow keys). Heights: about 1303 px at 1440, 1243 px at 390. 21st references: Spec Sheet 39793, Comparison Table 26827, Segmented Control 43311.
- 3 · Ряд (Fable): all seven in one row as a photo matrix: flowers (1:1) on top, bushes (3:4) below, name, colour and vanaf price on shared lines; each column one link. Below 1200 px a swipe rail (5.4 columns at 1024, 4.4 at 768, 2.4 on phone) with arrows for the mouse. Heights: about 946 px at 1440, 875 px at 390. 21st reference: Gallery Grid with Captions 26909.
  - Fable extended the square Roseum Elegans bush photo with its own background mirrored above and below; the strips showed reflected flowers and leaves, so it was replaced (11 Nov) by a plain 3:4 crop like the other bushes.
- Fable's ranking: Сад first (largest photos, all seven on the phone too), Ряд second (best on desktop, but a rail on tablet and phone), Прайс third (best for prices and facts, but dry for the homepage; better on the assortment page or next to the hedge calculator).
- Checks: no horizontal scroll at 360–1920 in all three; header, hero, Waarom wij and the founder block identical in sizes and computed styles to index.html; touch targets ≥ 44 px.
- Owner (11 Nov): Сад is good; Ряд with one of its two photo rows removed would be Сад again. Substrate as an eighth card: advised against (it breaks "seven varieties", it is priced per bag of 40 litres without sizes, and accessories sell at the point of need: product page, cart, hedge calculator; at most a slim separate line on the homepage). Сад needs an "изюминка".

## Assortiment — Сад accents (11 Nov), in review

Page `waarom-kweker/assortiment-4.html`, built by `tools/build_assortiment4.py` (Fable) with `tools/as4.css` (a copy of the Сад base plus the accents). Review bar: 0 · Как есть, A · Медальон, B · Цвет сорта, C · Карточка, A+C; Субстрат: нет / да.
- A · Цветок-медальон: a round real flower close-up (`img/<slug>-sm.webp`, focus and zoom per variety) in the bush photo's lower right corner, hanging a quarter below the photo edge, separated by a 4 px page-coloured ring; 97 px on a 312 px desktop card, 64 px on a 169 px phone card; the heart of the bush stays free; the five pink and lilac varieties become distinguishable. +26 px at 1440, +16 px at 390. Risk: Ponticum's flower photo is a single flower, not the truss. Lowest contrast 5.66:1. Fable's pick.
- B · Цвет сорта: each card is a soft grained panel in its own flower colour (data hex softened to 11–34 %), the photo inset 8 px like a passe-partout, colour strongest under the photo fading to sand. Narrower text; Nova Zembla's red softens towards salmon. Lowest contrast 5.79:1.
- C · Заголовок-карточка: the heading cell becomes a Поле gradient card with grain and a large moss "7" (part of the H2: "7 soorten uit eigen kweek."); on phone a full-width card above the grid (+44 px). Repeats "7 soorten" from the Waarom wij facts card. Lowest contrast 5.61:1 (the large "7").
- Substrate line: a slim strip under the grid on a light ground with a hairline border: round peat thumbnail (`img/tuinturf-sm.webp`), "Tuinturf-substraat", the site's upsell line, "€ 14,95 per zak van 40 liter", "Bekijk substraat"; one link. +90 px desktop, +194 px phone.
- Checks: no horizontal scroll at 360–1920 in every state; header, hero, Waarom wij and the founder block identical in sizes and computed styles to index.html (two inline spans differ by 0.03 px at 390: text-measurement noise).
- Owner on the accents (11 Nov): none really landed; the medallions are a clear no; C (heading card) and B (variety colour) "more or less". New idea from the owner: instead of a colour per variety, one light gradient background behind the whole block, with soft, blurred edges rather than a card edge.
- D · Общий фон (added to `assortiment-4.html`, now the default; A and A+C are off the review bar): one light Поле gradient field behind the whole grid (sage left, blush top right, pale sage right, linen along the bottom, cream centre; grain .26 overlay), feathered on all four sides by two intersected linear masks (about 56–120 px; 44 px on phone), so it dissolves into the page and fades into the gap above the block; the section clips only sideways. Secondary text one step darker (`--ink2`); the closing tile becomes a quiet translucent panel. D+C adds the heading card with the large 7. Lowest contrast 6.8:1 (D) and 6.77:1 (D+C); no horizontal scroll at 360–1920.
- Owner (11 Nov): the field is too faint, "практически ничего не видно"; make it more visible without getting muddy, and try 3–4 palettes. Four palettes added (html.fp-1..4, a "Палитра" group on the review bar, active for D and D+C), each about twice as saturated as the first field, the base tinted too, the feather narrowed (48–96 px). Neighbouring colours in each palette are related and pink never meets green in one place, so the mixes stay clean:
  - 1 · Поле: sage #a9bf8c left, blush #f1c0c8 top right, pale sage #bfd1a6 right, sand #e2c995 bottom. Lowest contrast 5.09:1.
  - 2 · Цветение (the flowers' own tones): lilac #d2bdf0, rose #f4b6cd, lavender #cbbff2, pink #efc6d8. Lowest 5.79:1.
  - 3 · Листва: leaf green #b0c995, pale lemon #e6e3a8, mint #c2dbb2, butter #ead79f. Lowest 5.52:1.
  - 4 · Рассвет: peach #f4c3ae, blush #f2b8c6, apricot #f2d2ae, butter #f1d39e. Lowest 6.18:1.
  - Phone: the tall narrow field gets its own blob layout in px (round blobs placed inward and repeated down the grid), because %-sized blobs stretched into edge stripes; the feather is 28 px there.
- Fable's review of palettes 1–4 (11 Nov): none is ready as is, mostly because of the field's composition. The base was almost the page colour, so all the visibility sat in saturated blobs at the edges (three separate patches); the top-right blob reads like a halo leaking from the Roseum Elegans photo; the colour peaked right at the narrow linear feather, so the edge still read as a blurred card border; on phone a 28 px feather 20 px from the screen edge read as a blurred plate. 1 · Поле: visible, but green, pink and sand are unconnected and green-to-sand turns khaki. 2 · Цветение: clean but fights the photos (lilac behind lilac bushes; Cunningham's White looks pinkish). 3 · Листва: best of the four. 4 · Рассвет: clean but "cosmetic", weakens the reds and pinks. D+C: gradient on gradient, not recommended.
- Fable's own variants (appended to as4.css, buttons 5 and 6): the tint moves into the base so the field is one even sheet clearly different from the page; large, close-toned blobs of one colour family peaking inside the field; a wider feather on a smooth curve; on phone the field is full screen width and fades only at the top and bottom (76 px).
  - 5 · Дымка: sage top left flowing diagonally into butter bottom right, a light patch behind the top row. Lowest contrast 5.89:1. Fable's pick.
  - 6 · Роса: cool eucalyptus and pale blue, the colour gathered in the caption band between the two rows; complementary to the pinks and purples; slightly cooler than the rest of the site ("аптечный"). Lowest contrast 5.94:1.
  - If 1 or 3 is chosen instead: drop the top-right blob, darken the base and soften the blobs, use the wider smooth feather, and go full width on phone.
- Owner (11 Nov), on the phone: is it critical that the facts card above has edges while the assortment field has none? Answer: not critical. A card is an object (edges), the field is the section's ground (no edges); it only looks accidental when the two read as the same material close together. Fix applied as 5+ · Дымка, правки (`html.fp-7`, button between 5 and 6): the field starts at the block's own top and builds up over a long eased top ramp (1.8× the feather on desktop, 170 px on phone), so there is more air under the card and no band right below it; the base is lighter at the top and the sage moves down behind the photos, so the card stays the densest colour. Lowest contrast 6.05:1; no horizontal scroll at 360–1920.
- Owner on 5+: "за много убрал, просто нежнее сделай". 5+ is now the same field as 5 (same blob layout and colour story), only gentler: colours about 20 % closer to the page, and a longer eased top ramp (1.5× the feather on desktop, 120 px on phone), so the green builds up under the facts card instead of starting as a band. Button renamed "5+ · Дымка, нежнее". Lowest contrast 5.9:1 or better; no horizontal scroll at 360–1920.
- Fable's check of 5+ (11 Nov): approve as is. Peak green about 76 % of 5; the card now reads as an object and the field as ground; the top ramp is smooth (clean page for about 20 px under the card on phone, full strength by about 130 px); clean, the photos look richer than on 5; the butter tone fades out before the founder card. Lowest contrast 6.63:1 at 390, 6.58:1 at 1440.

## Assortiment — APPROVED: «Сад» on the «Дымка, нежнее» field (11 Nov)

Owner: "да, переноси в основной макет". The main mockup `waarom-kweker/index.html` now has the Assortiment block between Waarom wij and a placeholder for Hoe het werkt (then the founder block).
- Markup: `tools/as3-sad.html` (written by `tools/build_as3_sad.py` from `mockup-v3/src/data/content.ts`) plus the field layer (`.sd-field` with `.sd-fbg` and the grain). CSS: `tools/assortiment.css`, flattened from the review state `iz-d fp-7 sb-n` on `assortiment-4.html` (only the rules in use: base Сад, the field, the 5+ colours and ramps). Inserted by `tools/finalize_main.py`.
- Content: heading "Zeven soorten uit eigen kweek." with "Elke soort is er in vier maten, van 40 tot 120 cm. U bestelt vanaf 1 plant."; seven cards (bush photo 4:5, name, colour dot and name, bloom, "vanaf € …" with "40–60 cm, met kluit"); "Bekijk alle planten" (desktop in the heading cell; tablet and phone as a translucent tile). No substrate line on the homepage (it belongs on the product page, in the cart and in the hedge calculator).
- Checks: the block matches the approved review state pixel for pixel at 360/768/1024/1440/1920 (at 390 only sub-pixel text antialiasing differs); header, hero, Waarom wij and the founder block are unchanged in sizes and computed styles; no horizontal scroll at 360–1920.
- Review pages (`assortiment.html`, `-2`, `-3`, `-4`) stay as snapshots; their build scripts expect the old placeholder in `index.html`, so they no longer rebuild from the current main mockup.
- For the code transfer: card links point to `#assortiment` in the mockup; on the site they go to the product pages.
- Owner (11 Nov): remove the colour (name and dot) from the cards everywhere; the heading corner on desktop has too much empty space between the lead and the button. Colour removed in the main mockup (`build_as3_sad.py`, `assortiment.css`): desktop cards are photo, name, bloom, price (4 subgrid rows); phone cards photo, name, price.
- Heading corner, in review on `waarom-kweker/assortiment-5.html` (built by `tools/build_assortiment5.py` from index.html; html.hd-0|1|2):
  - 1 · Над сеткой: the heading row spans the full width, H2 at the section size (clamp(34px,4.2vw,58px)) on the left and the lead on the right on its baseline; the grid is 4 columns from 768 px and 2 below, 7 cards + the «Bekijk alle planten» tile, so it closes without a gap at every width. +110 px at 1440; at 768 the block gets shorter (920 vs 1360 px). Recommended.
  - 2 · Собрать в ячейке: heading, lead and button together at the top of the first cell; the free space moves below the button.
  - Phone is the same in all three (the heading is already above the grid there).
- Fable's heading-corner options (11–12 Nov), on `waarom-kweker/assortiment-6.html` (built by `tools/build_assortiment6.py`; html.hf-0|1|a|b, default a). Both add the four sizes with the price range over the seven varieties, computed from content.ts: 40–60 cm € 22–29, 60–80 € 35–45, 80–100 € 50–65, 100–120 € 70–89, with "Per plant, met kluit. De prijs verschilt per soort."
  - A · Четыре размера: the heading stays the grid's first cell; the size scale on hairlines fills the void under the lead (the lead drops ", van 40 tot 120 cm", which the scale shows); the button stays on the price row. Desktop and tablet height unchanged; on phone the scale sits 2×2 above the grid (+125 px). Lowest contrast 6.28:1. Fable's pick.
  - B · Размеры в конце: the heading row above the grid (as 1); the last cell is a quiet panel "Prijs per maat" with the scale and a filled moss "Bekijk alle planten" button; tablet 3 columns with the panel spanning two cells. +109 px on desktop, +103 px on tablet. Lowest contrast 6.08:1.
  - Fable's ranking: A, B, 1 · Над сеткой (the end tile is almost empty, tablet cards small), 0.
  - Checks: no horizontal scroll at 360–1920 in all states; rest of the page identical in sizes and computed styles to index.html.
- Owner (12 Nov) asked whether a product block should hold only products. Answer: yes; on the homepage a product block is a heading, the products and one "view all" link. The size and price scale and the size guide belong on the product page (where the size is chosen), the catalogue and Plantgids, not in this block. So the empty corner is solved by layout, not by content.

## Assortiment — APPROVED: heading above the grid, «Bekijk alle planten» as the last card (12 Nov)

Owner: "Делай". In the main mockup (`build_as3_sad.py`, `assortiment.css`):
- The heading row spans the grid: "Zeven soorten uit eigen kweek." at the section size (clamp(34px,4.2vw,58px), as Waarom wij) on the left, the lead on the right on its baseline; one column on ≤767 px. The button in the heading is gone.
- The grid is 7 cards + the «Bekijk alle planten» card at every width: 4 columns from 768 px, 2 below, so it always closes without an empty cell.
- The last card is a link card of its own: a quiet translucent panel (white .5, hairline ring, hover .75) with a round moss arrow (48–56 px; 44 px on phone) at the top where the photos start, and at the bottom "Bekijk alle planten" (20–26 px, ink) with "Alle zeven soorten, maten en prijzen" under it, on the price row. The whole card is the link.
- Heights: about 1337 px at 1440, 920 px at 768 (4 columns instead of 3), 1526 px at 390. Lowest contrast 6.43:1. No horizontal scroll at 360–1920; header, hero, Waarom wij and the founder block unchanged.
- Owner on the «Bekijk alle planten» card (12 Nov): rejected outright ("это не дизайнерское решение"); keep just the seven varieties. Review page `waarom-kweker/assortiment-7.html` (built by `tools/build_assortiment7.py` from index.html; html.lay-1|2|3): no view-all card; the link to all plants is a plain moss text link "Bekijk alle planten →" under the lead in the heading row.
  - 1 · 4 + 3: two rows of equal cards on an 8-column grid, the second row of three centred. About 1383 px at 1440.
  - 2 · 3 + 4: a 12-column grid, three wider cards on top, four below, both rows full width. About 1524 px at 1440.
  - 3 · 7 в ряд: one line of seven whole bushes from 1200 px (about 657 px at 1440); below 1200 px as 4 + 3.
  - Phone (≤767 px), all three: two columns, the seventh card centred on its own row.
  - No horizontal scroll at 360–1920 in all three.
- Fable's verdict on the 7-card layouts (12 Nov): none of 1–3 is right as a whole. 1 · 4+3 is 1383 px tall at 1440 and its centred second row reads as "one missing"; 2 · 3+4 is the worst (1524 px, and it ranks three varieties above the others); 3 · 7 в ряд is the only right one on wide screens but falls back to 4+3 below 1200 px; on phone all three are about 1577 px with a lone centred 7th card. Fable added 4 · Fable (`tools/build_assortiment7b.py`, rebuilds `assortiment-7.html` with four buttons, default 4): one shelf of the seven cards, same anatomy, photos and field, nothing added. Seven in one row from 1000 px (633 px at 1440, 505 px at 1024); below that the same row becomes a swipe ribbon with scroll-snap, the next card cut by the screen edge (3.3 cards visible at 768, 1.7 at 390), the last card stops on the right margin; on phone the photos are larger (210 px vs 169), names fit one line and the bloom line returns; 657 px at 390. No arrows or dots on the ribbon. Markup change: the heading row `.sd-hd` sits before `.sd-grid` so only the grid scrolls. Lowest contrast 6.86:1; no horizontal page scroll at 360–1920; rest of the page unchanged.
- Owner (12 Nov) questioned whether Fable's choice was independent or produced under pressure. A blind review was run: a fresh reviewer (not Fable) got only the brief and neutral screenshots without names or history (desktop D1 = 4+3, D2 = 3+4, D3 = 7 in a row; phone P1 = 2 columns with the 7th centred, P2 = swipe ribbon, P3 = 2 columns with the 7th left).
  - Desktop: D3 > D1 > D2. D3 shows all seven at once under "Zeven soorten", prices compare on one line, the block fits one screen; cost: smaller photos. Confidence 60–65 % over D1; would switch to D1 if most desktop visitors are at ≤1280 px or the lilac varieties cannot be told apart at that size. D2 last (false hierarchy among equal products).
  - Phone: P1 > P3 > P2. All seven are seen by scrolling down; the centred 7th reads as a deliberate closing card, the left-aligned one as "something missing". The ribbon is last (about 1.7 cards visible, five hidden behind a swipe many people never make; the "only seven" message disappears). Confidence 85–90 % that P2 is last.
  - To ship: D3 on desktop with a switch to 4+3 centred below about 1200 px, and P1 on phone (the 7th card centred, same size). Optional: order the cards so distinct colours alternate; show the bloom line on phone.
  - This combination is exactly the existing option "3 · 7 в ряд" on `assortiment-7.html` (7 in a row from 1200 px, 4+3 centred below, 2 columns with the 7th centred on phone). Fable agreed on desktop but chose the ribbon on phone; the blind review overrules that.

## Assortiment — APPROVED: seven cards, one row on desktop, centred 7th on phone (12 Nov)

Owner: "переноси", and yes to alternating colours. In the main mockup (`build_as3_sad.py`, `assortiment.css`, `finalize_main.py`):
- Heading row above the grid (no longer a grid cell): H2 at the section size on the left; the lead and a moss text link "Bekijk alle planten →" on the right. No view-all card.
- Just the seven cards: one row from 1280 px (cards 155–174 px wide; the breakpoint moved up from 1200 so cards never drop below 150 px); 4 + 3 centred on an 8-column grid from 768 to 1279 px; two columns with the 7th centred at the same size on ≤767 px.
- Order so distinct colours alternate: Nova Zembla (red), Catawbiense Grandiflorum (pale lilac), Cunningham's White, Catawbiense Boursault (deep purple), Roseum Elegans (hot pink), Ponticum (violet), Ponticum Roseum (light pink-lilac).
- Heights: about 657 px at 1440, 1255 px at 1279, 936 px at 768, 1574 px at 390. No horizontal scroll at 360–1920; header, hero, Waarom wij and the founder block unchanged.
- Bloom line on phone: stays hidden (owner, 12 Nov: "оставь как есть"); it shows on tablet and desktop.

## Contact with the grower (audit item 1, 12 Nov)

Owner: both numbers; hours Mon–Fri 08:00–17:00, Sat 09:00–13:00. In the main mockup (`tools/contact.css`, `finalize_main.py`): the header shows "06 20 10 43 12" with a phone icon before «Bestellen» on desktop and a round 44 px phone button next to the menu button below 1024 px (tel:+31620104312); the Waarom wij advice reason now reads "Bel 06 20 10 43 12 of 06 20 29 78 49, of stuur een WhatsApp." with the hours "Ma–vr 08:00–17:00, za 09:00–13:00." on its own line (tel: and wa.me/31620297849 links, moss underline). No horizontal scroll at 360–1440; the rest of the page unchanged.
- Founder block contact (owner chose C, 12 Nov; `tools/founder-contact.css`, `finalize_main.py`): under the quote the sentence "Kom gerust langs, ook zonder afspraak: rondkijken, advies vragen of direct meenemen." (16.5 px ink), then a label | value list: Adres "Esserbroekweg 2, Otterlo" (maps link), Open "ma–vr 08:00–17:00 · za 09:00–13:00", Bellen both numbers (tel:), WhatsApp 06 20 29 78 49 (wa.me). Labels 13.5 px #45443f (the softer grey fell below AA on the photo-backed panel), values 15 px, links moss with a quiet underline; no buttons.
  - Desktop ≥1200: one column list; the block takes the panel's bottom padding, so the card height and portrait crop stay as approved (626 px at 1440, 522 at 1200).
  - 861–1199: compact 2 × 2 grid (label above value; the two-line hours and numbers share the first row), indented to the quote's text line because the shoulder reaches under the panel's lower left corner; card 495 px at 1024 as before, 443 vs 435 at 900.
  - Phone: after the quote, before the portrait, on the 22 px inset; hours and numbers one per line. Card about 950 px at 390 (was 682).
  - Lowest contrast 4.6:1 (the address at 900 px, over the backdrop); 4.9+ at 1200 and up; 7.4 on phone. Hero, Waarom wij and the assortment unchanged.
- Owner (12 Nov): phone version good; desktop "вообще не то". Reworked with the Impeccable layout/typeset references (the Impeccable context launcher is blocked by auto mode; the reference docs were followed directly). Desktop thesis: the card is the person (name, line, quote, exactly as approved), the contact is how to reach him, so it gets its own strip directly under the card, on the card's own grid: the invitation (18–21 px, 500) under the photo column; the details (label 13 px above value 15.5 px; Adres with the full address on two lines, Open, Bellen with both numbers, WhatsApp) under the text column, starting on the name's edge. Four details in one row from 1360 px, 2 × 2 below. The in-card list is phone only (unchanged). The desktop card is pixel-identical to the approved card before any contact was added (861–1920), so no crowding and no text over the shoulder.
- Fable's check of the strip (12 Nov): approve with small fixes, no redo (no hairline: the card's bottom edge already separates; invitation size and weight right; lowest contrast 8.14:1). Applied: the invitation breaks after the colon into two full lines from 1024 px ("Kom gerust langs, ook zonder afspraak: / rondkijken, advies vragen of direct meenemen."), no 30ch column with a stray last line; the 2 × 2 details spread over the text column (minmax(max-content,1fr), 24 px gap); four in a row from 1280 px (was 1360); on touch tablets (861–1199, pointer:coarse) the number links get 4 px vertical padding. The desktop card stays pixel-identical to the approved card; phone unchanged.
- Owner (13 Nov) on the revised strip: rejected ("этот вариант хуйня полная"); "прошлый вариант мне нравился больше". Reverted to the first strip version (commit 31b4811): the invitation as a 30ch block (three lines) under the photo column, the details 2 × 2 below 1360 px and four in a row from 1360 px. Fable's fixes are undone; the main mockup is byte-identical to that commit.
- Owner (13 Nov): he meant the version with everything inside the card. Restored commit 23173ad's founder block (contact list under the quote inside the card on desktop; compact 2 × 2 at 861–1199 stepped in to the quote's text line; phone unchanged). The strip is gone; the main mockup is byte-identical to 23173ad.
- Owner (13 Nov): on wide screens use the same structured 2 × 2 as on the narrower ones instead of one long label | value column. From 1200 px the details are a 2 × 2 grid with the label above the value (Open | Bellen, then Adres | WhatsApp), stepped in to the quote's text line, labels 13 px, values 15 px; the invitation is balanced over two lines. The card keeps its approved height (626 px at 1440, 522 at 1200); 861–1199 and phone unchanged.
- Owner (13 Nov): the desktop card text is cramped, the bottom presses towards the shoulder, too little air; asked Fable to set it. Fable's pass (`tools/founder-desktop.css`, appended after founder-contact.css, all under min-width:861px; phone pixel-identical):
  - three zones on one left line: who (name, role, line) · the quote · the visit (invitation and the 2 × 2 grid); equal space above and below the quote (45 px at 1440, was 78 / 35);
  - the contact as a distinct lower zone under a thin moss hairline (24 % opacity); 12–18 px between grid rows, wider column gap;
  - the bottom kept clear of the shoulder: panel bottom padding 63 px at 1440 (was 43), the text line moved 38 px right at 1440;
  - trade-off: the name 66 px at 1440 (was 78) and the quote 30 px (was 35); 40–54 px and 22–25 px at 861–1199;
  - the card grows a little and the portrait with it: 1920 608→663, 1440 626→646, 1280 556→586, 1200 522→561, 1024 495→523, 900 443→485. A 697 px card at 1440 was tried and dropped (face too big, hair cut at the left).
  - Weak spot: 861–900 px is denser (about 20 px between the address and the shoulder at 900). Lowest contrast 4.73:1; no horizontal scroll at 861–1920.

## Founder card: role, content and position (13 Nov), in review

Owner: the bottom left is still pressed down and there is room on the right; is the card overloaded, needed, should it be removed or rewritten, where should it stand? Fable's view: overloaded (nine text elements, three jobs: who, what he thinks, how to visit; the contact grid is a footer inside a portrait card). Spacing cannot fix it because the portrait scales with the card height; content has to go. The card is needed (the living grower is the proof of "personal advice"), but as a helper at the moment of doubt, not a business card at the end. Proposal on `waarom-kweker/fd-plan.html` (`tools/build_fd_plan.py`; html.fp2-0|1|2):
- 1 · Помощник (Fable's pick): the card moves right after the assortment, before Hoe het werkt; "Gert Top · Oprichter en kweker" as a byline, the heading "Twijfelt u welke soort past? Gert denkt met u mee.", one sentence ("Eén gewas, sinds 2001: … Bel of app met uw vraag, of kom langs in Otterlo. Dat kan zonder afspraak."), the two numbers as large text links (Bellen, WhatsApp), the hours; no quote, no grid; desktop text as one group centred in the panel height. Phone: the same light «Подпись», shorter. Address and hours move to a footer (sketch only) and later to the "afhalen" step of Hoe het werkt; the numbers leave the Waarom wij reason (draft: "Twijfelt u over soort of maat? U spreekt de kweker zelf: per telefoon, WhatsApp of op de kwekerij.").
- 2 · На месте, легче: stays last, the large name kept, "Oprichter en kweker", the quote replaced by "Kom gerust langs, ook zonder afspraak." and one line with the phone and WhatsApp; the footer right below.
- To confirm: the move; the name as a byline; removing the quote; all new Dutch copy is a draft. Lowest contrast 5.66:1; no horizontal scroll at 360–1920; no text over the shoulder.

## Founder card — APPROVED: «Помощник» right after the assortment (13 Nov)

Owner: "Берём 1 · Помощник". In the main mockup (`tools/founder-helper.css`, `finalize_main.py`), pixel-identical to option 1 on `fd-plan.html` at 360–1920:
- Page order: hero → Waarom wij → Assortiment → the founder card → Hoe het werkt (placeholder) → footer (placeholder).
- The card keeps the approved portraits (desktop extended shoulder, phone «Подпись»). Text: "Gert Top · Oprichter en kweker" as a byline; H2 "Twijfelt u welke soort past? Gert denkt met u mee."; "Eén gewas, sinds 2001: daardoor weten wij wat een rhododendron nodig heeft. Bel of app met uw vraag, of kom langs in Otterlo. Dat kan zonder afspraak."; Bellen 06 20 10 43 12 and WhatsApp 06 20 29 78 49 as large text links; "Ma–vr 08:00–17:00, za 09:00–13:00". No quote, no contact grid, no buttons. Desktop text as one group centred in the panel height.
- The Waarom wij advice reason no longer carries numbers: "Twijfelt u over soort of maat? U spreekt de kweker zelf: per telefoon, WhatsApp of op de kwekerij."
- The address, hours, "Zonder afspraak welkom" and both numbers live in the footer (a dark placeholder until audit item 13 designs it). The Hoe het werkt placeholder notes that the pick-up step will carry the address and hours.
- The quote "Een gezonde plant is geen toeval. Dat is onze standaard." and the large name are retired (owner's choice of option 1). All new Dutch copy came from Fable as drafts; the owner chose this option with that copy visible.
- No horizontal scroll at 360–1920; header, hero and the assortment unchanged.
- Owner (13 Nov): set the card text professionally, numbers in one column. The action is now one label | value list on a common value edge: Bellen 06 20 10 43 12, WhatsApp 06 20 29 78 49 (21–25 px, tabular figures), Open "ma–vr 08:00–17:00, za 09:00–13:00" as the quiet last row (15 px; two lines without the comma on phone). The paragraph measure is 48ch on desktop (cleaner breaks). Card heights unchanged on desktop (626 at 1440, 495 at 1024, 435 at 900); phone 789 px at 390. Lowest contrast 5.2:1; rest of the page unchanged.
- Owner (13 Nov): the role under the name instead of in one row. "Gert Top" (19 px, 600) with "Oprichter en kweker" (15 px) under it, a signature rather than a label over the heading. Desktop card heights unchanged; phone +23 px (812 at 390).

## Founder helper card: where the name goes (13 Nov), in review

Owner: the headline should come first; the name on top does not fit. Two review pages:
- Mine, `waarom-kweker/fd-name.html` (`tools/build_fd_name.py`; html.nm-0..3): 1 · the name and role as a signature after the paragraph, before the contacts; 2 · as a signature at the very end; 3 · no byline, the paragraph opens with "Gert Top is oprichter en kweker." (draft). My pick: 1.
- Fable's, `waarom-kweker/fd-name-fable.html` (`tools/build_fd_name_fable.py`; html.nf-0..2): 1 · one line right under the headline, "Gert Top, oprichter en kweker" (15.5 px, name 600, role grey), then the paragraph and contacts (editorial order: headline, byline, text); 2 · in the contacts: the list opens with "Kweker | Gert Top, oprichter" above Bellen, WhatsApp, Open (draft wording). Fable's pick: 1. His view of mine: (a) works but reads like a signature under a quote while the paragraph speaks as "wij", and it splits "Bel of app" from the numbers; (b) weakest on desktop (ends on a signature near the shoulder), good on phone; (c) cleanest structure but the name gets lost and repeats the headline's "Gert".
- All options keep the desktop card height; lowest contrast 5.45:1 (Fable's), no horizontal scroll.
- APPROVED (owner, 13 Nov: "если вы подтверждаете, берём 1 вариант"; both reviewers agreed): Fable's option 1. The headline comes first, then one byline "Gert Top, oprichter en kweker" (15.5 px; name 600 ink, role grey; 14.5 px at 861–1199, 15 px on phone), then the paragraph and the contact list. The stacked name/role above the headline is gone. In the main mockup (`finalize_main.py` P1, `tools/founder-helper.css`), pixel-identical to nf-1 on fd-name-fable.html at 360–1920. Desktop card heights unchanged; phone 783 px at 390.

## Founder helper card: Gert and the team (13 Nov), in review

Owner: not only Gert answers the calls, the team helps too; the byline under the headline feels foreign, maybe after the text, before the numbers. Review page `waarom-kweker/fd-team.html` (`tools/build_fd_team.py`; html.fe-0..3), all new Dutch copy as drafts:
- 1 · «Wij» + подпись: headline "Twijfelt u welke soort past? Wij denken met u mee."; after the paragraph, right above the numbers, "Gert Top en het team van de kwekerij" (15.5 px; name 600). Recommended.
- 2 · Герт и команда: headline "… Gert en het team denken met u mee." (three lines on desktop); above the numbers "U spreekt Gert Top, oprichter en kweker, of iemand van zijn team."
- 3 · Имя в тексте: headline "Wij denken met u mee."; the paragraph adds "Gert Top, oprichter en kweker, en zijn team helpen u graag."; no separate line.
- Desktop card heights unchanged in all; phone 784 / 835 / 800 px at 390.
- Fable's view (14 Nov): keep the headline "Wij denken met u mee."; one line right above the numbers, "Gert Top, oprichter en kweker, en zijn team".
- Owner (14 Nov): the name must be attached to something, not stand alone; Fable's line is not bad, but something is still off.

## Founder helper card: what the name is attached to (14 Nov), in review

Review page `waarom-kweker/fd-team2.html` (`tools/build_fd_team2.py`; html.ft-0..3). Options 1–3 share the headline "Twijfelt u welke soort past? Wij denken met u mee." All new Dutch copy is a draft:
- 1 · Fable: the line "Gert Top, oprichter en kweker, en zijn team" right above the numbers.
- 2 · Имя в призыве: the name belongs to the sentence that leads into the numbers, "Bel of app met Gert Top, oprichter en kweker, of met zijn team:". The paragraph keeps the walk-in: "Eén gewas, sinds 2001: daardoor weten wij wat een rhododendron nodig heeft. Kom gerust langs in Otterlo, ook zonder afspraak." Recommended.
- 3 · Слова Герта: the paragraph is set as Gert's own words on a 2 px moss rule (the line style approved for his quote), signed beneath on the same rule "Gert Top, oprichter en kweker".
- Measurements:
  - desktop card heights unchanged in all options (626 at 1440, 495 at 1024, 435 at 900);
  - phone card heights 783 / 784 / 807 / 785 px at 390;
  - no horizontal scroll.
- APPROVED (owner, 15 Nov): option 2 «Имя в призыве». The owner asked whether the role is there; it is, after the name, in the sentence's regular weight; the owner: keep it as it is, maybe return later.
  - Main mockup (`finalize_main.py` P1, `tools/founder-helper.css`): headline "Twijfelt u welke soort past? Wij denken met u mee."; the paragraph "Eén gewas, sinds 2001: daardoor weten wij wat een rhododendron nodig heeft. Kom gerust langs in Otterlo, ook zonder afspraak."; then `.fp-lead` "Bel of app met Gert Top, oprichter en kweker, of met zijn team:" (16 px #2f2e2a, name 600; 15 px at 861–1199, 15.5 px on phone) right above the Bellen / WhatsApp / Open list. The byline under the headline is gone.
  - Checked against ft-2 on fd-team2.html: pixel-identical at 360, 390, 768, 900, 1024, 1440 and 1920. At 1200 one glyph is antialiased differently (sub-pixel position).
  - Card heights: desktop unchanged; phone 807 px at 390, 763 px at 360.
  - Header, hero, Waarom wij, the assortment and the footer unchanged (0 diffs at 390 and 1440); no horizontal scroll.

## Delivery and payment by the prices (audit item 2, 15 Nov), in review

Owner's facts (15 Nov):
- delivery in the Netherlands only, with own transport;
- cost by distance and volume;
- the day by agreement;
- pick-up in Otterlo;
- iDEAL, bank transfer, or card or cash on receipt; businesses on invoice.

Review page `waarom-kweker/sd-lev.html` (`tools/build_sd_lev.py`; html.lv-0..2), right under the assortment grid. All new Dutch copy is a draft.
- 1 · Строка под ценами: one quiet line, 15 px, "Bezorgen in heel Nederland, kosten naar afstand en aantal · Afhalen in Otterlo · Betalen met iDEAL, overboeking of bij ontvangst". One line at 1000–1920; three lines without dots at ≤999. Recommended.
- 2 · Три факта: a hairline, then three columns (label | short text), stacked on phone:
  - Bezorgen: "In heel Nederland, met eigen transport. De kosten hangen af van afstand en aantal; de dag spreken we met u af."
  - Afhalen: "In Otterlo: wij zetten uw bestelling klaar."
  - Betalen: "iDEAL, overboeking, of pin of contant bij ontvangst. Zakelijk op factuur."
- Lowest text contrast 7.2:1 (labels 13.7:1); the decorative dot 4.8:1. No horizontal scroll at 360–1920.
- Block height: +24 px (option 1) / +165 px (option 2) at 1440; +98 / +280 px at 390.
- The details (how the day is agreed, the pick-up step) belong in Hoe het werkt, still a placeholder.
- Owner (16 Nov): option 1 is good. Add "u ziet de kosten vóór u betaalt", to remove the fear before the cart. All delivery and payment details are provisional until the company owner confirms them; the mockup shows the example and the reason. First, the assortment lead moves under the heading (below).

## Assortment: the lead under the heading (16 Nov), done

Owner: the text that belongs under the heading sat on the right; move it under the heading, as elsewhere on the page.
- In the main mockup (`tools/build_as3_sad.py` → `tools/as3-sad.html`, `tools/assortiment.css`):
  - H2, then the lead "Elke soort is er in vier maten, van 40 tot 120 cm. U bestelt vanaf 1 plant." on the left (16–17 px, 12–18 px under the heading).
  - From 600 px up, the lead breaks only between its two sentences. It is one line from 768 px.
  - "Bekijk alle planten →" stays on the right, on the lead's baseline, at the grid's right edge.
- Phone (≤767) unchanged: heading, lead and link were already stacked. Pixel-identical at 390; at 360 one glyph is antialiased differently.
- Block height at 1440: +4 px. No horizontal scroll at 360–1920.
- `sd-lev.html` rebuilt on the new heading.

## Assortment: "Bekijk alle planten" as a pill in the bottom right corner (16 Nov), done

Owner: the link with the arrow sat at the top right, attached to nothing; it should be a pill, probably in the bottom right corner. I should have flagged it myself.
- In the main mockup (`tools/build_as3_sad.py` → `tools/as3-sad.html`, `tools/assortiment.css`):
  - The heading row now holds only H2 + lead.
  - The block closes with `.sd-ft`, the pill "Bekijk alle planten →" in the bottom right corner on the grid's right edge, 28–44 px under the cards.
  - The pill uses the hero's outline pill: 52 px, radius 999px, 15 px 500, ink text, 1 px border at 60% ink, filled ink on hover.
  - On phone (≤599) it is full width under the last card.
- `sd-lev.html` rebuilt for the chosen delivery line (option 1) in the same bottom row:
  - The line sits left of the pill: "Bezorgen in heel Nederland, u ziet de kosten vóór u betaalt · Afhalen in Otterlo · Betalen met iDEAL, overboeking of bij ontvangst".
  - "naar afstand en aantal" was dropped to keep it to one line; it goes to Hoe het werkt.
  - Each fact stays whole. The dot that would start a line is clipped, so no dot dangles.
  - Layout by width:
    - one line at 1280–1920;
    - two lines at 900–1024;
    - three lines at 768;
    - on phone and ≤767, three lines above the pill.
  - Option 2 (three facts) was dropped (owner chose 1).
- No horizontal scroll at 360–1920.

## Assortment bottom row: Fable's review applied (16 Nov)

Fable's verdict: the composition is right (lead under H2; outline pill bottom right as a secondary action; one line left of the pill), but it needed fixes. Owner: apply 1–7. Applied:
1. Bottom row gap: `.sd-ft` margin-top 0 at ≥600 (main mockup too).
   - Before: 95–114 px from the price text to the row against 44–52 px from the lead to the photos.
   - After: the cards' own padding gives 46–56 px at 1280–1920 and 40 px at 600–1024, against 44–52 / 32–35 px above.
2. A fact may now wrap inside itself; only "ziet u vóór u betaalt" stays together. Tested with the line's font at ×1.2, ×1.5 and ×2: no clipping at 360–1920.
3. Copy (draft): "Bezorgen in heel Nederland – de bezorgkosten ziet u vóór u betaalt · Afhalen in Otterlo · Betalen met iDEAL, per overboeking of bij ontvangst".
4. 600–767: the list stays beside the pill, both on the bottom line, instead of the list above a pill pushed to the right edge.
5. Stacked list (≤767): 15 px, 8 px between facts.
6. Labels at weight 500, quieter against the variety names.
7. The separator dot has empty alt text (`content:"·" / ""`), so screen readers skip it.
- Not changed: the pill height (52 px vs 56 / 40 elsewhere; Fable unsure, I agreed to leave it).
- Layout:
  - one line at 1440–1920;
  - two lines at 900–1280;
  - three at 768;
  - on phone, three facts above a full-width pill.
- No horizontal scroll.
- Owner (16 Nov): drop the delivery line from the assortment altogether (it clutters, the labels compete with the variety names). Delivery and payment go to the product page and Hoe het werkt. It was never in the main mockup; `sd-lev.html` stays as a record. Next: an add-to-cart control with quantity on the variety cards (components searched on 21st).

## Add to cart on the variety cards (16 Nov), in review

Owner: put an add-to-cart icon and a quantity on the cards. Every variety has four sizes with their own prices (content.ts), so the options differ in how the size is chosen.
- Review page `waarom-kweker/sd-cart.html` (`tools/build_sd_cart.py`; html.ct-a|b|c), desktop and phone:
  - A · Быстро в корзину: a pill stepper "− 1 +" (40 px) and a round moss cart button (40 px) under the price; adds the 40–60 cm size the card shows.
  - B · Размер на карточке: a pill size select; the price follows it, so "vanaf" and the size line go. Then the stepper and the cart button.
  - C · Значок открывает выбор (my pick): only a round cart button on the price line. It opens a panel with the four sizes and prices, the stepper, the total and "In winkelwagen".
    - On desktop the panel is a popover that opens upwards over its own card, never down over Gert's portrait.
    - On phone it is a bottom sheet.
- The card link moved to the name and is stretched over the card, so no control sits inside a link; the grid alignment and the column spans are kept.
- Components looked up on 21st.dev (minimal stepper, pill number field, add-to-cart pill) and redrawn in the page's style; no 21st code installed.
- Smallest card 154 px (360) and 155 px (1280); the controls fit, no overflow, no horizontal scroll.
- Card height at 1440: 398 (C) / 452 (A) / 495 (B) px.
- Fable designs his own option in parallel (`sd-cart-fable.html`).
- Fable's option (`waarom-kweker/sd-cart-fable.html`, `tools/build_sd_cart_fable.py`; html.fc-1|2). His verdict: A puts 21 controls in a row and silently adds the smallest size; B is the noisiest and hides the other prices in a select; he picks C, refined:
  - The card: one round outline cart button (40 px, like the "Bekijk alle planten" pill).
    - fc-1: on the price line (his pick).
    - fc-2: white, in the photo's bottom right corner.
  - The panel (native `<dialog>`):
    - thumbnail, name, "Alle maten met kluit";
    - four radio rows size · price, 40–60 preselected;
    - "Aantal" stepper and "Totaal";
    - "In winkelwagen".
  - After adding: "In uw winkelwagen · 2 × …, 60–80 cm · € 70" with "Verder kijken" / "Naar winkelwagen", and a count badge on the card's button. So the quantity shows on the card only once there is one.
  - Popover from 768 px, bottom sheet on phone.
  - Fable's measurements:
    - contrast: icon 14–16:1, button outline 4.4:1;
    - targets 44–52 px;
    - no horizontal scroll.
  - My note: on desktop his popover opens downwards over the founder card (its headline, not the face); mine opens upwards.
- Owner (16 Nov): no cart on the cards at all, "it doesn't belong here". Neither option goes into the main mockup. The cards stay one link each, to the product page, which will hold size, quantity, cart, delivery and payment. The review pages stay as a record.

## The founder card as the guarantee block (16 Nov), in review

Owner's idea: turn Gert's card (right after the assortment) into the guarantee block. He also allows dropping today's help text.

The guarantee follows the research report (`reports/Гарантия приживаемости у конкурентов.md`):
- until 31 December of the year after delivery;
- a new plant delivered free;
- report with photos.

It is provisional until the owner confirms; all Dutch copy is a draft. In every option the first Waarom wij reason now reads "Aangroeigarantie tot eind volgend jaar / Slaat een plant niet aan? Dan krijgt u kosteloos een nieuwe." (one wording).

My page: `waarom-kweker/fd-gar.html` (`tools/build_fd_gar.py`; html.gr-1..4).
- 1 · Гарантия + номера:
  - "Slaat een plant niet aan? Dan krijgt u een nieuwe.";
  - three checked points (term, free delivery of the new plant, report with a photo via WhatsApp);
  - "Lees de garantievoorwaarden";
  - "Een vraag of iets melden? Bel of app met Gert Top, …";
  - Bellen and WhatsApp.
- 2 · Обещание Герта:
  - "Elke plant met aangroeigarantie, tot eind volgend jaar.";
  - his words on a moss rule: "Wij kweken elke rhododendron zelf. Slaat er toch een niet aan? Stuur ons een foto, dan brengen wij kosteloos een nieuwe." signed "Gert Top, oprichter en kweker";
  - the conditions link, then the contacts.
- 3 · Помощь + гарантия: today's card with a tinted guarantee line above the numbers.
  - At 861–1279 the hours row goes, and at 861–999 the walk-in sentence, so the card keeps its height.
- 4 · Только гарантия:
  - headline and the promise ("U hoeft niet uit te leggen waardoor het misging");
  - three steps to report (WhatsApp photo, an answer within two working days, a free new plant);
  - the conditions link; no phone list.
- Desktop card heights unchanged in all four at 900–1920; no horizontal scroll.

Fable's page: `waarom-kweker/fd-gar-fable.html` (`tools/build_fd_gar_fable.py`; html.gf-0|1).

His view:
- The card is the right home for the guarantee, but the help should not go entirely: it is the only invitation to call before buying, and the walk-in line goes with it.
- On my options:
  - 1 works but reads like a spec;
  - 2 is the most emotional but needs Gert's real words and signature, and the term does not fit a quote;
  - 3 leaves the guarantee a footnote;
  - 4 is the weakest: it shows the procedure for a dead plant before the purchase, and the phones go.

His version, "3 reversed":
- H2 "Slaat uw rhododendron niet aan? Dan krijgt u van ons een nieuwe.";
- "Aangroeigarantie tot eind volgend jaar. Dezelfde soort en maat, kosteloos bezorgd of klaargezet in Otterlo. De oorzaak hoeft u niet aan te tonen: een paar foto's volstaan.";
- "Lees de voorwaarden";
- "Vragen over soort of garantie? Bel of app met Gert Top, oprichter en kweker, of met zijn team:";
- the full contact list.

Fable's measurements:
- desktop heights unchanged;
- phone 907 px at 390 (807 now);
- lowest contrast 5.22:1.

He flags that "De oorzaak hoeft u niet aan te tonen" in the first year already follows from BW 7:18 (a lawyer to check against 6:193g j).
- APPROVED direction (owner, 16 Nov): Fable's version with my shorter headline, and the hours removed from the card (they live in the footer). In the main mockup (`finalize_main.py` P1, `tools/founder-helper.css`):
  - H2 "Slaat een plant niet aan? Dan krijgt u een nieuwe."
  - "Aangroeigarantie tot eind volgend jaar." (ink, 600), then "Dezelfde soort en maat, kosteloos bezorgd of klaargezet in Otterlo. De oorzaak hoeft u niet aan te tonen: een paar foto's volstaan.", then "Lees de voorwaarden" on its own line.
  - "Vragen over soort of garantie? Bel of app met Gert Top, oprichter en kweker, of met zijn team:", then Bellen and WhatsApp.
  - Waarom wij reason 1: "Aangroeigarantie tot eind volgend jaar / Slaat een plant niet aan? Dan krijgt u een nieuwe: kosteloos bezorgd of klaargezet in Otterlo."
  - Card heights unchanged at 900–1920 and 768. Phone 802 px at 390 (was 807), 788 at 360 (was 763).
  - Waarom wij +25 px on phone; hero, assortment and footer unchanged; no horizontal scroll.
  - To confirm or check:
    - the owner: the term and the promise;
    - a lawyer: "De oorzaak hoeft u niet aan te tonen", which in the first year already follows from BW 7:18 (6:193g j);
    - the conditions page is a placeholder link.
- Owner (16 Nov): 12–24 months is too long ("anything can happen in two years"). The "until the end of the first summer" option was offered; the owner chose **3 months, as most of the market**.
  - Main mockup: the card paragraph opens with "3 maanden aangroeigarantie na levering."; Waarom wij reason 1 reads "3 maanden aangroeigarantie / Slaat een plant niet aan? Dan krijgt u een nieuwe: kosteloos bezorgd of klaargezet in Otterlo."
  - Card heights unchanged; Waarom wij −30 px on phone at 390.
  - The conditions page must say the guarantee comes on top of the legal rights (BW 7:6a). A lawyer checks whether the 1-year presumption (7:18) applies to root-ball plants, and the phrase "De oorzaak hoeft u niet aan te tonen".

## A section heading above the guarantee card (16 Nov), in review

Owner: the assortment and the guarantee card sit close together and have different colours; give the card's block a heading to separate them.

Review page `waarom-kweker/fd-kop.html` (`tools/build_fd_kop.py`; html.fk-0|1|2). The heading uses the assortment H2's type and spacing.
- 1 · Обещание наружу (recommended): the promise "Slaat een plant niet aan? Dan krijgt u een nieuwe." becomes the section H2 above the card, on one line on desktop. On phone (≤860) each sentence gets its own line, at the size it had inside the card. The card then starts with the guarantee paragraph; no repeated headline.
- 2 · Отдельный заголовок: the H2 "Wij staan achter elke plant." above the card; the promise stays in the card.
- Desktop card heights unchanged; no horizontal scroll.
- Option 1 on phone: the card is 728 px at 390 (was 802), plus the heading above it.
- Fable (16 Nov), `waarom-kweker/fd-kop-fable.html` (`tools/build_fd_kop_fable.py`; html.fb-0|1|2).
  - His diagnosis: the clash is not the missing heading or the pill.
    - There is no clean page between the blocks: the field's lower feather ends 2 px above the card at 1440 and 19 px inside the card's top on phone.
    - Temperature: the field ends on its warmest corner (butter yellow), while the card's text panel answers with its coldest (grey-white).
  - On my options:
    - 1 separates, but the heading sits on the tail of the feather, and the card is left without an anchor.
    - 2 is a slogan without a fact, and two H2s in a row.
  - His fb-1 «Воздух и тон»:
    - a band of clean page after the field (pill to card 174 px at 1440, 107 on phone; clean page 63 / 32 px);
    - the desktop text-panel veil turned to warm paper;
    - the text is unchanged.
  - His fb-2: the same plus the heading, my option 1 refined.
    - The H2 is always two lines, question / answer.
    - The card panel opens with "3 maanden aangroeigarantie na levering." as a larger line (28 / 22 / 21 px).
    - No new words.
  - Desktop card heights unchanged; no horizontal scroll; lowest contrast 5.10:1.

## Waarom wij without the repeated guarantee; the transition to the guarantee card (16 Nov), done

Owner: the guarantee now appears twice (Waarom wij reason 1 and the card); replace it. Reason 3 echoed the card's "Bel of app" too: "if you noticed it, it means something", so replace it as well. Also move Fable's transition (option 2) into the main mockup.

In the main mockup (`finalize_main.py`, `tools/founder-helper.css`):
- Waarom wij reasons:
  - Reason 1 (highlighted): "Sterk wortelstelsel uit veenrijke bodem / Onze rhododendrons groeien in de volle grond op veenrijke bodem: de basis om in uw tuin goed aan te slaan." The fact comes from the hero line "Gekweekt op veenrijke bodem, met een sterk wortelstelsel". Why the plants take, while the card says what happens if one does not.
  - Reason 3: "Welkom op de kwekerij / Kom de rhododendrons in Otterlo zelf bekijken en uitzoeken. Dat kan zonder afspraak." The walk-in invitation (owner, 12 Nov) left the card when it became the guarantee block.
  - Reasons 2 and 4 unchanged. The guarantee now appears in the hero H1 (the hook) and in its own block (the promise), not in between.
- The move to the card (Fable's fb-2), pixel-equivalent to option 2 on fd-kop-fable.html at 360–1920 (only sub-pixel antialiasing differs):
  - the field's feather ends, then a band of clean page;
  - the promise "Slaat een plant niet aan? / Dan krijgt u een nieuwe." is the section H2 above the card (id h-kweker);
  - the card has no H2 of its own and opens with "3 maanden aangroeigarantie na levering." at a sub-heading size;
  - the desktop text panel is warm paper instead of cold grey-white.
- Measurements:
  - pill to card: 341 px at 1440 (was 109) and 189 px at 390 (was 56), the heading included;
  - desktop card heights unchanged (608 / 626 / 522 / 495 / 435);
  - the card is shorter on smaller screens: 880 at 768 (was 935), 761 at 390 (was 802), 720 at 360 (was 788);
  - Waarom wij unchanged on desktop, +6 px at 390;
  - no horizontal scroll.

## Weaving the three surfaces together; air above Gert's head (16 Nov), in review

Owner:
- the cut of the portrait is too close to Gert's hair; give the card a little more air above the head;
- the Waarom wij facts card dissolves at the top but shows hard edges at the bottom: either a gentle dissolve at the bottom too, or clear edges everywhere;
- the facts card, the assortment field and the guarantee card must not clash in colour or form: weave them together.

Diagnosis:
- The facts card's top only seems to dissolve because its top colour (#eceee6) is almost the page colour (#f1efea); the bottom is sandy ground (#d9cbb0, #c7b893), so it shows.
- The desktop portrait is 110% of the card height and lifted by 3.3%, and the hair starts 3.9% from the image top: about 6 px of air at 1440.

Review page `waarom-kweker/sv.html` (`tools/build_sv.py`), three switches:
- Края: ek-0 как сейчас; ek-1 the bottom dissolves gently (mask on the background layers only, a long ramp keeping a hint of the edge); ek-2 clear edges everywhere (the top takes a light sage tone #e2e6d7).
- Цвет: ec-0 как сейчас; ec-1 one palette with the assortment field (the sandy ground becomes butter and soft sage: #e6dcb2, #d6cd9c, #ece6cd).
- Над головой (desktop):
  - hd-0 as now;
  - hd-1 portrait scaled to 95%, same bottom; 39 px air at 1440, 31 at 1024;
  - hd-2 scaled to 90%; 73 / 57 px.
  - The image's top edge fades over 3% into the card (backdrop and card top are nearly the same colour), above the hair.
- Recommended system: ek-2 + ec-1 + hd-1. Two cards with the same 28 px radius and clear edges are the objects; the assortment's soft field is the garden air between them; one palette (sage, cream, butter, a faint blush).
- Card heights unchanged; no horizontal scroll.
- Fable's review (16 Nov). The logic is right (two clear cards as objects, the soft field between them) and ek-2 ec-1 hd-1 beats today, but three things fall short. His refinement: `waarom-kweker/sv-fable.html` (`tools/build_sv_fable.py`), state `fk-2 fr-1 fh-2`.
  1. A seam above the scaled portrait: the band above the photo shows the card colour (223,225,226) against the photo backdrop (231,234,233), about 25 px in hd-1. Fix: under the photo, a gradient made of the photo's own top-row colours (#e7eae8 → #dce1e2, fading out by 68%); 1–2 levels left. Same 95% scale and 39 px of air; fallback fh-3, 92.5% (about 56 px).
  2. The "clear edges everywhere" were not yet clear: the top edge ΔE was 4.3–5.1 against the page, and the guarantee card also dissolves at its right side and top-right corner. Fix:
     - a darker top on the facts card, --top:#dee4d1, --b2:#e4e9d8 (ΔE 6.7–7.5);
     - one rim inside both cards, inset 0 0 0 1px rgba(63,74,55,.12) (switch «Кант», fr-0 turns it off).
  3. The butter was too strong (yellow on phone). Lighter: --b3:#eae1bf, --b4:#e0d7ad, --bot:#ede8d4.
- Fable's measurements:
  - guarantee card heights unchanged;
  - facts card heights unchanged;
  - no horizontal scroll;
  - facts text contrast 5.38–9.13:1 on real pixels.
- Open: the fill above the portrait continues the photo's flat backdrop tone (not painted content), the owner decides. The rim is a new device on the approved guarantee card, hence its own switch.
- APPROVED (owner, 16 Nov: "Нравится"): Fable's refinement with the rim, state fk-2 fr-1 fh-2. In the main mockup, `tools/surfaces.css` is appended after `founder-helper.css` in `finalize_main.py`:
  - Facts card:
    - top light sage #dee4d1 / #e4e9d8, so the edge reads on every side;
    - the ground is the field's pale butter (#eae1bf, #e0d7ad, #ede8d4).
  - Both cards carry one hairline inside: inset 0 0 0 1px rgba(63,74,55,.12).
  - Desktop portrait:
    - scaled to 95%, same bottom; about 39 px above the hair at 1440;
    - its top fades over 3%;
    - the strip above it carries the photo backdrop's own top-row colours, so there is no seam.
  - Checks:
    - identical to sv-fable.html fk-2 fr-1 fh-2 at 1920, 1440, 900, 768, 390 and 360; at 1024, 0.04% of pixels differ (antialiasing);
    - card heights, hero, assortment and footer unchanged; no horizontal scroll.

## Sizes 40–225 cm; the assortment pill becomes "Alle maten en prijzen" (16 Nov), done

Owner: "Bekijk alle planten" makes no sense, all seven varieties are already in one row. The sizes on the reseller Rhododendronwal's site are Top's own ("размеры точно наши"): from 40 to 225 cm depending on the variety (`docs/maten-per-soort.md`).

In the main mockup:
- `tools/build_as3_sad.py` (assortment):
  - The lead reads "Van 40 tot 225 cm, afhankelijk van de soort. U bestelt vanaf 1 plant." (was "Elke soort is er in vier maten, van 40 tot 120 cm."). "U bestelt" is glued so no "U" hangs at a line end on phone.
  - The pill reads "Alle maten en prijzen →": the cards show the smallest size only, and the pill leads to every size and price.
- `finalize_main.py` (facts card): "7 soorten / van 40 tot 225 cm" (was "in 4 maten, 40 tot 120 cm").
- Desktop block heights unchanged; facts card −18 px on phone (one line); no horizontal scroll.

Still open for the owner:
- The prices per size.
- Which sizes are sold to private customers.
- The cards still show the site data's smallest band, "vanaf € … 40–60 cm, met kluit". The reseller lists 40–50 / 50–60 as the smallest bands.
- Owner (16 Nov): "why did nothing change in the product block?". The cards still said "40–60 cm, met kluit". Each card now shows its variety's own range (`tools/build_as3_sad.py`, RANGE):
  - Nova Zembla 50 tot 180 cm;
  - Catawbiense Grandiflorum, Cunningham's White and Roseum Elegans 50 tot 225 cm;
  - Catawbiense Boursault 40 tot 180 cm;
  - Ponticum 50 tot 120 cm;
  - Ponticum Roseum 40 tot 160 cm;
  - each followed by ", met kluit".

  "vanaf € …" stays the smallest size's price from the site data. The aria-label reads "…, vanaf € 29, van 50 tot 180 cm". One line on every card at 360–1920 (narrowest card 154 px); block heights unchanged.

## Typeface (17 Nov), in review

Owner: approve the font before phase 1 of the improvement plan (the type scale depends on it). Today the whole page uses one font, Manrope.

Review page `waarom-kweker/fonts.html` (`tools/build_fonts.py`; html.ff-0..4), all Google Fonts:
- 0 · Manrope (now).
- 1 · Fraunces headings (soft serif, 480) + Manrope text. Recommended: warm and organic, fits a family nursery since 2001, premium and calm; the body stays the approved Manrope.
- 2 · Newsreader headings (editorial serif, 500) + Inter text: calm, trustworthy.
- 3 · Instrument Serif headings (400) + Instrument Sans text: the most elegant, but thin and condensed; the facts numbers turn fragile.
- 4 · Hanken Grotesk (one sans): like now, a little more neutral.

The heading font goes to the H1, the section H2s, the facts numbers and the guarantee's lead line. Card names, reasons, prices and text use the text font. Sizes are unchanged; the scale is consolidated in phase 1 after the choice.
- Fable (17 Nov) recommends **Newsreader 500 (headings) + Manrope (text)**: state ff-5 on `waarom-kweker/fonts-fable.html` (`tools/build_fonts_fable.py`; also ff-6 Source Serif 4 + Manrope, ff-7 Fraunces 430 / SOFT 30).
  - Fraunces at 480 / SOFT 50 is heavy and "puffy" on dark-on-light H2s, closer to a craft DTC brand than a calm nursery. Its quirky figures (2, 7, 1) distract in the facts. It is wider: "geen minimumbestelling" wraps at 390 and the guarantee line breaks on desktop. The lighter ff-7 changes little.
  - Newsreader is narrower and lighter, with classic figures; "aangroeigarantie" sits evenly, the facts don't wrap, and the H1 reads over the photo.
  - On the other candidates:
    - Manrope looks like the competitors;
    - Newsreader + Inter: Inter is wider and more anonymous, and the approved Manrope would go;
    - Instrument is weak on phones for 45+;
    - Hanken is just a bold grotesque.
  - His settings:
    - Weight and tracking: weight 500, font-optical-sizing auto; H1 −0.018em, H2 −0.014em.
    - Figures: facts numbers in the heading font, lining figures; prices and phones in Manrope, tabular-nums.
    - The guarantee lead line goes back to Manrope 600.
    - URL: Newsreader:opsz,wght@6..72,500 and Manrope:wght@400..700.
  - Risks:
    - the H1 on phone is lighter (raise it to 550–600 if it looks weak);
    - Newsreader is a little more "newspaper" than "garden".
- APPROVED (owner, 17 Nov): **Newsreader + Manrope**. In the main mockup:
  - Fonts: the Google Fonts link loads Manrope 300..800 and Newsreader opsz 6..72, weight 500. `tools/fonts.css` is appended after surfaces.css in `finalize_main.py`.
  - Newsreader 500 (optical sizing, lining figures) goes to the H1, the section H2s and the facts numbers. Letter-spacing: H1 −0.018em, H2 −0.014em.
  - Manrope stays for everything else, including the guarantee lead line.
  - Unlike Fable's review page, the logo wordmark keeps its font: only the headings are targeted, the shared --font-display variable is not changed.
  - Checks:
    - equal to fonts-fable.html ff-5 below the header (0.01–0.06% antialiasing);
    - desktop block heights unchanged; Waarom wij 8–10 px shorter on phone;
    - no horizontal scroll.
  - The type scale (19 sizes → 6–7 steps, serif-aware) follows in phase 1 of `docs/plan-verbeteringen.md`.

## Phase 1, step A: type scale and section rhythm (17 Nov), approved

Plan items 1.4, 1.5 and 1.6 (`docs/plan-verbeteringen.md`). Review page `waarom-kweker/fase1a.html` (`tools/build_fase1a.py`; html.sc-0 до / sc-1 после); the CSS is `tools/scale.css`, written so it can be appended to the main build unchanged.

Type scale:
- 19 sizes become 7 steps (desktop / phone): display 66 / 34 (H1), heading 48 / 30 (H2s; facts numbers on desktop), sub 24 / 22 (reasons, prices, phone numbers, the guarantee's lead line, facts numbers on phone), lead 18 / 17 (hero line, assortment lead, the guarantee paragraph), body 16, small 14, micro 13 (the minimum; the card size line was 12.5 on phone).
- The first Waarom wij reason is no longer larger than the others (36 vs 27 px).
- The guarantee paragraph goes from 15.5–16.5 to 18 / 17 px.
- On phone the Waarom wij H2 wraps "Wij kweken alleen / rhododendrons." (text-wrap: pretty).

Rhythm:
- Measured content-to-content, the gaps hero→Waarom wij / Waarom wij→assortment / assortment→guarantee heading were 101 / 37 / 63 px at 1440 and 64 / 16 / 32 px at 390.
- They are now one rhythm: 101 / 101 / 100 at 1440, 72 / 72 / 72 at 1024, 64 / 64 / 64 on phone.

Checks:
- Measured: exactly 7 sizes at 1440 and 390; desktop guarantee card heights unchanged; no horizontal scroll.
- The phone card is longer: 776 px at 390 (was 761) and 770 at 360 (was 720), from the larger guarantee text.
- Owner (17 Nov): the first Waarom wij reason was highlighted for the guarantee; now that the guarantee has its own block, make it the same as the others. Done in the main mockup:
  - The `kt-hl` class is removed from the first reason (`finalize_main.py`), and its rules (larger H3, tighter tracking, larger and darker text) are removed from `tools/k-tekst.css`.
  - All four reasons now share the same H3 size and letter-spacing and the same text size and colour, in the main mockup and on fase1a.html.
- APPROVED (owner, 17 Nov): step A goes into the main mockup. `tools/scale.css` is appended after fonts.css in `finalize_main.py` (`__R__` → `:root`, `__S__` → empty). The main mockup is pixel-identical to fase1a.html sc-1 at 1920, 1440, 1024, 768, 390 and 360; no horizontal scroll.

## Phase 1, step B: hero and Waarom wij copy (17 Nov), approved

Plan items 1.1, 1.2, 1.3 and 1.7 (`docs/plan-verbeteringen.md`). Review page `waarom-kweker/fase1b.html` (`tools/build_fase1b.py`); html.sb-0 до / sb-1 после, html.hl-a / hl-b chooses the hero line. All new Dutch copy is a draft.

- 1.1 The H1 breaks by meaning: "Rhododendrons / die aanslaan. / Met aangroeigarantie." at every width from 360 to 1920 (two lines, "Rhododendrons die aanslaan. / Met aangroeigarantie.", where the first sentence fits, e.g. 600 px).
  - "die aanslaan." and "Met aangroeigarantie." are nowrap groups, so "Met" is never left alone (it was at 1366–1440 and on 820–900 px tablets).
  - "Met aangroeigarantie." is about 9.7 em wide, so the H1 column grows with the display size: desktop 36rem up to 40rem (the 1600 px value), tablet portrait 21.5rem up to 29rem. The scrim edge (--tc) follows.
- 1.2 The hero line no longer repeats Waarom wij (veenrijke bodem, vers gerooid, eigen transport are all there). Two drafts:
  - A "Rechtstreeks van onze familiekwekerij in Otterlo, sinds 2001."
  - B "Van onze familiekwekerij in Otterlo: zeven soorten, van 40 tot 225 cm."
- 1.3 Waarom wij: the two Otterlo reasons ("Welkom op de kwekerij", "Eigen transport of afhalen") become one, "Bezorgd of zelf uitzoeken: Wij bezorgen met eigen transport door heel Nederland. Of kies uw planten zelf uit in Otterlo, ook zonder afspraak."
  - With three reasons the list is shorter than the facts card, so on desktop the card follows the list, as before: it ends on the list's last line and the four facts share its height in equal slots.
- 1.7 Groothandel: in the hero a white underlined text link with an arrow instead of a second button; in the menu the same weight and colour as the other items.

Checks:
- "До" is pixel-identical to the main mockup at 1920, 1440, 1024, 900, 390 and 360.
- Waarom wij is shorter by 147 px at 1920, 146 at 1440, 128 at 1024 and 768, 103 at 390 and 128 at 360.
- The H1 has 3 lines everywhere; no horizontal scroll.
- APPROVED (owner, 17 Nov): step B goes into the main mockup with hero line A, "Rechtstreeks van onze familiekwekerij in Otterlo, sinds 2001."
  - `finalize_main.py`: reason 3 becomes "Bezorgd of zelf uitzoeken" and reason 4 is removed; reps for the H1 groups and break, the hero line, the hero link and the menu item; CSS in `tools/fase1b.css`, appended after scale.css.
  - The menu item gets the same classes as the other items (no override).
  - Two refinements over fase1b.html:
    - The hero link is `<a class="hero-link"><span>Groothandel</span><svg/></a>`. Only the word is underlined (on the review page the arrow had its own underline), the arrow is the main button's arrow, and the link is 48 px tall like the button.
    - 360–374 px: the button and the link need 333 px and the row has 320, so the link wrapped to a second row, 8 px in from the left. Now the button's side padding is 16 px (was 20) and the link's margin is 2 px (was 8): one row, 315 px.
  - Checks: the main mockup equals fase1b.html (sb-1 hl-a) pixel for pixel at 1920–390 except the arrow; H1 3 lines and no horizontal scroll at every width; guarantee card heights unchanged (608 / 626 / 522 / 495 / 435 at 1920 / 1440 / 1200 / 1024 / 900).
  - `tools/build_fase1b.py` builds from the main mockup as it was before step B; it no longer runs against the new one.

## Phase 1, step C: links, header actions, cart, phone menu, accessibility (17–18 Nov), approved

Plan items 1.8 and 1.9 plus the link map the owner approved on 17 Nov. Review page `waarom-kweker/fase1c.html` (`tools/build_fase1c.py`). The step itself is `tools/fase1c.py` (`apply(html)`, with `fase1c.css` and `fase1c.js`), so the main build can apply the same function after approval.

Links (the same addresses as the live site, gadzhaprod/rhododendrons):
- logo → /; Planten → /assortiment; "De kweker" becomes "Over ons" → the Waarom wij block (on the live site "Over ons" was this block too, /#over-ons); Advies → /plantgids; Groothandel in the menu and the hero → /groothandel; Bestellen → /assortiment.
- "Bekijk de planten" → the seven varieties on the page: smooth scroll, the heading lands 40 px (phone 24 px) under the header, focus moves there.
- The cards → /assortiment/<variety> (the live site's slugs); "Alle maten en prijzen" → /assortiment; "Lees de voorwaarden" → /garantie (the new guarantee page; the live site's Artikel 4 conflicts with the new promise and has to be rewritten).
- In the mockup, a link to a page that is not in it shows a short note, "Assortiment: deze pagina volgt /assortiment", instead of leading nowhere.
- Before: Planten, Bestellen and "Bekijk de planten" pointed to #planten, which does not exist; Advies to #advies, which does not exist; both Groothandel links to "#"; De kweker to the guarantee block.

Header (owner, 17 Nov: one main action per screen):
- Order on desktop: phone number · Bestellen · cart, with the menu in the true centre (it was offset by the right-hand group), so the right-hand group can change width without moving it.
- Review option bs-1, "Bestellen" after the first screen:
  - While the hero's "Bekijk de planten" is visible, the header has no Bestellen pill.
  - Once that button has scrolled under the header, the pill opens in its slot (0.5 s; the phone number slides left, the cart stays on the right edge). bs-0 keeps it always.
  - The hidden pill is not focusable.
- 1024–1179 px: the number becomes the round phone button (as on tablets), so the centred menu keeps at least 88 px from the right-hand group in both states.
- Cart: a bag icon, always visible, with a count badge (hidden at 0). It opens a drawer (right side, full width on phone):
  - "Winkelwagen", "Uw winkelwagen is nog leeg", "Kies een soort en een maat. U bestelt vanaf 1 plant.", "Bekijk de planten" (closes and scrolls to the varieties).
  - A footer "Liever persoonlijk bestellen? Bel of app de kwekerij." with Bellen / WhatsApp.
  - A dialog: Escape and the backdrop close it, focus stays inside and returns to the cart button. Dutch copy is a draft.
- Phone menu (was a button that opened nothing): drops down under the bar.
  - Planten, Over ons, Advies, Groothandel in Newsreader 24 px, then Bestellen, then Bellen / WhatsApp.
  - The burger turns into a cross. Escape, the backdrop and any link close it.
- Phone header, review option (360 px has room for two round buttons next to the logo, not three):
  - tp-a: call + menu, with the cart as a row in the menu;
  - tp-b: cart + menu, with calling in the menu.

Accessibility (1.9):
- A skip link "Naar de inhoud" as the first Tab stop (to `main`).
- The hero photo has alt "Ons rhododendronveld in Otterlo, in bloei" (it was hidden from screen readers).
- The page title is the live site's: "Top Rhododendrons | Kwekerij in Otterlo, sinds 2001".
- Menu items are 40 px tall (were 21); the phone numbers and the address in the guarantee card and the footer have a 30 px hit area (were 22) with no layout change.
- WhatsApp and the map open in a new tab.
- Measured: no text under 13 px and no target under 24 px at 1440 and 390.
- The "Top Rhododendron" alt typo from the review is no longer in the page.

Checks:
- Page height, guarantee card and footer heights are identical to the main mockup at 1920–360, and there is no horizontal scroll.
- No script errors.
- Owner (17 Nov): the bare number in the header ("06 20 10 43 12" with a phone icon) is not good enough.
  - A first round with Gert's face next to the number was rejected ("точно не фото"). The avatar file is removed.
  - Second round, five review options on fase1c.html, built from 21st.dev patterns (Text Roll and Action Swap Cascade, Expand Button, Popover) without their React/Motion code. Below 1180 px every option is the round phone button.
    - ph-0: as before.
    - ph-1: the icon in a soft green circle, "Bel de kweker" (13 px) over the number (15 px semibold); from 1240 px.
    - ph-2 (recommended): the header says "Bel de kweker" with the phone icon.
      - On hover or keyboard focus the letters roll one by one into "06 20 10 43 12" (26 ms stagger, springy easing). Both lines sit in one grid cell, so nothing moves.
      - A click calls, and the number is in the link's label for screen readers. With reduced motion the swap is a plain fade.
    - ph-3: a round phone button that opens to the left into a pill with the number on hover, and the phone icon rings once; from 1240 px.
    - ph-4: "Bel of app" as a quiet pill that opens a card: "Bel of app de kwekerij / Vragen over soort, maat of levering", Bellen 06 20 10 43 12, WhatsApp 06 20 29 78 49. From 1240 px.
  - With the menu centred, the gap to the phone is at least 81 px in every option and state.
- Fable (17 Nov) ranked the options with the number always visible (desktop visitors read it and dial on their mobile; hover-only options fail on touch laptops and for older buyers) and built ph-5: "Bel de kweker" over the number, no circle (`fase1c-fable.html`).
- Owner (18 Nov): "is the number needed in the header at all? it loads the header". Fable agreed and changed his advice, building ph-6:
  - On desktop the number does not do its job: no one calls from a browser, and the question comes up at the guarantee or a plant, not in the header.
  - It is the heaviest element in the header.
  - Trust comes from an easy-to-find contact with a person behind it.
  - So: no number on desktop and a fifth menu item "Contact" → the guarantee block with Gert and both numbers (both visible after the scroll at 1280, 1440 and 1920).
  - Phone: keep the round call button and Bellen / WhatsApp in the menu.
- Owner (18 Nov) asked why "Bestellen" appears only after the first screen and where it leads:
  - It leads to the catalogue (/assortiment: variety, size, quantity, cart).
  - On the first screen "Bekijk de planten" already does that job; two buttons with one meaning compete.
  - Once that button has scrolled away, "Bestellen" takes over, so ordering stays one click away for the rest of the page.
- APPROVED (owner, 18 Nov): step C goes into the main mockup with no number on desktop plus "Contact", "Bestellen" after the first screen, and the phone header call + menu.
  - When the cart has items, the count shows on the header cart (desktop) and on the menu button and the menu row (phone). This was Fable's condition for the call + menu option. `window.tbCart(n)` shows it in the mockup.
  - `tools/fase1c.py`, `fase1c.css` and `fase1c.js` now hold only the approved version and are applied by `finalize_main.py`.
  - The reviewed version with all options is `tools/fase1c_review.*` (used by `build_fase1c.py` for fase1c.html).
  - At 1024–1179 px the cart no longer has a ring: there is no round phone button next to it any more.
  - Checks:
    - The main mockup equals fase1c-fable.html (bs-1, tp-a, ph-6) pixel for pixel at 1920, 1440, 1280, 900, 390 and 360, at the top and after scrolling. The only difference is that ring at 1024.
    - Page heights are unchanged from before step C, and there is no horizontal scroll.
    - No text under 13 px and no target under 24 px.
    - No script errors.
    - The links, cart drawer, menu, Escape and focus return work.

## Phase 2, item 2.1: Hoe het werkt (18–19 Nov), approved

Review page `waarom-kweker/fase2a.html` (`tools/build_fase2a.py`, CSS `tools/hoe-werkt.css`). The block replaces the placeholder between the guarantee and the footer.

- Round 1 was rejected by the owner (18 Nov: "not our style at all"). It had icons in circles, "STAP 1" labels in capitals, payment chips and white cards: none of these exist anywhere on the page. The 21st.dev layouts were taken over with their details, and only the colours and fonts were changed.
- Round 2 uses only the page's own language:
  - Newsreader headings on the left.
  - Rows on hairlines with no icons (the Waarom wij list).
  - Large Newsreader figures in moss with Manrope text under them (the facts card).
  - The woven sage-cream surface with one inner hairline.
- Round 2 options:
  - hw-a Rijen: figure | title | text on one row, a hairline above each row.
  - hw-b Kolommen: four columns divided by hairlines, the figure on top. Two by two on tablets; rows on phone, the same as A.
  - hw-c Veld: the same columns inside one woven panel.

Copy (draft): H2 "Van ons veld naar uw tuin, / in vier stappen."
1. "Kies soort en maat: Bij elke soort staan alle maten met hun prijs. Kies er het aantal bij."
2. "Bestel online of telefonisch: Via de webshop of per telefoon. U betaalt met iDEAL, per overschrijving of bij ontvangst; zakelijk op factuur."
3. "Spreek de dag af: Samen kiezen we de dag van bezorgen of afhalen, wanneer het u uitkomt."
4. "Bezorgen of afhalen: Bezorgkosten hangen af van afstand en aantal; u ziet ze vóór u betaalt." Then "Afhalen: Esserbroekweg 2, Otterlo. Ma–vr 08:00–17:00, za 09:00–13:00."

- The steps say what happens and when; the reasons (fresh dug, own transport) stay in Waarom wij.
- The delivery cost sentence is provisional; the founder confirms it.
- No button in the block: "Bestellen" is in the header there.
- Rhythm: guarantee card → H2 and last step → footer are one --sec (100 / 72 / 64 px).
- Heights at 1440: A 833, B 537, C 635 px; at 390: A 781, B 778, C 902.
- No horizontal scroll, no text under 13 px, no target under 24 px.
- Owner (18 Nov) on round 2: "you just reused the cards from our other blocks, I saw nothing new; round 1 had none of our design handwriting". Round 3 is a new composition in the page's handwriting:
  - hw-d "Van veld naar tuin":
    - One rounded object with the woven sage-cream surface and the inner hairline.
    - At the top, our field (`img/hw-veld.webp`, a crop of hero-field.jpg) melts into a garden (`img/hw-tuin.webp`, a crop of the Cunningham's White bush beside a garden path from the old site). Both fade down into the "soil" (the real-photo-into-gradient move of the guarantee portrait).
    - Below them, the steps are a route of four Newsreader verbs at the heading size, each followed by a thin moss line that runs on to the next: Kiezen, Bestellen, Afspreken, Ontvangen.
    - On phone the route is a stem with four branches.
  - hw-e "Woorden": the route alone, on the page.
  - Copy:
    - Kiezen: "Soort, maat en aantal. Bij elke soort staan alle maten met hun prijs."
    - Bestellen: "Online of per telefoon. U betaalt met iDEAL, per overschrijving of bij ontvangst; zakelijk op factuur."
    - Afspreken: "Samen kiezen we de dag van bezorgen of afhalen, wanneer het u uitkomt."
    - Ontvangen: "Bezorgd of afgehaald. De bezorgkosten hangen af van afstand en aantal; u ziet ze vóór u betaalt." Then "Afhalen: Esserbroekweg 2, Otterlo. Ma–vr 08:00–17:00, za 09:00–13:00."
  - Heights at 1440: D 878, E 492 px; at 390: D 942, E 734. Rhythm 100 / 72 / 64. No horizontal scroll, no text under 13 px.
  - Fable builds an independent concept in parallel (`fase2a-fable.html`).
- Fable's independent concept (18 Nov), `fase2a-fable.html` ("De trap", the staircase):
  - Desktop, from 1100 px: the four steps stand as stairs. One hairline steps down from the heading to the right, with a small Newsreader figure in moss on each tread and the title and text under it.
  - Two real photos sit in opposite corners and dissolve inwards into the woven haze: our field (`B2BHERO-sm.webp`) under steps 1–2, bottom left; the garden bush (`cw-bush.webp`) above step 4, top right.
  - Tablet (700–1099): the steps as a list, with one tall picture where the field melts into the garden.
  - Phone: field strip → four steps → garden photo.
  - Step 4 links the address to the map.
  - Checked at 1920–360: no horizontal scroll, smallest text 14 px, lowest contrast 7.04:1 (measured on the real pixels), rhythm --sec.
  - Height 767 px at 1440, 1073 at 390.
- Owner (18 Nov): "give Fable the task of designing this block; let him use every tool, search the web if needed". Fable's final, `fase2a-fable2.html` ("De trap", second version):
  - Research:
    - Bower & Branch "How it works": buyer verbs, phone next to online, the agreed day as its own step.
    - Sarah Raven "Delivery": practical facts as label | value pairs.
    - 21st.dev 19074 "Editorial Collage Hero": two photos on a soft haze as one picture.
    - Rejected as anti-patterns: list-beside-photo and the round 1 widgets (21st 26064, 46738, 26891, 26916, 19861).
  - A rejected alternative, "Diagonal": the field top left melting into the garden bottom right. Heavier (about 950 px) and a muddy middle.
  - Changes against the first staircase:
    - The field lies under the stairs. It fades along a line parallel to the steps (16°) and dies out to the right, so line, fade and treads share one diagonal.
    - The stairs hold at every width: four treads in a row from 980 px, a steep stair (one step per row, each shifted right) at 700–979 and on phone.
    - Pickup is label | value pairs (Afhalen / Open), like the phone numbers in the guarantee card.
    - A visible focus on the address link and a selection colour from the palette.
  - The field photo is `img/hw-fable-veld.webp`: the same real B2BHERO shot at 1800 px from `mockup-v3/src/assets/img/`, for retina.
  - Checked at 1920–360:
    - No horizontal scroll; smallest text 14 px.
    - Lowest contrast 5.12:1, measured on real pixels.
    - Rhythm --sec.
    - Height 788 px at 1440, 711 at 1024, 1135 at 390.
  - Fable overwrote the tracked `img/hw-veld.webp` by mistake and restored it with git; the repository shows no change to it.
- Owner (18 Nov): "let him think about more variants". Fable, `fase2a-fable3.html` (review bar: 0 Лестница, 1 Поле, 2 Фраза, 3 Лист).
  - 1 "Veld": one photo carries the block. Under the heading the field fills the screen width, appearing from the page colour and running into the footer's dark green; the four steps are written light in that dusk (2×2 on desktop). Ideas from the page's own hero and 21st.dev 19077 (Editorial Image Hero). 900 px at 1440, 844 at 390. Bottom gap is not --sec, because it merges with the footer.
  - 2 "Zin": the heading continues as one sentence in the same type, in moss: "¹Kies soort en maat, ²bestel online of telefonisch, ³spreek met ons de dag af en ⁴laat bezorgen, of haal af in Otterlo."
    - Small real photos sit in the line like words; the details are numbered footnotes beside it.
    - Ideas from 21st.dev 46739 (Scroll Fill Headline) and 19322 (Image Text).
    - 501 px at 1440, 721 at 390, the most compact.
  - 3 "Blad": one tall picture in a frame, where the field melts into the garden bush; the steps are captions left and right, tied to it by hairlines, like a botanical plate. Idea from 21st.dev 28273. 819 px at 1440, 871 at 390.
  - Fable's ranking: 0 staircase > 2 sentence > 3 plate > 1 field. He would show the staircase and the sentence as the two real choices.
  - Checked at 1920–360: no horizontal scroll; smallest text 13.5 px; lowest contrast 5.11:1.
- Owner (18 Nov): "of all the variants, D is the one". Refine it, and try other pictures (from the internet or generated) to see how it looks, since reusing the page's own photos is weak. Review page `fase2b.html` (`tools/build_fase2b.py`, CSS `tools/hoe-werkt-d.css`); the review bar switches the photo set.
  - Refinements over hw-d:
    - The panorama is taller on desktop (clamp 240–390 px).
    - A soft mist where the two photos cross, so the meeting reads as air, not as a double exposure.
    - The line stops 14 px short of the next verb; the verbs sit fully below the photos.
    - A taller panorama on phone (190–270 px).
    - Fixed: the route's padding was reset by `.hw ol{padding:0}`.
  - Photo sets:
    - ps-0: our photos.
    - ps-1: a rhododendron nursery field on dark peat soil in Edewecht (Ammerland) melting into a pink rhododendron on a lawn at Bowood.
    - ps-2: green nursery rows in Edewecht melting into rhododendrons along a garden path.
  - The example photos are from Wikimedia Commons (CC BY-SA 4.0 and CC0; authors and links in `img/voorbeeld/CREDITS.md`), cropped and in two cases mirrored. They are another nursery's field and other gardens: only for the preview, never for the live site, which uses the nursery's own photos (phase 3).
  - The review page shows a small credits line under the block when an example set is on.
  - Unsplash was not used: its internal search was refused by the session's permission check. Pexels and Pixabay block automated access; not worked around. No image generation tool is available in this session.
  - Heights at 1440: 927 px with our photos, 961 with an example set (the credits line); at 390: 971 / 1066. Rhythm 100 / 72 / 64. No horizontal scroll.
- Owner (18 Nov), D round 2: "take only c08, one photo in the card; remove the opening hours in Ontvangen; move all the steps down to the bottom of the card, keeping the balance".
  - One photo across the card: `img/voorbeeld/hw-v3-veld.webp`, the Edewecht nursery field with flowering bushes on peat soil, uncropped. It is an example photo (Wikimedia Commons, JoachimKohler-HB, CC BY-SA 4.0), so the live site needs the nursery's own field photo.
  - The photo is 36vw high (300–520 px), about 73 % of the card at 1440, and fades into the soil.
  - The route of verbs stands at the bottom, pulled up into the fade by 20–40 px. Its side and bottom padding are one value (clamp 28–52 px; 49 px at 1440), so the steps sit with the same air left, right and below.
  - "Ontvangen" ends with "Afhalen: Esserbroekweg 2, Otterlo." (no hours; they are in the footer).
  - The photo-set switch is gone; the review page keeps the credits line.
  - Card 708 px at 1440, 589 at 1024, 808 at 390. No horizontal scroll.
- Owner (18 Nov), D round 3: "we lost the step between blocks again: this card looks very much like the guarantee card, in its form and its whole treatment". Review page `fase2c.html` (`tools/build_fase2c.py`, CSS `tools/hoe-werkt-d.css` + `tools/hoe-werkt-open.css`):
  - hv-0: the card, as before, for comparison.
  - hv-1 "open":
    - No card, no frame, no rounded corners. The field runs edge to edge across the screen, 38vw high (300–640 px; 240–360 on phone).
    - It appears out of the page colour at the top (0–18 %) and dissolves back into it at the bottom (58–100 %).
    - The route of verbs stands on the page where the field has dissolved, aligned with the page's text column.
    - The guarantee stays an object in a frame; this block is an open landscape, so the two blocks no longer repeat each other.
  - An option with the heading in the field's sky was tried and dropped: over the trees it read worse.
  - Heights at 1440: 965 px with the credits line; at 390: 1025. Rhythm 100 / 72 / 64.
  - No horizontal scroll; no text under 13 px; no target under 24 px.
- Owner (18 Nov): "let Fable look and analyse". Fable's analysis of hv-1 and fixes, `fase2c-fable.html` (button "2 · После правок Фабла", CSS only, under html.hv-2):
  - Verdict: hv-1 solves the complaint (no frame, no photo dissolving into a soft surface; an open landscape after an object in a frame). It does not repeat the hero (dark, full screen, white text on the photo); the field at the start and at the end frames the page. It is worth taking, but not as it was.
  - Problems found:
    - The bottom fade started at 58 % while the bushes stand at about 80 %: half of the bushes were in a grey mist (about rgb 162 158 156 against the page's 241 239 234), and the peat soil hardly showed.
    - The white sky was lighter than the page.
    - The verbs went 49–60 px into the photo, "Ontvangen" on a pink haze and the others on grey.
    - At 600–860 px the route was one list with 681 px lines.
    - On 1366×768 the band left the descriptions below the fold.
  - Contrast was fine: verbs from 9.6:1, text 5.66:1.
  - Fixes in hv-2:
    - The crop is lower and the fade shorter (from 70 % on desktop, 76 % on phone), so the bushes are whole and the soil fades.
    - The photo is multiplied with the page colour, so the sky becomes the page and there is no grey mist.
    - The verbs go only 20 px into the photo, all on one background; contrast from 11.8:1.
    - The route is 2×2 at 600–860 px, aligned with the heading.
    - The band height is tied to the viewport (at most 58 % of it on desktop, 52 % on phone): 445 px on 1366×768, and the block is 956 px at 1920 instead of 1044.
  - Not built, for the owner:
    - The verbs one step smaller than the heading.
    - The pickup address as a map link, as in the footer.
    - Screens wider than 1920 (the nursery's own photo needs 2880 px or more).
  - Photo brief from the analysis: the bushes in the middle third, the soil in the bottom third, a calm background without loud green, no bush cut off at the right.
  - Heights after the fixes: 963 px at 1440, 861 at 1024, 877 at 768, 1039 at 390.
- APPROVED (owner, 19 Nov): Fable's fixed open version goes into the main mockup (`tools/hoe_werkt.py`, CSS `tools/hoe-werkt-main.css`, applied by `finalize_main.py` after fase1c).
  - The verbs are one step below the heading (owner): the sub step, 24 px on desktop, 22 on phone (were the heading size, 48 / 30).
  - Pickup in "Ontvangen" is the owner's map pin from a phone screenshot: 52.0914891, 5.7283254, plus code 3PRH+H8W Wekerom.
    - OpenStreetMap places it on Apeldoornseweg, 6733 SC Wekerom (Ede); it has no house number.
    - The text is "Afhalen: Apeldoornseweg, Wekerom", a link to those coordinates on Google Maps (new tab).
    - The pin is about 1.9 km from Esserbroekweg 2, Otterlo, the "kwekerij & kantoor" address on the old site and in the footer's "Bezoek". The owner decides which address goes where (plan 3.14).
  - Under the block, a 13 px Dutch credit line for the example photo: "Voorbeeldfoto, niet van onze kwekerij: …, JoachimKohler-HB, Wikimedia Commons, CC BY-SA 4.0". The nursery's own photo replaces it (plan 3.13).
  - The tablet layout (2×2) now runs at 600–860 px and the phone stem below 600.
  - Checks at 1920×1080 to 360×780:
    - The rhythm (guarantee card → heading, credit line → footer) is one --sec.
    - The band is 626 px at 1920, 522 at 1440, 445 on 1366×768, 380 on tablets, 265 at 390.
    - Block height 946 px at 1440, 992 at 390.
    - No horizontal scroll, no text under 13 px, no target under 24 px, no script errors.
- Owner (19 Nov): the map pin is the field; Esserbroekweg 2 is the office. Main mockup:
  - "Ontvangen" in Hoe het werkt: pickup at the field, as above.
  - Footer "Bezoek": the field ("Kwekerij", Apeldoornseweg, Wekerom, linked to the pin), the hours and "Zonder afspraak welkom".
  - Footer "Contact": a new last row "Kantoor", Esserbroekweg 2, 6731 DB Otterlo, as plain text with no map link, so visitors are not sent to the office.
  - The footer's map link carries target and rel in `finalize_main.py`; the old Esserbroekweg rep left `tools/fase1c.py`.
  - The brand line "Familiekwekerij in Otterlo", "kies uw planten zelf uit in Otterlo" (Waarom wij) and "klaargezet in Otterlo" (guarantee) are unchanged: the field lies between Otterlo and Wekerom.
- Owner (19 Nov): link the office to the map as well (the labels say which is field and which is office); the hours are certain.
  - "Kantoor" now links to Esserbroekweg 2, 6731 DB Otterlo through the Google Maps URL scheme, in a new tab.
  - Both links open the place in Google Maps (app or browser), where "Route" starts the navigation. The field has no house number, so the coordinates are the exact target.
- Owner (19 Nov): he likes the field photo; the bush on the right is cut — can more of it be shown? No: the original (5400 × 3600) ends at that bush too, and the bush stands in front of the second large bush, so cropping it away would cut that bush. Crop options on `fase2c`-style review page `fase2e.html` (`tools/build_fase2e.py`):
  - fc-0: as now.
  - fc-1 "soft sides": the left and right edges dissolve into the page like the top and bottom (left 0–9 %, right 78–100 %), so the cut bush melts away instead of being cut by the screen edge.
  - fc-2 "mirrored": the photo flipped, with soft sides; the cut bush moves to the left edge and the open field runs on to the right.
  - Block height unchanged (946 px at 1440); no horizontal scroll.
- Owner (19 Nov) asked whether the guarantee block and Hoe het werkt sit too close; sent to Fable for a professional read.
- Fable (19 Nov), the guarantee → Hoe het werkt transition, `fase2d-fable.html` (review bar "Переход"):
  - The owner's eye is right: this transition is about half the others. Measured from the end of one block's content to the next heading:
    - Waarom wij → assortment: 197 / 139 / 128 px (1440 / 1024 / 390).
    - Assortment → guarantee: 211 / 151 / 139.
    - Guarantee card → Hoe het werkt: 100 / 72 / 64.
  - Formally every gap is --sec, but the other blocks add their own inner padding and this one does not.
  - The heaviest object on the page (the guarantee card, 626 px) sits right above, and two large serif H2s follow each other.
  - My earlier statement "the same gap as everywhere" was wrong: it compared the --sec value, not the gaps as they appear.
  - Options:
    - sp-0: as now.
    - sp-1 "more air": the gap above the heading matches the other transitions (200 px at 1440, 128 on phone). Recommended.
    - sp-2 "field first": the field follows the card (125 / 80 px) and the heading stands under it with the steps. Breaks the page's "every block starts with its heading" and puts the two photos close together.
  - No divider or tone change needed: there are none elsewhere, and the full-width field already changes tone.
- Owner (19 Nov) chose Fable's sp-1 "more air", and the photo as it is (no soft sides).
  - The top fade of the field is shorter (owner: the tops of the bushes too faded): 0–10 % on desktop (was 0–20 %), 0–9 % on phone (was 0–16 %). The bottom fade is unchanged.
  - In the main mockup (`tools/hoe-werkt-main.css`), the heading's top padding is 2 × --sec minus the guarantee section's bottom padding.
  - Gap guarantee card → "Van ons veld" heading: 200 px at 1440, 143 at 1024, 128 on phone.
  - The other transitions are 197 / 211 px at 1440 and 128 / 139 on phone.
  - Credits line → footer: one --sec.
  - No horizontal scroll, no text under 13 px, no target under 24 px, no script errors.
- Fable (19 Nov) on the shorter top fade, `fase2f-fable.html` (review bar "Верх фото"):
  - The 200 px gap and the heading → photo link are fine.
  - But on desktop and tablet (600 px and wider) the new top reads as neither a fade nor a clean edge. The photo reaches full strength within 24 px, and the row colour drops from the page colour (241, 239, 234) to (137, 154, 135) at 1440. At that height the frame shows dark foliage, not sky, so the multiply cannot help: a blurred straight band across the tree tops, 35 px under the heading.
  - Phone is fine: the sky meets the page softly.
  - Fable's tf-1: the bushes keep their place and scale, full strength from the first pixel. The photo shows 56–104 px more of itself above them (92 px at 1440), and only that added strip of trees and sky dissolves.
    - Heading → photo at full strength: 101 px at 1440. The block is about 70 px taller.
    - The frame is taller (more trees), the width unchanged.
    - If "the photo as it is" includes the height, his fallback is a fully sharp top edge.

## Phase 2, item 2.2: the guarantee conditions page (19 Nov), in review

`waarom-kweker/garantie.html` (`tools/build_garantie.py`, CSS `tools/garantie.css`): the target of "Lees de voorwaarden".
- Built from the main mockup's header, cart, phone menu and footer. On this page the homepage anchors become notes, and "Bestellen" is visible from the start (subpage).
- Copy: the Dutch draft from the guarantee report, rewritten for 3 months after delivery and for pickup at the field. It is a draft: the owner confirms it and a lawyer checks it (plan 3.12), and a small "Concepttekst" pill says so on the page.
- Structure:
  - Breadcrumb; H1 "Slaat een plant niet aan? / Dan krijgt u een nieuwe." (the display step).
  - Lead: "3 maanden aangroeigarantie na levering, bovenop uw wettelijke rechten …".
  - Four promises on hairlines: 3 maanden · Zelfde soort en maat · Kosteloos · Foto's volstaan.
  - Desktop: a sticky "Op deze pagina" list on the left and eight numbered sections on the right:
    1. Wat deze garantie u geeft
    2. Voor welke planten
    3. Zo vervangen wij
    4. Wat wij van u vragen (the four conditions)
    5. Wanneer wij niet vervangen ("als vaststaat dat…", we come and look)
    6. Zo meldt u het (3 steps; answer in 2 working days, decision in 14 days)
    7. Uw wettelijke rechten
    8. Wie geeft de garantie (legal name a visible placeholder, KvK 82480273, office address, e-mail, phone, WhatsApp)
  - The end: "Gaat een plant achteruit?" with WhatsApp / Bellen / E-mail.
- Checks at 1440, 1024, 768, 390, 360:
  - No horizontal scroll, no text under 13 px, no target under 24 px, no script errors.
  - The index jumps to the section with its heading under the header.
- Owner (19 Nov): back to the earlier top fade of the field (0–20 % on desktop, 0–16 % on phone). The shorter fade showed a band across the tree tops, and Fable's taller-crop option still showed a band. The 200 px gap stays. Fable's tf-1 (`fase2f-fable.html`) is not taken.
- Owner (19 Nov): generate our own field picture instead of the example photo; he provided an OpenRouter key.
  - The secure form could not be shown in his phone app. He saved the key as the variable API_KEY in a separate environment "Openrouter", which this session cannot move onto (unrestricted network).
  - So a child session ran in that environment: text-only prompts A and B, model `google/gemini-3-pro-image-preview` at 16:9 / 4K, 4 images of 5504 × 3072, $0.975.
    - The first attempt with `google/gemini-3-pro-image` failed: 4K is not supported there, and nothing was billed.
  - The originals are on branch `gen/veld-foto`. In `img/gen/` there are 3:1 bands (3840 × 1280) cropped to the sharp zone (`img/gen/README.md`).
  - Review page `fase2g.html` (`tools/build_fase2g.py`, review bar "Фото поля"): gp-0 the example photo, gp-1 A1, gp-2 A2, gp-3 B1, gp-4 B2. The credit line is hidden for the generated pictures.
  - B1 and B2 put four front shrubs roughly above the four steps.
- Owner (19 Nov): "I need shrubs as large as in our original picture; give it the source." Round 2 with the example photo as the image reference: R1–R4 (`img/gen/README.md`), $0.976. They are added to `fase2g.html` as gp-5..gp-8, default R2.
  - R1: almost the example again, including the cut shrub at the right.
  - R2: two large shrubs, whole, inside the centre.
  - R3 / R4: three large shrubs in one row across the width (the model made three, not four).
  - These are derivatives of the CC BY-SA example photo: mockup only.
- Owner (19 Nov): "none of them, redo; R3 is not bad but something is off".
  - The diagnosis of R3: staged identical domes in a line, a wide-angle look, neon flowers everywhere, too much sky.
  - Round 3, T1–T4 (`img/gen/README.md`, $0.978): a telephoto look with one large shrub left of centre and a second one further back, irregular shrubs behind, buds and open trusses, soft per-shrub colour, peat with wood fibres and dry tufts, a thin strip of sky.
  - T1/T2 are text only; T3/T4 used the example as a look reference.
  - Added to `fase2g.html` as gp-9..12, default T3.
- Owner (19 Nov) on T1–T4: the shrubs are small, and two varieties in one frame; it must be the source's variety.
  - Round 4 (`img/gen/README.md`, $0.975), the example as an image input in all four:
    - E1, E2: edits of the example. The two big shrubs are kept, the cut-off foreground shrub is removed, and the frame is widened to 16:9.
    - N1, N2: new photos with two tall dome shrubs of the same lilac-violet variety. The example's average flower colour was measured at rgb(208,149,210), hue ≈ 300°.
  - Checks by the child session and by me:
    - One variety in all four.
    - E1's shrubs are about 15 % smaller than in the example; E2 matches the example's size; N1 and N2 are bigger.
    - Small shrubs cut at the edges remain in all four. N1 and N2 copied the example's cut-off foreground shrub; N1 is trimmed at the right.
  - Added to `fase2g.html` as gp-13..16, default E2.
- So far, four generation rounds cost $3.90 in total, on the owner's OpenRouter key.
- Owner (19 Nov) on E1–N2: "it feels like one photo, just zoomed differently".
  - Round 5 (`img/gen/README.md`, $0.977): only one shrub cropped from the example as the plant reference, and new scenes in text.
    - V1: along the row, by a pine forest with mist.
    - V2: across the field, oaks and a sandy track.
    - V3: one hero shrub, too big for the band.
    - V4: the field edge, with grass and a fence.
  - All four read as different photos with the same lilac-violet variety and big domes.
  - V1 has shrubs cut at both edges; V2 and V4 have every shrub whole; V2's shrubs are a little smaller than the example's.
  - Added to `fase2g.html` as gp-17..19, default V2.
- Five generation rounds so far: $4.88 on the owner's key.
- Owner (19 Nov): "either V2 or V3; let Fable look, I only see it on a phone". Fable's verdict: V2. His V3 attempt is in `fase2h-fable.html` ("V3 · Фабл": the whole V3 frame in `img/gen/veld-V3-fable.webp`, a slightly taller band and a 10 % top fade, for this photo only).
  - V2 reads as a nursery field: several whole shrubs on peat, a sandy track, oaks. V3 reads as one shrub: it takes 82 % of the frame height.
  - On desktop V3 cannot be shown whole: it would need a band of about 800 px at 1440, the size of the hero. In a reasonable band the base of the dome dissolves and the shrub "hangs".
  - V2 spreads the shrubs over all four steps; V3 puts all its mass over "Afspreken" and "Ontvangen".
  - V2 is closer to the example the owner liked.
  - On a phone both work, which is why V3 looks stronger there.
  - V2's small flaw: at 1024 and on phone the left shrub is cut by the screen edge; it can be fixed with a shift of the crop.
- Owner (19 Nov): the example photo stays. It looks best, also on phones; V2 is acceptable on desktop but poor on a phone.
  - The main mockup is unchanged: `img/voorbeeld/hw-v3-veld.webp` with its credit line under the block.
  - The generated candidates stay on `fase2g.html` / `fase2h-fable.html` and on branch `gen/veld-foto` for reference.
  - For the live site the photo needs the attribution (CC BY-SA 4.0, JoachimKohler-HB, Wikimedia Commons) or the nursery's own field photo (plan 3.13).
- Owner (19 Nov): remove the credit line under the block. Done in `tools/hoe_werkt.py` and `hoe-werkt-main.css`; the source stays in `img/voorbeeld/CREDITS.md`.
  - The last step → footer gap is still one --sec (100 / 72 / 64 px).
  - Round 6 asked for the example photo edited with one more shrub on the left (L1–L3).
- Round 6 (owner: "take the source and just add one more shrub on the left"): L1–L3, $0.729; review page `fase2i.html` (`tools/build_fase2i.py`) with exactly the main mockup's crop and fades.
  - L2 changes the least and keeps the colour.
  - In L1 and L3 the new shrub's flowers are a little brighter pink than the others, and it crowds the left main shrub.
- Six generation rounds so far: $5.61 on the owner's key.
- Owner (19 Nov): "L1 or L2, give it to Fable". Fable's verdict: L2.
  - L2 reads as a real photo: the shrub sits in the second row, slightly softer by depth, the same flower colour, ground and shadow. L1's shrub is brighter and cooler lilac, denser and smoother: visibly pasted.
  - In L1 the shrubs stick together, with no soil between them, which is not plausible in a field.
  - L1 is cut by the left screen edge at 1440, 1024 and on phone, so the frame has cut shrubs at both sides. L2's shrub is whole everywhere.
  - L2 gives three domes in an even rhythm over the steps; in L1 the heaviest, brightest mass hangs over "Kiezen".
  - Caveat: L2's shrub is about a third smaller, so on phone it reads as "further back", not as a third equal shrub.
  - No crop change would help either.
- Fable also found that `fase2i.html`'s review group `lp` cleared the page's own `lp-u` class (the Waarom wij layout) on the first click. The group is renamed `ks`.
- APPROVED (owner, 19 Nov): L2 goes into the main mockup.
  - `tools/hoe_werkt.py` now uses `img/gen/veld-L2.webp`: the example photo with one more shrub at the back left, alt "Bloeiende rhododendrons op het veld".
  - Crop and fades are unchanged.
  - Source of the base photo: Wikimedia Commons, "Rhododendronfeld einer Baumschule in Edewecht (2024)" by JoachimKohler-HB, CC BY-SA 4.0 (a rhododendron nursery in Edewecht, Ammerland, Lower Saxony, Germany). L2 is an AI edit of it, so a derivative under the same licence. For public use it needs the attribution and the same licence, or the nursery's own photo (plan 3.13).
- Owner (19 Nov): Fable designs the guarantee page with 21st.dev patterns in our palette and blur. Result: `garantie-fable.html` (`tools/build_garantie_fable.py`, CSS `tools/garantie-fable.css`).
  - 21st.dev patterns:
    - 18113 / 34517: a table of contents that follows the reader.
    - 26910: a two-column FAQ with a sticky left column.
    - 8764: a CTA card with a photo.
    - Process timelines with circles (28381, 26902, 19863, 26891) used as anti-patterns.
  - The page carries the draft copy on the homepage's surfaces:
    - The promise next to the H1 is a woven sage-butter card with four Newsreader lines in moss, like the facts card.
    - Section 04 "Wat wij van u vragen" is the plant card itself: a woven card with a real peat photo dissolving in on the right (`tuinturf-sm.webp`).
    - Section 06 "Zo meldt u het" is a three-step route on one hairline, as in Hoe het werkt.
    - The end "Gaat een plant achteruit?" is a card where Gert's portrait dissolves into a warm woven surface, with WhatsApp / Bellen / E-mail.
  - Added short headings, with no facts changed: Binnen 14 dagen, In zure grond, Niet te diep, Water geven; Melden, Foto's sturen, Antwoord.
  - Checked at 1920–360: no horizontal scroll, text ≥ 13 px, lowest contrast 4.78:1 on real pixels, rhythm --sec.
  - My fix: the page has no hero, so `hb-on` is set from the start and "Bestellen" does not animate in on load.
- Owner (20 Nov) on garantie-fable.html: "he repeated what we already have on the homepage; I saw no new solutions".
  - Fable's second round, `garantie-fable2.html` (`tools/build_garantie_fable2.py`, CSS `tools/garantie-fable2.css`, review bar "Гарантия"), has three concepts with no homepage components and no photos; the blur is only light behind content:
    1. "Drie maanden": a calendar of the guarantee, 13 weeks from delivery to 3 months, with bars for the whole guarantee, planting in the first 14 days, watering (dots), reporting with the answer and decision, and the end. Desktop: shared scale with a week grid. ≤ 900 px: a mini scale per row.
    2. "De wet + wij": "Wat de wet u geeft, en wat wij erbij doen". Three rows, the legal right quiet on the left, a large "+", our extra on the right in soft light, then the conditions as native disclosure sections. The lawyer should check the pairing.
    3. "Het garantiebewijs": the guarantee as a paper sheet with a string hole like a plant label, the fields Soort / Maat / Geleverd op / Ordernummer, eight numbered articles, a seal, and a perforated tear-off "Gaat een plant achteruit?" with the contacts. "Download als pdf" is a placeholder.
  - Fable's ranking: 1 > 3 > 2.
  - Checked at 1920–360: no horizontal scroll, text ≥ 13 px, lowest contrast 5.42:1, rhythm --sec.

- Owner (20 Nov) on garantie-fable2.html: concept 1 no (the panel on the green background is unclear), concept 2 does not work on desktop, concept 3 "the right side is fine, the left side is just emptiness"; he likes the seal.
  - Fable's third round, `garantie-fable3.html` (`tools/build_garantie_fable3.py`, CSS `tools/garantie-fable3.css`, review bar "Слева от листа", group `gb`), develops concept 3 only. The sheet, its fields, the eight articles and the perforated tear-off stay; the articles are 16 px on desktop (14 on tablet and phone).
  - The seal is redrawn: a serrated edge, two rings, ticks, "TOP RHODODENDRONS" and "OTTERLO · SINDS 2001" on arcs, a large "3" and "maanden" in Newsreader, moss ink, slightly tilted.
  - Three desktop layouts (below 1100 px all three are the same page as in round 2):
    1. "Коротко слева": a sticky left column with the heading, the intro, the seal with the four promises beside it, WhatsApp / Bellen / E-mail and "Download als pdf"; the seal is not on the sheet. Fable's recommendation.
    2. "Лист по центру": no left column; the heading and the intro across the width, the sheet centred and wider (1080 px), the seal up to 232 px stamped over its top right corner.
    3. "Бирка на шнурке": the heading across the width; a sticky, slightly tilted plant label on a string beside the sheet with the nursery's name, the seal, "Aangroeigarantie", the four promises and the pdf link.
  - Checked at 1920–360 for all three: no horizontal scroll, text ≥ 13 px (the lettering inside the seal is graphics), lowest contrast 5.21:1, rhythm --sec; the sticky parts fit at 1366×768, 1440×900 and 1920×1080.
- Owner (20 Nov) on garantie-fable3.html: the plant label of option 3 with the seal is the one ("прикольная"); the rest shorter; no fields to fill in on the website (Soort / Maat / ...), instead how the guarantee works; the cord did not go into the hole ("the cord design is bad, the label is good").
  - `garantie4.html` (`tools/build_garantie4.py`, CSS `tools/garantie4.css`, no review bar): option 3 only.
  - The cord is redrawn: a twine loop with a knot and two loose ends, two strands down to the label; the back one goes behind the top edge, the front one runs over the paper into the eyelet, which has a sage reinforcement ring. The sheet no longer has its own hole and string.
  - The sheet: "Zo werkt het" in four steps (Planten, Melden, Antwoord, Nieuwe plant), then "Goed om te weten" (Voor welke planten, Niet meer leverbaar, Wanneer wij niet vervangen, Uw wettelijke rechten, Wie geeft de garantie), the perforation and the tear-off with the contacts.
  - The copy is shortened from the draft, with no new facts. Left out of the short version: "kleine, onbedoelde fouten bij de verzorging rekenen wij u niet aan", the legal presumption of one year, the plant card note. The full draft stays in `tools/build_garantie.py`; the lawyer checks the final text.
  - Below 1100 px there is no label, the seal is stamped on the sheet. The page on the phone: 3420 px instead of 4681.
  - Checked at 1920, 1440, 1366×768, 1024 and 390: no horizontal scroll, text ≥ 13 px, lowest contrast 8.27:1 on the sheet; the sticky label fits at 1366×768.
- Owner (20 Nov) on garantie4.html round 1: the cord still did not go through the hole; the subtitle must sit under the heading, as on the other pages, not to its right; no step numbers 1–4; the phone page was far too long: on the phone the label with the main points and the pdf for the details.
  - Round 2 of `garantie4.html`:
    - The cord, my drawing, checked at 4×: the label has a metal eyelet with a dark hole. The front strand runs over the top edge and down the paper into the hole, bears on its top and turns away behind the label; the lower part of the hole stays empty. The back strand is a separate layer under the label, so the paper covers it where it goes behind. The ends at the knot are short.
    - The head: heading, then the subtitle under it, then the draft note.
    - The steps without numbers: the verb in Newsreader, the text under it.
    - Below 900 px: the head, the label (the seal, "Aangroeigarantie", the four promises, an outlined pill "Alle voorwaarden als pdf"), "Gaat een plant achteruit?" with the three contacts, and one "Lees alle voorwaarden" button that opens the sheet (how it works and the conditions) in place. The page on the phone is 2264 px closed (it was 4681 in fable3), 3859 px open.
    - Desktop now from 900 px (it was 1100); at 900–1099 the steps and the conditions are one column.
    - Fixed on the way: on the phone the label's room for the cord collapsed (a child margin through the label), so the cord lay over the seal; the room is now the label's padding.
  - Checked at 1920, 1440, 1366×768, 1024×768, 768 and 390 (closed and open): no horizontal scroll, text ≥ 13 px, the sticky label fits at 1366×768 and 1024×768.
