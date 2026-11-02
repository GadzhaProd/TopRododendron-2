import { useMemo, useState } from 'react'
import { Check, SlidersHorizontal, X } from 'lucide-react'
import { SiteHeader } from '@/components/site-header'
import { SiteFooter } from '@/components/site-footer'
import { CartDrawer } from '@/components/cart-drawer'
import { Toast } from '@/components/toast'
import { Button } from '@/components/button'
import { Reveal } from '@/components/reveal'
import { SectionHead, Swatch } from '@/components/section-head'
import { Select } from '@/components/fields'
import { cn } from '@/lib/utils'
import { addToCart, openCart } from '@/lib/store'
import { varieties, popularOrder, filters, tuinturf, img, srcset, company, type Variety } from '@/data/content'

type Facet = keyof typeof filters
type Sel = Record<Facet, string[]>
const empty: Sel = { kleur: [], standplaats: [], hoogte: [], geschikt: [] }
const facetLabel: Record<Facet, string> = { kleur: 'Bloemkleur', standplaats: 'Standplaats', hoogte: 'Max. hoogte', geschikt: 'Geschikt voor' }
const sorts = [
  { v: 'populair', l: 'Populair' }, { v: 'naam', l: 'Naam A–Z' }, { v: 'prijs', l: 'Prijs, laag–hoog' }, { v: 'prijs-desc', l: 'Prijs, hoog–laag' }, { v: 'bloei', l: 'Vroegste bloei' }, { v: 'hoogte', l: 'Hoogte, laag–hoog' },
]
const matches = (v: Variety, sel: Sel) =>
  (!sel.kleur.length || sel.kleur.some((k) => v.kleurFilter.includes(k))) &&
  (!sel.standplaats.length || sel.standplaats.some((k) => v.standplaatsFilter.includes(k))) &&
  (!sel.hoogte.length || sel.hoogte.includes(v.hoogteFilter)) &&
  (!sel.geschikt.length || sel.geschikt.some((k) => v.geschiktVoor.includes(k)))

/** Filter chips (pattern: 21st.dev "Chip Group" 35042) — real toggle buttons. */
function Chips({ facet, sel, onToggle }: { facet: Facet; sel: Sel; onToggle: (f: Facet, v: string) => void }) {
  return (
    <div role="group" aria-label={facetLabel[facet]} className="flex flex-col gap-2">
      <span className="label text-muted">{facetLabel[facet]}</span>
      <div className="flex flex-wrap gap-2">
        {filters[facet].map((o) => {
          const on = sel[facet].includes(o)
          return (
            <button key={o} type="button" aria-pressed={on} onClick={() => onToggle(facet, o)} className={cn('inline-flex h-10 items-center gap-1.5 rounded-full px-3.5 text-[14px] font-medium transition-colors', on ? 'bg-night text-white' : 'bg-surface text-ink ring-1 ring-ink/20 hover:ring-ink/50')}>
              {on && <Check className="size-3.5" strokeWidth={2.5} aria-hidden="true" />}{o}
            </button>
          )
        })}
      </div>
    </div>
  )
}

