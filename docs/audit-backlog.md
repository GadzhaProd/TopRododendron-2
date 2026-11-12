# Homepage audit backlog (12 Nov)

Source: the independent conversion and consumer-psychology review of the main mockup
(`mockup-v3/block-mockups/waarom-kweker/index.html`), 12 Nov. We work through it in order, one item at a time.
Each item gets a status: open, in progress, done, skipped (with the owner's reason), or waiting for owner data.

Evidence labels from the review: strong (Baymard, NN/g, meta-analyses), medium, heuristic.

## Real data already on the current site (`mockup-v3/src/data/content.ts`, mirror of the live site)

- Phones: 06 20 10 43 12 and 06 20 29 78 49; WhatsApp: +31 6 20 29 78 49.
- E-mail: info@toprhododendrons.nl.
- Address: Esserbroekweg 2, 6731 DB Otterlo. Pick-up: "Afhalen in Otterlo mogelijk: wij zetten uw bestelling klaar."
- KvK: 82480273. Founder role: "Oprichter en kweker". Tagline: "Kwekerij in Otterlo, sinds 2001".
- Hours (company data): Monday–Friday 08:00–17:00, Saturday 09:00–13:00, Sunday closed.
- Delivery: own transport throughout the Netherlands; the delivery moment is agreed after ordering; shipping costs "worden berekend bij afrekenen" (the amount is not stated anywhere).
- Planting: all year except frost periods; best March–April and September–October.

## Conflicts in the existing copy (the owner must decide)

- Hours: Waarom wij says "ma–za 09:00–17:00"; the company data says Mon–Fri 08:00–17:00 and Sat 09:00–13:00.
- Guarantee: "Niet aangeslagen in het eerste seizoen? Wij vervangen kosteloos." (Waarom wij, groothandel FAQ), but the
  consumer FAQ says "Groeit een plant niet aan ondanks de juiste verzorging? Neem dan contact met ons op, wij zoeken samen
  naar een passende oplossing", and other copy says "De garantie vervalt bij onjuiste verzorging of buitengewone
  weersomstandigheden" and "100% aangroeigarantie bij correcte aanplant".

## High priority

1. Contact with Gert wherever it is promised: header (number on desktop, icon on phone), the advice reason in Waarom wij
   (tel: and WhatsApp), a button in the founder block, footer. Status: waiting for owner (which number, which hours).
2. Delivery (cost, area, timing) and payment visible before the cart: a line by the prices, details in Hoe het werkt.
   Status: waiting for owner (delivery cost, payment methods; area "heel Nederland" vs "NL, DE, BE" in the plan).
3. Guarantee: exact term, conditions, how to claim; one wording site-wide; a link to the conditions.
   Status: waiting for owner (see the conflict above).
4. Help in choosing: under the grid "Twijfelt u? Gert denkt met u mee" with a real contact. (The review's other idea,
   colour words on the cards, conflicts with the owner's decision to remove colour; not taken.) Status: open.
5. First screen: bring back "Familiekwekerij in Otterlo · sinds 2001" above the H1; break the H1 by meaning:
   "Rhododendrons die aanslaan. / Met aangroeigarantie." Status: open.

## Medium priority

6. Tighten Waarom wij so the range starts higher (facts as a slim strip, reasons 2×2 on desktop, logistics to Hoe het
   werkt). Option B (range right after the hero, Gert after the range) to be tested on people. Status: open.
7. Founder block: a contact button; "Oprichter en kweker"; a smaller name; a concrete quote; later a photo on the field.
   Several of these conflict with approved choices (the name size, the role line, the quote); owner decides. Status: open.
8. Remove repeated facts (the range lead repeats the facts card; transport and "vers gerooid" belong in Hoe het werkt;
   "met kluit" as one shared line only if the owner changes his rule). Status: open.
9. A value line by the prices: "Alle prijzen incl. btw · met kluit · vers gerooid · met aangroeigarantie"
   (owner confirms that prices include btw). Status: open.
10. Less weight on "Groothandel" for consumers: equal menu weight; the second hero button for consumers or a text link.
    Status: open.
11. Cart in the header on desktop and phone, a phone icon on phone. Status: open.
12. Photo proof: the root ball in Waarom wij; a real 40–60 cm plant to scale on the product page. Status: waiting for
    owner (photos).
13. Footer and legal: address, KvK, BTW, conditions, payment, returns (returns need a legal check). Status: open (most
    data exists; BTW number, payment and returns from the owner).
14. Fact checks: "veenrijke bodem"; "10.000 planten op voorraad" vs "op ons veld"; the delivery area. Status: waiting
    for owner.

## Low priority

15. Quieter headings: H2 44–48 px, the founder's name about 48 px. Status: open.
16. Remove the pink spots and simplify the gradients. Status: open.
17. "Bekijk alle planten" → "Alle maten en prijzen", and repeat the link under the grid. Status: open.
18. The headline word animation in the production code: static or very short. Status: open (code transfer).
19. Hero photo alt text: "Ons rhododendronveld in Otterlo". Status: open.
20. A seasonal line ("Nu is het plantseizoen"), only if true and kept up to date. Status: open.
21. Later: real reviews via an independent platform, the hedge calculator, the 3-question picker. Status: later.

## Do not do

Timers, "only 3 left", "12 people viewing", fake reviews or ratings, "bestseller" badges without sales data,
struck-through old prices, hidden delivery costs, pre-ticked paid add-ons, entry or exit pop-ups, chat bubbles over
content, confirmshaming, an unconditional "100% guarantee", animated counters, carousels in the hero, trust marks the
nursery does not hold, any comparison with garden centres.
