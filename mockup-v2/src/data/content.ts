// Single source of truth for real facts and copy (from the original site data).
const imgs = import.meta.glob('../assets/img/*.jpg', { eager: true, import: 'default' }) as Record<string, string>
export const img = (name: string) => imgs[`../assets/img/${name}.jpg`]

import heroDesktop from '../assets/hero-desktop.mp4'
import heroMobile from '../assets/hero-mobile.mp4'
import heroDesktopPoster from '../assets/hero-desktop-poster.jpg'
import heroMobilePoster from '../assets/hero-mobile-poster.jpg'
export const hero = { desktop: heroDesktop, mobile: heroMobile, desktopPoster: heroDesktopPoster, mobilePoster: heroMobilePoster }

export type Variety = {
  slug: string
  name: string
  color: string
  hex: string
  bloei: string
  standplaats: string
  hoogte: string
  groei: string
  from: string
  short: string
  long: string
  sizes: { label: string; price: string }[]
}

export const varieties: Variety[] = [
  { slug: 'nova-zembla', name: 'Nova Zembla', color: 'Helderrood', hex: '#b8273a', bloei: 'Mei – juni', standplaats: 'Halfschaduw, verdraagt zon', hoogte: 'tot 3 m', groei: 'Matig', from: '29',
    short: 'Vuurrode bloemtrossen, de meest geplante rhododendron van Nederland.',
    long: 'De vuurrode bloemtrossen zijn imposant en rijkelijk, en de plant bloeit betrouwbaar elk jaar in mei en juni. Uitstekend winterhard, geschikt als solitair of haag, en zontoleranter dan de meeste soorten.',
    sizes: [{ label: '40–60 cm', price: '29,00' }, { label: '60–80 cm', price: '45,00' }, { label: '80–100 cm', price: '65,00' }, { label: '100–120 cm', price: '89,00' }] },
  { slug: 'cunninghams-white', name: "Cunningham's White", color: 'Wit / lichtroze', hex: '#efe9df', bloei: 'April – mei', standplaats: 'Halfschaduw', hoogte: 'tot 2 m', groei: 'Langzaam', from: '25',
    short: 'Elegante witte bloemen met zachte roze accenten; de vroegste bloeier.',
    long: 'Een klassieke rhododendron die als eerste van alle soorten bloeit: al in april kleuren de witte bloemen met subtiele lichtroze tinten uw tuin. Groeit gestaag en vormt een mooie volle struik.',
    sizes: [{ label: '40–60 cm', price: '25,00' }, { label: '60–80 cm', price: '39,00' }, { label: '80–100 cm', price: '55,00' }, { label: '100–120 cm', price: '75,00' }] },
  { slug: 'roseum-elegans', name: 'Roseum Elegans', color: 'Warm roze', hex: '#d9679a', bloei: 'Mei – juni', standplaats: 'Halfschaduw, verdraagt zon en hitte', hoogte: 'tot 2,5 m', groei: 'Matig – snel', from: '27',
    short: 'Klassieke warmroze bloemen, hitte- en winterhard, uitstekend als haag.',
    long: 'Een tijdloze klassieker met warme roze bloemtrossen die rijkelijk bloeien in mei en juni. Groeit krachtig en breed, is uitstekend winterhard én hittebestendig.',
    sizes: [{ label: '40–60 cm', price: '27,00' }, { label: '60–80 cm', price: '42,00' }, { label: '80–100 cm', price: '60,00' }, { label: '100–120 cm', price: '82,00' }] },
  { slug: 'catawbiense-boursault', name: 'Catawbiense Boursault', color: 'Paars-lavendel', hex: '#9b6cc4', bloei: 'Mei – juni', standplaats: 'Halfschaduw, verdraagt zon', hoogte: 'tot 2,5 m', groei: 'Matig', from: '27',
    short: 'Paars-lavendel bloemen, ijzersterk en betrouwbaar; trekt vlinders en bijen.',
    long: 'Een van de meest betrouwbare rhododendrons voor de Nederlandse tuin. Bloeit rijkelijk in mei en juni, trekt vlinders en bijen, en vormt een compacte, goed vertakte struik.',
    sizes: [{ label: '40–60 cm', price: '27,00' }, { label: '60–80 cm', price: '42,00' }, { label: '80–100 cm', price: '60,00' }, { label: '100–120 cm', price: '82,00' }] },
  { slug: 'catawbiense-grandiflorum', name: 'Catawbiense Grandiflorum', color: 'Lila-roze', hex: '#b98fcf', bloei: 'Mei – juni', standplaats: 'Halfschaduw, verdraagt zon', hoogte: 'tot 3 m', groei: 'Matig – snel', from: '29',
    short: 'Lila-roze bloemen op indrukwekkend formaat; de keuze voor grote tuinen.',
    long: 'De kolos van ons assortiment: groot, krachtig en indrukwekkend. Ideaal voor haagvorming, privacyschermen of grootschalige beplanting. Populair bij hoveniers.',
    sizes: [{ label: '40–60 cm', price: '29,00' }, { label: '60–80 cm', price: '45,00' }, { label: '80–100 cm', price: '65,00' }, { label: '100–120 cm', price: '89,00' }] },
  { slug: 'ponticum-roseum', name: 'Ponticum Roseum', color: 'Roze / lichtpaars', hex: '#e3a2c3', bloei: 'Mei – juni', standplaats: 'Halfschaduw / schaduw', hoogte: 'tot 4 m', groei: 'Snel', from: '22',
    short: 'Robuust en snelgroeiend, met decoratieve rode jonge stelen.',
    long: 'Combineert de groeikracht van de Ponticum met zachte roze-lichtpaarse bloemen en decoratieve rode jonge stelen. Groeit snel tot indrukwekkende hoogte; het hele jaar sierwaarde.',
    sizes: [{ label: '40–60 cm', price: '22,00' }, { label: '60–80 cm', price: '35,00' }, { label: '80–100 cm', price: '50,00' }, { label: '100–120 cm', price: '70,00' }] },
  { slug: 'ponticum', name: 'Ponticum', color: 'Violet-paars', hex: '#7b5ea7', bloei: 'Mei – juni', standplaats: 'Halfschaduw / schaduw', hoogte: 'tot 4 m', groei: 'Snel', from: '22',
    short: 'De krachtigste soort: violet-paars, voor grote tuinen en bosranden.',
    long: 'De krachtigste soort uit ons assortiment. Ideaal voor grote tuinen, bosranden en privacyschermen. Kan tot 4 meter hoog worden en vergt weinig onderhoud.',
    sizes: [{ label: '40–60 cm', price: '22,00' }, { label: '60–80 cm', price: '35,00' }, { label: '80–100 cm', price: '50,00' }, { label: '100–120 cm', price: '70,00' }] },
]

