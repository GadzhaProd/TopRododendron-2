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

