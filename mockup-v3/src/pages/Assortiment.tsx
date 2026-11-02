import { useMemo, useState } from 'react'
import { Check, X } from 'lucide-react'
import { SiteHeader } from '@/components/site-header'
import { SiteFooter } from '@/components/site-footer'
import { CartDrawer } from '@/components/cart-drawer'
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
      <span className="eyebrow text-muted">{facetLabel[facet]}</span>
      <div className="flex flex-wrap gap-2">
        {filters[facet].map((o) => {
          const on = sel[facet].includes(o)
          return (
            <button key={o} type="button" aria-pressed={on} onClick={() => onToggle(facet, o)} className={cn('inline-flex h-9 items-center gap-1.5 rounded-ui border px-3 text-[13.5px] transition-colors', on ? 'border-ink bg-ink text-paper' : 'border-ink/50 bg-surface text-ink hover:border-ink')}>
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
      <SiteHeader current="assortiment" />
      <main id="main" className="pt-16 md:pt-[76px]">
        <section className="border-b border-line bg-paper-2">
          <div className="wrap container-x py-14 md:py-20">
            <SectionHead as="h1" size="xl" eyebrow="Assortiment · Otterlo, sinds 2001" title="Alle rhododendrons." text={`${varieties.length} variëteiten op voorraad, in vier maten van 40 tot 120 cm. Vers gerooid bij uw bestelling, rechtstreeks van onze kwekerij in Otterlo. Geen minimumbestelling, aangroeigarantie op elke plant.`} />
          </div>
        </section>

        {/* Filters */}
        <section aria-label="Filteren en sorteren" className="wrap container-x pt-10 md:pt-12">
          <div className="grid grid-cols-1 gap-6 md:grid-cols-2 xl:grid-cols-4">
            {(Object.keys(filters) as Facet[]).map((f) => <Chips key={f} facet={f} sel={sel} onToggle={toggle} />)}
          </div>
          <div className="mt-8 flex flex-col gap-4 border-y border-line py-4 sm:flex-row sm:items-center sm:justify-between">
            <p className="text-[14.5px] text-ink-2" role="status" aria-live="polite">
              <span className="num font-medium text-ink">{list.length}</span> van {varieties.length} soorten
              {active > 0 && <button type="button" onClick={() => setSel(empty)} className="ml-4 inline-flex items-center gap-1 underline underline-offset-4"><X className="size-3.5" aria-hidden="true" />Wis filters</button>}
            </p>
            <label className="flex items-center gap-3 text-[14px] text-ink-2"><span className="shrink-0">Sorteer op</span><Select value={sort} onChange={(e) => setSort(e.target.value)} className="h-10 w-[220px] text-[14px]" aria-label="Sorteren">{sorts.map((s) => <option key={s.v} value={s.v}>{s.l}</option>)}</Select></label>
          </div>
        </section>

        {/* List */}
        <section className="wrap container-x">
          {list.length === 0 ? (
            <div className="py-20 text-center"><p className="font-display text-[26px]">Geen soort voldoet aan deze combinatie.</p><p className="mt-2 text-ink-2">Probeer een filter minder, of bel ons: wij denken graag mee.</p><Button as="button" variant="outline" className="mt-6" onClick={() => setSel(empty)}>Wis filters</Button></div>
          ) : (
            <ol>
              {list.map((v, i) => (
                <Reveal as="li" key={v.slug} className="border-b border-line py-12 last:border-b-0 md:py-16">
                  <article className={cn('grid grid-cols-1 gap-8 lg:grid-cols-12 lg:gap-14', i % 2 === 1 && 'lg:[&>*:first-child]:order-2')}>
                    <a href={`product.html#${v.slug}`} className="group/i relative block lg:col-span-6" aria-label={`${v.name} bekijken`}>
                      <div className="aspect-[4/3] overflow-hidden rounded-img bg-paper-2"><img src={img(`${v.slug}-2`)} srcSet={srcset(`${v.slug}-2`)} sizes="(min-width: 1024px) 50vw, 100vw" alt={`Rhododendron ${v.name}, volle struik in bloei`} loading={i === 0 ? 'eager' : 'lazy'} className="h-full w-full object-cover img-treat transition-transform duration-[1000ms] ease-[cubic-bezier(.22,1,.36,1)] group-hover/i:scale-[1.03]" /></div>
                      <img src={img(`${v.slug}-sm`)} alt={`${v.name}, bloemtros van dichtbij`} loading="lazy" className="absolute -bottom-4 left-4 w-[28%] max-w-[150px] rounded-img border-[3px] border-paper object-cover shadow-md aspect-square" />
                    </a>
                    <div className="lg:col-span-6 lg:py-2">
                      <p className="num eyebrow text-bloom">{String(i + 1).padStart(2, '0')} · Rhododendron</p>
                      <h2 className="mt-3 font-display text-[clamp(30px,3.4vw,42px)] leading-[1.05]" style={{ fontVariationSettings: '"opsz" 72' }}>{v.name}</h2>
                      <p className="mt-3 flex flex-wrap items-center gap-x-2 gap-y-1 text-[14px] text-muted"><Swatch hex={v.hex} light={v.light} />{v.color}<span aria-hidden="true">·</span>{v.bloei}<span aria-hidden="true">·</span>{v.hoogte}<span aria-hidden="true">·</span>{v.standplaats.split(',')[0]}</p>
                      <p className="mt-5 max-w-[56ch] text-[16px] leading-relaxed text-ink-2">{v.long}</p>
                      <dl className="mt-7 grid grid-cols-2 gap-x-6 gap-y-4 border-t border-line pt-5 sm:grid-cols-4">
                        {v.sizes.map((s) => <div key={s.label}><dt className="text-[12px] uppercase tracking-[0.12em] text-muted">{s.label}</dt><dd className="num mt-1 font-display text-[22px]">€ {s.price.replace(',00', ',–')}</dd></div>)}
                      </dl>
                      <div className="mt-7 flex flex-wrap items-center gap-4">
                        <Button href={`product.html#${v.slug}`} variant="solid" size="md" arrow>Bekijk en bestel</Button>
                        <a href="plantgids.html#vergelijken" className="text-[14px] text-ink-2 underline underline-offset-4 hover:text-ink">Vergelijk in de plantgids</a>
                      </div>
                    </div>
                  </article>
                </Reveal>
              ))}
            </ol>
          )}
        </section>

        {/* Toebehoren */}
        <section className="bg-paper-2 py-16 md:py-24">
          <div className="wrap container-x grid grid-cols-1 items-center gap-8 lg:grid-cols-12 lg:gap-14">
            <Reveal className="lg:col-span-5"><div className="aspect-[4/3] overflow-hidden rounded-img"><img src={img('tuinturf')} srcSet={srcset('tuinturf')} sizes="(min-width: 1024px) 40vw, 100vw" alt="Tuinturf-substraat" loading="lazy" className="h-full w-full object-cover img-treat" /></div></Reveal>
            <Reveal index={1} className="lg:col-span-7">
              <SectionHead eyebrow="Toebehoren · voor optimale aanslag" title={tuinturf.fullName} text={tuinturf.short} />
              <p className="mt-4 max-w-[56ch] text-[15px] leading-relaxed text-ink-2">{tuinturf.upsell}</p>
              <p className="num mt-6 font-display text-[28px]">€ {tuinturf.price} <span className="font-body text-[14px] text-muted">{tuinturf.unit}</span></p>
              <div className="mt-6 flex flex-wrap gap-3">
                <Button as="button" variant="solid" size="md" onClick={() => { addToCart({ slug: tuinturf.slug, name: tuinturf.name, size: 'zak 40 L', price: tuinturf.price, qty: 1, image: 'tuinturf-sm' }); setTurfAdded(true); openCart() }}>{turfAdded ? <><Check className="size-4" /> Toegevoegd</> : 'In winkelwagen'}</Button>
                <Button href={`product.html#${tuinturf.slug}`} variant="outline" size="md" arrow>Kenmerken</Button>
              </div>
            </Reveal>
          </div>
        </section>

        {/* B2B strip */}
        <section className="wrap container-x py-16 md:py-20">
          <Reveal className="flex flex-col gap-6 rounded-img border border-line bg-surface p-7 md:flex-row md:items-center md:justify-between md:p-9">
            <div><p className="eyebrow text-bloom">Voor professionals</p><p className="mt-2 font-display text-[24px] leading-tight md:text-[28px]">Hovenier, gemeente of projectontwikkelaar? Partijprijzen vanaf 25 stuks.</p><p className="mt-2 text-[14.5px] text-ink-2">10.000 planten op stam, eigen transport, plantpaspoort, factuur op 30 dagen. Of bel direct: <a href={company.phone1Href} className="num underline underline-offset-4">{company.phone1}</a>.</p></div>
            <Button href="groothandel.html" variant="ink" size="lg" arrow className="shrink-0">Naar groothandel</Button>
          </Reveal>
        </section>
      </main>
      <SiteFooter />
      <CartDrawer />
    </>
  )
}
