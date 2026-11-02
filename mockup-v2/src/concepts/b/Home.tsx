import { VideoHero } from '@/components/ui/video-hero'
import { Button } from '@/components/ui/button'
import { Reveal } from '@/components/ui/reveal'
import { ScrollHorizontal } from '@/components/ui/scroll-horizontal'
import { SplitCta } from '@/components/ui/split-cta'
import { Faq } from '@/components/ui/faq'
import { ProductSheet } from '@/components/ui/product-sheet'
import { openSheet } from '@/lib/store'
import { HeaderB, FooterB, HeadB, Rule, SealB, ContactB } from './shared'
import { varieties, story, promises, faq, img, srcset, company, tuinturf, facts } from '@/data/content'

export default function Home() {
  return (
    <>
      <a href="#main" className="skip-link">Naar de inhoud</a>
      <HeaderB />
      <main id="main">
        <VideoHero
          align="center"
          above={<SealB simple className="mb-2 size-20 text-white/95 short:hidden md:size-24" id="hero-seal" />}
          eyebrow={<><span className="hidden sm:inline">Familiekwekerij op de Veluwe · </span>Otterlo · sinds 2001</>}
          title="Gekweekt op veenrijke grond. Geleverd met aangroeigarantie."
          titleClassName="text-[clamp(32px,4.8vw,68px)] short:text-[clamp(28px,4vw,52px)]"
          leading="leading-[1.1]"
          text="Tienduizend rhododendrons op ons veld in Otterlo, vers gerooid voor uw levering. Eén familie, één specialisme, sinds 2001."
          actions={<><Button href="#collectie" variant="white" size="lg" arrow>Ontdek de collectie</Button><Button href="groothandel.html" variant="outline-white" size="lg" className="short:hidden">Groothandel</Button></>}
        />

        {/* Facts band (dark) */}
        <section className="night border-b border-white/10 on-dark">
          <ul className="container-x mx-auto grid max-w-6xl grid-cols-2 divide-white/10 md:grid-cols-4 md:divide-x" aria-label="Kerngegevens">
            {facts.map((f) => <li key={f.k} className="py-6 text-center md:py-8"><p className="font-display text-[19px] md:text-[21px]">{f.k}</p><p className="mt-1 text-[13px] text-white/75">{f.v}</p></li>)}
          </ul>
        </section>

        {/* Statement */}
        <section className="container-x py-20 text-center md:py-32">
          <Reveal className="mx-auto max-w-4xl">
            <p className="eyebrow text-accent-2">De kwekerij</p>
            <h2 className="mt-6 font-display text-[clamp(30px,4.4vw,60px)] text-balance leading-[1.1]">{story.h}</h2>
            <Rule className="mx-auto my-10 max-w-xs" />
            <p className="mx-auto max-w-2xl text-[17px] leading-relaxed text-fg-2 md:text-[19px]">{story.p1} {story.p2}</p>
          </Reveal>
        </section>

        {/* Collectie: horizontal scroll */}
        <section id="collectie" className="border-y border-line bg-bg-2 pb-10 lg:pb-0">
          <ScrollHorizontal
            items={varieties}
            maxItemWidth={440}
            gap={28}
            mobileWidth={290}
            captionHeight={170}
            header={<div className="container-x mb-8 flex flex-col gap-3 pt-14 lg:mb-8 lg:flex-row lg:items-end lg:justify-between lg:pt-0"><HeadB align="left" eyebrow="De collectie" title="Zeven soorten, alle winterhard." /><p className="max-w-[44ch] text-[14.5px] text-muted lg:text-right">Prijs per plant in 40–60 cm. Ook in 60–80, 80–100 en 100–120 cm. Geen minimumbestelling. <span className="hidden lg:inline">Scroll om verder te kijken.</span></p></div>}
            render={(v, i) => (
              <button type="button" onClick={() => openSheet(v.slug)} className="group/c block w-full text-left">
                <div className="frame relative aspect-[4/5] overflow-hidden bg-surface">
                  <img src={img(`${v.slug}-2`)} srcSet={srcset(`${v.slug}-2`)} sizes="(min-width: 1024px) 440px, 290px" alt={v.name} loading="lazy" className="h-full w-full object-cover img-treat transition-transform duration-[1200ms] ease-[cubic-bezier(.22,1,.36,1)] group-hover/c:scale-[1.04]" />
                  <span className="absolute left-4 top-4 bg-bg/90 px-2.5 py-1 font-display text-[13px] tracking-[0.2em] text-fg">{String(i + 1).padStart(2, '0')}</span>
                </div>
                <div className="mt-7 flex items-start justify-between gap-4">
                  <div><h3 className="font-display text-[22px] leading-tight md:text-[24px]">{v.name}</h3><p className="mt-1.5 text-[13.5px] text-muted">{v.color} · {v.bloei} · {v.hoogte}</p></div>
                  <p className="shrink-0 font-display text-[19px] text-accent-2">vanaf € {v.from}</p>
                </div>
                <p className="mt-3 max-w-[40ch] text-[14.5px] leading-relaxed text-fg-2">{v.short}</p>
              </button>
            )}
          />
          <div className="container-x mx-auto flex max-w-6xl flex-col items-center gap-4 border-t border-line py-10 text-center md:flex-row md:justify-between md:text-left">
            <p className="text-[14.5px] text-muted">Bij uw bestelling verkrijgbaar: {tuinturf.name}, € {tuinturf.price} {tuinturf.unit}.</p>
            <Button as="button" type="button" variant="outline" size="md" arrow onClick={() => openSheet(varieties[0].slug)}>Maten en prijzen</Button>
          </div>
        </section>

        {/* Kweker */}
        <section id="kwekerij" className="container-x py-20 md:py-32">
          <div className="mx-auto grid grid-cols-1 max-w-6xl items-center gap-14 md:grid-cols-2 md:gap-16 lg:gap-24">
            <Reveal>
              <figure className="mx-auto max-w-[420px]">
                <div className="frame aspect-[3/4] overflow-hidden bg-surface"><img src={img('owner-portrait')} alt={`${company.founder}, oprichter van ${company.name}`} loading="lazy" className="h-full w-full object-cover img-treat" /></div>
                <figcaption className="mt-6 text-center"><p className="font-display text-[20px]">{company.founder}</p><p className="text-[12px] tracking-[0.2em] uppercase text-muted">Oprichter &amp; kweker</p></figcaption>
              </figure>
            </Reveal>
            <div>
              <Reveal><HeadB align="left" eyebrow="De kweker" title={`„${story.quote}”`} /></Reveal>
              <Reveal index={1}><p className="mt-7 max-w-[56ch] text-[16.5px] leading-relaxed text-fg-2">{story.p2} {story.p3}</p></Reveal>
              <ul className="mt-10 grid grid-cols-1 gap-x-10 gap-y-7 lg:grid-cols-2">
                {promises.map((p, i) => (
                  <Reveal as="li" key={p.title} index={i}><p className="eyebrow text-accent-2">0{i + 1}</p><h3 className="mt-2 font-display text-[19px] leading-snug">{p.title}</h3><p className="mt-2 text-[14.5px] leading-relaxed text-fg-2">{p.text}</p></Reveal>
                ))}
              </ul>
            </div>
          </div>
        </section>

        {/* Veld */}
        <section className="relative overflow-hidden night on-dark">
          <img src={img('B2BHERO')} srcSet={srcset('B2BHERO')} sizes="100vw" alt="Rijen witte rhododendrons op het veld van de kwekerij in Otterlo" loading="lazy" className="h-[60vh] min-h-[380px] w-full object-cover object-[50%_60%] img-treat md:h-[78vh]" />
          <div className="absolute inset-0 bg-gradient-to-t from-night via-night/30 to-transparent" />
          <Reveal className="absolute inset-x-0 bottom-0 pb-12 text-center md:pb-16"><p className="eyebrow text-brass">Het veld · Esserbroekweg, Otterlo</p><p className="mt-3 font-display text-[clamp(24px,3.2vw,40px)]">10.000 planten, gekweekt op veenrijke grond.</p></Reveal>
        </section>

        {/* Voor uw tuin / professionals */}
        <div className="container-x py-20 md:py-28">
          <Reveal>
            <SplitCta
              className="gap-5"
              minH="min-h-[420px] md:min-h-[520px]"
              panels={[
                { eyebrow: 'Voor uw tuin', title: 'Vanaf één plant, bezorgd of af te halen in Otterlo.', text: 'Geen minimumbestelling. Persoonlijk advies over soort, maat en standplaats.', action: <Button href="#collectie" variant="white" size="md" arrow>Bekijk de collectie</Button>, image: img('cunninghams-white-2'), dark: true, className: 'frame' },
                { eyebrow: 'Voor professionals', title: 'Hoveniers, gemeenten en projecten.', text: 'Partijprijzen vanaf 25 stuks, vaste contactpersoon, plantpaspoort via NAK Tuinbouw, factuur op 30 dagen.', action: <Button href="groothandel.html" variant="white" size="md" arrow>Naar groothandel</Button>, image: img('B2BHERO'), dark: true, className: 'frame' },
              ]}
            />
          </Reveal>
        </div>

        {/* Advies */}
        <section id="advies" className="border-t border-line bg-bg-2 py-20 md:py-28">
          <div className="container-x mx-auto max-w-4xl">
            <Reveal><HeadB eyebrow="Advies · veelgestelde vragen" title="Wat u wilt weten voordat u plant." /></Reveal>
            <Reveal index={1} className="mt-12"><Faq items={faq} /></Reveal>
          </div>
        </section>

        {/* Bezoek */}
        <section id="bezoek" className="container-x py-20 md:py-28">
          <div className="mx-auto max-w-6xl">
            <Reveal><HeadB eyebrow="Bezoek" title="Welkom op de kwekerij in Otterlo." text="Kom kijken op het veld, of bel voor persoonlijk advies over soort, maat en standplaats." /></Reveal>
            <Reveal index={1} className="mt-8 flex flex-wrap justify-center gap-3"><Button href={company.phone1Href} variant="solid" size="lg">Bel {company.phone1}</Button><Button href={company.whatsapp} variant="outline" size="lg">WhatsApp</Button><Button href={`mailto:${company.email}`} variant="outline" size="lg">E-mail</Button></Reveal>
            <Rule className="my-14" />
            <Reveal index={2}><ContactB /></Reveal>
          </div>
        </section>
      </main>
      <FooterB compact />
      <ProductSheet />
    </>
  )
}
