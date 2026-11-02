import { motion, useReducedMotion } from 'framer-motion'
import { VideoHero } from '@/components/ui/video-hero'
import { Button } from '@/components/ui/button'
import { Reveal } from '@/components/ui/reveal'
import { ScrollHorizontal } from '@/components/ui/scroll-horizontal'
import { CtaFloatingGallery } from '@/components/ui/cta-floating-gallery'
import { Faq } from '@/components/ui/faq'
import { HeaderB, FooterB, HeadB, Rule, SealB, ContactB } from './shared'
import { varieties, story, promises, faq, img, company, tuinturf, facts } from '@/data/content'

export default function Home() {
  const reduce = useReducedMotion()
  return (
    <>
      <HeaderB />
      <main className="on-dark">
        <VideoHero
          align="center"
          overlay="soft"
          eyebrow="Familiekwekerij op de Veluwe · Otterlo · sinds 2001"
          title="Gekweekt op veenrijke grond. Geleverd met garantie."
          titleClassName="text-[clamp(36px,5.2vw,76px)] uppercase tracking-[0.02em]"
          leading="leading-[1.08]"
          text="Tienduizend rhododendrons op stam, vers gerooid op de dag van levering. Eén familie, één specialisme, sinds 2001."
          actions={<><Button href="#collectie" variant="white" size="lg" arrow>Ontdek de collectie</Button><Button href="groothandel.html" variant="outline-white" size="lg">Groothandel</Button></>}
        >
          <motion.div initial={reduce ? false : { opacity: 0, scale: 0.9 }} animate={{ opacity: 1, scale: 1 }} transition={{ duration: 1.2, ease: [0.16, 1, 0.3, 1] }} className="pointer-events-none absolute inset-x-0 top-[22%] flex justify-center md:top-[18%]">
            <SealB className="size-28 text-white/90 md:size-36" id="hero-seal" />
          </motion.div>
        </VideoHero>

        {/* Facts band */}
        <section className="border-b border-white/10 bg-bg-2">
          <ul className="container-x mx-auto grid max-w-6xl grid-cols-2 divide-white/10 md:grid-cols-4 md:divide-x">
            {facts.map((f) => <li key={f.k} className="py-7 text-center md:py-9"><p className="font-display text-[20px] md:text-[22px]">{f.k}</p><p className="mt-1 text-[12.5px] tracking-[0.1em] uppercase text-muted">{f.v}</p></li>)}
          </ul>
        </section>

        {/* Statement */}
        <section className="container-x py-24 text-center md:py-36">
          <Reveal className="mx-auto max-w-4xl">
            <p className="eyebrow text-accent">Het landgoed</p>
            <h2 className="mt-6 font-display text-[clamp(32px,4.6vw,64px)] leading-[1.1] text-balance">{story.h}</h2>
            <Rule className="mx-auto my-10 max-w-xs" />
            <p className="mx-auto max-w-2xl text-[17px] leading-relaxed text-fg-2 md:text-[19px]">{story.p1} {story.p2}</p>
          </Reveal>
        </section>

        {/* Collectie: horizontal scroll */}
        <section id="collectie" className="border-y border-white/10 bg-bg-2 pb-10 md:pb-0">
          <ScrollHorizontal
            items={varieties}
            itemWidth={460}
            gap={28}
            mobileWidth={290}
            header={<div className="container-x mb-8 flex flex-col gap-3 pt-14 md:mb-10 md:flex-row md:items-end md:justify-between md:pt-0"><HeadB align="left" eyebrow="De collectie" title="Zeven soorten, alle winterhard." /><p className="max-w-[40ch] text-[14.5px] text-muted md:text-right">Prijs per plant in 40–60 cm. Ook in 60–80, 80–100 en 100–120 cm. Geen minimumbestelling.</p></div>}
            render={(v, i) => (
              <a href="#" className="group/c block">
                <div className="relative aspect-[4/5] overflow-hidden bg-surface frame">
                  <img src={img(`${v.slug}-2`)} alt={v.name} loading="lazy" className="h-full w-full object-cover img-treat transition-transform duration-[1200ms] ease-[cubic-bezier(.22,1,.36,1)] group-hover/c:scale-[1.04]" />
                  <span className="absolute left-4 top-4 bg-bg/80 px-2.5 py-1 font-display text-[13px] tracking-[0.2em]">{String(i + 1).padStart(2, '0')}</span>
                </div>
                <div className="mt-7 flex items-start justify-between gap-4">
                  <div><h3 className="font-display text-[24px] leading-tight md:text-[26px]">{v.name}</h3><p className="mt-1.5 text-[13px] tracking-[0.08em] uppercase text-muted">{v.color} · {v.bloei} · {v.hoogte}</p></div>
                  <p className="shrink-0 font-display text-[20px] text-accent">€ {v.from}</p>
                </div>
                <p className="mt-3 max-w-[40ch] text-[14.5px] leading-relaxed text-fg-2">{v.short}</p>
              </a>
            )}
          />
          <div className="container-x mx-auto flex max-w-6xl flex-col items-center gap-4 border-t border-white/10 py-10 text-center md:flex-row md:justify-between md:text-left">
            <p className="text-[14.5px] text-muted">Bij elke bestelling: {tuinturf.name}, € {tuinturf.price} {tuinturf.unit}.</p>
            <Button href="#" variant="outline-white" size="md" arrow>Alle maten en prijzen</Button>
          </div>
        </section>

        {/* Kweker */}
        <section id="kwekerij" className="container-x py-24 md:py-36">
          <div className="mx-auto grid max-w-6xl items-center gap-14 md:grid-cols-2 md:gap-24">
            <Reveal>
              <figure className="mx-auto max-w-[420px]">
                <div className="frame aspect-[3/4] overflow-hidden bg-surface"><img src={img('owner-portrait')} alt={`${company.founder}, oprichter van ${company.name}`} className="h-full w-full object-cover img-treat" /></div>
                <figcaption className="mt-6 text-center"><p className="font-display text-[20px]">{company.founder}</p><p className="text-[12px] tracking-[0.2em] uppercase text-muted">Oprichter &amp; kweker</p></figcaption>
              </figure>
            </Reveal>
            <div>
              <Reveal><HeadB align="left" eyebrow="De kweker" title={`„${story.quote}”`} /></Reveal>
              <Reveal index={1}><p className="mt-7 max-w-[56ch] text-[16.5px] leading-relaxed text-fg-2">{story.p2} Wij rooien op de dag van levering, niet eerder: zo komt elke plant in optimale conditie aan.</p></Reveal>
              <ul className="mt-10 grid gap-x-10 gap-y-7 sm:grid-cols-2">
                {promises.map((p, i) => (
                  <Reveal as="li" key={p.title} index={i}><p className="eyebrow text-accent">0{i + 1}</p><h3 className="mt-2 font-display text-[19px] leading-snug">{p.title}</h3><p className="mt-2 text-[14.5px] leading-relaxed text-fg-2">{p.text}</p></Reveal>
                ))}
              </ul>
            </div>
          </div>
        </section>

        {/* Veld */}
        <section className="relative overflow-hidden">
          <img src={img('B2BHERO')} alt="Rijen witte rhododendrons op het veld van de kwekerij in Otterlo" className="h-[60vh] min-h-[380px] w-full object-cover object-[50%_60%] img-treat md:h-[78vh]" />
          <div className="absolute inset-0 bg-gradient-to-t from-bg via-bg/20 to-transparent" />
          <Reveal className="absolute inset-x-0 bottom-0 pb-12 text-center md:pb-16"><p className="eyebrow text-accent">Het veld · Esserbroekweg, Otterlo</p><p className="mt-3 font-display text-[clamp(26px,3.4vw,44px)]">10.000 planten op stam, in bloei begin mei.</p></Reveal>
        </section>

        {/* CTA groothandel */}
        <CtaFloatingGallery
          dark
          eyebrow="Voor professionals"
          title="Hoveniers, gemeenten en projecten: één kweker, vaste contactpersoon."
          description="Partijprijzen vanaf 25 stuks, aangroeigarantie op elke plant, eigen transport op de afgesproken dag. Plantpaspoort via NAK Tuinbouw, factuur op 30 dagen."
          actions={<><Button href="groothandel.html" variant="solid" size="lg" arrow>Naar groothandel</Button><Button href={company.whatsapp} variant="outline-white" size="lg">WhatsApp</Button></>}
          images={[{ src: img('catawbiense-grandiflorum-2-sm'), alt: 'Catawbiense Grandiflorum' }, { src: img('nova-zembla-2-sm'), alt: 'Nova Zembla' }, { src: img('ponticum-2-sm'), alt: 'Ponticum' }, { src: img('cunninghams-white-2-sm'), alt: "Cunningham's White" }, { src: img('B2BHERO-sm'), alt: 'Het veld in Otterlo' }, { src: img('roseum-elegans-2-sm'), alt: 'Roseum Elegans' }]}
          className="mx-auto max-w-7xl"
        />

        {/* Advies */}
        <section id="advies" className="border-t border-white/10 bg-bg-2 py-24 md:py-32">
          <div className="container-x mx-auto max-w-4xl">
            <Reveal><HeadB eyebrow="Advies" title="Wat u wilt weten voordat u plant." /></Reveal>
            <Reveal index={1} className="mt-12"><Faq dark items={faq} /></Reveal>
          </div>
        </section>

        {/* Bezoek */}
        <section id="bezoek" className="container-x py-24 md:py-32">
          <div className="mx-auto max-w-6xl">
            <Reveal><HeadB eyebrow="Bezoek" title="Welkom op het landgoed in Otterlo." text="Kom kijken op het veld, of bel voor persoonlijk advies over soort, maat en standplaats." /></Reveal>
            <Reveal index={1} className="mt-8 flex flex-wrap justify-center gap-3"><Button href={company.phone1Href} variant="solid" size="lg">Bel {company.phone1}</Button><Button href={company.whatsapp} variant="outline-white" size="lg">WhatsApp</Button><Button href={`mailto:${company.email}`} variant="outline-white" size="lg">E-mail</Button></Reveal>
            <Rule className="my-14" />
            <Reveal index={2}><ContactB /></Reveal>
          </div>
        </section>
      </main>
      <FooterB />
    </>
  )
}
