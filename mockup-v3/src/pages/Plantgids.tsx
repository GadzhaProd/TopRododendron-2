import { SiteHeader } from '@/components/site-header'
import { SiteFooter } from '@/components/site-footer'
import { CartDrawer } from '@/components/cart-drawer'
import { Toast } from '@/components/toast'
import { Button, ext } from '@/components/button'
import { Reveal } from '@/components/reveal'
import { SectionHead } from '@/components/section-head'
import { CompareTable } from '@/components/compare-table'
import { BloomCalendar, BloomLegend } from '@/components/bloom-calendar'
import { Faq } from '@/components/faq'
import { WhatsAppIcon } from '@/components/whatsapp-float'
import { varieties, popularOrder, care, tips, faq, tuinturf, company, img, srcset } from '@/data/content'

const ordered = popularOrder.map((s) => varieties.find((v) => v.slug === s)!)
const nav = [['#vergelijken', 'Vergelijken'], ['#kalender', 'Bloeikalender'], ['#planten', 'Planten en verzorgen'], ['#lessen', 'Zeven lessen'], ['#vragen', 'Vragen']]

export default function Plantgids() {
  return (
    <>
      <a href="#main" className="skip-link">Naar de inhoud</a>
      <SiteHeader page="plantgids" />
      <main id="main" className="pt-16 md:pt-20">
        {/* head on the field photo */}
        <section className="relative overflow-hidden bg-night text-white on-dark">
          <img src={img('B2BHERO')} srcSet={srcset('B2BHERO')} sizes="100vw" alt="" className="absolute inset-0 h-full w-full object-cover object-[50%_45%] img-treat opacity-70" />
          <div className="absolute inset-0 bg-gradient-to-t from-night via-night/80 to-night/40" />
          <div className="relative wrap container-x py-14 md:py-24">
            <SectionHead dark as="h1" size="xl" label="Plantgids" title="Adviezen uit eigen kwekerij." text="Vergelijk variëteiten op kenmerken die ertoe doen. En zeven lessen die wij elke klant willen meegeven." />
            <nav aria-label="Op deze pagina" className="mt-8 flex flex-wrap gap-2">
              {nav.map(([h, l]) => <a key={h} href={h} className="rounded-full bg-white/12 px-3.5 py-2 text-[13.5px] font-semibold text-white hover:bg-white/22">{l}</a>)}
            </nav>
          </div>
        </section>

        {/* Vergelijken */}
        <section id="vergelijken" className="wrap container-x scroll-mt-20 py-14 md:py-20">
          <Reveal><SectionHead title="Vergelijk alle variëteiten op kenmerken die ertoe doen." text="Klik op een kolomkop om te sorteren. Klik op een naam voor foto's, maten en prijzen." /></Reveal>
          <Reveal index={1} className="mt-8"><CompareTable /></Reveal>
          <p className="mt-4 text-[12.5px] text-muted">* Gegevens zijn indicatief. Exacte maten kunnen variëren per standplaats en klimaat.</p>
        </section>

        {/* Kalender (night) */}
        <section id="kalender" className="scroll-mt-20 bg-night py-14 text-white on-dark md:py-20">
          <div className="wrap container-x">
            <Reveal><SectionHead dark title="Wanneer bloeit wat, en wanneer plant u." text="Cunningham's White opent het seizoen in april; de overige soorten bloeien in mei en juni. Planten kan het hele jaar door, behalve bij strenge vorst of droogte; maart–april en september–oktober zijn ideaal." /></Reveal>
            <Reveal index={1} className="mt-8 rounded-panel bg-white/[0.04] p-4 ring-1 ring-white/10 sm:p-6 md:p-8"><BloomCalendar rows={ordered} photos dark /><BloomLegend className="mt-6" dark /></Reveal>
          </div>
        </section>

        {/* Planten en verzorgen */}
        <section id="planten" className="wrap container-x scroll-mt-20 py-14 md:py-20">
          <Reveal><SectionHead title="Drie dingen die het verschil maken." /></Reveal>
          <div className="mt-8 grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-4">
            {care.map((c) => (
              <Reveal key={c.title} className="rounded-img bg-surface p-5 md:p-6">
                <h3 className="text-[21px] font-semibold leading-tight tracking-[-0.01em]">{c.title}</h3>
                <p className="mt-2.5 text-[15px] leading-relaxed text-ink-2">{c.text}</p>
              </Reveal>
            ))}
            <Reveal index={3}>
              <a href={`product.html#${tuinturf.slug}`} className="group/t flex h-full flex-col overflow-hidden rounded-img bg-moss text-white on-dark transition-colors hover:bg-moss-2">
                <div className="aspect-[16/9] overflow-hidden"><img src={img('tuinturf-sm')} srcSet={srcset('tuinturf')} sizes="(min-width: 1024px) 25vw, 100vw" alt="Tuinturf-substraat" loading="lazy" className="h-full w-full object-cover img-treat transition-transform duration-[900ms] group-hover/t:scale-[1.03]" /></div>
                <div className="flex flex-1 flex-col p-5">
                  <p className="label text-white/65">Voor de beste start</p>
                  <h3 className="mt-1.5 text-[20px] font-semibold leading-tight">{tuinturf.name}</h3>
                  <p className="mt-2 text-[14px] leading-relaxed text-white/80">{tuinturf.short}</p>
                  <p className="num mt-auto pt-4 text-[14.5px]"><span className="font-semibold">€ {tuinturf.price}</span> <span className="text-white/65">per zak 40 L</span> <span className="ml-2 font-semibold underline underline-offset-4">Bekijk</span></p>
                </div>
              </a>
            </Reveal>
          </div>
        </section>

        {/* Zeven lessen */}
        <section id="lessen" className="scroll-mt-20 bg-bg-2 py-14 md:py-20">
          <div className="wrap container-x">
            <Reveal className="flex flex-col gap-6 md:flex-row md:items-end md:justify-between"><SectionHead label="De geheimen van de kweker" title="Wat wij elke klant willen meegeven." text="Omdat een gezonde plant geen toeval is." /><Button href={company.phone1Href} variant="outline" size="md" className="shrink-0">Liever persoonlijk advies? Bel ons</Button></Reveal>
            <ol className="mt-8 grid grid-cols-1 gap-4 md:grid-cols-2">
              {tips.map((t, i) => (
                <Reveal as="li" key={t.title} index={i % 2} className="flex gap-4 rounded-img bg-surface p-5 md:p-6">
                  <span className="num grid size-10 shrink-0 place-items-center rounded-full bg-night text-[15px] font-semibold text-white">{i + 1}</span>
                  <div><h3 className="text-[19px] font-semibold leading-tight tracking-[-0.01em] md:text-[21px]">{t.title}</h3><p className="mt-2 text-[15px] leading-relaxed text-ink-2">{t.body}</p></div>
                </Reveal>
              ))}
            </ol>
          </div>
        </section>

        {/* Vragen */}
        <section id="vragen" className="wrap container-x scroll-mt-20 grid grid-cols-1 gap-10 py-14 md:py-20 lg:grid-cols-12 lg:gap-14">
          <Reveal className="lg:col-span-5"><SectionHead title="Over levering, grond en garantie." text="Staat uw vraag er niet tussen? Neem gerust contact met ons op, wij helpen u persoonlijk verder." /><div className="mt-7 flex flex-wrap gap-3"><Button href={company.phone1Href} variant="solid">Bel {company.phone1}</Button><Button href={company.whatsapp} {...ext} variant="outline"><WhatsAppIcon className="size-4" />WhatsApp</Button></div></Reveal>
          <Reveal index={1} className="lg:col-span-7"><Faq items={faq} /></Reveal>
        </section>

        <section className="bg-moss py-14 text-white on-dark md:py-20">
          <div className="wrap container-x flex flex-col gap-6 md:flex-row md:items-end md:justify-between">
            <SectionHead dark title="Zeven soorten, vier maten, vers van het veld." text="Bezorgd door heel Nederland of af te halen in Otterlo. Met aangroeigarantie." />
            <Button href="assortiment.html" variant="white" size="lg" arrow className="shrink-0">Naar het assortiment</Button>
          </div>
        </section>
      </main>
      <SiteFooter />
      <CartDrawer />
      <Toast />
    </>
  )
}
