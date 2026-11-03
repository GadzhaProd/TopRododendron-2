import { useEffect, useRef, useState } from 'react'
import { ArrowLeft, Check, ChevronRight, ShieldCheck, Truck, Scissors, Phone } from 'lucide-react'
import { SiteHeader } from '@/components/site-header'
import { SiteFooter } from '@/components/site-footer'
import { CartDrawer } from '@/components/cart-drawer'
import { Toast } from '@/components/toast'
import { Button, ext } from '@/components/button'
import { Reveal } from '@/components/reveal'
import { SectionHead, Swatch } from '@/components/section-head'
import { Gallery } from '@/components/gallery'
import { Quantity } from '@/components/quantity'
import { Checkbox } from '@/components/fields'
import { BloomCalendar, BloomLegend } from '@/components/bloom-calendar'
import { VarietyCard } from '@/components/variety-card'
import { WhatsAppIcon } from '@/components/whatsapp-float'
import { cn } from '@/lib/utils'
import { addToCart, openCart, productSlug } from '@/lib/store'
import { varieties, popularOrder, bySlug, kenmerken, tuinturf, company, fmtEur, parsePrice, img, type Variety } from '@/data/content'

const ordered = popularOrder.map((s) => varieties.find((v) => v.slug === s)!)

function Breadcrumb({ name }: { name: string }) {
  return (
    <nav aria-label="Kruimelpad" className="flex flex-wrap items-center gap-1.5 text-[13.5px] text-muted">
      <a href="index.html" className="hover:text-ink">Home</a><ChevronRight className="size-3.5" aria-hidden="true" />
      <a href="assortiment.html" className="hover:text-ink">Assortiment</a><ChevronRight className="size-3.5" aria-hidden="true" />
      <span className="font-medium text-ink" aria-current="page">{name}</span>
    </nav>
  )
}

/** In-page switcher so every variety (and tuinturf) is reachable when this page is viewed on its own. */
function Switcher({ current }: { current: string }) {
  return (
    <nav aria-label="Kies een soort" className="no-scrollbar -mx-5 flex gap-2 overflow-x-auto px-5 pb-1 md:mx-0 md:flex-wrap md:px-0">
      {[...ordered.map((v) => ({ slug: v.slug, name: v.name, thumb: `${v.slug}-sm` })), { slug: tuinturf.slug, name: 'Tuinturf', thumb: 'tuinturf-sm' }].map((x) => (
        <a key={x.slug} href={`#${x.slug}`} aria-current={x.slug === current ? 'page' : undefined} className={cn('flex h-11 shrink-0 items-center gap-2 rounded-full pl-1 pr-3.5 text-[13.5px] font-semibold transition-colors', x.slug === current ? 'bg-night text-white' : 'bg-surface text-ink ring-1 ring-ink/15 hover:ring-ink/40')}>
          <img src={img(x.thumb)} alt="" className="size-9 rounded-full object-cover" />{x.name}
        </a>
      ))}
    </nav>
  )
}

function TrustLines({ items }: { items: [React.ElementType, string][] }) {
  return <ul className="flex flex-col gap-2.5 text-[14px] text-ink-2">{items.map(([Icon, t]) => <li key={t} className="flex items-center gap-2.5"><Icon className="size-4 shrink-0 text-moss" strokeWidth={1.8} aria-hidden="true" />{t}</li>)}</ul>
}
function Helper() {
  return (
    <div className="flex flex-col gap-3 rounded-img bg-surface p-4 sm:flex-row sm:items-center sm:justify-between">
      <div><p className="text-[15px] font-semibold">Nog vragen over úw plant?</p><p className="text-[13.5px] text-ink-2">De kweker helpt u persoonlijk, ma–za 09:00–17:00.</p></div>
      <div className="flex gap-2"><Button href={company.whatsapp} {...ext} variant="moss" size="sm"><WhatsAppIcon className="size-4" />WhatsApp</Button><Button href={company.phone1Href} variant="outline" size="sm"><Phone className="size-4" aria-hidden="true" />Bel</Button></div>
    </div>
  )
}
function Kenmerken({ rows }: { rows: [string, string][] }) {
  return <dl className="grid grid-cols-1 gap-2 sm:grid-cols-2">{rows.map(([k, v]) => <div key={k} className="grid grid-cols-[120px_1fr] gap-3 rounded-[10px] bg-surface px-4 py-3 text-[14.5px]"><dt className="text-muted">{k}</dt><dd className="font-medium text-ink">{v}</dd></div>)}</dl>
}

