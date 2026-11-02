import { ArrowRight } from 'lucide-react'
import { SiteHeader } from '@/components/site-header'
import { SiteFooter } from '@/components/site-footer'
import { CartDrawer } from '@/components/cart-drawer'
import { VideoHero } from '@/components/video-hero'
import { Button } from '@/components/button'
import { Reveal } from '@/components/reveal'
import { SectionHead } from '@/components/section-head'
import { VarietyCard } from '@/components/variety-card'
import { BloomCalendar, BloomLegend } from '@/components/bloom-calendar'
import { Faq } from '@/components/faq'
import { ContactForm } from '@/components/forms'
import { ContactBlock } from '@/components/contact-block'
import { varieties, popularOrder, trust, story, promises, faq, company, tuinturf, img, srcset } from '@/data/content'

const ordered = popularOrder.map((s) => varieties.find((v) => v.slug === s)!)

export default function Home() {
  return (
    <>
      <a href="#main" className="skip-link">Naar de inhoud</a>
      <SiteHeader current="home" />
      <main id="main">
        <VideoHero
          eyebrow={<>Kwekerij in Otterlo, Veluwe <span className="hidden sm:inline">· familiebedrijf</span> sinds 2001</>}
          title="Rhododendrons die aanslaan."
          text="Zeven winterharde soorten van eigen veld. Vers gerooid, bezorgd met eigen transport en geleverd met aangroeigarantie. Voor uw tuin, en voor uw project."
          actions={<><Button href="assortiment.html" variant="paper" size="lg" arrow>Bekijk het assortiment</Button><Button href="groothandel.html" variant="outline-white" size="lg" className="short:hidden">Groothandel</Button></>}
          bottomBar={
            <dl className="grid grid-cols-4 gap-6">
              {trust.map((t) => <div key={t.k}><dt className="eyebrow text-white/65">{t.k}</dt><dd className="mt-1.5 font-display text-[22px] leading-tight text-white">{t.v}</dd></div>)}
            </dl>
          }
        />
        {/* facts strip on phones (hero keeps only the message) */}
        <section aria-label="Kerngegevens" className="border-b border-line bg-paper-2 md:hidden">
          <dl className="container-x grid grid-cols-2 gap-x-6 gap-y-4 py-6">
            {trust.map((t) => <div key={t.k}><dt className="eyebrow text-muted">{t.k}</dt><dd className="mt-1 font-display text-[19px] leading-tight">{t.v}</dd></div>)}
          </dl>
        </section>

        {/* Assortiment */}
        <section id="assortiment" className="wrap container-x py-20 md:py-28">
          <Reveal className="flex flex-col gap-6 md:flex-row md:items-end md:justify-between">
            <SectionHead eyebrow="Assortiment · zeven soorten" title="Zeven soorten. Alle winterhard, alle van eigen veld." text="Prijs per plant vanaf 40–60 cm; ook leverbaar tot 120 cm en meer. Bezorgd door heel Nederland of af te halen in Otterlo." />
            <Button href="assortiment.html" variant="outline" size="md" arrow className="shrink-0">Alle maten en prijzen</Button>
          </Reveal>
          <div className="mt-10 grid grid-cols-2 gap-x-4 gap-y-9 sm:gap-x-6 sm:gap-y-12 lg:grid-cols-4">
            {ordered.map((v, i) => (
              <Reveal key={v.slug} index={i % 4}><VarietyCard v={v} index={i + 1} sizes="(min-width: 1024px) 25vw, 50vw" /></Reveal>
            ))}
            <Reveal index={3} className="flex">
              <a href={`product.html#${tuinturf.slug}`} className="group/t flex h-full w-full flex-col justify-between rounded-img bg-moss p-6 text-white on-dark transition-colors hover:bg-moss-2">
                <div>
                  <p className="eyebrow text-white/70">Bij het planten</p>
                  <h3 className="mt-3 font-display text-[26px] leading-tight">{tuinturf.name}</h3>
                  <p className="mt-3 text-[14.5px] leading-relaxed text-white/85">{tuinturf.short}</p>
                </div>
                <div className="mt-8 flex items-end justify-between gap-4">
                  <p className="num text-[15px]"><span className="font-semibold">€ {tuinturf.price}</span> <span className="text-white/70">per zak 40 L</span></p>
                  <span className="grid size-9 place-items-center rounded-full border border-white/50 transition-colors group-hover/t:bg-white group-hover/t:text-moss"><ArrowRight className="size-4" /></span>
                </div>
              </a>
            </Reveal>
          </div>
        </section>

        {/* Bloeikalender */}
        <section id="bloeikalender" className="bg-paper-2 py-20 md:py-28">
          <div className="wrap container-x">
            <Reveal><SectionHead eyebrow="Bloei- & plantkalender" title="Wanneer bloeit úw favoriete soort?" text="Plan uw aankoop rondom het bloeimoment. Rhododendrons kunnen het hele jaar door geplant worden, behalve bij strenge vorst of droogte; maart–april en september–oktober zijn ideaal." /></Reveal>
            <Reveal index={1} className="mt-10 rounded-img border border-line bg-paper p-4 sm:p-6 md:p-8">
              <BloomCalendar rows={ordered} />
              <BloomLegend className="mt-6" />
            </Reveal>
            <Reveal index={2} className="mt-8 flex flex-wrap items-center gap-4">
              <Button href="plantgids.html" variant="solid" size="lg" arrow>Bekijk de plantgids</Button>
              <p className="text-[14.5px] text-ink-2">Vergelijking van alle soorten, plantadvies en zeven lessen uit de kwekerij.</p>
            </Reveal>
          </div>
        </section>

        {/* De kwekerij */}
        <section id="kwekerij" className="wrap container-x py-20 md:py-28">
          <div className="grid grid-cols-1 gap-12 lg:grid-cols-12 lg:gap-16">
            <Reveal className="lg:col-span-6">
              <div className="relative aspect-[4/3] overflow-hidden rounded-img bg-paper-2 lg:aspect-[4/5]">
                <img src={img('B2BHERO')} srcSet={srcset('B2BHERO')} sizes="(min-width: 1024px) 50vw, 100vw" alt="Het veld van de kwekerij aan de Esserbroekweg in Otterlo, rijen witte rhododendrons" loading="lazy" className="absolute inset-0 h-full w-full object-cover object-[50%_65%] img-treat" />
              </div>
              <p className="mt-3 text-[13px] text-muted">Het veld · Esserbroekweg, Otterlo</p>
            </Reveal>
            <div className="lg:col-span-6">
              <Reveal><SectionHead eyebrow={story.eyebrow} title={story.h} size="lg" text={story.p1} /></Reveal>
              <Reveal index={1}><p className="mt-5 max-w-[56ch] text-[16px] leading-relaxed text-ink-2 md:text-[17px]">{story.p2}</p></Reveal>
              <ol className="mt-10 border-t border-line">
                {promises.map((p, i) => (
                  <Reveal as="li" key={p.title} index={i} className="grid grid-cols-[44px_1fr] gap-4 border-b border-line py-5">
                    <span className="num pt-1 font-display text-[18px] text-bloom">0{i + 1}</span>
                    <div><h3 className="font-display text-[22px] leading-tight">{p.title}</h3><p className="mt-1.5 max-w-[58ch] text-[14.5px] leading-relaxed text-ink-2">{p.text}</p></div>
                  </Reveal>
                ))}
              </ol>
            </div>
          </div>
        </section>

        {/* De kweker */}
        <section className="border-y border-line bg-surface">
          <div className="wrap container-x grid grid-cols-1 items-center gap-10 py-16 md:grid-cols-12 md:gap-12 md:py-24">
            <Reveal className="md:col-span-4 lg:col-span-3">
              <div className="aspect-[4/5] max-w-[360px] overflow-hidden rounded-img bg-paper-2"><img src={img('owner-portrait')} alt={`${company.founder}, oprichter van ${company.name}`} loading="lazy" className="h-full w-full object-cover object-[50%_20%] img-treat" /></div>
            </Reveal>
            <div className="md:col-span-8 lg:col-span-9">
              <Reveal>
                <blockquote>
                  <p className="font-display text-balance text-[clamp(28px,3.6vw,48px)] leading-[1.12]" style={{ fontVariationSettings: '"opsz" 72' }}>„{story.quote}”</p>
                  <footer className="mt-5 text-[14.5px] text-ink-2"><span className="font-medium text-ink">{company.founder}</span> · {company.founderRole}, {company.name}</footer>
                </blockquote>
              </Reveal>
              <Reveal index={1}><p className="mt-6 max-w-[60ch] text-[16px] leading-relaxed text-ink-2">{story.p3} U spreekt rechtstreeks met de kweker, van vraag tot levering.</p></Reveal>
              <Reveal index={2} className="mt-7 flex flex-wrap gap-3"><Button href={company.phone1Href} variant="ink" size="md">Bel de kweker</Button><Button href={company.whatsapp} variant="outline" size="md">WhatsApp</Button></Reveal>
            </div>
          </div>
        </section>

        {/* Twee deuren */}
        <section className="wrap container-x py-20 md:py-28">
          <div className="grid grid-cols-1 gap-5 md:grid-cols-2">
            {[
              { eyebrow: 'Voor uw tuin', title: 'Vanaf één plant, bezorgd of af te halen in Otterlo.', text: 'Geen minimumbestelling. Persoonlijk advies over soort, maat en standplaats.', cta: 'Bekijk het assortiment', href: 'assortiment.html', photo: 'roseum-elegans-2', pos: '50% 40%' },
              { eyebrow: 'Voor professionals', title: 'Hoveniers, gemeenten en projectontwikkelaars.', text: 'Partijprijzen vanaf 25 stuks, vaste contactpersoon, plantpaspoort, factuur op 30 dagen.', cta: 'Naar groothandel', href: 'groothandel.html', photo: 'B2BHERO', pos: '50% 60%' },
            ].map((p, i) => (
              <Reveal key={p.href} index={i}>
                <a href={p.href} className="group/d relative flex min-h-[440px] flex-col justify-end overflow-hidden rounded-img bg-night text-white on-dark md:min-h-[520px]">
                  <img src={img(p.photo)} srcSet={srcset(p.photo)} sizes="(min-width: 768px) 50vw, 100vw" alt="" loading="lazy" className="absolute inset-0 h-full w-full object-cover img-treat transition-transform duration-[1200ms] ease-[cubic-bezier(.22,1,.36,1)] group-hover/d:scale-[1.03]" style={{ objectPosition: p.pos }} />
                  <div className="absolute inset-0 bg-gradient-to-t from-[#0b120e]/90 via-[#0b120e]/40 to-transparent" />
                  <div className="relative p-7 md:p-9">
                    <p className="eyebrow text-white/75">{p.eyebrow}</p>
                    <h3 className="mt-3 max-w-[20ch] font-display text-[clamp(26px,3vw,36px)] leading-[1.08]">{p.title}</h3>
                    <p className="mt-3 max-w-[44ch] text-[14.5px] leading-relaxed text-white/85">{p.text}</p>
                    <span className="mt-6 inline-flex h-11 items-center gap-2 rounded-ui bg-paper px-5 text-[14px] font-medium text-ink">{p.cta}<ArrowRight className="size-4 transition-transform group-hover/d:translate-x-1" /></span>
                  </div>
                </a>
              </Reveal>
            ))}
          </div>
        </section>

        {/* Vraag & advies */}
        <section id="advies" className="bg-paper-2 py-20 md:py-28">
          <div className="wrap container-x grid grid-cols-1 gap-12 lg:grid-cols-12">
            <Reveal className="lg:col-span-5"><SectionHead eyebrow="Vraag & advies" title="Alles wat u wilt weten." text="Staat uw vraag er niet tussen? Neem gerust contact op, wij helpen u persoonlijk verder. Uitgebreider advies vindt u in de plantgids." /><div className="mt-8 flex flex-wrap gap-3"><Button href="plantgids.html" variant="outline" arrow>Naar de plantgids</Button><Button href={company.phone1Href} variant="ghost">Bel {company.phone1}</Button></div></Reveal>
            <Reveal index={1} className="lg:col-span-7"><Faq items={faq} /></Reveal>
          </div>
        </section>

        {/* Contact */}
        <section id="contact" className="wrap container-x py-20 md:py-28">
          <Reveal><SectionHead eyebrow="Contact" title="Kom langs op de kwekerij, of stuur een bericht." text="Wilt u advies over de juiste soort voor uw tuin, of een vrijblijvende prijsopgave? Wij reageren binnen één werkdag." /></Reveal>
          <div className="mt-12 grid grid-cols-1 gap-12 lg:grid-cols-12 lg:gap-16">
            <Reveal index={1} className="lg:col-span-7"><ContactForm /></Reveal>
            <Reveal index={2} className="lg:col-span-5"><div className="rounded-img border border-line bg-surface p-6 md:p-8"><ContactBlock className="lg:grid-cols-1" /><p className="mt-6 border-t border-line pt-5 text-[14px] text-ink-2">Hovenier, gemeente of projectontwikkelaar? <a href="groothandel.html" className="underline underline-offset-4">Naar de groothandelpagina</a> voor partijprijzen en een projectofferte.</p></div></Reveal>
          </div>
        </section>
      </main>
      <SiteFooter />
      <CartDrawer />
    </>
  )
}
