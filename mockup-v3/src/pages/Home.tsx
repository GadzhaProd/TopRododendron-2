import { ArrowRight } from 'lucide-react'
import { SiteHeader } from '@/components/site-header'
import { SiteFooter } from '@/components/site-footer'
import { CartDrawer } from '@/components/cart-drawer'
import { Toast } from '@/components/toast'
import { VideoHero } from '@/components/video-hero'
import { Button, ext } from '@/components/button'
import { Reveal } from '@/components/reveal'
import { SectionHead } from '@/components/section-head'
import { VarietyCard } from '@/components/variety-card'
import { BloomCalendar, BloomLegend } from '@/components/bloom-calendar'
import { Faq } from '@/components/faq'
import { ContactForm } from '@/components/forms'
import { ContactBlock } from '@/components/contact-block'
import { WhatsAppIcon } from '@/components/whatsapp-float'
import { varieties, popularOrder, trust, story, promises, faq, company, tuinturf, img, srcset } from '@/data/content'

const ordered = popularOrder.map((s) => varieties.find((v) => v.slug === s)!)

export default function Home() {
  return (
    <>
      <a href="#main" className="skip-link">Naar de inhoud</a>
      <SiteHeader page="home" hero />
      <main id="main">
        <VideoHero
          eyebrow={<>Kwekerij in Otterlo · sinds 2001</>}
          title="Rhododendrons die aanslaan."
          text="Zeven winterharde soorten van eigen veld. Vers gerooid, geleverd met eigen transport en met aangroeigarantie."
          actions={<><Button href="assortiment.html" variant="white" size="lg" arrow>Bekijk het assortiment</Button><Button href="groothandel.html" variant="outline-white" size="lg" className="short:hidden">Groothandel</Button></>}
          bottomBar={
            <dl className="grid grid-cols-4 gap-6">
              {trust.map((t) => <div key={t.k}><dt className="label text-white/65">{t.k}</dt><dd className="mt-1 text-[21px] font-semibold tracking-[-0.01em] text-white">{t.v}</dd></div>)}
            </dl>
          }
        />
        {/* facts strip on phones */}
        <section aria-label="Kerngegevens" className="bg-night text-white on-dark md:hidden">
          <dl className="container-x grid grid-cols-2 gap-x-6 gap-y-4 py-6">
            {trust.map((t) => <div key={t.k}><dt className="label text-white/60">{t.k}</dt><dd className="mt-0.5 text-[17px] font-semibold leading-tight">{t.v}</dd></div>)}
          </dl>
        </section>

        {/* Assortiment */}
        <section id="assortiment" className="wrap container-x py-16 md:py-24">
          <Reveal className="flex flex-col gap-6 md:flex-row md:items-end md:justify-between">
            <SectionHead size="lg" title="Zeven soorten van ons veld." text="Prijs per plant in 40–60 cm; leverbaar in vier maten tot 120 cm. Bezorgd door heel Nederland of af te halen in Otterlo." />
            <Button href="assortiment.html" variant="outline" size="md" arrow className="shrink-0">Alle maten en prijzen</Button>
          </Reveal>
          <div className="mt-10 grid grid-cols-2 gap-x-4 gap-y-8 sm:gap-x-6 sm:gap-y-10 lg:grid-cols-3">
            {ordered.map((v, i) => <Reveal key={v.slug} index={i % 3}><VarietyCard v={v} eager={i < 2} /></Reveal>)}
            <Reveal index={1} className="col-span-2 lg:col-span-2">
              <a href={`product.html#${tuinturf.slug}`} className="group/t flex h-full flex-col gap-5 rounded-img bg-moss p-5 text-white on-dark transition-colors hover:bg-moss-2 sm:flex-row sm:items-center sm:p-6">
                <img src={img('tuinturf-sm')} alt="" className="aspect-[4/3] w-full rounded-[10px] object-cover sm:aspect-square sm:w-36" loading="lazy" />
                <div className="flex-1">
                  <p className="label text-white/65">Bij het planten</p>
                  <h3 className="mt-1.5 text-[22px] font-semibold leading-tight sm:text-[24px]">{tuinturf.fullName}</h3>
                  <p className="mt-2 max-w-[52ch] text-[14.5px] leading-relaxed text-white/80">{tuinturf.upsell}</p>
                  <p className="num mt-4 flex items-center gap-3 text-[15px] font-semibold">€ {tuinturf.price} <span className="font-medium text-white/65">per zak 40 L</span><span className="ml-auto grid size-9 place-items-center rounded-full bg-white/12 transition-colors group-hover/t:bg-white group-hover/t:text-moss"><ArrowRight className="size-4" /></span></p>
                </div>
              </a>
            </Reveal>
          </div>
        </section>

        {/* Bloeikalender (night) */}
        <section id="bloeikalender" className="bg-night py-16 text-white on-dark md:py-24">
          <div className="wrap container-x">
            <Reveal className="flex flex-col gap-6 lg:flex-row lg:items-end lg:justify-between">
              <SectionHead dark size="lg" label="Bloei- & plantkalender" title="Wanneer bloeit úw favoriete soort?" text="Plan uw aankoop rondom het bloeimoment. Rhododendrons kunnen het hele jaar door geplant worden, behalve bij strenge vorst of droogte." />
              <Button href="plantgids.html" variant="white" size="lg" arrow className="shrink-0">Bekijk de plantgids</Button>
            </Reveal>
            <Reveal index={1} className="mt-10 rounded-panel bg-white/[0.04] p-4 ring-1 ring-white/10 sm:p-6 md:p-8">
              <BloomCalendar rows={ordered} />
              <BloomLegend className="mt-6" />
            </Reveal>
          </div>
        </section>

        {/* De kwekerij: big field photo + story + promises */}
        <section id="kwekerij" className="scroll-mt-16">
          <div className="relative h-[62svh] min-h-[380px] w-full overflow-hidden bg-moss-3">
            <img src={img('B2BHERO')} srcSet={srcset('B2BHERO')} sizes="100vw" alt="Het veld van de kwekerij: rijen witte rhododendrons in bloei" loading="lazy" className="h-full w-full object-cover object-[50%_60%] img-treat" />
            <div className="absolute inset-x-0 bottom-0 h-1/2 bg-gradient-to-t from-night/70 to-transparent" />
            <p className="label absolute bottom-5 left-5 text-white/90 text-shadow md:bottom-8 md:left-[clamp(20px,4vw,64px)]">Het veld van de kwekerij, Otterlo</p>
          </div>
          <div className="wrap container-x grid grid-cols-1 gap-12 py-16 md:py-24 lg:grid-cols-12 lg:gap-16">
            <div className="lg:col-span-5">
              <Reveal><SectionHead size="lg" title={story.h} text={story.p1} /></Reveal>
              <Reveal index={1}><p className="mt-5 max-w-[56ch] text-[16px] leading-relaxed text-ink-2 md:text-[17px]">{story.p2}</p></Reveal>
            </div>
            <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:col-span-7">
              {promises.map((p, i) => (
                <Reveal key={p.title} index={i} className="rounded-img bg-surface p-5 md:p-6">
                  <h3 className="text-[19px] font-semibold leading-tight tracking-[-0.01em] md:text-[21px]">{p.title}</h3>
                  <p className="mt-2 text-[14.5px] leading-relaxed text-ink-2">{p.text}</p>
                </Reveal>
              ))}
            </div>
          </div>
        </section>

        {/* De kweker (moss) */}
        <section className="bg-moss text-white on-dark">
          <div className="wrap container-x grid grid-cols-1 items-center gap-10 py-16 md:grid-cols-12 md:gap-12 md:py-24">
            <Reveal className="md:col-span-5 lg:col-span-4">
              <div className="aspect-[4/5] overflow-hidden rounded-panel bg-moss-3"><img src={img('owner-portrait')} alt={`${company.founder}, oprichter van ${company.name}`} loading="lazy" className="h-full w-full object-cover object-[50%_20%] img-treat" /></div>
            </Reveal>
            <div className="md:col-span-7 lg:col-span-8">
              <Reveal>
                <blockquote>
                  <p className="title text-balance text-[clamp(30px,4vw,56px)] leading-[1.05]">„{story.quote}”</p>
                  <footer className="mt-5 text-[15px] text-white/75"><span className="font-semibold text-white">{company.founder}</span> · Eigenaar {company.name}</footer>
                </blockquote>
              </Reveal>
              <Reveal index={1}><p className="mt-6 max-w-[60ch] text-[16px] leading-relaxed text-white/80">{story.p3}</p></Reveal>
              <Reveal index={2} className="mt-7 flex flex-wrap gap-3"><Button href={company.phone1Href} variant="white" size="md">Bel de kweker</Button><Button href={company.whatsapp} {...ext} variant="outline-white" size="md"><WhatsAppIcon className="size-4" />WhatsApp</Button></Reveal>
            </div>
          </div>
        </section>

        {/* Twee deuren */}
        <section className="wrap container-x py-16 md:py-24">
          <div className="grid grid-cols-1 gap-4 md:grid-cols-2 md:gap-5">
            {[
              { label: 'Voor uw tuin', title: 'Vanaf één plant, bezorgd of af te halen in Otterlo.', text: 'Geen minimumbestelling. Persoonlijk advies over soort, maat en standplaats.', cta: 'Bekijk het assortiment', href: 'assortiment.html', photo: 'roseum-elegans-2', pos: '50% 40%' },
              { label: 'Voor professionals', title: 'Hoveniers, gemeenten en projectontwikkelaars.', text: 'Partijprijzen vanaf 25 stuks, plantpaspoort, factuur op 30 dagen.', cta: 'Naar groothandel', href: 'groothandel.html', photo: 'B2BHERO', pos: '50% 20%' },
            ].map((p, i) => (
              <Reveal key={p.href} index={i}>
                <a href={p.href} className="group/d relative flex min-h-[460px] flex-col justify-end overflow-hidden rounded-panel bg-night text-white on-dark md:min-h-[540px]">
                  <img src={img(p.photo)} srcSet={srcset(p.photo)} sizes="(min-width: 768px) 50vw, 100vw" alt="" loading="lazy" className="absolute inset-0 h-full w-full object-cover img-treat transition-transform duration-[1200ms] ease-[cubic-bezier(.22,1,.36,1)] group-hover/d:scale-[1.03]" style={{ objectPosition: p.pos }} />
                  <div className="absolute inset-0 bg-gradient-to-t from-night from-12% via-night/80 via-50% to-night/5" />
                  <div className="relative p-6 md:p-9">
                    <p className="label text-white">{p.label}</p>
                    <h3 className="title mt-3 max-w-[20ch] text-[clamp(26px,3vw,38px)]">{p.title}</h3>
                    <p className="mt-3 max-w-[44ch] text-[15px] leading-relaxed text-white">{p.text}</p>
                    <span className="mt-6 inline-flex h-12 items-center gap-2 rounded-ui bg-white px-5 text-[15px] font-semibold text-ink">{p.cta}<ArrowRight className="size-4 transition-transform group-hover/d:translate-x-1" /></span>
                  </div>
                </a>
              </Reveal>
            ))}
          </div>
        </section>

        {/* Vraag & advies */}
        <section id="advies" className="bg-bg-2 py-16 md:py-24">
          <div className="wrap container-x grid grid-cols-1 gap-10 lg:grid-cols-12 lg:gap-14">
            <Reveal className="lg:col-span-5"><SectionHead title="Alles wat u wilt weten." text="Staat uw vraag er niet tussen? Neem gerust contact met ons op, wij helpen u persoonlijk verder." /><div className="mt-7 flex flex-wrap gap-3"><Button href="plantgids.html" variant="solid" arrow>Naar de plantgids</Button><Button href={company.phone1Href} variant="outline">Bel {company.phone1}</Button></div></Reveal>
            <Reveal index={1} className="lg:col-span-7"><Faq items={faq} /></Reveal>
          </div>
        </section>

        {/* Contact */}
        <section id="contact" className="wrap container-x scroll-mt-16 py-16 md:py-24">
          <Reveal><SectionHead size="lg" title="Kom langs op de kwekerij, of stuur een bericht." text="Vul het formulier in voor advies of ontvang direct een vrijblijvende prijsopgave." /></Reveal>
          <div className="mt-10 grid grid-cols-1 gap-10 lg:grid-cols-12 lg:gap-14">
            <Reveal index={1} className="rounded-panel bg-surface p-5 md:p-8 lg:col-span-7"><ContactForm /></Reveal>
            <Reveal index={2} className="lg:col-span-5"><ContactBlock /><p className="mt-8 rounded-img bg-surface p-5 text-[14.5px] text-ink-2">Bent u professional of grootverbruiker? Voor hoveniers, gemeenten en projectontwikkelaars hebben wij een aparte aanvraagpagina met partijprijzen, leveringsplanning en zakelijke voorwaarden. <a href="groothandel.html" className="font-semibold text-ink underline underline-offset-4">Naar de groothandelpagina</a></p></Reveal>
          </div>
        </section>
      </main>
      <SiteFooter home />
      <CartDrawer />
      <Toast />
    </>
  )
}