/** Sticky buy bar on phones: shows when the main CTA has scrolled out of view. */
function StickyBar({ price, label, onAdd, watch }: { price: number; label: string; onAdd: () => void; watch: React.RefObject<HTMLElement> }) {
  const [show, setShow] = useState(false)
  useEffect(() => {
    const el = watch.current; if (!el) return
    const footer = document.querySelector('footer')
    let past = false, foot = false
    const upd = () => setShow(past && !foot)
    const io = new IntersectionObserver(([e]) => { past = !e.isIntersecting && e.boundingClientRect.top < 0; upd() }, { threshold: 0 })
    const io2 = new IntersectionObserver(([e]) => { foot = e.isIntersecting; upd() }, { threshold: 0 })
    io.observe(el); if (footer) io2.observe(footer)
    return () => { io.disconnect(); io2.disconnect() }
  }, [watch])
  return (
    <div aria-hidden={!show} className={cn('fixed inset-x-0 bottom-0 z-40 border-t border-line bg-bg/95 px-4 py-3 backdrop-blur transition-transform duration-300 lg:hidden', show ? 'translate-y-0' : 'translate-y-full')} style={{ paddingBottom: 'max(12px, env(safe-area-inset-bottom))' }}>
      <div className="flex items-center justify-between gap-4"><div><p className="text-[13px] text-muted">{label}</p><p className="num text-[20px] font-semibold leading-tight">{fmtEur(price)}</p></div><Button as="button" variant="solid" size="md" onClick={onAdd} tabIndex={show ? 0 : -1}>In winkelwagen</Button></div>
    </div>
  )
}

