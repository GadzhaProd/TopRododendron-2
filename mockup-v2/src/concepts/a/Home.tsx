import { VideoHero } from '@/components/ui/video-hero'
import { Button } from '@/components/ui/button'
import { Reveal } from '@/components/ui/reveal'
import { StickyScroll, type StickyItem } from '@/components/ui/sticky-scroll'
import { ImageCardGrid } from '@/components/ui/image-card-grid'
import { Faq } from '@/components/ui/faq'
import { ProductSheet } from '@/components/ui/product-sheet'
import { openSheet } from '@/lib/store'
import { HeaderA, FooterA, SectionHead, ContactStrip } from './shared'
import { varieties, story, promises, facts, faq, img, srcset, company, tuinturf } from '@/data/content'

export default function Home() {
  const items: StickyItem[] = varieties.map((v) => ({ slug: v.slug, title: v.name, description: v.short, media: img(`${v.slug}-2`), srcSet: srcset(`${v.slug}-2`), meta: [v.color, v.bloei, v.hoogte], price: v.from, swatch: v.hex }))
  return (
    <>
      <a href="#main" className="skip-link">Naar de inhoud</a>
      <HeaderA />
      <main id="main">
        <VideoHero
          eyebrow={<><span className="hidden sm:inline">Familiekwekerij · </span>Otterlo, Veluwe · sinds 2001</>}
          title="Rhododendrons van eigen kwekerij."
          titleClassName="text-[clamp(38px,7vw,100px)] short:text-[clamp(32px,6vw,72px)]"
          text="Gekweekt op de veenrijke bodem van de Veluwe. Vers gerooid voor uw levering, met aangroeigarantie op elke plant."
          actions={<><Button href="#assortiment" variant="white" size="lg" arrow>Bekijk de collectie</Button><Button href="groothandel.html" variant="outline-white" size="lg" className="short:hidden">Groothandel</Button></>}
          bottomBar={<ul className="grid grid-cols-4 gap-8 text-white/85">{facts.map((f) => <li key={f.k}><p className="text-[15px] text-white">{f.k}</p><p className="text-[13px] text-white/75">{f.v}</p></li>)}</ul>}
        />
        <ul className="grid grid-cols-2 gap-x-6 gap-y-4 border-b border-line container-x py-6 md:hidden" aria-label="Kerngegevens">
          {facts.map((f) => <li key={f.k}><p className="text-[15px]">{f.k}</p><p className="text-[13px] text-muted">{f.v}</p></li>)}
        </ul>

        {/* Statement */}
        <section className="container-x py-24 md:py-36">
          <div className="mx-auto grid grid-cols-1 max-w-6xl gap-12 lg:grid-cols-12">
            <Reveal className="lg:col-span-7"><h2 className="font-display text-[clamp(36px,5vw,70px)] text-balance leading-[1.02]">{story.h}</h2></Reveal>
            <div className="flex flex-col gap-6 lg:col-span-5 lg:pt-3">
              <Reveal index={1}><p className="text-[18px] leading-relaxed text-fg">{story.p1}</p></Reveal>
              <Reveal index={2}><p className="text-[16px] leading-relaxed text-fg-2">{story.p2}</p></Reveal>
              <Reveal index={3}><a href="#kwekerij" className="eyebrow inline-flex items-center gap-3 text-fg hover:opacity-70"><span className="h-px w-10 bg-fg" />Over de kwekerij</a></Reveal>
            </div>
          </div>
        </section>

        {/* Assortiment */}
        <section id="assortiment" className="border-t border-line bg-bg-2/60 py-20 md:py-28">
          <div className="container-x">
            <Reveal><SectionHead eyebrow="Assortiment" title="Zeven soorten. Alle winterhard, alle van eigen veld." text="Prijs per plant in maat 40–60 cm; ook leverbaar in 60–80, 80–100 en 100–120 cm. Geen minimumbestelling voor particulieren." /></Reveal>
            <StickyScroll
              className="mt-14 md:mt-20"
              items={items}
              render={(it) => (
                <div>
                  <p className="eyebrow text-muted">{String(items.indexOf(it) + 1).padStart(2, '0')} / {String(items.length).padStart(2, '0')}</p>
                  <h3 className="mt-4 font-display text-[clamp(36px,3.6vw,54px)] leading-[1]">{it.title}</h3>
                  <p className="mt-4 flex items-center gap-3 text-[14px] text-fg-2"><span className="size-3 rounded-full border border-fg/15" style={{ background: it.swatch }} />{it.meta?.[0]}</p>
                  <p className="mt-5 max-w-[46ch] text-[17px] leading-relaxed text-fg-2">{it.description}</p>
                  <dl className="mt-7 grid max-w-md grid-cols-2 gap-x-6 gap-y-3 border-t border-line pt-5 text-[14px]">
                    <div><dt className="eyebrow text-muted">Bloei</dt><dd className="mt-1">{it.meta?.[1]}</dd></div>
                    <div><dt className="eyebrow text-muted">Hoogte</dt><dd className="mt-1">{it.meta?.[2]}</dd></div>
                  </dl>
                  <div className="mt-7 flex items-center gap-6">
                    <p className="font-display text-[26px]">vanaf € {it.price}</p>
                    <Button as="button" type="button" href="#" variant="outline" size="sm" arrow onClick={() => openSheet(it.slug)}>Bekijk plant</Button>
                  </div>
                </div>
              )}
              mobileRender={(it, i) => (
                <article className="border-b border-line pb-8">
                  <button type="button" onClick={() => openSheet(it.slug)} className="block w-full text-left" aria-label={`${it.title}: bekijk maten en prijzen`}>
                    <div className="aspect-[4/5] overflow-hidden bg-bg-2"><img src={it.media} srcSet={it.srcSet} sizes="100vw" alt={it.title} loading={i === 0 ? 'eager' : 'lazy'} className="h-full w-full object-cover img-treat" /></div>
                  </button>
                  <p className="eyebrow mt-5 text-muted">{String(i + 1).padStart(2, '0')}</p>
                  <h3 className="mt-2 font-display text-[32px] leading-none">{it.title}</h3>
                  <p className="mt-3 text-[15px] leading-relaxed text-fg-2">{it.description}</p>
                  <p className="mt-3 text-[13px] text-muted">{it.meta?.join(' · ')}</p>
                  <div className="mt-4 flex items-center justify-between"><p className="font-display text-[22px]">vanaf € {it.price}</p><Button as="button" type="button" variant="outline" size="sm" arrow onClick={() => openSheet(it.slug)}>Bekijk</Button></div>
                </article>
              )}
            />
            <Reveal className="mt-16 flex flex-col gap-6 border-t border-line pt-8 md:flex-row md:items-center md:justify-between">
              <div className="flex items-center gap-5"><img src={img('tuinturf-sm')} alt="Tuinturf-substraat" loading="lazy" className="size-20 object-cover img-treat" /><div><p className="eyebrow text-muted">Bij uw bestelling verkrijgbaar</p><p className="mt-1 font-display text-[22px]">{tuinturf.name} · € {tuinturf.price} {tuinturf.unit}</p><p className="text-[14px] text-fg-2">{tuinturf.text}</p></div></div>
              <Button as="button" type="button" variant="outline" size="md" onClick={() => openSheet(varieties[0].slug)}>Maten en prijzen</Button>
            </Reveal>
          </div>
        </section>

        {/* Kwekerij */}
        <section id="kwekerij" className="container-x py-24 md:py-36">
          <div className="mx-auto grid grid-cols-1 max-w-6xl gap-14 md:gap-12 lg:grid-cols-12 lg:gap-20">
            <Reveal className="lg:col-span-5">
              <figure>
                <div className="aspect-[3/4] overflow-hidden bg-bg-2"><img src={img('owner-portrait')} alt={`${company.founder}, oprichter van ${company.name}`} loading="lazy" className="h-full w-full object-cover img-treat" /></div>
                <figcaption className="mt-4 flex justify-between text-[12px] tracking-[0.18em] uppercase text-muted"><span>{company.founder}</span><span>Oprichter &amp; kweker</span></figcaption>
              </figure>
            </Reveal>
            <div className="lg:col-span-7">
              <Reveal><SectionHead eyebrow="De kwekerij" title="Een gezonde plant is geen toeval. Dat is onze standaard." /></Reveal>
              <Reveal index={1}><p className="mt-8 max-w-[58ch] text-[17px] leading-relaxed text-fg-2">{story.p2} {story.p3}</p></Reveal>
              <ol className="mt-10 border-t border-line">
                {promises.map((p, i) => (
                  <Reveal as="li" index={i} key={p.title} className="grid grid-cols-1 gap-2 border-b border-line py-5 md:grid-cols-[56px_1fr]">
                    <span className="eyebrow pt-1 text-muted">0{i + 1}</span>
                    <div><h3 className="font-display text-[22px] leading-tight">{p.title}</h3><p className="mt-1.5 max-w-[56ch] text-[15px] leading-relaxed text-fg-2">{p.text}</p></div>
                  </Reveal>
                ))}
              </ol>
            </div>
          </div>
        </section>

        {/* Field + doors */}
        <section className="container-x pb-24 md:pb-36">
          <Reveal>
            <figure className="relative overflow-hidden">
              <img src={img('B2BHERO')} srcSet={srcset('B2BHERO')} sizes="100vw" alt="Rijen witte rhododendrons op het veld van de kwekerij in Otterlo" loading="lazy" className="h-[52vh] min-h-[360px] w-full object-cover img-treat md:h-[70vh]" />
              <figcaption className="absolute bottom-5 left-5 bg-bg/90 px-4 py-2 text-[12px] tracking-[0.18em] uppercase text-fg md:bottom-8 md:left-8">Het veld · Esserbroekweg, Otterlo</figcaption>
            </figure>
          </Reveal>
          <Reveal className="mt-5 md:mt-6">
            <ImageCardGrid
              cols={3}
              aspect="aspect-[4/3] md:aspect-[4/5]"
              cards={[
                { name: 'Advies & vragen', description: 'Grond, standplaats, plantmoment en snoei: alles wat u wilt weten.', image: img('nova-zembla-2-sm'), srcSet: srcset('nova-zembla-2'), href: '#advies', meta: 'Plantgids' },
                { name: 'Bezoek de kwekerij', description: 'Kom kijken op het veld in Otterlo. Wij zetten uw bestelling klaar voor afhaal.', image: img('B2BHERO-sm'), srcSet: srcset('B2BHERO'), href: '#contact', meta: 'Otterlo', position: '50% 60%' },
                { name: 'Groothandel', description: 'Voor hoveniers, gemeenten en projecten. Partijprijzen vanaf 25 stuks.', image: img('catawbiense-grandiflorum-2-sm'), srcSet: srcset('catawbiense-grandiflorum-2'), href: 'groothandel.html', meta: 'Zakelijk' },
              ]}
            />
          </Reveal>
        </section>

        {/* Advies / FAQ */}
        <section id="advies" className="border-t border-line py-24 md:py-32">
          <div className="container-x mx-auto grid grid-cols-1 max-w-6xl gap-12 lg:grid-cols-12">
            <Reveal className="lg:col-span-5"><SectionHead eyebrow="Advies · veelgestelde vragen" title="Wat u wilt weten voordat u plant." text="Twijfelt u over soort, maat of standplaats? Bel ons; wij adviseren graag persoonlijk." /><Button href={company.phone1Href} variant="outline" className="mt-8" arrow>Bel voor advies</Button></Reveal>
            <Reveal index={1} className="lg:col-span-7"><Faq items={faq} /></Reveal>
          </div>
        </section>

        {/* Contact */}
        <section id="contact" className="border-t border-line bg-accent py-24 text-white on-dark md:py-32">
          <div className="container-x mx-auto max-w-6xl">
            <Reveal><SectionHead dark eyebrow="Contact" title="Kom langs op de kwekerij, of bel ons." text="Wilt u advies over de juiste soort voor uw tuin? Wij helpen u graag persoonlijk." /></Reveal>
            <Reveal index={1} className="mt-8 flex flex-wrap gap-3"><Button href={company.phone1Href} variant="white" size="lg">Bel {company.phone1}</Button><Button href={company.whatsapp} variant="outline-white" size="lg">WhatsApp</Button><Button href={`mailto:${company.email}`} variant="outline-white" size="lg">E-mail</Button></Reveal>
            <Reveal index={2} className="mt-14 border-t border-white/15 pt-10"><ContactStrip dark /></Reveal>
          </div>
        </section>
      </main>
      <FooterA compact />
      <ProductSheet />
    </>
  )
}
