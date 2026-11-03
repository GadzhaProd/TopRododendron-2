// Homepage = concept C "Veld" (round 2, post-audit) one-to-one: header, hero copy,
// "Waarom" (field photo + four promises), "Planten" (grid + tuinturf banner),
// "De kweker", split CTA, FAQ, contact block, compact footer, product sheet.
// Added in C's own language: the bloom & planting calendar (after the varieties)
// with the entry into the plantgids. Copy follows the old site where the audits
// flagged C's wording (promises, "tot 120 cm", field caption, guarantee FAQ).
import { useState } from 'react'
import { ArrowUpRight, Check } from 'lucide-react'
import { SiteHeader } from '@/components/site-header'
import { SiteFooter } from '@/components/site-footer'
import { CartDrawer } from '@/components/cart-drawer'
import { ProductSheet } from '@/components/product-sheet'
import { Toast } from '@/components/toast'
import { VideoHero } from '@/components/video-hero'
import { Button, ext } from '@/components/button'
import { Reveal } from '@/components/reveal'
import { SectionHead as HeadC } from '@/components/section-head'
import { SplitCta } from '@/components/split-cta'
import { Faq } from '@/components/faq'
import { BloomCalendar, BloomLegend } from '@/components/bloom-calendar'
import { ContactBlock } from '@/components/contact-block'
import { openSheet, addToCart } from '@/lib/store'
import { varieties, story, promises, faq, img, srcset, company, tuinturf } from '@/data/content'

// C's order of the varieties (content array), also used for the calendar rows
const ordered = varieties

