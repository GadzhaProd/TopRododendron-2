# Generated field photos (19 Nov 2026)

Generated with `google/gemini-3-pro-image-preview` on OpenRouter, using the owner's key. The prompts were text only: A and B from `docs/prompt-foto-veld.md`, with no reference photo. 4 images at 5504 × 3072; the total cost was $0.975. The originals, with `meta.json` (exact parameters per image), are on the branch `gen/veld-foto`.

Each `veld-*-band.webp` file here is a 3:1 band (3840 × 1280), cropped from the original so the shrubs sit in the block's sharp zone (`docs/img/schema-kadra-16x9.png`):

| File | Prompt | Crop (y in the 3072 px original) |
|---|---|---|
| veld-A1-band.webp | A | 1150 to 2985 |
| veld-A2-band.webp | A | 1043 to 2878 |
| veld-B1-band.webp | B | 1237 to 3072 |
| veld-B2-band.webp | B | 1000 to 2835 |

These are generated images, not the nursery's field. They are for the mockup. On the live site, the block "Van ons veld naar uw tuin" needs a real photo of the field (plan item 3.13).

## Round 2: large shrubs, with the example photo as the reference (owner, 19 Nov)

Same model, 16:9, 4K. Each request sent the example photo `img/voorbeeld/hw-v3-veld.webp` as an image input with the prompt (prompts written out in `meta-ref.json` on the branch). The total cost was $0.976.

These are derivatives of a CC BY-SA 4.0 photo ("Rhododendronfeld einer Baumschule in Edewecht", JoachimKohler-HB, Wikimedia Commons). They are for the mockup only; any public use needs that attribution and the same licence.

| File | Idea | Crop (y in the 3072 px original) |
|---|---|---|
| veld-R1-band.webp | the same scene, new photo | 910 to 2745 |
| veld-R2-band.webp | the same scene, new photo | 849 to 2684 |
| veld-R3-band.webp | the same scale, three in a row | 1125 to 2960 |
| veld-R4-band.webp | the same scale, three in a row | 1064 to 2899 |

## Round 3: telephoto look, natural layout (owner, 19 Nov: none of R1–R4; R3 close but "something is off")

The diagnosis of R3 against the example:
- staged: three identical domes evenly lined up;
- a wide-angle look, with everything sharp;
- dense neon-lilac flowers all over;
- too much sky.

The round 3 prompt asked for a 135 mm telephoto: one large shrub left of centre, a second one further back and paler, irregular shrubs behind, about half the trusses in closed buds, soft colours that differ per shrub, dark fibrous peat, and a thin strip of sky. Prompts are in `meta-T.json` on the branch. The total cost was $0.978.

| File | Reference | Crop (in the 5504 × 3072 original) |
|---|---|---|
| veld-T1-band.webp | text only | x 44 to 5460 (film border strips removed), y 782 to 2587 |
| veld-T2-band.webp | text only | y 603 to 2438 |
| veld-T3-band.webp | example photo as a look reference (CC BY-SA 4.0 derivative, mockup only) | y 664 to 2499 |
| veld-T4-band.webp | example photo as a look reference (CC BY-SA 4.0 derivative, mockup only) | y 719 to 2554 |

## Round 4: one variety, large domes (owner, 19 Nov: in T "the shrubs are small, and two different varieties in one frame")

All four requests sent the example photo as an image input; the total cost was $0.975. Prompts are in `meta-EN.json` on the branch. Every image is a CC BY-SA 4.0 derivative, for the mockup only.

| File | How it was made | Crop (in the 5504 × 3072 original) |
|---|---|---|
| veld-E1-band.webp | an edit of the example: the cut-off foreground shrub removed, the frame widened to 16:9 | y 930 to 2765 |
| veld-E2-band.webp | the same edit, camera nearly unchanged | y 880 to 2715 |
| veld-N1-band.webp | a new photo, the example as a strict reference | x 0 to 4840 (the cut-off foreground shrub trimmed), y 950 to 2785 |
| veld-N2-band.webp | a new photo, the example as a strict reference | y 850 to 2685 |

## Round 5: the same plant, different photos (owner, 19 Nov: E1–N2 "feel like one photo, just zoomed")

Only one shrub cropped from the example (`img/voorbeeld/hw-ref-struik.webp`) was sent as the plant reference, and the scenes were described in text. The total cost was $0.977; prompts are in `meta-V.json` on the branch. These are CC BY-SA 4.0 derivatives, for the mockup only.

| File | Scene | Crop (y in the 3072 px original) |
|---|---|---|
| veld-V1-band.webp | along the row: pine and birch forest, ground mist | 794 to 2629 |
| veld-V2-band.webp | across the field: oaks, a sandy track | 1015 to 2850 |
| veld-V4-band.webp | the field edge: grass, a post-and-wire fence, meadow | 818 to 2653 |

V3 (one hero shrub) is not cropped: the hero takes 82 % of the height and does not fit the band.

## Round 6: the example with one more shrub on the left (owner, 19 Nov)

These are edits of the full example photo at 3:2 / 4K (5056 × 3392), with a total cost of $0.729; prompts are in `meta-L.json` on the branch. Here they are scaled to 2400 × 1600 webp, as `veld-L1.webp` to `veld-L3.webp`, and shown with the main mockup's crop on `fase2i.html`. They are CC BY-SA 4.0 derivatives, for the mockup only.
- L1: the new shrub as large as the main one, in the front row. It touches the left edge and overlaps the main shrub.
- L2: the existing small shrub at the back left became a larger one. The cleanest edit: the left main shrub is untouched.
- L3: the new shrub in the front row, lower and wider. It sits close to the left edge and overlaps the main shrub.