export default function Assortiment() {
  const [sel, setSel] = useState<Sel>(empty)
  const [sort, setSort] = useState('populair')
  const [showFilters, setShowFilters] = useState(false)
  const [turfAdded, setTurfAdded] = useState(false)
  const toggle = (f: Facet, v: string) => setSel((s) => ({ ...s, [f]: s[f].includes(v) ? s[f].filter((x) => x !== v) : [...s[f], v] }))
  const active = Object.values(sel).reduce((n, a) => n + a.length, 0)
  const list = useMemo(() => {
    const base = popularOrder.map((s) => varieties.find((v) => v.slug === s)!).filter((v) => matches(v, sel))
    const p = (v: Variety) => parseFloat(v.from)
    switch (sort) {
      case 'naam': return [...base].sort((a, b) => a.name.localeCompare(b.name, 'nl'))
      case 'prijs': return [...base].sort((a, b) => p(a) - p(b))
      case 'prijs-desc': return [...base].sort((a, b) => p(b) - p(a))
      case 'bloei': return [...base].sort((a, b) => a.bloeiStart - b.bloeiStart)
      case 'hoogte': return [...base].sort((a, b) => a.hoogteNum - b.hoogteNum)
      default: return base
    }
  }, [sel, sort])

  return (
    <>
      <a href="#main" className="skip-link">Naar de inhoud</a>
      <SiteHeader page="assortiment" />
      <main id="main" className="pt-[68px] md:pt-20">
        <section className="bg-night text-white on-dark">
          <div className="wrap container-x py-12 md:py-20">
            <SectionHead dark as="h1" size="xl" title="Alle rhododendrons." text={`${varieties.length} variëteiten op voorraad, in vier maten van 40 tot 120 cm. Dagvers gerooid bij uw bestelling, rechtstreeks vanaf onze kwekerij in Otterlo. Geen minimumbestelling.`} />
          </div>
        </section>

        {/* Filters */}
        <section aria-label="Filteren en sorteren" className="wrap container-x pt-6 md:pt-10">
          <div className="flex flex-wrap items-center justify-between gap-3">
            <button type="button" onClick={() => setShowFilters((s) => !s)} aria-expanded={showFilters} aria-controls="filters" className="inline-flex h-11 items-center gap-2 rounded-ui bg-surface px-4 text-[14.5px] font-semibold ring-1 ring-ink/20 md:hidden"><SlidersHorizontal className="size-4" aria-hidden="true" />Filters{active > 0 && <span className="num grid size-5 place-items-center rounded-full bg-night text-[11px] text-white">{active}</span>}</button>
            <p className="text-[14.5px] text-ink-2"><span role="status" aria-live="polite"><span className="num font-semibold text-ink">{list.length}</span> van {varieties.length} soorten</span>{active > 0 && <button type="button" onClick={() => setSel(empty)} className="ml-4 inline-flex items-center gap-1 font-medium underline underline-offset-4"><X className="size-3.5" aria-hidden="true" />Wis filters</button>}</p>
            <label className="flex items-center gap-3 text-[14px] text-ink-2"><span className="shrink-0">Sorteer op</span><Select value={sort} onChange={(e) => setSort(e.target.value)} className="h-11 w-[200px] text-[14px]" aria-label="Sorteren">{sorts.map((s) => <option key={s.v} value={s.v}>{s.l}</option>)}</Select></label>
          </div>
          <div id="filters" className={cn('mt-5 grid grid-cols-1 gap-5 rounded-panel bg-surface p-5 md:grid md:grid-cols-2 md:p-6 xl:grid-cols-4', showFilters ? 'grid' : 'hidden md:grid')}>
            {(Object.keys(filters) as Facet[]).map((f) => <Chips key={f} facet={f} sel={sel} onToggle={toggle} />)}
          </div>
        </section>

        {/* Grid */}
        <section className="wrap container-x py-10 md:py-14">
          {list.length === 0 ? (
            <div className="rounded-panel bg-surface px-6 py-16 text-center"><p className="text-[24px] font-semibold">Geen soort voldoet aan deze combinatie.</p><p className="mt-2 text-ink-2">Probeer een filter minder, of bel ons: wij denken graag mee.</p><Button as="button" variant="outline" className="mt-6" onClick={() => setSel(empty)}>Wis filters</Button></div>
          ) : (
            <ol className="grid grid-cols-1 gap-6 lg:grid-cols-2 lg:gap-8">
              {list.map((v, i) => (
                <Reveal as="li" key={v.slug} index={i % 2} className="overflow-hidden rounded-panel bg-surface">
                  <a href={`product.html#${v.slug}`} className="group/i relative block" aria-label={`${v.name} bekijken`}>
                    <div className="aspect-[4/3] overflow-hidden bg-bg-2"><img src={img(`${v.slug}-2`)} srcSet={srcset(`${v.slug}-2`)} sizes="(min-width: 1024px) 50vw, 100vw" alt={`Rhododendron ${v.name}, volle struik in bloei`} loading={i < 2 ? 'eager' : 'lazy'} className="h-full w-full object-cover img-treat transition-transform duration-[1000ms] ease-[cubic-bezier(.22,1,.36,1)] group-hover/i:scale-[1.03]" /></div>
                    <img src={img(`${v.slug}-sm`)} alt={`${v.name}, bloemtros van dichtbij`} loading="lazy" className="absolute bottom-4 right-4 aspect-square w-[26%] max-w-[120px] rounded-[12px] border-[3px] border-surface object-cover shadow-md" />
                  </a>
                  <div className="p-5 md:p-6">
                    <div className="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-1">
                      <h2 className="text-[26px] font-semibold tracking-[-0.02em] leading-tight md:text-[30px]">{v.name}</h2>
                      <p className="num text-[15px] text-ink-2">vanaf <span className="font-semibold text-ink">€ {v.from},–</span></p>
                    </div>
                    <p className="mt-2 flex flex-wrap items-center gap-x-2 gap-y-1 text-[14px] text-muted"><Swatch hex={v.hex} light={v.light} />{v.color}<span aria-hidden="true">·</span>{v.bloei}<span aria-hidden="true">·</span>{v.hoogte}<span aria-hidden="true">·</span>{v.standplaats.split(',')[0]}</p>
                    <p className="mt-3 max-w-[60ch] text-[15px] leading-relaxed text-ink-2">{v.short}</p>
                    <dl className="mt-5 grid grid-cols-2 gap-2 sm:grid-cols-4">
                      {v.sizes.map((s) => <div key={s.label} className="rounded-[10px] bg-bg px-3 py-2"><dt className="text-[12px] font-medium text-muted">{s.label}</dt><dd className="num text-[16px] font-semibold">€ {s.price.replace(',00', ',–')}</dd></div>)}
                    </dl>
                    <div className="mt-5 flex flex-wrap items-center gap-4">
                      <Button href={`product.html#${v.slug}`} variant="solid" size="md" arrow>Bekijk en bestel</Button>
                      <a href="plantgids.html#vergelijken" className="text-[14px] font-medium text-ink-2 underline underline-offset-4 hover:text-ink">Vergelijk in de plantgids</a>
                    </div>
                  </div>
                </Reveal>
              ))}
            </ol>
          )}
        </section>

        {/* Toebehoren */}
        <section className="wrap container-x pb-10 md:pb-14">
          <Reveal className="grid grid-cols-1 items-center gap-6 overflow-hidden rounded-panel bg-moss text-white on-dark md:grid-cols-12">
            <div className="md:col-span-5"><div className="aspect-[4/3] md:aspect-auto md:h-full"><img src={img('tuinturf')} srcSet={srcset('tuinturf')} sizes="(min-width: 768px) 40vw, 100vw" alt="Tuinturf-substraat" loading="lazy" className="h-full w-full object-cover img-treat" /></div></div>
            <div className="p-6 md:col-span-7 md:py-10 md:pr-10">
              <p className="label text-white/65">Toebehoren · voor optimale aanslag</p>
              <h2 className="title mt-2 text-[clamp(26px,3vw,38px)]">{tuinturf.fullName}</h2>
              <p className="mt-3 max-w-[56ch] text-[15px] leading-relaxed text-white/80">{tuinturf.short} {tuinturf.upsell}</p>
              <p className="num mt-5 text-[26px] font-semibold">€ {tuinturf.price} <span className="text-[14px] font-medium text-white/65">{tuinturf.unit}</span></p>
              <div className="mt-5 flex flex-wrap gap-3">
                <Button as="button" variant="white" size="md" onClick={() => { addToCart({ slug: tuinturf.slug, name: tuinturf.name, size: 'zak 40 L', price: tuinturf.price, qty: 1, image: 'tuinturf-sm' }); setTurfAdded(true); openCart() }}>{turfAdded ? <><Check className="size-4" /> Toegevoegd</> : 'Voeg Tuinturf toe'}</Button>
                <Button href={`product.html#${tuinturf.slug}`} variant="outline-white" size="md" arrow>Kenmerken</Button>
              </div>
            </div>
          </Reveal>
        </section>

        {/* B2B strip */}
        <section className="wrap container-x pb-16 md:pb-24">
          <Reveal className="flex flex-col gap-6 rounded-panel bg-surface p-6 md:flex-row md:items-center md:justify-between md:p-8">
            <div><p className="label text-muted">Voor hoveniers en grootverbruikers</p><p className="mt-1.5 text-[22px] font-semibold tracking-[-0.01em] leading-tight md:text-[26px]">Vanaf 25 stuks: scherpe partijprijzen, eigen transport en plantservice.</p><p className="mt-2 text-[14.5px] text-ink-2">Of bel direct: <a href={company.phone1Href} className="num font-semibold underline underline-offset-4">{company.phone1}</a>.</p></div>
            <Button href="groothandel.html" variant="solid" size="lg" arrow className="shrink-0">Naar groothandel</Button>
          </Reveal>
        </section>
      </main>
      <SiteFooter />
      <CartDrawer />
      <Toast />
    </>
  )
}
