import { SiteHeader } from '@/components/site-header'
import { SiteFooter } from '@/components/site-footer'
import { CartDrawer } from '@/components/cart-drawer'
import { Button } from '@/components/button'
import { Reveal } from '@/components/reveal'
import { SectionHead } from '@/components/section-head'
import { CompareTable } from '@/components/compare-table'
import { BloomCalendar, BloomLegend } from '@/components/bloom-calendar'
import { Faq } from '@/components/faq'
import { varieties, popularOrder, care, tips, faq, tuinturf, company, img, srcset } from '@/data/content'

const ordered = popularOrder.map((s) => varieties.find((v) => v.slug === s)!)
const nav = [['#vergelijken', 'Vergelijken'], ['#kalender', 'Bloeikalender'], ['#planten', 'Planten en verzorgen'], ['#lessen', 'Zeven lessen'], ['#vragen', 'Vragen']]

export default function Plantgids() {
  return (
    <>
      <a href="#main" className="skip-link">Naar de inhoud</a>
      <SiteHeader current="plantgids" />
      <main id="main" className="pt-16 md:pt-[76px]">
        <section className="border-b border-line bg-paper-2">
          <div className="wrap container-x py-14 md:py-20">
            <SectionHead as="h1" size="xl" eyebrow="Plantgids" title="Adviezen uit eigen kwekerij." text="Vergelijk de variëteiten op kenmerken die ertoe doen, zie wanneer wat bloeit, en lees de zeven lessen die wij elke klant willen meegeven. Omdat een gezonde plant geen toeval is." />
            <nav aria-label="Op deze pagina" className="mt-10 flex flex-wrap gap-x-6 gap-y-2 border-t border-line-2 pt-5 text-[14px]">
              {nav.map(([h, l]) => <a key={h} href={h} className="text-ink-2 underline-offset-4 hover:text-ink hover:underline">{l}</a>)}
            </nav>
          </div>
        </section>

        {/* Vergelijken */}
        <section id="vergelijken" className="wrap container-x scroll-mt-24 py-16 md:py-24">
          <Reveal><SectionHead eyebrow="Vergelijken" title="Alle variëteiten naast elkaar." text="Klik op een kolomkop om te sorteren. Klik op een naam voor foto's, maten en prijzen." /></Reveal>
          <Reveal index={1} className="mt-10"><CompareTable /></Reveal>
          <p className="mt-4 text-[12.5px] text-muted">* Gegevens zijn indicatief. Exacte maten kunnen variëren per standplaats en klimaat.</p>
        </section>

        {/* Kalender */}
        <section id="kalender" className="scroll-mt-24 bg-paper-2 py-16 md:py-24">
          <div className="wrap container-x">
            <Reveal><SectionHead eyebrow="Bloei- & plantkalender" title="Wanneer bloeit wat, en wanneer plant u." text="Cunningham's White opent het seizoen in april; de overige soorten bloeien in mei en juni. Planten kan het hele jaar door, behalve bij strenge vorst of droogte; maart–april en september–oktober zijn ideaal." /></Reveal>
            <Reveal index={1} className="mt-10 rounded-img border border-line bg-paper p-4 sm:p-6 md:p-8"><BloomCalendar rows={ordered} /><BloomLegend className="mt-6" /></Reveal>
          </div>
        </section>

        {/* Planten en verzorgen */}
        <section id="planten" className="wrap container-x scroll-mt-24 py-16 md:py-24">
          <Reveal><SectionHead eyebrow="Planten en verzorgen" title="Drie dingen die het verschil maken." /></Reveal>
          <div className="mt-10 grid grid-cols-1 gap-10 lg:grid-cols-12">
            <div className="grid grid-cols-1 gap-8 sm:grid-cols-3 lg:col-span-8">
              {care.map((c, i) => (
                <Reveal key={c.title} index={i} className="border-t border-line-2 pt-5">
                  <p className="num font-display text-[18px] text-bloom">0{i + 1}</p>
                  <h3 className="mt-2 font-display text-[24px] leading-tight">{c.title}</h3>
                  <p className="mt-3 text-[15px] leading-relaxed text-ink-2">{c.text}</p>
                </Reveal>
              ))}
            </div>
            <Reveal index={3} className="lg:col-span-4">
              <a href={`product.html#${tuinturf.slug}`} className="group/t flex h-full flex-col overflow-hidden rounded-img border border-line bg-surface transition-colors hover:border-ink/40">
                <div className="aspect-[16/9] overflow-hidden"><img src={img('tuinturf-sm')} srcSet={srcset('tuinturf')} sizes="(min-width: 1024px) 33vw, 100vw" alt="Tuinturf-substraat" loading="lazy" className="h-full w-full object-cover img-treat transition-transform duration-[900ms] group-hover/t:scale-[1.03]" /></div>
                <div className="flex flex-1 flex-col p-6">
                  <p className="eyebrow text-muted">Voor de beste start</p>
                  <h3 className="mt-2 font-display text-[22px] leading-tight">{tuinturf.name}</h3>
                  <p className="mt-2 text-[14.5px] leading-relaxed text-ink-2">{tuinturf.short}</p>
                  <p className="num mt-auto pt-4 text-[14.5px]"><span className="font-semibold">€ {tuinturf.price}</span> <span className="text-muted">per zak 40 L</span> <span className="ml-2 underline underline-offset-4">Bekijk</span></p>
                </div>
              </a>
            </Reveal>
          </div>
        </section>

        {/* Zeven lessen */}
        <section id="lessen" className="scroll-mt-24 border-y border-line bg-surface py-16 md:py-24">
          <div className="wrap container-x grid grid-cols-1 gap-12 lg:grid-cols-12">
            <Reveal className="lg:col-span-4"><SectionHead eyebrow="De geheimen van de kweker" title="Zeven lessen die wij elke klant meegeven." text="Veel rhododendrons sterven niet aan de winter, maar aan goedbedoelde verzorging. Dit zijn de fouten die wij het vaakst zien." /><div className="mt-8"><Button href={company.phone1Href} variant="outline" size="md">Liever persoonlijk advies? Bel ons</Button></div></Reveal>
            <ol className="lg:col-span-8">
              {tips.map((t, i) => (
                <Reveal as="li" key={t.title} index={i % 3} className="grid grid-cols-[56px_1fr] gap-5 border-b border-line py-6 first:border-t md:grid-cols-[72px_1fr]">
                  <span className="num font-display text-[36px] leading-none text-bloom md:text-[44px]" style={{ fontVariationSettings: '"opsz" 72' }}>{i + 1}.</span>
                  <div><h3 className="font-display text-[23px] leading-tight md:text-[26px]">{t.title}</h3><p className="mt-2 max-w-[62ch] text-[15px] leading-relaxed text-ink-2">{t.body}</p></div>
                </Reveal>
              ))}
            </ol>
          </div>
        </section>

        {/* Vragen */}
        <section id="vragen" className="wrap container-x scroll-mt-24 grid grid-cols-1 gap-12 py-16 md:py-24 lg:grid-cols-12">
          <Reveal className="lg:col-span-5"><SectionHead eyebrow="Veelgestelde vragen" title="Over levering, grond en garantie." text="Staat uw vraag er niet tussen? Neem gerust contact met ons op, wij helpen u persoonlijk verder." /><div className="mt-8 flex flex-wrap gap-3"><Button href={company.phone1Href} variant="ink">Bel {company.phone1}</Button><Button href={company.whatsapp} variant="outline">WhatsApp</Button></div></Reveal>
          <Reveal index={1} className="lg:col-span-7"><Faq items={faq} /></Reveal>
        </section>

        <section className="bg-moss py-16 text-white on-dark md:py-20">
          <div className="wrap container-x flex flex-col gap-6 md:flex-row md:items-end md:justify-between">
            <SectionHead dark eyebrow="Klaar om te kiezen?" title="Zeven soorten, vier maten, vers van het veld." text="Bezorgd door heel Nederland of af te halen in Otterlo. Met aangroeigarantie." />
            <Button href="assortiment.html" variant="paper" size="lg" arrow className="shrink-0">Naar het assortiment</Button>
          </div>
        </section>
      </main>
      <SiteFooter />
      <CartDrawer />
    </>
  )
}
