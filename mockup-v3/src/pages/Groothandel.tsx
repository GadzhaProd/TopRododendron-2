import { Phone } from 'lucide-react'
import { SiteHeader } from '@/components/site-header'
import { SiteFooter } from '@/components/site-footer'
import { Button } from '@/components/button'
import { Reveal } from '@/components/reveal'
import { SectionHead } from '@/components/section-head'
import { Faq } from '@/components/faq'
import { OfferteForm, PrijslijstModal } from '@/components/forms'
import { WhatsAppFloat } from '@/components/whatsapp-float'
import { openModal } from '@/lib/store'
import { b2b, company, img, srcset } from '@/data/content'

export default function Groothandel() {
  return (
    <>
      <a href="#main" className="skip-link">Naar de inhoud</a>
      <SiteHeader variant="b2b" />
      <main id="main">
        {/* Hero: the field, full bleed */}
        <section className="relative flex min-h-[92svh] flex-col justify-end overflow-hidden bg-night text-white on-dark">
          <img src={img('B2BHERO')} srcSet={srcset('B2BHERO')} sizes="100vw" alt="" className="absolute inset-0 h-full w-full object-cover object-[55%_60%] img-treat" />
          <div className="absolute inset-0 bg-gradient-to-r from-[#0b120e]/80 via-[#0b120e]/45 to-[#0b120e]/15" />
          <div className="absolute inset-x-0 bottom-0 h-[75%] bg-gradient-to-t from-[#0b120e]/92 via-[#0b120e]/50 to-transparent" />
          <div className="relative wrap container-x w-full pb-10 pt-32 md:pb-12">
            <div className="flex max-w-[48rem] flex-col items-start gap-5">
              <p className="eyebrow text-white/85">Groothandel · direct van de kweker</p>
              <h1 className="font-display-tight text-balance text-[clamp(38px,6vw,84px)] leading-[0.98]">{b2b.title}</h1>
              <p className="max-w-[40rem] text-[16px] leading-relaxed text-white/88 md:text-[18px]">{b2b.sub} {b2b.intro}</p>
              <div className="mt-1 flex flex-wrap gap-3">
                <Button href="#offerte" variant="paper" size="lg" arrow>Vraag offerte aan</Button>
                <Button as="button" variant="outline-white" size="lg" onClick={() => openModal('prijslijst')}>Prijslijst ontvangen</Button>
                <Button href={company.phone1Href} variant="outline-white" size="lg" className="hidden sm:inline-flex"><Phone className="size-4" aria-hidden="true" /><span className="num">{company.phone1}</span></Button>
              </div>
            </div>
            <dl className="mt-10 hidden grid-cols-4 gap-6 border-t border-white/22 pt-5 md:grid">
              {b2b.facts.map(([k, v]) => <div key={k}><dt className="font-display text-[24px] leading-tight text-white">{k}</dt><dd className="mt-1 text-[13.5px] text-white/75">{v}</dd></div>)}
            </dl>
          </div>
        </section>
        <section aria-label="Kerngegevens" className="border-b border-line bg-paper-2 md:hidden">
          <dl className="container-x grid grid-cols-2 gap-x-6 gap-y-4 py-6">
            {b2b.facts.map(([k, v]) => <div key={k}><dt className="font-display text-[20px] leading-tight">{k}</dt><dd className="mt-0.5 text-[13px] text-muted">{v}</dd></div>)}
          </dl>
        </section>

        {/* Wie wij beleveren */}
        <section id="doelgroepen" className="wrap container-x scroll-mt-20 py-20 md:py-28">
          <Reveal><SectionHead eyebrow="Voor professionals" title="Wie wij beleveren." text="Wij leveren rechtstreeks aan professionals die met grote aantallen werken. Familiebedrijf sinds 2001, één gewas: daardoor weten wij wat u nodig heeft." /></Reveal>
          <div className="mt-12 grid grid-cols-1 gap-6 md:grid-cols-3">
            {b2b.groups.map((g, i) => (
              <Reveal key={g.title} index={i} className="flex flex-col rounded-img border border-line bg-surface p-6 md:p-7">
                <p className="num font-display text-[18px] text-bloom">0{i + 1}</p>
                <h3 className="mt-2 font-display text-[26px] leading-tight">{g.title}</h3>
                <p className="mt-1 text-[14.5px] text-muted">{g.text}</p>
                <dl className="mt-6 border-t border-line">
                  {g.rows.map(([k, v]) => <div key={k} className="flex justify-between gap-4 border-b border-line py-3 text-[14.5px]"><dt className="text-muted">{k}</dt><dd className="text-right text-ink">{v}</dd></div>)}
                </dl>
              </Reveal>
            ))}
          </div>
        </section>

        {/* Werkwijze */}
        <section id="werkwijze" className="scroll-mt-20 border-y border-line bg-surface py-20 md:py-28">
          <div className="wrap container-x grid grid-cols-1 gap-12 lg:grid-cols-12">
            <Reveal className="lg:col-span-4"><SectionHead eyebrow="Onze voordelen" title="Hoe wij voor u werken." text="Vier zekerheden bij elke projectorder, van offerte tot oplevering." /></Reveal>
            <dl className="grid grid-cols-1 gap-x-10 sm:grid-cols-2 lg:col-span-8">
              {b2b.services.map((s, i) => (
                <Reveal key={s.title} index={i} className="border-t border-line-2 py-6">
                  <dt className="font-display text-[23px] leading-tight">{s.title}</dt>
                  <dd className="mt-2 max-w-[48ch] text-[14.5px] leading-relaxed text-ink-2">{s.text}</dd>
                </Reveal>
              ))}
            </dl>
          </div>
        </section>

        {/* Voorraad */}
        <section id="voorraad" className="wrap container-x scroll-mt-20 py-20 md:py-28">
          <div className="grid grid-cols-1 gap-12 lg:grid-cols-12">
            <Reveal className="lg:col-span-4"><SectionHead eyebrow="Direct beschikbaar" title="Beschikbare maten." text="Standaard op voorraad in alle gangbare maten. Specifieke soorten en grootformaten op aanvraag." /><p className="mt-6 max-w-[40ch] text-[13.5px] leading-relaxed text-muted">{b2b.sizesNote}</p></Reveal>
            <Reveal index={1} className="lg:col-span-8">
              <table className="w-full border-collapse text-left text-[15px]">
                <thead><tr className="border-b border-line-2">{['Maat', 'Voorraad', 'Geschikt voor'].map((h) => <th key={h} scope="col" className="py-3 pr-4 text-[12px] font-semibold uppercase tracking-[0.12em] text-muted">{h}</th>)}</tr></thead>
                <tbody>
                  {b2b.sizes.map(([m, s, g]) => (
                    <tr key={m} className="border-b border-line">
                      <td className="num whitespace-nowrap py-4 pr-4 font-display text-[19px]">{m}</td>
                      <td className="py-4 pr-4"><span className="inline-flex items-center gap-2"><span className={`size-2 rounded-full ${s.startsWith('Ruim') ? 'bg-moss' : s === 'Op voorraad' ? 'bg-moss/55' : 'border border-ink/40'}`} aria-hidden="true" />{s}</span></td>
                      <td className="py-4 pr-4 text-ink-2">{g}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </Reveal>
          </div>
        </section>

        {/* Proces */}
        <section className="bg-paper-2 py-20 md:py-28">
          <div className="wrap container-x">
            <Reveal><SectionHead eyebrow="Het proces" title="Hoe werkt een projectorder." text="Vier stappen, van aanvraag tot levering." /></Reveal>
            <ol className="mt-12 grid grid-cols-1 gap-8 md:grid-cols-4 md:gap-6">
              {b2b.steps.map((s, i) => (
                <Reveal as="li" key={s.title} index={i} className="relative border-t border-line-2 pt-5">
                  <span className="num font-display text-[40px] leading-none text-bloom" style={{ fontVariationSettings: '"opsz" 72' }}>{i + 1}</span>
                  <h3 className="mt-3 font-display text-[23px] leading-tight">{s.title}</h3>
                  <p className="mt-2 text-[14.5px] leading-relaxed text-ink-2">{s.text}</p>
                </Reveal>
              ))}
            </ol>
          </div>
        </section>

        {/* Tarieven */}
        <section id="tarieven" className="wrap container-x scroll-mt-20 py-20 md:py-28">
          <div className="grid grid-cols-1 gap-12 lg:grid-cols-12">
            <Reveal className="lg:col-span-4"><SectionHead eyebrow="Tarieven" title="Zakelijke tarieven." text="Drie staffels op basis van projectomvang. Definitieve prijs in de offerte." /><div className="mt-8 flex flex-wrap gap-3"><Button as="button" variant="ink" onClick={() => openModal('prijslijst')}>Prijslijst ontvangen</Button></div></Reveal>
            <ol className="lg:col-span-8">
              {b2b.tiers.map((t, i) => (
                <Reveal as="li" key={t.range} index={i} className="grid grid-cols-[1fr_auto] gap-x-6 gap-y-2 border-b border-line py-6 first:border-t md:grid-cols-[180px_1fr_auto] md:items-center">
                  <div><p className="eyebrow text-muted">{t.label}</p><p className="num mt-1 font-display text-[24px] leading-tight">{t.range}</p></div>
                  <p className="num row-start-1 col-start-2 self-start font-display text-[34px] leading-none text-moss md:col-start-3 md:text-[40px]" style={{ fontVariationSettings: '"opsz" 72' }}>{t.discount}</p>
                  <p className="col-span-2 max-w-[52ch] text-[14.5px] leading-relaxed text-ink-2 md:col-span-1 md:col-start-2 md:row-start-1">{t.text}</p>
                </Reveal>
              ))}
            </ol>
            <p className="text-[12.5px] text-muted lg:col-span-8 lg:col-start-5">{b2b.tiersNote}</p>
          </div>
        </section>

        {/* FAQ */}
        <section id="faq" className="scroll-mt-20 border-y border-line bg-surface py-20 md:py-28">
          <div className="wrap container-x grid grid-cols-1 gap-12 lg:grid-cols-12">
            <Reveal className="lg:col-span-4"><SectionHead eyebrow="Veelgestelde vragen" title="Praktische antwoorden voor zakelijke afnemers." /></Reveal>
            <Reveal index={1} className="lg:col-span-8"><Faq items={b2b.faq} /></Reveal>
          </div>
        </section>

        {/* Offerte */}
        <section id="offerte" className="scroll-mt-16 bg-moss py-20 text-white on-dark md:py-28">
          <div className="wrap container-x grid grid-cols-1 gap-12 lg:grid-cols-12 lg:gap-16">
            <div className="lg:col-span-5">
              <Reveal><SectionHead dark eyebrow="Projectofferte" title="Projectofferte aanvragen." text="Vul het formulier in voor een gespecificeerde offerte met partijprijzen, levering en planning. Reactie binnen 24 uur, rechtstreeks van de kweker." /></Reveal>
              <Reveal index={1} className="mt-10 flex items-center gap-5 rounded-img border border-white/15 bg-white/5 p-5">
                <img src={img('owner-sm')} alt={company.founder} className="size-20 shrink-0 rounded-img object-cover object-[50%_20%]" />
                <div>
                  <p className="font-display text-[22px] leading-tight">{company.founder}</p>
                  <p className="text-[13.5px] text-white/70">{company.founderRole} · uw vaste contactpersoon</p>
                  <div className="mt-2 flex flex-wrap gap-x-4 gap-y-1 text-[14px]">
                    <a href={company.phone1Href} className="num underline underline-offset-4">{company.phone1}</a>
                    <a href={company.whatsapp} target="_blank" rel="noopener noreferrer" className="underline underline-offset-4">WhatsApp</a>
                    <a href={`mailto:${company.email}`} className="underline underline-offset-4">{company.email}</a>
                  </div>
                </div>
              </Reveal>
              <Reveal index={2}><p className="mt-8 text-[14px] leading-relaxed text-white/75">Liever eerst de prijslijst? <button type="button" onClick={() => openModal('prijslijst')} className="underline underline-offset-4">Ontvang de prijslijst per e-mail</button>. Particulier? <a href="index.html" className="underline underline-offset-4">Naar de pagina voor uw tuin</a>.</p></Reveal>
            </div>
            <Reveal index={1} className="lg:col-span-7"><OfferteForm /></Reveal>
          </div>
        </section>
      </main>
      <SiteFooter />
      <PrijslijstModal />
      <WhatsAppFloat />
    </>
  )
}
