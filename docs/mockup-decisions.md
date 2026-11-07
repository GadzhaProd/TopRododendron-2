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

## Waarom wij — variant A chosen (7 Nov), design still to come

- Mockup: `mockup-v3/block-mockups/waarom-kweker/` (upper block). Owner chose A "Список" (numbered rows 01–04 on hairlines). B "Преимущества" (icon grid) is dropped, and so is the review bar. The owner will say how A should be designed.
- Copy: H2 "Wij kweken rhododendrons. Niet meer, niet minder."; lead "Onze planten groeien in de volle grond op veenrijke bodem en ontwikkelen daar een sterk wortelstelsel. Gerooid met kluit, direct van het veld naar uw tuin."; facts row 10.000 planten op voorraad / Sinds 2001 familiekwekerij in Otterlo / 7 soorten in 4 maten, 40 tot 120 cm / Vanaf 1 plant geen minimumbestelling.
- Rows: 01 Aangroeigarantie op elke plant; 02 Vers gerooid voor uw levering; 03 Persoonlijk advies van de kweker; 04 Eigen transport of afhalen.
- Row 03 text, for now (owner, 7 Nov): the old site's "De kweker helpt u persoonlijk, ma–za 09:00–17:00." (note "Ma–za 09:00–17:00"), replacing "U spreekt rechtstreeks met Gert, van vraag tot levering", which the owner disliked. May be rewritten later.
- "Sinds 2001" lives only here, in the facts row (removed from the founder text).
