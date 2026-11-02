import { motion, useReducedMotion } from 'framer-motion'
import { Button } from '@/components/ui/button'
import { Reveal } from '@/components/ui/reveal'
import { ProcessTimeline } from '@/components/ui/process-timeline'
import { OfferteForm } from '@/components/ui/offerte-form'
import { Faq } from '@/components/ui/faq'
import { WordsPullUp } from '@/components/ui/video-hero'
import { HeaderB, FooterB, HeadB, Rule, SealB } from './shared'
import { b2b, img, company } from '@/data/content'

export default function Groothandel() {
  const reduce = useReducedMotion()
  const fade = (d: number) => ({ initial: reduce ? false : { y: 18, opacity: 0 }, animate: { y: 0, opacity: 1 }, transition: { duration: 0.8, delay: d, ease: [0.16, 1, 0.3, 1] as any } })
  return (
    <>
      <HeaderB b2b />
      <main className="on-dark">
        <section className="relative flex min-h-[92svh] items-center overflow-hidden bg-black text-center">
          <img src={img('B2BHERO')} alt="" aria-hidden="true" className="absolute inset-0 h-full w-full object-cover object-[50%_60%] img-treat" />
          <div className="absolute inset-0 bg-gradient-to-b from-black/50 via-black/40 to-bg" />
          <div className="container-x relative mx-auto max-w-4xl pb-16 pt-36">
            <motion.div {...fade(0)} className="flex justify-center"><SealB className="size-24 text-accent" id="b2b-seal" /></motion.div>
            <motion.p {...fade(0.15)} className="eyebrow mt-8 text-accent">Groothandel · direct van de kweker</motion.p>
            <h1 className="mt-5 font-display text-[clamp(25px,4.8vw,68px)] uppercase tracking-[0.02em] text-balance leading-[1.08] [overflow-wrap:anywhere]"><WordsPullUp text="Voor hoveniers, gemeenten en projectontwikkelaars." delay={0.25} className="justify-center" /></h1>
            <motion.p {...fade(0.7)} className="mx-auto mt-6 max-w-2xl text-[17px] leading-relaxed text-white/85 md:text-lg">{b2b.intro}</motion.p>
            <motion.div {...fade(0.85)} className="mt-9 flex flex-wrap justify-center gap-3"><Button href="#offerte" variant="solid" size="lg" arrow>Offerte aanvragen</Button><Button href={company.whatsapp} variant="outline-white" size="lg">WhatsApp</Button><Button href={company.phone1Href} variant="outline-white" size="lg">{company.phone1}</Button></motion.div>
          </div>
        </section>

        <section className="border-y border-white/10 bg-bg-2">
          <ul className="container-x mx-auto grid max-w-6xl grid-cols-2 divide-white/10 md:grid-cols-4 md:divide-x">
            {[['10.000 planten', 'op stam, 40 – 120+ cm'], ['Vanaf 25 stuks', 'scherpe partijprijzen'], ['Factuur 30 dagen', 'btw verlegd mogelijk'], ['NAK Tuinbouw', 'plantpaspoort bij elke partij']].map(([k, v]) => <li key={k} className="py-7 text-center md:py-9"><p className="font-display text-[20px] md:text-[22px]">{k}</p><p className="mt-1 text-[12.5px] tracking-[0.1em] uppercase text-muted">{v}</p></li>)}
          </ul>
        </section>

        <section id="doelgroepen" className="container-x py-24 md:py-32">
          <Reveal><HeadB eyebrow="Projecten" title="Eén kweker, drie soorten projecten." text="Wij kweken uitsluitend rhododendrons en leveren rechtstreeks van het veld. Korte lijnen, verse planten, een vaste contactpersoon." /></Reveal>
          <div className="mx-auto mt-14 grid max-w-6xl gap-6 md:grid-cols-3">
            {b2b.groups.map((g, i) => (
              <Reveal key={g.title} index={i} className="frame bg-surface p-8 md:p-10">
                <p className="eyebrow text-accent">0{i + 1}</p>
                <h3 className="mt-4 font-display text-[24px] leading-snug">{g.title}</h3>
                <p className="mt-2 text-[14.5px] text-fg-2">{g.text}</p>
                <dl className="mt-8 border-t border-white/10">{g.rows.map(([k, v]) => <div key={k} className="flex justify-between gap-4 border-b border-white/10 py-3 text-[14px]"><dt className="text-muted">{k}</dt><dd className="text-right">{v}</dd></div>)}</dl>
              </Reveal>
            ))}
          </div>
        </section>

        <section id="werkwijze" className="border-t border-white/10 bg-bg-2 py-24 md:py-32">
          <div className="container-x mx-auto max-w-6xl">
            <Reveal><HeadB eyebrow="Werkwijze" title="Van aanvraag tot aanplant in vier stappen." /></Reveal>
            <Reveal index={1} className="mt-16"><ProcessTimeline dark steps={b2b.steps} horizontal /></Reveal>
          </div>
        </section>

        <section id="maten" className="container-x py-24 md:py-32">
          <div className="mx-auto grid max-w-6xl gap-14 md:grid-cols-2 md:gap-20">
            <Reveal>
              <HeadB align="left" eyebrow="Voorraad" title="Van 40 tot 120 centimeter en meer." text="Wij reserveren de planten op stam en rooien op uw leverdatum. Dat voorkomt droogtestress en zorgt voor maximale aanslagkans." />
              <table className="mt-10 w-full border-t border-accent/60 text-[14.5px]">
                <thead><tr className="text-left">{['Maat', 'Voorraad', 'Geschikt voor'].map((h) => <th key={h} className="eyebrow py-3 font-medium text-muted">{h}</th>)}</tr></thead>
                <tbody>{b2b.sizes.map((r) => <tr key={r[0]} className="border-t border-white/10">{r.map((c, j) => <td key={j} className={j === 0 ? 'py-3.5 font-display text-[18px]' : 'py-3.5 text-fg-2'}>{c}</td>)}</tr>)}</tbody>
              </table>
            </Reveal>
            <div>
              <Reveal><p className="eyebrow text-accent">Partijprijzen</p></Reveal>
              <div className="mt-6 flex flex-col gap-4">{b2b.tiers.map((t, i) => <Reveal key={t.range} index={i} className="border border-white/10 bg-surface p-7"><p className="font-display text-[24px]">{t.range}</p><p className="mt-2 text-[14.5px] leading-relaxed text-fg-2">{t.text}</p></Reveal>)}</div>
              <Reveal index={3} className="mt-8 grid gap-6 sm:grid-cols-2">{b2b.services.map((s) => <div key={s.title} className="border-t border-white/10 pt-4"><h3 className="text-[15px] font-medium">{s.title}</h3><p className="mt-1.5 text-[14px] leading-relaxed text-fg-2">{s.text}</p></div>)}</Reveal>
            </div>
          </div>
        </section>

        <section id="offerte" className="border-t border-white/10 bg-bg-2 py-24 md:py-32">
          <div className="container-x mx-auto grid max-w-6xl gap-14 md:grid-cols-12 md:gap-20">
            <Reveal className="md:col-span-5">
              <HeadB align="left" eyebrow="Offerte" title="Vertel ons wat u nodig heeft." text="Soorten, maten, aantallen en gewenste leverdatum. Binnen 24 uur een gespecificeerde offerte met partijprijzen, levering en planning." />
              <Rule className="my-9" />
              <div className="flex items-center gap-5"><img src={img('owner-sm')} alt={company.founder} className="size-16 rounded-full object-cover object-[50%_20%]" /><div><p className="font-display text-[20px]">{company.founder}</p><p className="text-[13px] text-muted">Uw vaste contactpersoon, van offerte tot oplevering.</p></div></div>
              <div className="mt-8 flex flex-col gap-2 text-[15px]"><a href={company.phone1Href} className="hover:text-accent">{company.phone1}</a><a href={company.whatsapp} className="hover:text-accent">WhatsApp</a><a href={`mailto:${company.email}`} className="hover:text-accent">{company.email}</a></div>
            </Reveal>
            <Reveal index={1} className="md:col-span-7"><OfferteForm dark buttonVariant="solid" /></Reveal>
          </div>
        </section>

        <section className="container-x py-24 md:py-32">
          <div className="mx-auto max-w-4xl">
            <Reveal><HeadB eyebrow="Veelgestelde vragen" title="Over garantie, levering en documenten." /></Reveal>
            <Reveal index={1} className="mt-12"><Faq dark items={b2b.faq} /></Reveal>
          </div>
        </section>
      </main>
      <FooterB />
    </>
  )
}
