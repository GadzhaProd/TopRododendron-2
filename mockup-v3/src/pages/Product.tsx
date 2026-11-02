import { useEffect, useState } from 'react'
import { ArrowLeft, Check, ChevronRight, ShieldCheck, Truck, Scissors } from 'lucide-react'
import { SiteHeader } from '@/components/site-header'
import { SiteFooter } from '@/components/site-footer'
import { CartDrawer } from '@/components/cart-drawer'
import { Button } from '@/components/button'
import { Reveal } from '@/components/reveal'
import { SectionHead, Swatch } from '@/components/section-head'
import { Gallery } from '@/components/gallery'
import { Quantity } from '@/components/quantity'
import { Checkbox } from '@/components/fields'
import { BloomCalendar, BloomLegend } from '@/components/bloom-calendar'
import { VarietyCard } from '@/components/variety-card'
import { cn } from '@/lib/utils'
import { addToCart, openCart, productSlug } from '@/lib/store'
import { varieties, bySlug, kenmerken, tuinturf, company, fmtEur, parsePrice, img, type Variety } from '@/data/content'

function Breadcrumb({ name }: { name: string }) {
  return (
    <nav aria-label="Kruimelpad" className="flex flex-wrap items-center gap-1.5 text-[13.5px] text-muted">
      <a href="index.html" className="hover:text-ink">Home</a><ChevronRight className="size-3.5" aria-hidden="true" />
      <a href="assortiment.html" className="hover:text-ink">Assortiment</a><ChevronRight className="size-3.5" aria-hidden="true" />
      <span className="text-ink" aria-current="page">{name}</span>
    </nav>
  )
}

function TrustLines({ items }: { items: [React.ElementType, string][] }) {
  return (
    <ul className="flex flex-col gap-2.5 text-[14px] text-ink-2">
      {items.map(([Icon, t]) => <li key={t} className="flex items-center gap-2.5"><Icon className="size-4 shrink-0 text-moss" strokeWidth={1.7} aria-hidden="true" />{t}</li>)}
    </ul>
  )
}

function Kenmerken({ rows }: { rows: [string, string][] }) {
  return (
    <dl className="grid grid-cols-1 border-t border-line sm:grid-cols-2 sm:gap-x-10">
      {rows.map(([k, v]) => <div key={k} className="grid grid-cols-[130px_1fr] gap-4 border-b border-line py-3 text-[14.5px]"><dt className="text-muted">{k}</dt><dd className="text-ink">{v}</dd></div>)}
    </dl>
  )
}