function PlantView({ v }: { v: Variety }) {
  const [size, setSize] = useState(0)
  const [qty, setQty] = useState(1)
  const [turf, setTurf] = useState(false)
  const [added, setAdded] = useState(false)
  const ctaRef = useRef<HTMLDivElement>(null)
  useEffect(() => { setSize(0); setQty(1); setTurf(false); setAdded(false) }, [v.slug])
  const s = v.sizes[size]
  const total = parsePrice(s.price) * qty + (turf ? parsePrice(tuinturf.price) : 0)
  const others = ordered.filter((x) => x.slug !== v.slug)
  function add() {
    addToCart({ slug: v.slug, name: v.name, size: s.label, price: s.price, qty, image: `${v.slug}-sm` })
    if (turf) addToCart({ slug: tuinturf.slug, name: tuinturf.name, size: 'zak 40 L', price: tuinturf.price, qty: 1, image: 'tuinturf-sm' })
    setAdded(true); openCart()
  }
  return (
    <>
      <div className="wrap container-x flex flex-col gap-4 pb-5 pt-5"><Breadcrumb name={v.name} /><Switcher current={v.slug} /></div>
      <section className="wrap container-x grid grid-cols-1 gap-8 pb-14 lg:grid-cols-12 lg:gap-14">
        <div className="lg:col-span-7"><Gallery photos={[{ name: `${v.slug}-2`, alt: `Rhododendron ${v.name}, volle struik in bloei` }, { name: v.slug, alt: `Rhododendron ${v.name}, bloemtros van dichtbij` }]} /></div>
        <div className="lg:col-span-5">
          <div className="lg:sticky lg:top-24">
            <p className="flex items-center gap-2 text-[14px] font-medium text-ink-2"><Swatch hex={v.hex} light={v.light} />Rhododendron · {v.color}</p>
            <h1 className="title mt-2 text-[clamp(34px,4.4vw,56px)]">{v.name}</h1>
            <p className="mt-2 text-[14.5px] text-muted">{v.bloei} · {v.hoogte} · {v.standplaats.split(',')[0]} · winterhard</p>
            <p className="mt-4 text-[15.5px] leading-relaxed text-ink-2">{v.short}</p>

            <fieldset className="mt-6">
              <legend className="label mb-3 text-ink-2">Kies uw maat <span className="font-normal text-muted">(hoogte bij levering)</span></legend>
              <div className="grid grid-cols-2 gap-2">
                {v.sizes.map((x, i) => (
                  <button key={x.label} type="button" onClick={() => { setSize(i); setAdded(false) }} aria-pressed={size === i} className={cn('flex items-center justify-between rounded-field px-4 py-3 text-left text-[14.5px] font-medium transition-colors', size === i ? 'bg-night text-white' : 'bg-surface ring-1 ring-ink/20 hover:ring-ink/50')}>
                    <span>{x.label}</span><span className="num font-semibold">€ {x.price.replace(',00', ',–')}</span>
                  </button>
                ))}
              </div>
            </fieldset>

            <div className="mt-4 flex flex-wrap items-center gap-4">
              <Quantity value={qty} onChange={(n) => { setQty(n); setAdded(false) }} />
              <p className="text-[14px] text-ink-2">Totaal <span className="num ml-1 text-[26px] font-semibold tracking-[-0.02em] text-ink">{fmtEur(total)}</span></p>
            </div>

            <div className={cn('mt-4 rounded-img p-4 transition-colors', turf ? 'bg-moss/10 ring-1 ring-moss' : 'bg-surface')}>
              <Checkbox id="turf" checked={turf} onChange={(x) => { setTurf(x); setAdded(false) }}>
                <span className="flex items-start gap-3">
                  <img src={img('tuinturf-sm')} alt="" className="size-14 shrink-0 rounded-[10px] object-cover" />
                  <span><span className="block text-[14.5px] font-semibold">Vergeet de Tuinturf niet <span className="num font-medium text-muted">(+ € {tuinturf.price}, zak 40 L)</span></span><span className="mt-0.5 block text-[13.5px] leading-relaxed text-ink-2">{tuinturf.upsell}</span></span>
                </span>
              </Checkbox>
            </div>

            <div ref={ctaRef} className="mt-4 flex flex-col gap-3 sm:flex-row">
              <Button as="button" variant="solid" size="lg" onClick={add} className="w-full sm:flex-1">{added ? <><Check className="size-4" /> Toegevoegd aan winkelwagen</> : 'In winkelwagen'}</Button>
            </div>
            <div className="mt-4"><Helper /></div>
            <div className="mt-5"><TrustLines items={[[ShieldCheck, 'Aangroeigarantie op al onze planten'], [Truck, 'Eigen transport door heel Nederland'], [Scissors, 'Dagvers gerooid bij uw bestelling']]} /></div>
            <p className="mt-4 text-[12.5px] text-muted">Demo: de winkelwagen is in de mockup nog niet gekoppeld aan een afrekenpagina.</p>
          </div>
        </div>
      </section>
      <StickyBar price={total} label={`${v.name} · ${s.label} × ${qty}`} onAdd={add} watch={ctaRef} />

      <section className="bg-bg-2 py-14 md:py-20">
        <div className="wrap container-x grid grid-cols-1 gap-10 lg:grid-cols-12 lg:gap-14">
          <Reveal className="lg:col-span-7">
            <SectionHead size="sm" title={`Over ${v.name}`} />
            <p className="mt-4 max-w-[62ch] text-[16px] leading-relaxed text-ink-2">{v.long}</p>
            <h3 className="mt-8 text-[20px] font-semibold">Kenmerken</h3>
            <div className="mt-4"><Kenmerken rows={kenmerken(v)} /></div>
          </Reveal>
          <Reveal index={1} className="lg:col-span-5">
            <SectionHead size="sm" title={`Bloeit in ${v.bloei.toLowerCase()}`} text="Planten kan het hele jaar door, behalve tijdens vorstperiodes; maart–april en september–oktober zijn ideaal." />
            <div className="mt-6 rounded-img bg-surface p-4"><BloomCalendar rows={[v]} compact dark={false} /><BloomLegend className="mt-4" dark={false} /></div>
            <a href="plantgids.html" className="mt-4 inline-block text-[14px] font-medium underline underline-offset-4">Alle soorten vergelijken in de plantgids</a>
          </Reveal>
        </div>
      </section>

      <section className="wrap container-x py-14 md:py-20">
        <Reveal className="flex flex-col gap-5 rounded-panel bg-moss p-6 text-white on-dark md:flex-row md:items-center md:justify-between md:p-8">
          <div><p className="label text-white/65">Voor hoveniers en grootverbruikers</p><p className="mt-1.5 text-[22px] font-semibold leading-tight tracking-[-0.01em] md:text-[26px]">Vanaf 25 stuks bieden wij scherpe partijprijzen, eigen transport en plantservice.</p></div>
          <Button href="groothandel.html" variant="white" size="md" arrow className="shrink-0">Bekijk groothandel-condities</Button>
        </Reveal>
      </section>

      <section className="wrap container-x pb-24 md:pb-28">
        <Reveal className="flex items-end justify-between gap-6"><SectionHead size="sm" title="Andere soorten" /><a href="assortiment.html" className="hidden text-[14px] font-medium underline underline-offset-4 sm:inline">Alle soorten</a></Reveal>
        <div className="mt-6 grid grid-cols-2 gap-x-4 gap-y-8 md:grid-cols-3 lg:grid-cols-6">
          {others.map((o) => <VarietyCard key={o.slug} v={o} href={`#${o.slug}`} compact sizes="(min-width: 1024px) 16vw, (min-width: 768px) 33vw, 50vw" />)}
        </div>
        <a href="assortiment.html" className="mt-10 inline-flex items-center gap-2 text-[14.5px] font-medium text-ink-2 hover:text-ink"><ArrowLeft className="size-4" aria-hidden="true" />Terug naar assortiment</a>
      </section>
    </>
  )
}

