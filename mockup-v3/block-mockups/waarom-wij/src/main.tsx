// Three mockups of homepage block 2 "Waarom wij" (scheme C: copy + reasons left,
// Gert's portrait with caption right, a full-width proof strip below), each
// assembled from ready 21st.dev components (see src/components, one file per
// component with its id and what was changed). Copy follows
// docs/positioning-plan.md; unknown details are Dutch placeholders in [brackets].
import { createRoot } from 'react-dom/client'
import { MessageCircle, ShieldCheck, Shovel, Sprout } from 'lucide-react'
import './styles.css'
import { Content06 } from '@/components/content-06'
import { ComparisonOutcomes, ComparisonPanels } from '@/components/comparison-03'
import { Feature08Grid, Feature08Header } from '@/components/feature-08'
import { BoldStats } from '@/components/stats-bold'
import { SectionHeader, ServicesList } from '@/components/services-01'
import { KeyValueList } from '@/components/key-value-list'
import { QuoteCard } from '@/components/testimonials-2'
import { CaptionedFigure } from '@/components/gallery-02-figure'
import portrait from './img/owner-portrait.webp'
import heroField from './img/hero-field.webp'
import novaZembla from './img/nova-zembla-2.webp'

const PHONE = '06 20 10 43 12'
const portraitAlt = 'Gert Top, oprichter en kweker van Top Rhododendrons'

/* ───────── mockup chrome: label + hero stub ───────── */
function Label({ n, name, parts }: { n: string; name: string; parts: string }) {
  return (
    <div className="bg-foreground px-4 py-2.5 text-[13px] leading-[1.45] text-background sm:px-7 sm:py-3 sm:text-[14px]">
      <b className="font-bold">Вариант {n}</b> — {name} · <span className="opacity-80">компоненты 21st: {parts}</span>
    </div>
  )
}
function HeroStub() {
  return (
    <div aria-hidden className="relative h-40 bg-cover bg-[center_78%] sm:h-[200px]" style={{ backgroundImage: `url(${heroField})` }}>
      <div className="absolute inset-0 bg-[linear-gradient(180deg,rgba(0,0,0,.22),rgba(0,0,0,.42))]" />
    </div>
  )
}
const Eyebrow = ({ children }: { children: string }) => <p className="text-[12px] font-semibold uppercase tracking-[0.14em] text-primary">{children}</p>

/* ───────── Variant 1: comparison ───────── */
const V1 = () => (
  <section id="v1" className="pb-16 sm:pb-20 lg:pb-24">
    <Content06
      eyebrow={<Eyebrow>Waarom Top Rhododendrons</Eyebrow>}
      title={<>Uit de volle grond, met kluit. Daarom slaan ze aan.</>}
      description="Onze rhododendrons groeien jaren buiten, op veenrijke bodem in Otterlo. We rooien ze pas voor uw levering, met de kluit eromheen. Geen potplant uit de kas."
      media={<CaptionedFigure src={portrait} alt={portraitAlt} caption="Gert Top" sub={<>Oprichter en kweker, Otterlo · <span className="whitespace-nowrap">Persoonlijk advies: {PHONE}</span></>} />}
      reasons={
        <ComparisonPanels
          before={{ title: 'Containerplant uit het tuincentrum', items: ['Gekweekt in een pot, meestal in de kas', 'Wortels beperkt tot de maat van de pot', 'Herkomst en leeftijd van de plant onbekend', 'Geen contact met de kweker'] }}
          after={{ title: 'Van ons veld in Otterlo', items: ['Jaren buiten gegroeid in de volle grond', 'Sterk wortelstelsel dankzij veenrijke bodem', 'Gerooid met kluit, vlak voor bezorging of afhalen', 'Advies van de kweker zelf, met aangroeigarantie'] }}
        />
      }
    />
    <div className="container">
      <ComparisonOutcomes outcomes={[
        { value: 'Sinds 2001', label: 'familiekwekerij in Otterlo' },
        { value: '10.000', label: 'planten op het veld' },
        { value: '7 soorten', label: 'in maten van 40 tot 120 cm' },
        { value: 'Vanaf 1 plant', label: 'zonder minimum' },
      ]} />
    </div>
  </section>
)