function PlantView({ v }: { v: Variety }) {
  const [size, setSize] = useState(0)
  const [qty, setQty] = useState(1)
  const [turf, setTurf] = useState(false)
  const [added, setAdded] = useState(false)
  useEffect(() => { setSize(0); setQty(1); setTurf(false); setAdded(false) }, [v.slug])
  const s = v.sizes[size]
  const total = parsePrice(s.price) * qty + (turf ? parsePrice(tuinturf.price) : 0)
  const others = varieties.filter((x) => x.slug !== v.slug)
  function add() {
    addToCart({ slug: v.slug, name: v.name, size: s.label, price: s.price, qty, image: `${v.slug}-sm` })
    if (turf) addToCart({ slug: tuinturf.slug, name: tuinturf.name, size: 'zak 40 L', price: tuinturf.price, qty: 1, image: 'tuinturf-sm' })
    setAdded(true); openCart()
  }
  return (
    <>
      <div className="wrap container-x pb-4 pt-6"><Breadcrumb name={v.name} /></div>
      <section className="wrap container-x grid grid-cols-1 gap-10 pb-16 lg:grid-cols-12 lg:gap-16">
        <div className="lg:col-span-7"><Gallery photos={[{ name: `${v.slug}-2`, alt: `Rhododendron ${v.name}, volle struik in bloei` }, { name: v.slug, alt: `Rhododendron ${v.name}, bloemtros van dichtbij` }]} /></div>
        <div className="lg:col-span-5">
          <div className="lg:sticky lg:top-24">
            <p className="eyebrow flex items-center gap-2 text-bloom"><Swatch hex={v.hex} light={v.light} />Rhododendron · {v.color}</p>
            <h1 className="mt-3 font-display text-[clamp(36px,4.4vw,56px)] leading-[1.02]" style={{ fontVariationSettings: '"opsz" 72' }}>{v.name}</h1>
            <p className="mt-2 text-[14.5px] text-muted">{v.bloei} · {v.hoogte} · {v.standplaats.split(',')[0]} · winterhard</p>
            <p className="mt-5 text-[15.5px] leading-relaxed text-ink-2">{v.long}</p>

            <fieldset className="mt-8">
              <legend className="mb-3 text-[13px] font-medium text-ink-2">Kies uw maat <span className="text-muted">(hoogte bij levering)</span></legend>
              <div className="grid grid-cols-2 gap-2">
                {v.sizes.map((x, i) => (
                  <button key={x.label} type="button" onClick={() => { setSize(i); setAdded(false) }} aria-pressed={size === i} className={cn('flex items-center justify-between rounded-field border px-4 py-3 text-left text-[14.5px] transition-colors', size === i ? 'border-ink bg-ink text-paper' : 'border-ink/50 bg-surface hover:border-ink')}>
                    <span>{x.label}</span><span className="num font-medium">€ {x.price.replace(',00', ',–')}</span>
                  </button>
                ))}
              </div>
            </fieldset>

            <div className="mt-5 flex flex-wrap items-center gap-4">
              <Quantity value={qty} onChange={(n) => { setQty(n); setAdded(false) }} />
              <p className="text-[14px] text-ink-2">Totaal <span className="num ml-1 font-display text-[26px] text-ink">{fmtEur(total)}</span></p>
            </div>

            <div className={cn('mt-5 rounded-img border p-4 transition-colors', turf ? 'border-moss bg-moss/[0.06]' : 'border-line bg-surface')}>
              <Checkbox id="turf" checked={turf} onChange={(x) => { setTurf(x); setAdded(false) }}>
                <span className="flex items-start gap-3">
                  <img src={img('tuinturf-sm')} alt="" className="size-14 shrink-0 rounded-img object-cover" />
                  <span><span className="block text-[14.5px] font-medium">Voeg {tuinturf.name} toe <span className="num text-muted">(+ € {tuinturf.price}, zak 40 L)</span></span><span className="mt-0.5 block text-[13.5px] leading-relaxed text-ink-2">{tuinturf.upsell}</span></span>
                </span>
              </Checkbox>
            </div>

            <div className="mt-5 flex flex-col gap-3 sm:flex-row">
              <Button as="button" variant="solid" size="lg" onClick={add} className="w-full sm:flex-1">{added ? <><Check className="size-4" /> Toegevoegd aan winkelwagen</> : 'In winkelwagen'}</Button>
              <Button href={company.phone1Href} variant="outline" size="lg" className="w-full sm:w-auto">Bel voor advies</Button>
            </div>
            <div className="mt-6"><TrustLines items={[[ShieldCheck, 'Aangroeigarantie op al onze planten'], [Truck, 'Eigen transport door heel Nederland, of afhalen in Otterlo'], [Scissors, 'Vers gerooid bij uw bestelling']]} /></div>
            <p className="mt-5 text-[12.5px] text-muted">Demo: de winkelwagen is in de mockup nog niet gekoppeld aan een afrekenpagina.</p>
          </div>
        </div>
      </section>

      <section className="border-t border-line bg-surface py-16 md:py-20">
        <div className="wrap container-x grid grid-cols-1 gap-12 lg:grid-cols-12 lg:gap-16">
          <Reveal className="lg:col-span-7">
            <SectionHead size="sm" eyebrow="Kenmerken" title={`${v.name} in cijfers`} />
            <div className="mt-8"><Kenmerken rows={kenmerken(v)} /></div>
          </Reveal>
          <Reveal index={1} className="lg:col-span-5">
            <SectionHead size="sm" eyebrow="Bloei en plantmoment" title={`Bloeit in ${v.bloei.toLowerCase()}`} text="Planten kan het hele jaar door, behalve bij vorst; maart–april en september–oktober zijn ideaal." />
            <div className="mt-8 rounded-img border border-line bg-paper p-4"><BloomCalendar rows={[v]} compact /><BloomLegend className="mt-4" /></div>
            <a href="plantgids.html" className="mt-4 inline-block text-[14px] underline underline-offset-4">Alle soorten vergelijken in de plantgids</a>
          </Reveal>
        </div>
      </section>

      <section className="wrap container-x py-16 md:py-20">
        <Reveal className="flex flex-col gap-5 rounded-img bg-moss p-7 text-white on-dark md:flex-row md:items-center md:justify-between md:p-9">
          <div><p className="eyebrow text-white/70">Voor hoveniers en grootverbruikers</p><p className="mt-2 font-display text-[24px] leading-tight md:text-[28px]">Vanaf 25 stuks: scherpe partijprijzen, eigen transport en plantservice.</p></div>
          <Button href="groothandel.html" variant="paper" size="md" arrow className="shrink-0">Groothandelcondities</Button>
        </Reveal>
      </section>

      <section className="wrap container-x pb-20 md:pb-28">
        <Reveal className="flex items-end justify-between gap-6"><SectionHead size="sm" eyebrow="Ook van ons veld" title="Andere soorten" /><a href="assortiment.html" className="hidden text-[14px] underline underline-offset-4 sm:inline">Alle soorten</a></Reveal>
        <div className="mt-8 grid grid-cols-2 gap-x-5 gap-y-10 md:grid-cols-3 lg:grid-cols-6">
          {others.map((o) => <VarietyCard key={o.slug} v={o} sizes="(min-width: 1024px) 16vw, (min-width: 768px) 33vw, 50vw" className="[&_h3]:text-[18px] [&_p:nth-of-type(2)]:hidden [&_.swatch]:hidden" />)}
        </div>
        <a href="assortiment.html" className="mt-10 inline-flex items-center gap-2 text-[14.5px] text-ink-2 hover:text-ink"><ArrowLeft className="size-4" aria-hidden="true" />Terug naar het assortiment</a>
      </section>
    </>
  )
}

