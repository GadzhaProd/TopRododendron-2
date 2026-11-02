import { VideoHero } from '@/components/ui/video-hero'
import { Button } from '@/components/ui/button'
import { Reveal } from '@/components/ui/reveal'
import { SplitCta } from '@/components/ui/split-cta'
import { Faq } from '@/components/ui/faq'
import { HeaderC, FooterC, HeadC, Pill, ContactC } from './shared'
import { varieties, story, promises, faq, img, company, tuinturf } from '@/data/content'
import { ArrowUpRight } from 'lucide-react'

export default function Home() {
  return (
    <>
      <HeaderC />
      <main>
        <VideoHero
          overlay="bottom"
          eyebrow="Otterlo, Veluwe · familiekwekerij sinds 2001"
          title="Rhododendrons die aanslaan. Gegarandeerd."
          titleClassName="text-[clamp(42px,6.4vw,96px)] font-medium tracking-[-0.04em]"
          text="Gekweekt op veenrijke bodem, met een sterk wortelstelsel. Vers gerooid op de dag van levering, bezorgd met eigen transport."
          actions={<><Button href="#planten" variant="white" size="lg" arrow>Bekijk de planten</Button><Button href="groothandel.html" variant="outline-white" size="lg">Groothandel</Button></>}
        />

        {/* Waarom: bento with real photos */}
        <section id="waarom" className="container-x py-20 md:py-28">
          <Reveal><HeadC eyebrow="Waarom Top Rhododendrons" title="Vier redenen waarom onze planten aanslaan." size="lg" /></Reveal>
          <div className="mt-12 grid gap-4 md:grid-cols-6 md:grid-rows-2 md:gap-5">
            <Reveal className="relative min-h-[380px] overflow-hidden rounded-img bg-bg-2 md:col-span-4 md:row-span-2">
              <img src={img('B2BHERO')} alt="Het veld van de kwekerij in Otterlo" className="absolute inset-0 h-full w-full object-cover object-[50%_60%] img-treat" />
              <div className="absolute inset-0 bg-gradient-to-t from-black/70 via-black/10 to-transparent" />
              <div className="absolute inset-x-0 bottom-0 p-7 text-white on-dark md:p-9"><p className="eyebrow text-white/70">01 · Veenrijke bodem</p><h3 className="mt-3 max-w-[22ch] font-display text-[clamp(26px,2.6vw,36px)] leading-[1.05]">Het veld in Otterlo geeft onze planten een sterk wortelstelsel.</h3><p className="mt-3 max-w-[48ch] text-[15px] text-white/80">{story.p2}</p></div>
            </Reveal>
            <Reveal index={1} className="rounded-img bg-accent p-7 text-white on-dark md:col-span-2 md:p-8"><p className="eyebrow text-white/70">02 · Garantie</p><h3 className="mt-3 font-display text-[clamp(24px,2.2vw,30px)] leading-[1.05]">Aangroeigarantie op elke plant.</h3><p className="mt-3 text-[14.5px] leading-relaxed text-white/80">{promises[0].text}</p></Reveal>
            <Reveal index={2} className="relative min-h-[260px] overflow-hidden rounded-img bg-bg-2 md:col-span-2">
              <img src={img('cunninghams-white-2-sm')} alt="Cunningham's White, vers gerooid" className="absolute inset-0 h-full w-full object-cover img-treat" />
              <div className="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent" />
              <div className="absolute inset-x-0 bottom-0 p-7 text-white on-dark"><p className="eyebrow text-white/70">03 · Vers gerooid</p><h3 className="mt-3 font-display text-[24px] leading-[1.05]">Gerooid op de dag van levering.</h3></div>
            </Reveal>
          </div>
          <Reveal index={3} className="mt-4 grid gap-4 md:mt-5 md:grid-cols-3 md:gap-5">
            <div className="rounded-img bg-surface p-7 md:p-8"><p className="eyebrow text-muted">04 · Eigen transport</p><h3 className="mt-3 font-display text-[24px] leading-[1.05]">Door heel Nederland, wanneer het u uitkomt.</h3><p className="mt-3 text-[14.5px] leading-relaxed text-fg-2">{promises[2].text}</p></div>
            <div className="rounded-img bg-surface p-7 md:p-8"><p className="eyebrow text-muted">Persoonlijk advies</p><h3 className="mt-3 font-display text-[24px] leading-[1.05]">Rechtstreeks van de kweker.</h3><p className="mt-3 text-[14.5px] leading-relaxed text-fg-2">{promises[3].text}</p></div>
            <div className="rounded-img bg-surface p-7 md:p-8"><p className="eyebrow text-muted">Voorraad</p><h3 className="mt-3 font-display text-[24px] leading-[1.05]">10.000 planten op stam.</h3><p className="mt-3 text-[14.5px] leading-relaxed text-fg-2">Zeven soorten in maten van 40 tot 120 cm en meer. Geen minimumbestelling voor particulieren.</p></div>
          </Reveal>
        </section>

        {/* Planten */}
        <section id="planten" className="bg-bg-2 py-20 md:py-28">
          <div className="container-x">
            <Reveal className="flex flex-col gap-6 md:flex-row md:items-end md:justify-between"><HeadC eyebrow="Assortiment" title="Zeven soorten. Alle winterhard." text="Prijs per plant in 40–60 cm; ook leverbaar tot 120 cm. Bezorgd of afhalen in Otterlo." /><div className="flex flex-wrap gap-2"><Pill>Rood</Pill><Pill>Wit</Pill><Pill>Roze</Pill><Pill>Paars</Pill><Pill>Haag</Pill><Pill>Solitair</Pill></div></Reveal>
            <div className="mt-12 grid gap-5 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
              {varieties.map((v, i) => (
                <Reveal key={v.slug} index={i % 4} className={i === 0 ? 'sm:col-span-2 lg:col-span-2 xl:col-span-2' : ''}>
                  <a href="#" className="group/p block overflow-hidden rounded-img bg-surface">
                    <div className={`${i === 0 ? 'aspect-[16/11]' : 'aspect-[4/5]'} overflow-hidden`}>
                      <img src={img(`${v.slug}-2`)} alt={v.name} loading="lazy" className="h-full w-full object-cover img-treat transition-transform duration-[1000ms] ease-[cubic-bezier(.22,1,.36,1)] group-hover/p:scale-[1.04]" />
                    </div>
                    <div className="p-5 md:p-6">
                      <div className="flex items-start justify-between gap-4"><h3 className="font-display text-[22px] leading-tight">{v.name}</h3><span className="inline-flex size-9 shrink-0 items-center justify-center rounded-full border border-fg/12 transition-colors group-hover/p:bg-fg group-hover/p:text-bg"><ArrowUpRight className="size-4" /></span></div>
                      <p className="mt-1.5 flex items-center gap-2 text-[13px] text-muted"><span className="size-2.5 rounded-full" style={{ background: v.hex, boxShadow: 'inset 0 0 0 1px rgba(0,0,0,.12)' }} />{v.color} · {v.bloei} · {v.hoogte}</p>
                      <p className="mt-3 text-[14.5px] leading-relaxed text-fg-2">{v.short}</p>
                      <p className="mt-4 text-[15px] font-semibold">vanaf € {v.from}</p>
                    </div>
                  </a>
                </Reveal>
              ))}
              <Reveal index={3} className="flex flex-col justify-between rounded-img bg-fg p-6 text-bg on-dark md:p-7">
                <div><p className="eyebrow text-white/60">Bij het planten</p><h3 className="mt-3 font-display text-[24px] leading-tight">{tuinturf.name}</h3><p className="mt-3 text-[14.5px] leading-relaxed text-white/75">{tuinturf.text}</p></div>
                <div className="mt-6 flex items-center justify-between"><p className="text-[15px] font-semibold">€ {tuinturf.price} <span className="font-normal text-white/60">{tuinturf.unit}</span></p><Button href="#" variant="white" size="sm">Voeg toe</Button></div>
              </Reveal>
            </div>
          </div>
        </section>

        {/* Kweker */}
        <section id="kweker" className="container-x py-20 md:py-28">
          <div className="grid items-center gap-10 md:grid-cols-12 md:gap-16">
            <Reveal className="md:col-span-5"><div className="aspect-[4/5] overflow-hidden rounded-img bg-bg-2"><img src={img('owner-portrait')} alt={`${company.founder}, oprichter van ${company.name}`} className="h-full w-full object-cover object-[50%_15%] img-treat" /></div></Reveal>
            <div className="md:col-span-7">
              <Reveal><HeadC eyebrow={`${company.founder} · oprichter & kweker`} title={story.h} size="lg" /></Reveal>
              <Reveal index={1}><p className="mt-7 max-w-[58ch] text-[17px] leading-relaxed text-fg-2">{story.p1}</p><p className="mt-4 max-w-[58ch] text-[16px] leading-relaxed text-fg-2">Wij rooien op de dag van levering, niet eerder: zo komt elke plant in optimale conditie aan. U spreekt rechtstreeks met de kweker, van vraag tot levering.</p></Reveal>
              <Reveal index={2} className="mt-8 rounded-img border border-fg/10 bg-surface p-6 md:p-7"><p className="font-display text-[22px] leading-snug md:text-[24px]">„{story.quote}”</p><p className="mt-3 text-[13px] text-muted">{company.founder}, {company.name}</p></Reveal>
              <Reveal index={3} className="mt-8 flex flex-wrap gap-3"><Button href={company.phone1Href} variant="solid" size="md">Bel de kweker</Button><Button href={company.whatsapp} variant="outline" size="md">WhatsApp</Button></Reveal>
            </div>
          </div>
        </section>

        {/* Split CTA */}
        <div className="container-x pb-20 md:pb-28">
          <Reveal>
            <SplitCta
              className="gap-4 md:gap-5"
              minH="min-h-[420px] md:min-h-[520px]"
              panels={[
                { eyebrow: 'Voor uw tuin', title: 'Vanaf één plant, bezorgd of afhalen in Otterlo.', text: 'Geen minimumbestelling. Persoonlijk advies over soort, maat en standplaats.', action: <Button href="#planten" variant="white" size="md" arrow>Bekijk de planten</Button>, image: img('roseum-elegans-2'), dark: true, className: 'rounded-img' },
                { eyebrow: 'Voor professionals', title: 'Hoveniers, gemeenten en projecten.', text: 'Partijprijzen vanaf 25 stuks, vaste contactpersoon, plantpaspoort, factuur op 30 dagen.', action: <Button href="groothandel.html" variant="white" size="md" arrow>Naar groothandel</Button>, image: img('catawbiense-grandiflorum-2'), dark: true, className: 'rounded-img' },
              ]}
            />
          </Reveal>
        </div>

        {/* FAQ */}
        <section id="plantgids" className="bg-bg-2 py-20 md:py-28">
          <div className="container-x grid gap-12 md:grid-cols-12">
            <Reveal className="md:col-span-5"><HeadC eyebrow="Plantgids" title="Wat u wilt weten voordat u plant." text="Twijfelt u over soort, maat of standplaats? Bel ons; wij adviseren graag persoonlijk." /><Button href="#" variant="outline" className="mt-8" arrow>Naar de plantgids</Button></Reveal>
            <Reveal index={1} className="md:col-span-7"><Faq items={faq} /></Reveal>
          </div>
        </section>

        {/* Contact */}
        <section id="contact" className="container-x py-20 md:py-28">
          <Reveal className="rounded-img bg-accent p-8 text-white on-dark md:p-14">
            <HeadC dark eyebrow="Contact" title="Kom langs op de kwekerij, of bel ons." text="Wilt u advies over de juiste soort voor uw tuin? Wij helpen u graag persoonlijk." />
            <div className="mt-8 flex flex-wrap gap-3"><Button href={company.phone1Href} variant="white" size="lg">Bel {company.phone1}</Button><Button href={company.whatsapp} variant="outline-white" size="lg">WhatsApp</Button><Button href={`mailto:${company.email}`} variant="outline-white" size="lg">E-mail</Button></div>
            <div className="mt-12 border-t border-white/15 pt-10"><ContactC dark /></div>
          </Reveal>
        </section>
      </main>
      <FooterC />
    </>
  )
}