function TurfView() {
  const [qty, setQty] = useState(1)
  const [added, setAdded] = useState(false)
  const ctaRef = useRef<HTMLDivElement>(null)
  const t = tuinturf
  const add = () => { addToCart({ slug: t.slug, name: t.name, size: 'zak 40 L', price: t.price, qty, image: 'tuinturf-sm' }); setAdded(true); openCart() }
  return (
    <>
      <div className="wrap container-x flex flex-col gap-4 pb-5 pt-5"><Breadcrumb name={t.name} /><Switcher current={t.slug} /></div>
      <section className="wrap container-x grid grid-cols-1 gap-8 pb-14 lg:grid-cols-12 lg:gap-14">
        <div className="lg:col-span-7"><Gallery photos={[{ name: 'tuinturf', alt: t.fullName }]} /></div>
        <div className="lg:col-span-5">
          <p className="text-[14px] font-medium text-ink-2">Accessoire</p>
          <h1 className="title mt-2 text-[clamp(32px,4vw,52px)]">{t.fullName}</h1>
          <p className="mt-4 text-[15.5px] leading-relaxed text-ink-2">{t.short}</p>
          <p className="mt-3 text-[15.5px] leading-relaxed text-ink-2">{t.long}</p>
          <p className="num mt-6 text-[28px] font-semibold tracking-[-0.02em]">€ {t.price} <span className="text-[14px] font-medium text-muted">{t.unit}</span></p>
          <div className="mt-4 flex flex-wrap items-center gap-4"><Quantity value={qty} onChange={(n) => { setQty(n); setAdded(false) }} /><p className="text-[14px] text-ink-2">Totaal <span className="num ml-1 text-[26px] font-semibold text-ink">{fmtEur(parsePrice(t.price) * qty)}</span></p></div>
          <div ref={ctaRef} className="mt-4 flex flex-col gap-3 sm:flex-row">
            <Button as="button" variant="solid" size="lg" onClick={add} className="w-full sm:flex-1">{added ? <><Check className="size-4" /> Toegevoegd</> : 'In winkelwagen'}</Button>
            <Button href="assortiment.html" variant="outline" size="lg" className="w-full sm:w-auto">Naar de planten</Button>
          </div>
          <div className="mt-4"><Helper /></div>
          <div className="mt-5"><TrustLines items={[[ShieldCheck, t.points[0]], [Truck, t.points[1]], [Scissors, t.points[2]]]} /></div>
          <p className="mt-4 text-[12.5px] text-muted">Demo: de winkelwagen is in de mockup nog niet gekoppeld aan een afrekenpagina.</p>
        </div>
      </section>
      <StickyBar price={parsePrice(t.price) * qty} label={`${t.name} × ${qty}`} onAdd={add} watch={ctaRef} />
      <section className="bg-bg-2 py-14 md:py-20">
        <div className="wrap container-x max-w-[900px]"><SectionHead size="sm" title="Kenmerken" /><div className="mt-6"><Kenmerken rows={t.kenmerken} /></div></div>
      </section>
      <section className="wrap container-x py-14 pb-24 md:py-20 md:pb-28">
        <Reveal><SectionHead size="sm" title="De rhododendrons" /></Reveal>
        <div className="mt-6 grid grid-cols-2 gap-x-4 gap-y-8 md:grid-cols-4 lg:grid-cols-7">
          {ordered.map((o) => <VarietyCard key={o.slug} v={o} href={`#${o.slug}`} compact sizes="(min-width: 1024px) 14vw, (min-width: 768px) 25vw, 50vw" />)}
        </div>
      </section>
    </>
  )
}

