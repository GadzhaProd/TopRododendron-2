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
- Copy: quote, H2 "Gert Top", "Familiekwekerij in Otterlo, op de Veluwe, sinds 2001", short text, buttons "Bel Gert · 06 20 10 43 12" (moss) and "WhatsApp". No role caption on the photo.
- Phone: still open; current proposal = clean inset photo inside the same glass card, text below.
- If a cleaner extension is ever needed: redo the right 380 px with Photoshop Generative Expand on the original file.

## De kwekerij (block 2) — in progress

- Scheme C: text left, Gert's portrait right, quote card overlapping only the lower part of the photo (face never covered), no eyebrow, no "eigenaar", no CTA buttons.
- Copy: `mockup-v3/block-mockups/kweker-final/` (trimmed old-site copy).
- Open: background colour (21st palettes rejected), and whether the facts (10.000 planten · 7 soorten · vanaf 1 plant) return inside the block or are dropped.

## Rejected (do not offer again)

- 21st.dev colour themes for the block; the Royal Blue store skill (owner: work on our own concept C instead); the dissolve transition of the photo; the dark (charcoal) trust bar.