export const tuinturf = { name: 'Tuinturf-substraat', price: '14,95', unit: 'per 40 L zak', text: 'Speciaal samengesteld substraat voor optimale groei en aanslag van rhododendrons. Zuurminnend, vochtregelend en rijk aan voedingsstoffen.' }

export const company = {
  name: 'Top Rhododendrons',
  tagline: 'Kwekerij in Otterlo, sinds 2001',
  founder: 'Gert Top',
  street: 'Esserbroekweg 2',
  postal: '6731 DB Otterlo',
  region: 'Veluwe, Gelderland',
  kvk: '82480273',
  email: 'info@toprhododendrons.nl',
  phone1: '06 20 10 43 12',
  phone1Href: 'tel:+31620104312',
  phone2: '06 20 29 78 49',
  phone2Href: 'tel:+31620297849',
  whatsapp: 'https://wa.me/31620297849',
  instagram: 'https://www.instagram.com/toprhododendrons',
  maps: 'https://www.google.com/maps/search/Esserbroekweg+2+Otterlo',
  hours: [['Maandag – vrijdag', '08:00 – 17:00'], ['Zaterdag', '09:00 – 13:00'], ['Zondag', 'Gesloten']],
}

export const promises = [
  { title: 'Aangroeigarantie op elke plant', text: 'Niet aangeslagen in het eerste seizoen? Wij vervangen kosteloos.' },
  { title: 'Vers gerooid, flexibel geleverd', text: 'Uw planten staan niet onnodig te wachten. We rooien ze vers voor uw geplande bezorging of het moment dat u ze komt afhalen.' },
  { title: 'Eigen transport door heel Nederland', text: 'Wij stemmen de levering af op uw planning, of zetten uw bestelling klaar voor afhaal in Otterlo.' },
  { title: 'Persoonlijk advies van de kweker', text: 'U spreekt rechtstreeks met de kweker. Eén aanspreekpunt, van vraag tot levering.' },
]

