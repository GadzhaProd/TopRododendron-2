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

## Waarom wij — variant A chosen (7 Nov), design in review

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
