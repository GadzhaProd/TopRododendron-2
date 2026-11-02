import { motion, useReducedMotion } from 'framer-motion'
import { Button } from '@/components/ui/button'
import { Reveal } from '@/components/ui/reveal'
import { ProcessTimeline } from '@/components/ui/process-timeline'
import { OfferteForm } from '@/components/ui/offerte-form'
import { Faq } from '@/components/ui/faq'
import { WordsPullUp } from '@/components/ui/video-hero'
import { HeaderC, FooterC, HeadC, Pill } from './shared'
import { b2b, img, srcset, company } from '@/data/content'

export default function Groothandel() {
  const reduce = useReducedMotion()
  const fade = (d: number) => ({ initial: reduce ? false : { y: 18, opacity: 0 }, animate: { y: 0, opacity: 1 }, transition: { duration: 0.8, delay: d, ease: [0.16, 1, 0.3, 1] as any } })
  return (
    <>
      <a href="#main" className="skip-link">Naar de inhoud</a>
      <HeaderC b2b />
      <main id="main">
        <section className="container-x pt-24 md:pt-32">
          <div className="relative flex min-h-[72svh] flex-col justify-end overflow-hidden rounded-img bg-black text-white on-dark">
            <img src={img('B2BHERO')} srcSet={srcset('B2BHERO')} sizes="100vw" alt="" aria-hidden="true" className="absolute inset-0 h-full w-full object-cover object-[50%_60%] img-treat" />
            <div className="absolute inset-0 bg-gradient-to-t from-black/90 via-black/55 to-black/20" />
            <div className="relative w-full p-7 md:p-12">
              <motion.div {...fade(0.05)} className="flex flex-wrap gap-2"><Pill className="border-white/40 bg-white/15 text-white">Groothandel</Pill><Pill className="border-white/40 bg-white/15 text-white">Vanaf 25 stuks</Pill><Pill className="border-white/40 bg-white/15 text-white">NAK Tuinbouw</Pill></motion.div>
              <h1 className="mt-6 max-w-4xl font-display text-[clamp(31px,5.4vw,76px)] font-medium tracking-[-0.04em] text-balance leading-[1.0]"><WordsPullUp text="Voor hoveniers, gemeenten en projectontwikkelaars." delay={0.2} /></h1>
              <motion.p {...fade(0.7)} className="mt-5 max-w-2xl text-[16.5px] leading-relaxed text-white/90 md:text-lg">{b2b.intro}</motion.p>
              <motion.div {...fade(0.85)} className="mt-8 flex flex-wrap gap-3"><Button href="#offerte" variant="white" size="lg" arrow>Offerte aanvragen</Button><Button href={company.whatsapp} variant="outline-white" size="lg">WhatsApp</Button><Button href={company.phone1Href} variant="outline-white" size="lg">{company.phone1}</Button></motion.div>
              <motion.ul {...fade(1)} className="mt-8 grid grid-cols-2 gap-5 border-t border-white/25 pt-6 md:grid-cols-4">
                {b2b.facts.map(([k, v]) => <li key={k}><p className="font-display text-[19px]">{k}</p><p className="text-[13px] text-white/80">{v}</p></li>)}
              </motion.ul>
            </div>
          </div>
        </section>

        <section id="doelgroepen" className="container-x py-20 md:py-28">
          <Reveal><HeadC eyebrow="Projecten" title="Eén kweker, drie soorten projecten." text="Wij kweken uitsluitend rhododendrons en leveren rechtstreeks van het veld. Korte lijnen, verse planten, een vaste contactpersoon." size="lg" /></Reveal>
          <div className="mt-12 grid grid-cols-1 gap-4 lg:grid-cols-3 md:gap-5">
            {b2b.groups.map((g, i) => (
              <Reveal key={g.title} index={i} className="rounded-img bg-surface p-7 md:p-8">
                <p className="eyebrow text-muted">0{i + 1}</p>
                <h3 className="mt-3 font-display text-[24px] leading-tight">{g.title}</h3>
                <p className="mt-2 text-[14.5px] text-fg-2">{g.text}</p>
                <dl className="mt-7 border-t border-fg/10">{g.rows.map(([k, v]) => <div key={k} className="flex justify-between gap-4 border-b border-fg/10 py-3 text-[14px]"><dt className="text-muted">{k}</dt><dd className="text-right font-medium">{v}</dd></div>)}</dl>
              </Reveal>
            ))}
          </div>
        </section>

        <section id="werkwijze" className="bg-bg-2 py-20 md:py-28">
          <div className="container-x">
            <Reveal><HeadC eyebrow="Werkwijze" title="Van aanvraag tot aanplant in vier stappen." /></Reveal>
            <Reveal index={1} className="mt-12 rounded-img bg-surface p-7 md:p-10"><ProcessTimeline steps={b2b.steps} horizontal /></Reveal>
          </div>
        </section>

        <section id="maten" className="container-x py-20 md:py-28">
          <div className="grid grid-cols-1 gap-12 md:grid-cols-2 md:gap-12 lg:gap-16">
            <Reveal>
              <HeadC eyebrow="Voorraad" title="Van 40 tot 120 centimeter en meer." text="Wij reserveren de planten op stam en rooien op uw leverdatum. Dat voorkomt droogtestress en zorgt voor maximale aanslagkans." />
              <div className="mt-8 overflow-hidden rounded-img bg-surface">
                <table className="w-full text-[14.5px]">
                  <thead><tr className="bg-bg-2 text-left">{['Maat', 'Voorraad', 'Geschikt voor'].map((h) => <th key={h} className="eyebrow whitespace-nowrap px-4 py-3.5 font-medium text-muted md:px-5">{h}</th>)}</tr></thead>
                  <tbody>{b2b.sizes.map((r) => <tr key={r[0]} className="border-t border-fg/8">{r.map((c, j) => <td key={j} className={j === 0 ? 'whitespace-nowrap px-4 py-3.5 font-display text-[18px] md:px-5' : 'px-4 py-3.5 text-fg-2 md:px-5'}>{c}</td>)}</tr>)}</tbody>
                </table>
              </div>
            </Reveal>
            <div>
              <Reveal><p className="eyebrow text-muted">Partijprijzen</p></Reveal>
              <div className="mt-5 flex flex-col gap-4">{b2b.tiers.map((t, i) => <Reveal key={t.range} index={i} className="rounded-img bg-surface p-6 md:p-7"><p className="font-display text-[24px]">{t.range}</p><p className="mt-2 text-[14.5px] leading-relaxed text-fg-2">{t.text}</p></Reveal>)}</div>
              <Reveal index={3} className="mt-6 grid grid-cols-1 gap-4 sm:grid-cols-2">{b2b.services.map((s) => <div key={s.title} className="rounded-img border border-fg/10 p-5"><h3 className="text-[15px] font-semibold">{s.title}</h3><p className="mt-1.5 text-[14px] leading-relaxed text-fg-2">{s.text}</p></div>)}</Reveal>
            </div>
          </div>
        </section>

        <section id="offerte" className="container-x pb-20 md:pb-28">
          <Reveal className="grid grid-cols-1 gap-12 rounded-img bg-accent p-7 text-white on-dark md:gap-12 md:p-12 lg:grid-cols-12 lg:gap-16 lg:p-14">
            <div className="lg:col-span-5">
              <HeadC dark eyebrow="Offerte" title="Vertel ons wat u nodig heeft." text="Soorten, maten, aantallen en gewenste leverdatum. Binnen 24 uur een gespecificeerde offerte met partijprijzen, levering en planning." />
              <div className="mt-10 flex items-center gap-4 border-t border-white/15 pt-8"><img src={img('owner-sm')} alt={company.founder} loading="lazy" className="size-14 rounded-full object-cover object-[50%_20%]" /><div><p className="font-display text-[20px]">{company.founder}</p><p className="text-[13.5px] text-white/80">Uw vaste contactpersoon, van offerte tot oplevering.</p></div></div>
              <div className="mt-6 flex flex-col gap-2 text-[15px]"><a href={company.phone1Href} className="hover:opacity-70">{company.phone1}</a><a href={company.whatsapp} className="hover:opacity-70">WhatsApp</a><a href={`mailto:${company.email}`} className="hover:opacity-70">{company.email}</a></div>
            </div>
            <div className="lg:col-span-7"><OfferteForm dark /></div>
          </Reveal>
        </section>

        <section className="bg-bg-2 py-20 md:py-28">
          <div className="container-x grid grid-cols-1 gap-12 lg:grid-cols-12">
            <Reveal className="lg:col-span-5"><HeadC eyebrow="Veelgestelde vragen" title="Over garantie, levering en documenten." /></Reveal>
            <Reveal index={1} className="lg:col-span-7"><Faq items={b2b.faq} /></Reveal>
          </div>
        </section>
      </main>
      <FooterC />
    </>
  )
}