export const story = {
  h: 'Wij kweken rhododendrons. Niet meer, niet minder.',
  p1: 'Familiebedrijf in Otterlo, op de Veluwe. 10.000 planten op voorraad, direct van het veld naar uw tuin.',
  p2: 'Dankzij onze veenrijke bodem en een uitgebalanceerde watergift ontwikkelen onze planten een sterk wortelstelsel. Daardoor passen ze zich moeiteloos aan in uw tuin, met aangroeigarantie.',
  quote: 'Een gezonde plant is geen toeval. Dat is onze standaard.',
}

export const facts = [
  { k: 'Otterlo, Veluwe', v: 'Veenrijke, zure bodem' },
  { k: 'Sinds 2001', v: 'Familiebedrijf' },
  { k: '10.000 planten', v: 'Op stam, 40 – 120+ cm' },
  { k: 'Aangroeigarantie', v: 'Op elke plant' },
]

export const faq = [
  { q: 'Hoe en wanneer wordt mijn rhododendron geleverd?', a: 'Wij leveren met eigen transport door heel Nederland. Na uw bestelling nemen wij contact met u op om een leveringsmoment af te stemmen. Uw plant wordt vers gerooid en direct geleverd, zo komt hij in optimale conditie aan.' },
  { q: 'Wanneer kan ik een rhododendron aanplanten?', a: 'Het hele jaar door, behalve tijdens vorstperiodes. De ideale momenten zijn vroege lente (maart–april) en herfst (september–oktober). Plant u in de zomer, zorg dan voor voldoende water in de eerste weken.' },
  { q: 'Welke grond heeft een rhododendron nodig?', a: 'Zure, luchtige grond: zandgrond of veengrond met een pH tussen 4,5 en 6. Op zware kleigrond groeit de plant minder goed. Voeg bij het aanplanten tuinturf-substraat toe voor de beste start.' },
  { q: 'Wat houdt de aangroeigarantie in?', a: 'Al onze planten worden geleverd met aangroeigarantie. Groeit een plant niet aan ondanks de juiste verzorging? Neem contact met ons op, wij zoeken samen naar een passende oplossing.' },
  { q: 'Kan ik ook één plant bestellen?', a: 'Ja. Voor particulieren geldt geen minimumbestelling. Heeft u als hovenier een kleinere opdracht? Neem contact op, we denken graag mee.' },
  { q: 'Moet ik mijn rhododendron snoeien?', a: 'Snoeien is niet noodzakelijk. Snoei bij voorkeur direct na de bloei, van eind april tot half juni. Radicaal snoeien raden wij af: dit vertraagt de bloei met twee tot drie jaar.' },
]

