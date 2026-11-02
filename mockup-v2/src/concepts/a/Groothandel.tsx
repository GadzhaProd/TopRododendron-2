import { motion, useReducedMotion } from 'framer-motion'
import { Button } from '@/components/ui/button'
import { Reveal } from '@/components/ui/reveal'
import { ProcessTimeline } from '@/components/ui/process-timeline'
import { OfferteForm } from '@/components/ui/offerte-form'
import { Faq } from '@/components/ui/faq'
import { WordsPullUp } from '@/components/ui/video-hero'
import { HeaderA, FooterA, SectionHead } from './shared'
import { b2b, img, company } from '@/data/content'

export default function Groothandel() {
  const reduce = useReducedMotion()
  const fade = (d: number) => ({ initial: reduce ? false : { y: 18, opacity: 0 }, animate: { y: 0, opacity: 1 }, transition: { duration: 0.8, delay: d, ease: [0.16, 1, 0.3, 1] as any } })
  return (
    <>
      <HeaderA b2b />
      <main>
        <section className="relative flex min-h-[86svh] items-end overflow-hidden bg-black text-white on-dark">
          <img src={img('B2BHERO')} alt="" aria-hidden="true" className="absolute inset-0 h-full w-full object-cover object-[50%_60%] img-treat" />
          <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/30 to-black/20" />
          <div className="container-x relative w-full pb-12 pt-40 md:pb-16">
            <div className="max-w-4xl">
              <motion.p {...fade(0.1)} className="eyebrow text-white/80">Groothandel · direct van de kweker</motion.p>
              <h1 className="mt-5 font-display text-[clamp(38px,6.4vw,92px)] leading-[0.98] text-balance [overflow-wrap:anywhere]"><WordsPullUp text="Voor hoveniers, gemeenten en projectontwikkelaars." delay={0.2} /></h1>
              <motion.p {...fade(0.7)} className="mt-6 max-w-2xl text-[17px] leading-relaxed text-white/85 md:text-lg">{b2b.intro}</motion.p>
              <motion.div {...fade(0.85)} className="mt-8 flex flex-wrap gap-3"><Button href="#offerte" variant="white" size="lg" arrow>Offerte aanvragen</Button><Button href={company.whatsapp} variant="outline-white" size="lg">WhatsApp</Button><Button href={company.phone1Href} variant="outline-white" size="lg">{company.phone1}</Button></motion.div>
            </div>
            <motion.ul {...fade(1)} className="mt-12 grid grid-cols-2 gap-6 border-t border-white/20 pt-6 md:grid-cols-4">
              {[['10.000 planten', 'op stam, 40 – 120+ cm'], ['Vanaf 25 stuks', 'scherpe partijprijzen'], ['Factuur 30 dagen', 'btw verlegd mogelijk'], ['NAK Tuinbouw', 'plantpaspoort bij elke partij']].map(([k, v]) => <li key={k}><p className="font-display text-[22px]">{k}</p><p className="text-[13px] text-white/65">{v}</p></li>)}
            </motion.ul>
          </div>
        </section>

        <section id="doelgroepen" className="container-x py-24 md:py-32">
          <Reveal><SectionHead eyebrow="Doelgroepen" title="Eén kweker, drie soorten projecten." text="Wij kweken uitsluitend rhododendrons en leveren rechtstreeks van het veld. Dat betekent korte lijnen, verse planten en een vaste contactpersoon." /></Reveal>
          <div className="mt-14 grid gap-px border border-line bg-line md:grid-cols-3">
            {b2b.groups.map((g, i) => (
              <Reveal key={g.title} index={i} className="bg-bg p-8 md:p-10">
                <p className="eyebrow text-muted">0{i + 1}</p>
                <h3 className="mt-4 font-display text-[28px] leading-tight">{g.title}</h3>
                <p className="mt-2 text-[15px] text-fg-2">{g.text}</p>
                <dl className="mt-8 border-t border-line">{g.rows.map(([k, v]) => <div key={k} className="flex justify-between gap-4 border-b border-line py-3 text-[14px]"><dt className="text-muted">{k}</dt><dd className="text-right">{v}</dd></div>)}</dl>
              </Reveal>
            ))}
          </div>
        </section>

        <section id="werkwijze" className="border-t border-line bg-bg-2/60 py-24 md:py-32">
          <div className="container-x">
            <Reveal><SectionHead eyebrow="Werkwijze" title="Van aanvraag tot aanplant in vier stappen." /></Reveal>
            <Reveal index={1} className="mt-14"><ProcessTimeline steps={b2b.steps} horizontal /></Reveal>
          </div>
        </section>

        <section id="maten" className="container-x py-24 md:py-32">
          <div className="grid gap-14 md:grid-cols-12 md:gap-20">
            <Reveal className="md:col-span-6">
              <SectionHead eyebrow="Maten & voorraad" title="Van 40 tot 120 centimeter en meer." text="Wij reserveren de planten op stam en rooien op uw leverdatum. Dat voorkomt droogtestress en zorgt voor maximale aanslagkans." />
              <table className="mt-10 w-full border-t border-fg text-[14.5px]">
                <thead><tr className="text-left">{['Maat', 'Voorraad', 'Geschikt voor'].map((h) => <th key={h} className="eyebrow py-3 font-medium text-muted">{h}</th>)}</tr></thead>
                <tbody>{b2b.sizes.map((r) => <tr key={r[0]} className="border-t border-line">{r.map((c, j) => <td key={j} className={j === 0 ? 'py-3.5 font-display text-[20px]' : 'py-3.5 text-fg-2'}>{c}</td>)}</tr>)}</tbody>
              </table>
            </Reveal>
            <div className="md:col-span-6">
              <Reveal><p className="eyebrow text-muted">Partijprijzen</p></Reveal>
              <div className="mt-6 flex flex-col gap-4">
                {b2b.tiers.map((t, i) => <Reveal key={t.range} index={i} className="border border-line bg-surface p-7"><p className="font-display text-[28px] leading-none">{t.range}</p><p className="mt-3 text-[15px] leading-relaxed text-fg-2">{t.text}</p></Reveal>)}
              </div>
              <Reveal index={3} className="mt-8 grid gap-6 sm:grid-cols-2">
                {b2b.services.map((s) => <div key={s.title} className="border-t border-line pt-4"><h3 className="text-[15px] font-medium">{s.title}</h3><p className="mt-1.5 text-[14px] leading-relaxed text-fg-2">{s.text}</p></div>)}
              </Reveal>
            </div>
          </div>
        </section>

        <section id="offerte" className="border-t border-line bg-accent py-24 text-white on-dark md:py-32">
          <div className="container-x grid gap-14 md:grid-cols-12 md:gap-20">
            <Reveal className="md:col-span-5">
              <SectionHead dark eyebrow="Offerte" title="Vertel ons wat u nodig heeft." text="Soorten, maten, aantallen en gewenste leverdatum. Binnen 24 uur ontvangt u een gespecificeerde offerte met partijprijzen, levering en planning." />
              <div className="mt-10 flex items-center gap-5 border-t border-white/15 pt-8">
                <img src={img('owner-sm')} alt={company.founder} className="size-16 rounded-full object-cover object-[50%_20%]" />
                <div><p className="font-display text-[22px] leading-none">{company.founder}</p><p className="mt-1 text-[13px] text-white/65">Uw vaste contactpersoon, van offerte tot oplevering.</p></div>
              </div>
              <div className="mt-8 flex flex-col gap-2 text-[15px]">
                <a href={company.phone1Href} className="hover:opacity-70">{company.phone1}</a>
                <a href={company.whatsapp} className="hover:opacity-70">WhatsApp</a>
                <a href={`mailto:${company.email}`} className="hover:opacity-70">{company.email}</a>
              </div>
            </Reveal>
            <Reveal index={1} className="md:col-span-7"><OfferteForm dark /></Reveal>
          </div>
        </section>

        <section className="container-x py-24 md:py-32">
          <div className="mx-auto grid max-w-6xl gap-12 md:grid-cols-12">
            <Reveal className="md:col-span-5"><SectionHead eyebrow="Veelgestelde vragen" title="Over garantie, levering en documenten." /></Reveal>
            <Reveal index={1} className="md:col-span-7"><Faq items={b2b.faq} /></Reveal>
          </div>
        </section>
      </main>
      <FooterA />
    </>
  )
}