function NotFound({ slug }: { slug: string }) {
  return (
    <section className="wrap container-x py-10 md:py-16">
      <Breadcrumb name="Niet gevonden" />
      <div className="mt-8 rounded-panel bg-surface p-8 md:p-12">
        <h1 className="title text-[clamp(30px,4vw,48px)]">Soort niet gevonden.</h1>
        <p className="mt-3 max-w-[50ch] text-[16px] text-ink-2">«{slug}» kennen wij niet. Kies hieronder een van onze zeven soorten, of ga naar het assortiment.</p>
        <div className="mt-8"><Switcher current="" /></div>
        <Button href="assortiment.html" variant="outline" size="md" arrow className="mt-8">Naar het assortiment</Button>
      </div>
    </section>
  )
}

export default function Product() {
  const slug = productSlug.use() || 'nova-zembla'
  const v = bySlug(slug)
  const isTurf = slug === tuinturf.slug
  const name = isTurf ? tuinturf.fullName : v?.name
  useEffect(() => { document.title = name ? `${isTurf ? name : `Rhododendron ${name}`} kopen · Top Rhododendrons` : 'Soort niet gevonden · Top Rhododendrons' }, [name, isTurf])
  return (
    <>
      <a href="#main" className="skip-link">Naar de inhoud</a>
      <SiteHeader page="product" />
      <main id="main" className="pt-16 md:pt-20">
        {isTurf ? <TurfView /> : v ? <PlantView v={v} /> : <NotFound slug={slug} />}
      </main>
      <SiteFooter />
      <CartDrawer />
      <Toast />
    </>
  )
}
