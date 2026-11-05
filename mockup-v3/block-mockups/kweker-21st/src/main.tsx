// Three mockups of the homepage block "De kwekerij", each assembled from ready
// 21st.dev components (see src/components). Copy and facts come from the site
// (mockup-v3/src/data/content.ts) and the old site; nothing invented.
import { createRoot } from 'react-dom/client'
import { ShieldCheck, Sprout, MessageCircle } from 'lucide-react'
import './styles.css'
import { AboutPrebuiltui } from '@/components/about-prebuiltui'
import TestimonialsBlock from '@/components/testimonials-2'
import { About3 } from '@/components/about-3'
import { TestimonialsSection } from '@/components/testimonials-1'
import { Feature2 } from '@/components/feature-2'
import { Button } from '@/components/ui/button'
import { LogoMark } from '@/components/ui/logo-mark'
import portrait from './img/owner-portrait.webp'
import shrub from './img/cunninghams-white-2.webp'

const quote = 'Een gezonde plant is geen toeval. Dat is onze standaard.'
const story = 'Familiebedrijf in Otterlo, op de Veluwe. 10.000 planten op voorraad, direct van het veld naar uw tuin. Dankzij onze veenrijke bodem en een uitgebalanceerde watergift ontwikkelen onze planten een sterk wortelstelsel, met aangroeigarantie.'
const tel = 'tel:+31620104312'
const wa = 'https://wa.me/31620297849'
const features = [
  { icon: <ShieldCheck className="size-5" />, title: 'Aangroeigarantie op elke plant', desc: 'Niet aangeslagen in het eerste seizoen? Wij vervangen kosteloos.' },
  { icon: <Sprout className="size-5" />, title: 'Vers gerooid, flexibel geleverd', desc: 'We rooien uw planten vers voor de geplande bezorging of het moment dat u ze komt afhalen.' },
  { icon: <MessageCircle className="size-5" />, title: 'Persoonlijk advies van de kweker', desc: 'U spreekt rechtstreeks met de kweker, van vraag tot levering.' },
]
const actions = <><Button asChild><a href={tel}>Bel de kweker</a></Button><Button variant="outline" asChild><a href={wa} target="_blank" rel="noopener">WhatsApp</a></Button></>

function Label({ n, name, parts }: { n: string; name: string; parts: string }) {
  return (
    <div className="sticky top-0 z-20 bg-foreground px-5 py-3 text-[13px] text-background">
      <b className="font-semibold">Вариант {n} — {name}.</b> <span className="opacity-80">Компоненты 21st.dev: {parts}</span>
    </div>
  )
}

function App() {
  return (
    <main>
      <Label n="1" name="Портрет и обещания + цитата с фактами" parts="About (prebuiltui, id 6907) + Single Voice Spotlight Testimonial (id 28169)" />
      <section id="variant-1">
        <AboutPrebuiltui
          title="Wij kweken rhododendrons. Niet meer, niet minder."
          subtitle="Familiekwekerij in Otterlo, op de Veluwe, sinds 2001."
          image={portrait} imageAlt="Gert Top, oprichter en kweker van Top Rhododendrons"
          heading="Waarom onze planten aanslaan"
          text="Dankzij onze veenrijke bodem en een uitgebalanceerde watergift ontwikkelen onze planten een sterk wortelstelsel. Daardoor passen ze zich moeiteloos aan in uw tuin."
          features={features} actions={actions}
        />
        <div className="-mt-16">
          <TestimonialsBlock
            testimonial={{ quote, name: 'Gert Top', role: 'Oprichter en kweker', company: 'Top Rhododendrons', initials: 'GT', avatar: portrait }}
            metrics={[{ value: '2001', label: 'familiekwekerij' }, { value: '10.000', label: 'planten op voorraad' }, { value: '7', label: 'soorten' }]}
          />
        </div>
      </section>

      <Label n="2" name="Фото куста, карточка с цитатой, портрет и цифры" parts="About 3 (shadcnblocks, id 2202)" />
      <section id="variant-2">
        <About3
          title="Wij kweken rhododendrons. Niet meer, niet minder."
          description={story}
          mainImage={{ src: shrub, alt: "Bloeiende Cunningham's White op de kwekerij", className: 'object-[50%_45%] lg:max-h-none' }}
          secondaryImage={{ src: portrait, alt: 'Gert Top, oprichter en kweker', className: 'aspect-[4/5] object-[50%_25%] lg:aspect-auto lg:min-h-[460px]' }}
          breakout={{ logo: <LogoMark className="size-12" />, title: <>„{quote}”</>, description: 'Gert Top, oprichter en kweker. U spreekt rechtstreeks met de kweker, van vraag tot levering.', buttonText: 'Bel de kweker', buttonUrl: tel }}
          achievementsTitle="Onze kwekerij in cijfers"
          achievementsDescription="Alles van eigen veld in Otterlo, vers gerooid op de dag van levering, met aangroeigarantie op elke plant."
          achievements={[{ label: 'Familiekwekerij sinds', value: '2001' }, { label: 'Planten op voorraad', value: '10.000' }, { label: 'Soorten', value: '7' }, { label: 'Maten', value: '40–120 cm' }]}
        />
      </section>

      <Label n="3" name="Цитата по центру + история с фото" parts="Centered Testimonial (id 18914) + Feature 2 (shadcnblocks, id 2219)" />
      <section id="variant-3">
        <div className="px-6 pt-24 pb-4">
          <TestimonialsSection logo={<LogoMark className="size-7" />} brand="Top Rhododendrons" quote={<>„<span className="font-medium">Een gezonde plant</span> is geen toeval. Dat is onze standaard.”</>} name="Gert Top" role="Oprichter en kweker, sinds 2001" avatar={portrait} />
        </div>
        <Feature2
          title="Wij kweken rhododendrons. Niet meer, niet minder."
          description={story}
          imageSrc={shrub} imageAlt="Bloeiende Cunningham's White op de kwekerij"
          buttonPrimary={{ label: 'Bel de kweker', href: tel }}
          buttonSecondary={{ label: 'WhatsApp', href: wa }}
        >
          <ul className="mb-8 flex flex-col gap-3 text-left text-[15px] text-foreground">
            {features.map((f) => <li key={f.title} className="flex items-center gap-3"><span className="text-primary">{f.icon}</span>{f.title}</li>)}
          </ul>
        </Feature2>
      </section>
    </main>
  )
}
createRoot(document.getElementById('root')!).render(<App />)