export const b2b = {
  intro: '10.000 rhododendrons op stam. Voor hoveniers, gemeenten en projectontwikkelaars. Aangroeigarantie, eigen transport, scherpe partijprijzen vanaf 25 stuks.',
  groups: [
    { title: 'Hoveniers en tuinarchitecten', text: 'Voor tuin- en landschapsprojecten', rows: [['Volume per project', '30 – 150 stuks'], ['Levering', 'Op afgesproken datum'], ['Voorwaarden', 'Factuur 30 dagen']] },
    { title: 'Openbaar groen en gemeenten', text: 'Voor parken, plantsoenen en wijken', rows: [['Volume per project', '100 – 500 stuks'], ['Levering', 'Gefaseerd mogelijk'], ['Voorwaarden', 'Plantpaspoort + fytosanitair']] },
    { title: 'Vastgoed en wooncomplexen', text: 'Voor binnentuinen en gemeenschappelijke tuinen', rows: [['Volume per project', '150 – 1000 stuks'], ['Levering', 'Afgestemd op oplevering'], ['Voorwaarden', 'Btw verlegd mogelijk']] },
  ],
  services: [
    { title: 'Plantservice op locatie', text: 'Optioneel laten planten door ons team, inclusief grondverbetering met tuinturf-substraat.' },
    { title: 'Vaste contactpersoon', text: 'U spreekt rechtstreeks met de kweker. Eén aanspreekpunt van offerte tot oplevering.' },
    { title: 'Factuur op 30 dagen, btw verlegd', text: 'Voor geregistreerde bedrijven leveren wij op factuur (30 dagen). Btw verlegd voor zakelijke afnemers.' },
    { title: 'Plantpaspoort en fyto', text: 'Aangesloten bij NAK Tuinbouw. Plantpaspoort bij elke partij; fytosanitaire certificaten voor export op aanvraag.' },
  ],
  sizes: [
    ['40–60 cm', 'Ruim op voorraad', 'Haag · groepsbeplanting'],
    ['60–80 cm', 'Ruim op voorraad', 'Haag · solitair'],
    ['80–100 cm', 'Op voorraad', 'Solitair · accent'],
    ['100–120 cm', 'Op voorraad', 'Solitair · openbaar groen'],
    ['120 cm +', 'Op aanvraag', 'Grootformaat'],
  ],
  steps: [
    { title: 'U vraagt aan', text: 'Via het formulier of telefonisch. U geeft soorten, maten, aantallen en gewenste leverdatum door.' },
    { title: 'Wij maken offerte', text: 'Binnen 24 uur ontvangt u een gespecificeerde offerte met partijprijzen, levering en planning.' },
    { title: 'Wij reserveren op stam', text: 'Akkoord op de offerte? Wij reserveren de planten op stam en blokken uw leverdatum in onze planning.' },
    { title: 'Vers gerooid, geleverd', text: 'Op de afgesproken datum rooien wij vers en bezorgen met eigen transport. Plantservice optioneel.' },
  ],
  tiers: [
    { range: '25 – 49 planten', text: 'Vanaf 25 stuks scherpe partijprijzen. Eigen transport en plantservice optioneel.' },
    { range: '50 – 149 planten', text: 'Voor grotere projecten. Vaste contactpersoon en voorranglevering inbegrepen.' },
    { range: '150+ planten', text: 'Maatwerkprijs voor gemeenten en grote projecten. Inclusief plantpaspoort en fyto.' },
  ],
  faq: [
    { q: 'Geldt de aangroeigarantie ook bij grote partijen?', a: 'Ja. De aangroeigarantie geldt op elke plant, ook bij projectorders van 100 of 1.000 stuks. Slaat een plant niet aan in het eerste seizoen? Wij vervangen kosteloos.' },
    { q: 'Verzorgen jullie ook de aanplant op locatie?', a: 'Ja, plantservice is optioneel beschikbaar. Wij komen met eigen team, inclusief grondverbetering met tuinturf-substraat indien gewenst. Vraag in de offerte naar het tarief per plant.' },
    { q: 'Kunnen wij de leverdatum zelf bepalen?', a: 'Ja. Wij rooien op uw leverdatum, niet eerder. Dit voorkomt droogtestress en zorgt voor maximale aanslagkans. U geeft uw planning door, wij houden de planten op stam.' },
    { q: 'Hoe werkt de facturatie?', a: 'Voor geregistreerde bedrijven leveren wij op factuur met 30 dagen betaaltermijn. Btw wordt verlegd bij zakelijke afnemers met geldig btw-nummer.' },
    { q: 'Leveren jullie plantpaspoort en fytosanitaire documenten?', a: 'Ja. Wij zijn aangesloten bij de NAK Tuinbouw en leveren bij elke partij het verplichte plantpaspoort. Fytosanitaire certificaten voor export verzorgen wij op aanvraag.' },
  ],
}
