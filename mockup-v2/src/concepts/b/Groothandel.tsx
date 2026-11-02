import { motion, useReducedMotion } from 'framer-motion'
import { Button } from '@/components/ui/button'
import { Reveal } from '@/components/ui/reveal'
import { ProcessTimeline } from '@/components/ui/process-timeline'
import { OfferteForm } from '@/components/ui/offerte-form'
import { Faq } from '@/components/ui/faq'
import { WordsPullUp } from '@/components/ui/video-hero'
import { HeaderB, FooterB, HeadB, Rule, SealB } from './shared'
import { b2b, img, srcset, company } from '@/data/content'

export default function Groothandel() {
  const reduce = useReducedMotion()
  const fade = (d: number) => ({ initial: reduce ? false : { y: 18, opacity: 0 }, animate: { y: 0, opacity: 1 }, transition: { duration: 0.8, delay: d, ease: [0.16, 1, 0.3, 1] as any } })
  return (
    <>
      <a href="#main" className="skip-link">Naar de inhoud</a>
      <HeaderB b2b />
      <main id="main">
        <section className="relative flex min-h-[88svh] flex-col justify-end overflow-hidden bg-black text-center text-white on-dark">
          <img src={img('B2BHERO')} srcSet={srcset('B2BHERO')} sizes="100vw" alt="" aria-hidden="true" className="absolute inset-0 h-full w-full object-cover object-[50%_60%] img-treat" />
          <div className="absolute inset-0 bg-gradient-to-b from-black/45 via-black/55 to-night" />
          <div className="container-x relative mx-auto max-w-4xl pb-12 pt-32">
            <motion.div {...fade(0)} className="flex justify-center short:hidden"><SealB simple className="size-20 text-brass" id="b2b-seal" /></motion.div>
            <motion.p {...fade(0.15)} className="eyebrow mt-7 text-white/90">Groothandel · direct van de kweker</motion.p>
            <h1 className="mt-5 font-display text-[clamp(30px,4.6vw,64px)] text-balance leading-[1.1]"><WordsPullUp text="Voor hoveniers, gemeenten en projectontwikkelaars." delay={0.25} className="justify-center" /></h1>
            <motion.p {...fade(0.7)} className="mx-auto mt-6 max-w-2xl text-[17px] leading-relaxed text-white/90 md:text-lg">{b2b.intro}</motion.p>
            <motion.div {...fade(0.85)} className="mt-9 flex flex-wrap justify-center gap-3"><Button href="#offerte" variant="white" size="lg" arrow>Offerte aanvragen</Button><Button href={company.whatsapp} variant="outline-white" size="lg">WhatsApp</Button><Button href={company.phone1Href} variant="outline-white" size="lg">{company.phone1}</Button></motion.div>
          </div>
        </section>

        <section className="night border-y border-white/10 on-dark">
          <ul className="container-x mx-auto grid max-w-6xl grid-cols-2 divide-white/10 md:grid-cols-4 md:divide-x" aria-label="Kerngegevens">
            {b2b.facts.map(([k, v]) => <li key={k} className="py-6 text-center md:py-8"><p className="font-display text-[19px] md:text-[21px]">{k}</p><p className="mt-1 text-[13px] text-white/75">{v}</p></li>)}
          </ul>
        </section>

        <section id="doelgroepen" className="container-x py-20 md:py-32">
          <Reveal><HeadB eyebrow="Projecten" title="Eén kweker, drie soorten projecten." text="Wij kweken uitsluitend rhododendrons en leveren rechtstreeks van het veld. Korte lijnen, verse planten, een vaste contactpersoon." /></Reveal>
          <div className="mx-auto mt-16 grid grid-cols-1 max-w-6xl gap-8 lg:grid-cols-3">
            {b2b.groups.map((g, i) => (
              <Reveal key={g.title} index={i} className="frame bg-surface p-8 md:p-10">
                <p className="eyebrow text-accent-2">0{i + 1}</p>
                <h3 className="mt-4 font-display text-[24px] leading-snug">{g.title}</h3>
                <p className="mt-2 text-[14.5px] text-fg-2">{g.text}</p>
                <dl className="mt-8 border-t border-line">{g.rows.map(([k, v]) => <div key={k} className="flex justify-between gap-4 border-b border-line py-3 text-[14px]"><dt className="text-muted">{k}</dt><dd className="text-right">{v}</dd></div>)}</dl>
              </Reveal>
            ))}
          </div>
        </section>

        <section id="werkwijze" className="border-t border-line bg-bg-2 py-20 md:py-32">
          <div className="container-x mx-auto max-w-6xl">
            <Reveal><HeadB eyebrow="Werkwijze" title="Van aanvraag tot aanplant in vier stappen." /></Reveal>
            <Reveal index={1} className="mt-16"><ProcessTimeline steps={b2b.steps} horizontal /></Reveal>
          </div>
        </section>

        <section id="maten" className="container-x py-20 md:py-32">
          <div className="mx-auto grid grid-cols-1 max-w-6xl gap-14 md:grid-cols-2 md:gap-12 lg:gap-20">
            <Reveal>
              <HeadB align="left" eyebrow="Voorraad" title="Van 40 tot 120 centimeter en meer." text="Wij reserveren de planten op stam en rooien op uw leverdatum. Dat voorkomt droogtestress en zorgt voor maximale aanslagkans." />
              <div className="mt-10 overflow-x-auto"><table className="w-full min-w-[340px] border-t border-accent-2 text-[14.5px]">
                <thead><tr className="text-left">{['Maat', 'Voorraad', 'Geschikt voor'].map((h) => <th key={h} className="eyebrow py-3 pr-4 font-medium text-muted">{h}</th>)}</tr></thead>
                <tbody>{b2b.sizes.map((r) => <tr key={r[0]} className="border-t border-line">{r.map((c, j) => <td key={j} className={j === 0 ? 'whitespace-nowrap py-3.5 pr-4 font-display text-[18px]' : 'py-3.5 pr-4 text-fg-2'}>{c}</td>)}</tr>)}</tbody>
              </table></div>
            </Reveal>
            <div>
              <Reveal><p className="eyebrow text-accent-2">Partijprijzen</p></Reveal>
              <div className="mt-6 flex flex-col gap-4">{b2b.tiers.map((t, i) => <Reveal key={t.range} index={i} className="border border-line bg-surface p-7"><p className="font-display text-[24px]">{t.range}</p><p className="mt-2 text-[14.5px] leading-relaxed text-fg-2">{t.text}</p></Reveal>)}</div>
              <Reveal index={3} className="mt-8 grid grid-cols-1 gap-6 sm:grid-cols-2">{b2b.services.map((s) => <div key={s.title} className="border-t border-line pt-4"><h3 className="text-[15px] font-medium">{s.title}</h3><p className="mt-1.5 text-[14px] leading-relaxed text-fg-2">{s.text}</p></div>)}</Reveal>
            </div>
          </div>
        </section>

        <section id="offerte" className="night border-t border-white/10 py-20 on-dark md:py-32">
          <div className="container-x mx-auto grid grid-cols-1 max-w-6xl gap-14 md:gap-12 lg:grid-cols-12 lg:gap-20">
            <Reveal className="lg:col-span-5">
              <HeadB dark align="left" eyebrow="Offerte" title="Vertel ons wat u nodig heeft." text="Soorten, maten, aantallen en gewenste leverdatum. Binnen 24 uur een gespecificeerde offerte met partijprijzen, levering en planning." />
              <Rule dark className="my-9" />
              <div className="flex items-center gap-5"><img src={img('owner-sm')} alt={company.founder} loading="lazy" className="size-16 rounded-full object-cover object-[50%_20%]" /><div><p className="font-display text-[20px]">{company.founder}</p><p className="text-[13.5px] text-white/75">Uw vaste contactpersoon, van offerte tot oplevering.</p></div></div>
              <div className="mt-8 flex flex-col gap-2 text-[15px]"><a href={company.phone1Href} className="hover:text-brass">{company.phone1}</a><a href={company.whatsapp} className="hover:text-brass">WhatsApp</a><a href={`mailto:${company.email}`} className="hover:text-brass">{company.email}</a></div>
            </Reveal>
            <Reveal index={1} className="lg:col-span-7"><OfferteForm dark buttonVariant="white" /></Reveal>
          </div>
        </section>

        <section className="container-x py-20 md:py-32">
          <div className="mx-auto max-w-4xl">
            <Reveal><HeadB eyebrow="Veelgestelde vragen" title="Over garantie, levering en documenten." /></Reveal>
            <Reveal index={1} className="mt-12"><Faq items={b2b.faq} /></Reveal>
          </div>
        </section>
      </main>
      <FooterB />
    </>
  )
}
