// Three motion mockups of the homepage block "De kweker", assembled from animated
// 21st.dev components. Real copy and photos only.
import { createRoot } from 'react-dom/client'
import './styles.css'
import ScrollRevealImage from '@/components/scroll-reveal-image'
import { ReadingTextReveal } from '@/components/reading-text-reveal'
import { ZoomParallax } from '@/components/zoom-parallax'
import { StickyScroll } from '@/components/sticky-scroll-reveal'
import { Button } from '@/components/ui/button'
import portrait from './img/owner-portrait.webp'
import shrub from './img/cunninghams-white-2.webp'
import truss from './img/cunninghams-white.webp'
import nova from './img/nova-zembla-2.webp'
import roseum from './img/roseum-elegans-2.webp'
import boursault from './img/catawbiense-boursault-2.webp'
import ponticum from './img/ponticum-2.webp'
import ponticumRoseum from './img/ponticum-roseum-2.webp'

const tel = 'tel:+31620104312'
const wa = 'https://wa.me/31620297849'

function Label({ n, name, parts }: { n: string; name: string; parts: string }) {
  return <div className="relative z-30 bg-foreground px-5 py-3 text-[13px] text-background"><b className="font-semibold">Вариант {n} — {name}.</b> <span className="opacity-80">Компоненты 21st.dev: {parts}</span></div>
}
function Signature() {
  return (
    <div className="mt-14 flex flex-wrap items-center gap-x-6 gap-y-5">
      <div className="flex items-center gap-4">
        <img src={portrait} alt="Gert Top" className="size-16 rounded-full object-cover object-[50%_20%]" />
        <div><div className="text-[17px] font-semibold">Gert Top</div><div className="text-[15px] text-muted-foreground">Oprichter en kweker · Otterlo, sinds 2001</div></div>
      </div>
      <div className="flex gap-3"><Button asChild><a href={tel}>Bel de kweker</a></Button><Button variant="outline" asChild><a href={wa} target="_blank" rel="noopener">WhatsApp</a></Button></div>
    </div>
  )
}

function App() {
  return (
    <main>
      <Label n="1" name="Манифест проявляется по словам, затем раскрывается фото" parts="Reading Text Reveal (id 9386) + Scroll Reveal Image (id 24466)" />
      <section id="variant-1" className="pt-28 pb-24">
        <ReadingTextReveal
          minHeight="150vh"
          segments={[
            'Wij kweken rhododendrons. Niet meer, niet minder.',
            'Sinds 2001, op de veenrijke bodem van de Veluwe in Otterlo.',
            'Een gezonde plant is geen toeval. Dat is onze standaard.',
          ]}
          after={<Signature />}
        />
        <div className="mt-24">
          <ScrollRevealImage src={shrub} alt="Bloeiende Cunningham's White op de kwekerij" height="78vh" fromWidth="46vw" toWidth="92vw" innerWidth="92vw" toRadius="28px" imageClassName="object-[50%_40%]" />
        </div>
      </section>

      <Label n="2" name="Кинематографичный «влёт» в питомник" parts="Zoom Parallax (id 5967)" />
      <section id="variant-2">
        <ZoomParallax
          images={[
            { src: shrub, alt: "Cunningham's White" },
            { src: nova, alt: 'Nova Zembla' },
            { src: portrait, alt: 'Gert Top, oprichter en kweker', className: 'object-[50%_20%]' },
            { src: roseum, alt: 'Roseum Elegans' },
            { src: boursault, alt: 'Catawbiense Boursault' },
            { src: ponticum, alt: 'Ponticum' },
            { src: ponticumRoseum, alt: 'Ponticum Roseum' },
          ]}
          overlay={
            <div className="w-full bg-gradient-to-t from-black/75 via-black/35 to-transparent px-6 pt-40 pb-14 text-white md:px-16 md:pb-20">
              <p className="max-w-4xl text-4xl leading-[1.05] font-semibold tracking-[-0.035em] md:text-7xl">Wij kweken rhododendrons. Niet meer, niet minder.</p>
              <p className="mt-5 text-lg text-white/85">Gert Top, oprichter en kweker · Otterlo, sinds 2001</p>
            </div>
          }
        />
      </section>

      <Label n="3" name="История главами, фото рядом меняется" parts="Sticky Scroll Reveal (Aceternity, id 952)" />
      <section id="variant-3" className="py-24">
        <StickyScroll
          content={[
            { title: 'Wij kweken rhododendrons. Niet meer, niet minder.', description: 'Gert Top, oprichter en kweker. Familiekwekerij in Otterlo, op de Veluwe, sinds 2001.', content: <img src={portrait} alt="Gert Top" className="h-full w-full object-cover object-[50%_20%]" /> },
            { title: 'Veenrijke bodem, sterk wortelstelsel.', description: 'Dankzij onze veenrijke bodem en een uitgebalanceerde watergift passen onze planten zich moeiteloos aan in uw tuin.', content: <img src={truss} alt="Cunningham's White" className="h-full w-full object-cover" /> },
            { title: 'Vers gerooid voor uw levering.', description: 'Uw planten staan niet onnodig te wachten: we rooien ze vers voor de bezorging of voor het moment dat u ze komt afhalen.', content: <img src={nova} alt="Nova Zembla" className="h-full w-full object-cover" /> },
            { title: 'Aangroeigarantie op elke plant.', description: 'Niet aangeslagen in het eerste seizoen? Wij vervangen kosteloos. U spreekt rechtstreeks met de kweker.', content: <img src={roseum} alt="Roseum Elegans" className="h-full w-full object-cover" /> },
          ]}
        />
        <div className="mx-auto max-w-6xl px-6 md:px-10"><div className="flex gap-3"><Button asChild><a href={tel}>Bel de kweker</a></Button><Button variant="outline" asChild><a href={wa} target="_blank" rel="noopener">WhatsApp</a></Button></div></div>
      </section>
      <div className="h-[40vh]" />
    </main>
  )
}
createRoot(document.getElementById('root')!).render(<App />)
