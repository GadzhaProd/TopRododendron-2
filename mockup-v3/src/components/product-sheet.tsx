// Product sheet of concept C: the screen that follows a click on a variety on the
// homepage. A modal dialog with the two real photos, facts, size choice with the
// real price list, quantity, "In winkelwagen" (the v3 cart) and the delivery /
// guarantee facts next to the button, plus a link to the full product page.
import { useEffect, useRef, useState } from 'react'
import { AnimatePresence, motion, useReducedMotion } from 'framer-motion'
import { X, Minus, Plus, Check, ArrowRight } from 'lucide-react'
import { cn, lockPage, trapTab, rememberFocus } from '@/lib/utils'
import { Button } from './button'
import { sheetStore, closeSheet, addToCart } from '@/lib/store'
import { varieties, img, srcset, company, parsePrice, fmtEur } from '@/data/content'

export function ProductSheet() {
  const slug = sheetStore.use()
  const v = varieties.find((x) => x.slug === slug)
  const reduce = useReducedMotion()
  const [size, setSize] = useState(0)
  const [qty, setQty] = useState(1)
  const [added, setAdded] = useState(false)
  const closeRef = useRef<HTMLButtonElement>(null)
  const panelRef = useRef<HTMLDivElement>(null)

  useEffect(() => { setSize(0); setQty(1); setAdded(false) }, [slug])
  useEffect(() => {
    if (!v) return
    const restore = rememberFocus()
    lockPage(true)
    closeRef.current?.focus()
    const onKey = (e: KeyboardEvent) => { if (e.key === 'Escape') closeSheet(); trapTab(e, panelRef.current) }
    document.addEventListener('keydown', onKey)
    return () => { lockPage(false); document.removeEventListener('keydown', onKey); restore() }
  }, [v])

  const price = v ? parsePrice(v.sizes[size].price) * qty : 0
  const line = 'border-fg/12'

  return (
    <AnimatePresence>
      {v && (
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} transition={{ duration: reduce ? 0 : 0.2 }} className="fixed inset-0 z-[70] flex items-end justify-center bg-black/55 p-0 md:items-center md:p-6" onClick={(e) => { if (e.target === e.currentTarget) closeSheet() }}>
          <motion.div
            ref={panelRef} role="dialog" aria-modal="true" aria-labelledby="sheet-title"
            initial={reduce ? false : { y: 40, opacity: 0 }} animate={{ y: 0, opacity: 1 }} exit={reduce ? undefined : { y: 40, opacity: 0 }} transition={{ duration: 0.35, ease: [0.22, 1, 0.36, 1] }}
            className="relative grid max-h-[94svh] w-full max-w-5xl grid-cols-1 overflow-y-auto rounded-t-img bg-surface text-fg md:grid-cols-2 md:rounded-img"
          >
            <button ref={closeRef} type="button" onClick={closeSheet} aria-label="Sluiten" className="absolute right-4 top-4 z-10 grid size-11 place-items-center rounded-full border border-fg/20 bg-surface/80 text-fg backdrop-blur"><X className="size-5" /></button>
            <div className="grid grid-cols-2 gap-1 md:grid-cols-1">
              <img src={img(`${v.slug}-2`)} srcSet={srcset(`${v.slug}-2`)} sizes="(min-width: 768px) 40vw, 50vw" alt={`${v.name}, volle struik`} className="aspect-[4/5] w-full object-cover img-treat md:aspect-[4/5]" />
              <img src={img(v.slug)} srcSet={srcset(v.slug)} sizes="(min-width: 768px) 40vw, 50vw" alt={`${v.name}, bloemtros`} className="aspect-[4/5] w-full object-cover img-treat md:hidden" />
            </div>
            <div className="flex flex-col gap-5 p-6 md:p-9">
              <div>
                <p className="eyebrow text-muted">Rhododendron · {v.color}</p>
                <h2 id="sheet-title" className="mt-2 font-display text-[32px] leading-none md:text-[40px]">{v.name}</h2>
                <p className="mt-4 text-[15px] leading-relaxed text-fg-2">{v.long}</p>
              </div>
              <dl className={cn('grid grid-cols-2 gap-x-6 gap-y-2 border-y py-4 text-[14px]', line)}>
                {[['Bloeiperiode', v.bloei], ['Standplaats', v.standplaats], ['Max. hoogte', v.hoogte], ['Breedte', v.breedte], ['Groeisnelheid', v.groei], ['Winterhard', 'Ja']].map(([k, val]) => <div key={k}><dt className="text-[12px] text-muted">{k}</dt><dd className="text-fg">{val}</dd></div>)}
              </dl>
              <fieldset>
                <legend className="eyebrow mb-3 text-muted">Maat (hoogte bij levering)</legend>
                <div className="grid grid-cols-2 gap-2">
                  {v.sizes.map((s, i) => (
                    <button key={s.label} type="button" onClick={() => { setSize(i); setAdded(false) }} aria-pressed={size === i} className={cn('flex items-center justify-between rounded-field border px-4 py-3 text-left text-[14px] transition-colors', size === i ? 'border-fg bg-fg text-bg' : 'border-fg/30')}>
                      <span>{s.label}</span><span className="font-medium">€ {s.price}</span>
                    </button>
                  ))}
                </div>
              </fieldset>
              <div className="flex flex-wrap items-center gap-4">
                <div className="inline-flex h-12 items-center rounded-field border border-fg/30" role="group" aria-label="Aantal">
                  <button type="button" onClick={() => { setQty((q) => Math.max(1, q - 1)); setAdded(false) }} aria-label="Minder" className="grid size-12 place-items-center"><Minus className="size-4" /></button>
                  <span className="w-8 text-center text-[15px] tabular-nums" aria-live="polite">{qty}</span>
                  <button type="button" onClick={() => { setQty((q) => q + 1); setAdded(false) }} aria-label="Meer" className="grid size-12 place-items-center"><Plus className="size-4" /></button>
                </div>
                <p className="font-display text-[26px]">{fmtEur(price)}</p>
                <Button as="button" variant="solid" size="lg" onClick={() => { addToCart({ slug: v.slug, name: v.name, size: v.sizes[size].label, price: v.sizes[size].price, qty, image: `${v.slug}-sm` }); setAdded(true) }} className="w-full sm:w-auto">
                  {added ? <><Check className="size-4" /> Toegevoegd</> : 'In winkelwagen'}
                </Button>
              </div>
              <ul className="flex flex-col gap-1.5 text-[13.5px] text-fg-2">
                <li>Aangroeigarantie: niet aangeslagen in het eerste seizoen? Wij vervangen kosteloos.</li>
                <li>Vers gerooid voor uw bezorging. Eigen transport door heel Nederland; {company.pickup.toLowerCase()}</li>
                <li>Geen minimumbestelling. Vragen? Bel <a href={company.phone1Href} className="underline underline-offset-4">{company.phone1}</a>.</li>
              </ul>
              <a href={`product.html#${v.slug}`} className="inline-flex items-center gap-2 text-[14px] font-medium text-fg underline-offset-4 hover:underline">Alle foto's, kenmerken en bloeikalender<ArrowRight className="size-4" aria-hidden="true" /></a>
              <p className="text-[12px] text-muted">Demo: de winkelwagen is in de mockup nog niet gekoppeld aan een afrekenpagina.</p>
            </div>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  )
}
