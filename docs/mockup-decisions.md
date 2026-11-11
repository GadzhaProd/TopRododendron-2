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