/* ───────── Variant 2: hairline icon cards + bold number ───────── */
const V2 = () => (
  <section id="v2" className="pb-16 sm:pb-20 lg:pb-24">
    <Content06
      copy={<Feature08Header badge="Waarom wij" title="Wij kweken rhododendrons. Niet meer, niet minder." description="Familiekwekerij in Otterlo. Alles wat we verkopen groeit op ons eigen veld in de volle grond en gaat met kluit naar uw tuin." />}
      media={
        <CaptionedFigure src={portrait} alt={portraitAlt}
          below={<QuoteCard quote="Een gezonde plant is geen toeval. Dat is onze standaard." name="Gert Top" role="Oprichter en kweker, Otterlo" noteLabel="Persoonlijk advies" note={PHONE} />} />
      }
      reasons={
        <Feature08Grid features={[
          { icon: Sprout, title: 'Volle grond, geen pot', description: 'Jaren buiten gegroeid op veenrijke bodem. Dat geeft een sterk wortelstelsel.' },
          { icon: Shovel, title: 'Gerooid met kluit', description: 'Pas vlak voor uw bezorging of afhaling uit de grond, dus vers in uw tuin.' },
          { icon: ShieldCheck, title: 'Aangroeigarantie', description: 'Op elke bestelling, ook bij één plant. [voorwaarden volgen]' },
          { icon: MessageCircle, title: 'Direct met de kweker', description: 'Advies over soort, maat en standplaats komt van Gert zelf.' },
        ]} />
      }
    />
    <div>
      <BoldStats big="10.000" title="planten op ons veld in Otterlo" text="Zeven soorten in maten van 40 tot 120 cm, allemaal in de volle grond en gerooid met kluit." image={novaZembla} imageAlt="Rhododendron Nova Zembla in bloei"
        figures={[{ value: '2001', label: 'Familiekwekerij' }, { value: '7', label: 'Soorten' }, { value: '40–120 cm', label: 'Plantmaten' }, { value: 'Vanaf 1', label: 'Plant, geen minimum' }]} />
    </div>
  </section>
)

/* ───────── Variant 3: numbered list + fact sheet ───────── */
const V3 = () => (
  <section id="v3" className="pb-16 sm:pb-20 lg:pb-24">
    <Content06
      copy={<SectionHeader eyebrow="Waarom Top Rhododendrons" title="Rhododendrons van het veld, niet uit de pot." description="Specialist in één gewas, sinds 2001 in Otterlo. Vier redenen waarom onze planten aanslaan in uw tuin." />}
      media={<CaptionedFigure src={portrait} alt={portraitAlt} caption="Gert Top" sub={<>Oprichter en kweker, Otterlo · <span className="whitespace-nowrap">Persoonlijk advies: {PHONE}</span></>} />}
      reasons={
        <ServicesList services={[
          { title: 'Gegroeid in de volle grond', sub: 'Otterlo, Veluwe', description: 'Jaren buiten op veenrijke bodem: een sterk wortelstelsel.', deliverables: ['veenrijke bodem', 'winterhard'] },
          { title: 'Gerooid met kluit, op uw dag', sub: 'Vers van het veld', description: 'Uw planten blijven in de grond tot vlak voor bezorging of afhalen.', deliverables: ['met kluit', 'eigen transport'] },
          { title: 'Aangroeigarantie', sub: '[voorwaarden volgen]', description: 'Op elke bestelling, vanaf één plant. Aanplanten kunnen wij ook doen.', deliverables: ['vanaf 1 plant', 'aanplanten [prijs volgt]'] },
          { title: 'U spreekt de kweker zelf', sub: 'Gert Top', description: 'Advies over soort, maat en standplaats van wie de planten kweekt.', deliverables: ['telefoon', 'WhatsApp', 'op de kwekerij'] },
        ]} />
      }
    />
    <div className="container">
      <KeyValueList items={[
        { label: 'Kwekerij', value: 'Familiebedrijf in Otterlo', description: 'Sinds 2001, alleen rhododendrons' },
        { label: 'Teelt', value: 'Volle grond, veenrijke bodem', description: 'Gerooid met kluit' },
        { label: 'Voorraad', value: '10.000 planten op het veld' },
        { label: 'Assortiment', value: '7 soorten, 40–120 cm' },
        { label: 'Bestellen', value: 'Vanaf 1 plant', description: 'Geen minimumbestelling' },
        { label: 'Bezorging', value: 'Nederland, België, Duitsland', description: '[tarieven volgen]' },
        { label: 'Aanplanten', value: 'Aanplantservice mogelijk', description: '[prijs volgt]' },
        { label: 'Garantie', value: 'Aangroeigarantie', description: '[voorwaarden volgen]' },
      ]} />
    </div>
  </section>
)

function App() {
  return (
    <main>
      <Label n="1" name="сравнение: наше поле против контейнера из садового центра; внизу строка фактов" parts="Split Content Section (id 28310), Comparison Section (id 26826), Gallery Grid with Captions — figure с подписью (id 26909)" />
      <HeroStub />
      <V1 />

      <Label n="2" name="четыре карточки с иконками на тонких линиях; под портретом цитата Герта; внизу крупная цифра с фото и ряд фактов" parts="Split Content Section (id 28310), Feature Grid Spotlight Cards (id 26797), Single Voice Spotlight Testimonial (id 28169), Bold Stats (id 18908), figure (id 26909)" />
      <HeroStub />
      <V2 />

      <Label n="3" name="нумерованный список причин с чипами; внизу карточка «в двух словах» из пар факт — значение" parts="Services List (id 33903), Split Content Section (id 28310), Key Value List (id 25162), figure (id 26909)" />
      <HeroStub />
      <V3 />
    </main>
  )
}

createRoot(document.getElementById('root')!).render(<App />)