export default function Home() {
  const [turfAdded, setTurfAdded] = useState(false)
  return (
    <>
      <a href="#main" className="skip-link">Naar de inhoud</a>
      <SiteHeader page="home" hero />
      <main id="main">
        <VideoHero
          eyebrow={<><span className="hidden sm:inline">Familiekwekerij · </span>Otterlo, Veluwe · sinds 2001</>}
          title="Rhododendrons die aanslaan. Met aangroeigarantie."
          text="Gekweekt op veenrijke bodem, met een sterk wortelstelsel. Vers gerooid voor uw levering, bezorgd met eigen transport of af te halen in Otterlo."
          actions={<><Button href="#planten" variant="white" size="md" arrow className="px-5 split:h-14 split:px-8 split:text-[15px]">Bekijk de planten</Button><Button href="groothandel.html" variant="outline-white" size="md" className="px-5 split:h-14 split:px-8 split:text-[15px]">Groothandel</Button></>}
        />

        {/* Waarom: calm two-column */}
        <section id="waarom" className="container-x py-20 md:py-28">
          <div className="grid grid-cols-1 gap-10 md:grid-cols-2 md:gap-12 lg:gap-16">
            <Reveal className="relative min-h-[380px] overflow-hidden rounded-img bg-bg-2 md:min-h-full">
              <img src={img('B2BHERO')} srcSet={srcset('B2BHERO')} sizes="(min-width: 768px) 50vw, 100vw" alt="Het veld van de kwekerij in Otterlo" loading="lazy" className="absolute inset-0 h-full w-full object-cover object-[50%_60%] img-treat" />
              <div className="absolute inset-x-0 bottom-0 p-6 md:p-8"><span className="inline-block rounded-full bg-bg/90 px-3.5 py-1.5 text-[12px] font-medium text-fg">Het veld van de kwekerij, Otterlo</span></div>
            </Reveal>
            <div>
              <Reveal><HeadC eyebrow="Waarom Top Rhododendrons" title="Vier redenen waarom onze planten aanslaan." size="lg" /></Reveal>
              <Reveal index={1}><p className="mt-6 max-w-[56ch] text-[16.5px] leading-relaxed text-fg-2">{story.p2}</p></Reveal>
              <ol className="mt-8 divide-y divide-fg/10 border-y border-fg/10">
                {promises.map((p, i) => (
                  <Reveal as="li" key={p.title} index={i} className="grid grid-cols-1 gap-2 py-5 md:grid-cols-[48px_1fr]">
                    <span className="font-display text-[15px] text-muted">0{i + 1}</span>
                    <div><h3 className="font-display text-[21px] leading-tight">{p.title}</h3><p className="mt-1.5 max-w-[56ch] text-[14.5px] leading-relaxed text-fg-2">{p.text}</p></div>
                  </Reveal>
                ))}
              </ol>
              <Reveal index={4}><p className="mt-6 text-[14.5px] text-muted">10.000 planten op ons veld, zeven soorten in maten van 40 tot 120 cm. Geen minimumbestelling voor particulieren.</p></Reveal>
            </div>
          </div>
        </section>

        {/* Planten */}
        <section id="planten" className="bg-bg-2 py-20 md:py-28">
          <div className="container-x">
            <Reveal><HeadC eyebrow="Assortiment" title="Zeven soorten. Alle winterhard." text="Prijs per plant in 40–60 cm; ook leverbaar tot 120 cm. Bezorgd door heel Nederland of af te halen in Otterlo." /></Reveal>
            <div className="mt-12 grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
              {ordered.map((v, i) => (
                <Reveal key={v.slug} index={i % 4} className={i === 0 ? 'sm:col-span-2 lg:col-span-2 xl:col-span-2' : ''}>
                  <button type="button" onClick={() => openSheet(v.slug)} className="group/p block h-full w-full overflow-hidden rounded-img bg-surface text-left">
                    <div className={`${i === 0 ? 'aspect-[16/11]' : 'aspect-[4/5]'} overflow-hidden`}>
                      <img src={img(`${v.slug}-2`)} srcSet={srcset(`${v.slug}-2`)} sizes={i === 0 ? '(min-width: 1280px) 50vw, 100vw' : '(min-width: 1280px) 25vw, (min-width: 640px) 50vw, 100vw'} alt={v.name} loading="lazy" className="h-full w-full object-cover img-treat transition-transform duration-[1000ms] ease-[cubic-bezier(.22,1,.36,1)] group-hover/p:scale-[1.04]" />
                    </div>
                    <div className="p-5 md:p-6">
                      <div className="flex items-start justify-between gap-4"><h3 className="font-display text-[22px] leading-tight">{v.name}</h3><span className="inline-flex size-9 shrink-0 items-center justify-center rounded-full border border-fg/15 transition-colors group-hover/p:bg-fg group-hover/p:text-bg"><ArrowUpRight className="size-4" /></span></div>
                      <p className="mt-1.5 flex items-center gap-2 text-[13.5px] text-muted"><span className="size-2.5 shrink-0 rounded-full" style={{ background: v.hex, boxShadow: 'inset 0 0 0 1px rgba(0,0,0,.12)' }} />{v.color} · {v.bloei} · {v.hoogte}</p>
                      <p className="mt-3 text-[14.5px] leading-relaxed text-fg-2">{v.short}</p>
                      <p className="mt-4 text-[15px] font-semibold">vanaf € {v.from}</p>
                    </div>
                  </button>
                </Reveal>
              ))}
              <Reveal index={3} className="flex flex-col justify-between gap-5 rounded-img bg-fg p-6 text-bg on-dark md:p-7 xl:col-span-4 xl:flex-row xl:items-center">
                <div className="flex items-center gap-5">
                  <img src={img('tuinturf-sm')} alt="Tuinturf-substraat" loading="lazy" className="size-20 shrink-0 rounded-[14px] object-cover img-treat" />
                  <div><p className="eyebrow text-white/75">Bij het planten</p><h3 className="mt-2 font-display text-[22px] leading-tight">{tuinturf.name}</h3><p className="mt-2 max-w-[60ch] text-[14.5px] leading-relaxed text-white/85">{tuinturf.short}</p></div>
                </div>
                <div className="flex items-center justify-between gap-6 xl:justify-end"><p className="text-[15px] font-semibold">€ {tuinturf.price} <span className="font-normal text-white/75">per 40 L zak</span></p><Button as="button" type="button" variant="white" size="sm" onClick={() => { addToCart({ slug: tuinturf.slug, name: tuinturf.name, size: 'zak 40 L', price: tuinturf.price, qty: 1, image: 'tuinturf-sm' }); setTurfAdded(true) }}>{turfAdded ? <><Check className="size-4" /> Toegevoegd</> : 'Voeg toe'}</Button></div>
              </Reveal>
            </div>
          </div>
        </section>

        {/* Bloei- & plantkalender (added; data from the old site's bloom section) + entry into the plantgids */}
        <section id="kalender" className="bg-bg-2 pb-20 md:pb-28">
          <div className="container-x">
            <div className="grid grid-cols-1 gap-10 border-t border-fg/10 pt-16 md:pt-20 xl:grid-cols-12 xl:gap-16">
              <Reveal className="xl:col-span-5">
                <HeadC eyebrow="Bloei- & plantkalender" title="Wanneer bloeit úw favoriete soort?" text="Plan uw aankoop rondom het bloeimoment. Rhododendrons kunnen het hele jaar door geplant worden, behalve bij strenge vorst of droogte." />
                <Button href="plantgids.html" variant="solid" className="mt-8" arrow>Bekijk de plantgids</Button>
              </Reveal>
              <Reveal index={1} className="rounded-img bg-surface p-5 md:p-7 xl:col-span-7">
                <BloomCalendar rows={ordered} />
                <BloomLegend className="mt-6" />
              </Reveal>
            </div>
          </div>
        </section>

        {/* Kweker */}
        <section id="kweker" className="container-x py-20 md:py-28">
          <div className="grid grid-cols-1 items-center gap-10 md:grid-cols-2 md:gap-12 lg:grid-cols-12 lg:gap-16">
            <Reveal className="lg:col-span-5"><div className="aspect-[4/5] overflow-hidden rounded-img bg-bg-2"><img src={img('owner-portrait')} alt={`${company.founder}, oprichter van ${company.name}`} loading="lazy" className="h-full w-full object-cover object-[50%_15%] img-treat" /></div></Reveal>
            <div className="lg:col-span-7">
              <Reveal><HeadC eyebrow={`${company.founder} · oprichter & kweker`} title={story.h} size="lg" /></Reveal>
              <Reveal index={1}><p className="mt-7 max-w-[58ch] text-[17px] leading-relaxed text-fg-2">{story.p1}</p><p className="mt-4 max-w-[58ch] text-[16px] leading-relaxed text-fg-2">{story.p3} U spreekt rechtstreeks met de kweker, van vraag tot levering.</p></Reveal>
              <Reveal index={2} className="mt-8 rounded-img border border-fg/10 bg-surface p-6 md:p-7"><p className="font-display text-[22px] leading-snug md:text-[24px]">„{story.quote}”</p><p className="mt-3 text-[13.5px] text-muted">{company.founder}, {company.name}</p></Reveal>
              <Reveal index={3} className="mt-8 flex flex-wrap gap-3"><Button href={company.phone1Href} variant="solid" size="md">Bel de kweker</Button><Button href={company.whatsapp} {...ext} variant="outline" size="md">WhatsApp</Button></Reveal>
            </div>
          </div>
        </section>

        {/* Split CTA */}
        <div className="container-x pb-20 md:pb-28">
          <Reveal>
            <SplitCta
              className="gap-4 md:gap-5"
              minH="min-h-[420px] md:min-h-[520px]"
              panels={[
                { id: 'tuin', eyebrow: 'Voor uw tuin', title: 'Vanaf één plant, bezorgd of af te halen in Otterlo.', text: 'Geen minimumbestelling. Persoonlijk advies over soort, maat en standplaats.', action: <Button href="#planten" variant="white" size="md" arrow>Bekijk de planten</Button>, image: img('roseum-elegans-2'), imageSrcSet: srcset('roseum-elegans-2'), dark: true, className: 'rounded-img' },
                { id: 'pro', eyebrow: 'Voor professionals', title: 'Hoveniers, gemeenten en projecten.', text: 'Partijprijzen vanaf 25 stuks, vaste contactpersoon, plantpaspoort, factuur op 30 dagen.', action: <Button href="groothandel.html" variant="white" size="md" arrow>Naar groothandel</Button>, image: img('B2BHERO'), imageSrcSet: srcset('B2BHERO'), dark: true, className: 'rounded-img' },
              ]}
            />
          </Reveal>
        </div>

        {/* FAQ */}
        <section id="advies" className="bg-bg-2 py-20 md:py-28">
          <div className="container-x grid grid-cols-1 gap-12 lg:grid-cols-12">
            <Reveal className="lg:col-span-5"><HeadC eyebrow="Advies · veelgestelde vragen" title="Wat u wilt weten voordat u plant." text="Twijfelt u over soort, maat of standplaats? Bel ons; wij adviseren graag persoonlijk." /><Button href={company.phone1Href} variant="outline" className="mt-8" arrow>Bel voor advies</Button></Reveal>
            <Reveal index={1} className="lg:col-span-7"><Faq items={faq} variant="lines" /></Reveal>
          </div>
        </section>

        {/* Contact */}
        <section id="contact" className="container-x py-20 md:py-28">
          <Reveal className="rounded-img bg-accent p-8 text-white on-dark md:p-14">
            <HeadC dark eyebrow="Contact" title="Kom langs op de kwekerij, of bel ons." text="Wilt u advies over de juiste soort voor uw tuin? Wij helpen u graag persoonlijk." />
            <div className="mt-8 flex flex-wrap gap-3"><Button href={company.phone1Href} variant="white" size="lg">Bel {company.phone1}</Button><Button href={company.whatsapp} {...ext} variant="outline-white" size="lg">WhatsApp</Button><Button href={`mailto:${company.email}`} variant="outline-white" size="lg">E-mail</Button></div>
            <div className="mt-12 border-t border-white/15 pt-10"><ContactBlock dark /></div>
          </Reveal>
        </section>
      </main>
      <SiteFooter home />
      <ProductSheet />
      <CartDrawer />
      <Toast />
    </>
  )
}
