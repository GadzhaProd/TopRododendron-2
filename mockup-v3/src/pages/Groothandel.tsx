import { Phone } from 'lucide-react'
import { SiteHeader } from '@/components/site-header'
import { SiteFooter } from '@/components/site-footer'
import { Toast } from '@/components/toast'
import { Button, ext } from '@/components/button'
import { Reveal } from '@/components/reveal'
import { SectionHead } from '@/components/section-head'
import { Faq } from '@/components/faq'
import { OfferteForm, PrijslijstModal } from '@/components/forms'
import { WhatsAppFloat, WhatsAppIcon } from '@/components/whatsapp-float'
import { openModal } from '@/lib/store'
import { b2b, company, img, srcset } from '@/data/content'

export default function Groothandel() {
  return (
    <>
      <a href="#main" className="skip-link">Naar de inhoud</a>
      <SiteHeader variant="b2b" hero />
      <main id="main" className="pb-4">
        {/* Hero: the field, full bleed */}
        <section id="hero" className="relative flex min-h-[100svh] flex-col justify-end overflow-hidden bg-night text-white on-dark">
          <img src={img('B2BHERO')} srcSet={srcset('B2BHERO')} sizes="100vw" alt="" className="absolute inset-0 h-full w-full object-cover object-[55%_60%] img-treat" />
          <div className="absolute inset-x-0 top-0 h-[35%] bg-gradient-to-b from-night/80 to-transparent" />
          <div className="absolute inset-0 bg-gradient-to-r from-night/70 via-night/35 to-night/10" />
          <div className="absolute inset-x-0 bottom-0 h-[78%] bg-gradient-to-t from-night via-night/70 to-transparent" />
          <div className="relative wrap container-x w-full pb-8 pt-28 md:pb-12">
            <div className="flex max-w-[50rem] flex-col items-start gap-4 md:gap-6">
              <p className="label text-shadow text-white">Groothandel · direct van de kweker</p>
              <h1 className="display text-shadow text-balance text-[clamp(36px,6.4vw,92px)]">{b2b.title}</h1>
              <p className="text-shadow max-w-[40rem] text-[16px] font-medium leading-relaxed text-white md:text-[19px]">{b2b.sub} <span className="hidden sm:inline">{b2b.intro}</span></p>
              <div className="mt-1 flex flex-wrap gap-3">
                <Button href="#offerte" variant="white" size="lg" arrow>Vraag offerte aan</Button>
                <Button href={company.phone1Href} variant="outline-white" size="lg"><Phone className="size-4" aria-hidden="true" /><span className="num">{company.phone1}</span></Button>
                <Button as="button" variant="outline-white" size="lg" onClick={() => openModal('prijslijst')} className="hidden sm:inline-flex">Prijslijst ontvangen</Button>
              </div>
              <button type="button" onClick={() => openModal('prijslijst')} className="text-[14px] font-semibold text-white underline underline-offset-4 sm:hidden">Prijslijst ontvangen per e-mail</button>
            </div>
            <dl className="mt-10 hidden grid-cols-4 gap-6 border-t border-white/20 pt-5 md:grid">
              {b2b.facts.map(([k, v]) => <div key={k}><dt className="text-[22px] font-semibold tracking-[-0.01em] text-white">{k}</dt><dd className="mt-1 text-[13.5px] text-white/75">{v}</dd></div>)}
            </dl>
          </div>
        </section>
        <section aria-label="Kerngegevens" className="bg-night text-white on-dark md:hidden">
          <dl className="container-x grid grid-cols-2 gap-x-6 gap-y-4 border-t border-white/10 py-6">
            {b2b.facts.map(([k, v]) => <div key={k}><dt className="text-[18px] font-semibold leading-tight">{k}</dt><dd className="mt-0.5 text-[13px] text-white/65">{v}</dd></div>)}
          </dl>
        </section>

        {/* Wie wij beleveren */}
        <section id="doelgroepen" className="wrap container-x scroll-mt-20 py-16 md:py-24">
          <Reveal><SectionHead size="lg" title="Wie wij beleveren." text="Wij leveren rechtstreeks aan professionals die met grote aantallen werken. Familiebedrijf sinds 2001, één gewas: daardoor weten wij wat u nodig heeft." /></Reveal>
          <div className="mt-10 grid grid-cols-1 gap-4 md:grid-cols-3 md:gap-5">
            {b2b.groups.map((g, i) => (
              <Reveal key={g.title} index={i} className="flex flex-col rounded-panel bg-surface p-6 md:p-7">
                <h3 className="text-[24px] font-semibold leading-tight tracking-[-0.01em]">{g.title}</h3>
                <p className="mt-1 text-[14.5px] text-muted">{g.text}</p>
                <dl className="mt-5 flex flex-col gap-2">
                  {g.rows.map(([k, v]) => <div key={k} className="flex justify-between gap-4 rounded-[10px] bg-bg px-3.5 py-2.5 text-[14.5px]"><dt className="text-muted">{k}</dt><dd className="text-right font-medium text-ink">{v}</dd></div>)}
                </dl>
              </Reveal>
            ))}
          </div>
        </section>

        {/* Werkwijze */}
        <section id="werkwijze" className="scroll-mt-20 bg-bg-2 py-16 md:py-24">
          <div className="wrap container-x grid grid-cols-1 gap-10 lg:grid-cols-12">
            <Reveal className="lg:col-span-4"><SectionHead title="Hoe wij voor u werken." text="Familiebedrijf sinds 2001. Eén gewas; daardoor weten wij wat u nodig heeft." /></Reveal>
            <dl className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:col-span-8">
              {b2b.services.map((s, i) => (
                <Reveal key={s.title} index={i} className="rounded-img bg-surface p-5 md:p-6">
                  <dt className="text-[20px] font-semibold leading-tight tracking-[-0.01em]">{s.title}</dt>
                  <dd className="mt-2 text-[14.5px] leading-relaxed text-ink-2">{s.text}</dd>
                </Reveal>
              ))}
            </dl>
          </div>
        </section>

        {/* Voorraad */}
        <section id="voorraad" className="wrap container-x scroll-mt-20 py-16 md:py-24">
          <div className="grid grid-cols-1 gap-10 lg:grid-cols-12">
            <Reveal className="lg:col-span-4"><SectionHead title="Beschikbare aantallen." text="Standaard op voorraad in alle gangbare maten. Specifieke soorten en grootformaten op aanvraag." /><p className="mt-5 max-w-[40ch] text-[13.5px] leading-relaxed text-muted">{b2b.sizesNote}</p></Reveal>
            <Reveal index={1} className="lg:col-span-8">
              <div className="overflow-x-auto rounded-panel bg-surface">
                <table className="w-full border-collapse text-left text-[15px]">
                  <thead><tr className="border-b border-line">{['Maat', 'Voorraad', 'Geschikt voor'].map((h) => <th key={h} scope="col" className="label px-4 py-3 text-muted md:px-5">{h}</th>)}</tr></thead>
                  <tbody>
                    {b2b.sizes.map(([m, s, g]) => (
                      <tr key={m} className="border-b border-line last:border-b-0">
                        <td className="num whitespace-nowrap px-4 py-4 text-[18px] font-semibold md:px-5">{m}</td>
                        <td className="px-4 py-4 md:px-5"><span className="inline-flex items-center gap-2"><span className={`size-2.5 rounded-full ${s.startsWith('Ruim') ? 'bg-moss' : s === 'Op voorraad' ? 'bg-leaf' : 'ring-1 ring-ink/50'}`} aria-hidden="true" />{s}</span></td>
                        <td className="px-4 py-4 text-ink-2 md:px-5">{g}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </Reveal>
          </div>
        </section>

        {/* Proces */}
        <section className="bg-night py-16 text-white on-dark md:py-24">
          <div className="wrap container-x">
            <Reveal><SectionHead dark title="Hoe werkt een projectorder." text="Vier stappen, van aanvraag tot levering." /></Reveal>
            <ol className="mt-10 grid grid-cols-1 gap-4 md:grid-cols-4">
              {b2b.steps.map((s, i) => (
                <Reveal as="li" key={s.title} index={i} className="rounded-img bg-white/[0.06] p-5 ring-1 ring-white/10 md:p-6">
                  <span className="num grid size-10 place-items-center rounded-full bg-white text-[15px] font-semibold text-night">{i + 1}</span>
                  <h3 className="mt-4 text-[21px] font-semibold leading-tight tracking-[-0.01em]">{s.title}</h3>
                  <p className="mt-2 text-[14.5px] leading-relaxed text-white/75">{s.text}</p>
                </Reveal>
              ))}
            </ol>
          </div>
        </section>

        {/* Tarieven */}
        <section id="tarieven" className="wrap container-x scroll-mt-20 py-16 md:py-24">
          <div className="grid grid-cols-1 gap-10 lg:grid-cols-12">
            <Reveal className="lg:col-span-4"><SectionHead title="Zakelijke tarieven." text="Drie staffels op basis van projectomvang. Definitieve prijs in de offerte." /><div className="mt-7"><Button as="button" variant="solid" onClick={() => openModal('prijslijst')}>Prijslijst ontvangen</Button></div></Reveal>
            <ol className="flex flex-col gap-3 lg:col-span-8">
              {b2b.tiers.map((t, i) => (
                <Reveal as="li" key={t.range} index={i} className="grid grid-cols-[1fr_auto] gap-x-6 gap-y-2 rounded-img bg-surface p-5 md:grid-cols-[200px_1fr_auto] md:items-center md:p-6">
                  <div><p className="label text-muted">{t.label}</p><p className="num mt-1 text-[22px] font-semibold leading-tight tracking-[-0.01em]">{t.range}</p></div>
                  <p className="num col-start-2 row-start-1 self-start text-[32px] font-semibold tracking-[-0.03em] text-moss md:col-start-3 md:text-[38px]">{t.discount}</p>
                  <p className="col-span-2 max-w-[52ch] text-[14.5px] leading-relaxed text-ink-2 md:col-span-1 md:col-start-2 md:row-start-1">{t.text}</p>
                </Reveal>
              ))}
            </ol>
            <p className="text-[12.5px] text-muted lg:col-span-8 lg:col-start-5">{b2b.tiersNote}</p>
          </div>
        </section>

        {/* FAQ */}
        <section id="faq" className="scroll-mt-20 bg-bg-2 py-16 md:py-24">
          <div className="wrap container-x grid grid-cols-1 gap-10 lg:grid-cols-12">
            <Reveal className="lg:col-span-4"><SectionHead title="Praktische antwoorden voor zakelijke afnemers." /></Reveal>
            <Reveal index={1} className="lg:col-span-8"><Faq items={b2b.faq} /></Reveal>
          </div>
        </section>

        {/* Offerte */}
        <section id="offerte" className="scroll-mt-16 bg-moss py-16 text-white on-dark md:py-24">
          <div className="wrap container-x grid grid-cols-1 gap-10 lg:grid-cols-12 lg:gap-14">
            <div className="lg:col-span-5">
              <Reveal><SectionHead dark size="lg" title="Projectofferte aanvragen." text="Vul het formulier in voor een gespecificeerde offerte. Reactie binnen 24 uur, rechtstreeks van de kweker." /></Reveal>
              <Reveal index={1} className="mt-8 flex items-center gap-5 rounded-img bg-white/8 p-5 ring-1 ring-white/12">
                <img src={img('owner-sm')} alt={company.founder} className="size-20 shrink-0 rounded-[12px] object-cover object-[50%_20%]" />
                <div>
                  <p className="text-[20px] font-semibold leading-tight">{company.founder}</p>
                  <p className="text-[13.5px] text-white/70">Eigenaar {company.name}. U spreekt rechtstreeks met de kweker.</p>
                  <div className="mt-2 flex flex-wrap gap-x-4 gap-y-1 text-[14px] font-medium">
                    <a href={company.phone1Href} className="num underline underline-offset-4">{company.phone1}</a>
                    <a href={company.whatsapp} {...ext} className="inline-flex items-center gap-1.5 underline underline-offset-4"><WhatsAppIcon className="size-4" />WhatsApp</a>
                    <a href={`mailto:${company.email}`} className="underline underline-offset-4">{company.email}</a>
                  </div>
                </div>
              </Reveal>
              <Reveal index={2}><p className="mt-6 text-[14px] leading-relaxed text-white/75">Liever eerst de prijslijst? <button type="button" onClick={() => openModal('prijslijst')} className="font-semibold text-white underline underline-offset-4">Ontvang de prijslijst per e-mail</button>. Particulier? <a href="index.html" className="font-semibold text-white underline underline-offset-4">Naar de pagina voor uw tuin</a>.</p></Reveal>
            </div>
            <Reveal index={1} className="lg:col-span-7"><OfferteForm /></Reveal>
          </div>
        </section>
      </main>
      <SiteFooter />
      <PrijslijstModal />
      <WhatsAppFloat />
      <Toast />
    </>
  )
}