function TurfView() {
  const [qty, setQty] = useState(1)
  const [added, setAdded] = useState(false)
  const t = tuinturf
  return (
    <>
      <div className="wrap container-x pb-4 pt-6"><Breadcrumb name={t.name} /></div>
      <section className="wrap container-x grid grid-cols-1 gap-10 pb-16 lg:grid-cols-12 lg:gap-16">
        <div className="lg:col-span-7"><Gallery photos={[{ name: 'tuinturf', alt: t.fullName }]} /></div>
        <div className="lg:col-span-5">
          <p className="eyebrow text-bloom">Toebehoren</p>
          <h1 className="mt-3 font-display text-[clamp(34px,4vw,52px)] leading-[1.02]" style={{ fontVariationSettings: '"opsz" 72' }}>{t.fullName}</h1>
          <p className="mt-5 text-[15.5px] leading-relaxed text-ink-2">{t.short}</p>
          <p className="mt-3 text-[15.5px] leading-relaxed text-ink-2">{t.long}</p>
          <p className="num mt-7 font-display text-[30px]">€ {t.price} <span className="font-body text-[14px] text-muted">{t.unit}</span></p>
          <div className="mt-5 flex flex-wrap items-center gap-4"><Quantity value={qty} onChange={(n) => { setQty(n); setAdded(false) }} /><p className="text-[14px] text-ink-2">Totaal <span className="num ml-1 font-display text-[26px] text-ink">{fmtEur(parsePrice(t.price) * qty)}</span></p></div>
          <div className="mt-5 flex flex-col gap-3 sm:flex-row">
            <Button as="button" variant="solid" size="lg" onClick={() => { addToCart({ slug: t.slug, name: t.name, size: 'zak 40 L', price: t.price, qty, image: 'tuinturf-sm' }); setAdded(true); openCart() }} className="w-full sm:flex-1">{added ? <><Check className="size-4" /> Toegevoegd</> : 'In winkelwagen'}</Button>
            <Button href="assortiment.html" variant="outline" size="lg" className="w-full sm:w-auto">Naar de planten</Button>
          </div>
          <div className="mt-6"><TrustLines items={[[ShieldCheck, t.points[0]], [Truck, t.points[1]], [Scissors, t.points[2]]]} /></div>
          <p className="mt-5 text-[12.5px] text-muted">Demo: de winkelwagen is in de mockup nog niet gekoppeld aan een afrekenpagina.</p>
        </div>
      </section>
      <section className="border-t border-line bg-surface py-16 md:py-20">
        <div className="wrap container-x max-w-[900px]"><SectionHead size="sm" eyebrow="Kenmerken" title="Samenstelling en toepassing" /><div className="mt-8"><Kenmerken rows={t.kenmerken} /></div></div>
      </section>
      <section className="wrap container-x py-16 md:py-24">
        <Reveal className="flex items-end justify-between gap-6"><SectionHead size="sm" eyebrow="Van ons veld" title="De rhododendrons" /></Reveal>
        <div className="mt-8 grid grid-cols-2 gap-x-5 gap-y-10 md:grid-cols-4 lg:grid-cols-7">
          {varieties.map((o) => <VarietyCard key={o.slug} v={o} sizes="(min-width: 1024px) 14vw, (min-width: 768px) 25vw, 50vw" className="[&_h3]:text-[17px] [&_p:nth-of-type(2)]:hidden" />)}
        </div>
      </section>
    </>
  )
}

export default function Product() {
  const slug = productSlug.use()
  const v = bySlug(slug)
  const isTurf = slug === tuinturf.slug
  const name = isTurf ? tuinturf.fullName : (v?.name ?? 'Nova Zembla')
  useEffect(() => { document.title = `${isTurf ? name : `Rhododendron ${name}`} kopen · Top Rhododendrons` }, [name, isTurf])
  return (
    <>
      <a href="#main" className="skip-link">Naar de inhoud</a>
      <SiteHeader current="assortiment" />
      <main id="main" className="pt-16 md:pt-[76px]">
        {isTurf ? <TurfView /> : <PlantView v={v ?? varieties[0]} />}
      </main>
      <SiteFooter />
      <CartDrawer />
    </>
  )
}
