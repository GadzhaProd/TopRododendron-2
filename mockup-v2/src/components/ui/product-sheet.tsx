// Product sheet: the one screen that follows a click on a variety. A modal dialog
// with the two real photos, facts, size choice with the real price list, quantity,
// "In winkelwagen" (mock cart) and the delivery/guarantee facts next to the button.
import { useEffect, useRef, useState } from 'react'
import { AnimatePresence, motion, useReducedMotion } from 'framer-motion'
import { X, Minus, Plus, Check } from 'lucide-react'
import { cn } from '@/lib/utils'
import { Button } from './button'
import { sheetStore, closeSheet, addToCart } from '@/lib/store'
import { varieties, img, srcset, company } from '@/data/content'

export function ProductSheet({ dark = false }: { dark?: boolean }) {
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
    document.body.style.overflow = 'hidden'
    document.querySelector('main')?.setAttribute('inert', '')
    closeRef.current?.focus()
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') closeSheet()
      if (e.key === 'Tab' && panelRef.current) {
        const f = Array.from(panelRef.current.querySelectorAll<HTMLElement>('a[href], button:not([disabled]), input, [tabindex="0"]'))
        if (!f.length) return
        const first = f[0], last = f[f.length - 1]
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus() }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus() }
      }
    }
    document.addEventListener('keydown', onKey)
    return () => { document.body.style.overflow = ''; document.querySelector('main')?.removeAttribute('inert'); document.removeEventListener('keydown', onKey) }
  }, [v])

  const price = v ? parseFloat(v.sizes[size].price.replace(',', '.')) * qty : 0
  const fmt = (n: number) => '€ ' + n.toFixed(2).replace('.', ',')
  const t = dark ? 'text-white' : 'text-fg'
  const m = dark ? 'text-white/70' : 'text-muted'
  const line = dark ? 'border-white/15' : 'border-fg/12'

  return (
    <AnimatePresence>
      {v && (
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} transition={{ duration: reduce ? 0 : 0.2 }} className="fixed inset-0 z-[70] flex items-end justify-center bg-black/55 p-0 md:items-center md:p-6" onClick={(e) => { if (e.target === e.currentTarget) closeSheet() }}>
          <motion.div
            ref={panelRef} role="dialog" aria-modal="true" aria-labelledby="sheet-title"
            initial={reduce ? false : { y: 40, opacity: 0 }} animate={{ y: 0, opacity: 1 }} exit={reduce ? undefined : { y: 40, opacity: 0 }} transition={{ duration: 0.35, ease: [0.22, 1, 0.36, 1] }}
            className={cn('relative grid grid-cols-1 max-h-[94svh] w-full max-w-5xl overflow-y-auto rounded-t-img md:grid-cols-2 md:rounded-img', dark ? 'bg-night text-white on-dark' : 'bg-surface text-fg')}
          >
            <button ref={closeRef} type="button" onClick={closeSheet} aria-label="Sluiten" className={cn('absolute right-4 top-4 z-10 grid size-11 place-items-center rounded-full border backdrop-blur', dark ? 'border-white/30 bg-night/60 text-white' : 'border-fg/20 bg-surface/80 text-fg')}><X className="size-5" /></button>
            <div className="grid grid-cols-2 gap-1 md:grid-cols-1">
              <img src={img(`${v.slug}-2`)} srcSet={srcset(`${v.slug}-2`)} sizes="(min-width: 768px) 40vw, 50vw" alt={`${v.name}, volle struik`} className="aspect-[4/5] w-full object-cover img-treat md:aspect-[4/5]" />
              <img src={img(v.slug)} srcSet={srcset(v.slug)} sizes="(min-width: 768px) 40vw, 50vw" alt={`${v.name}, bloemtros`} className="aspect-[4/5] w-full object-cover img-treat md:hidden" />
            </div>
            <div className="flex flex-col gap-5 p-6 md:p-9">
              <div>
                <p className={cn('eyebrow', m)}>Rhododendron · {v.color}</p>
                <h2 id="sheet-title" className="mt-2 font-display text-[32px] leading-none md:text-[40px]">{v.name}</h2>
                <p className={cn('mt-4 text-[15px] leading-relaxed', dark ? 'text-white/85' : 'text-fg-2')}>{v.long}</p>
              </div>
              <dl className={cn('grid grid-cols-2 gap-x-6 gap-y-2 border-y py-4 text-[14px]', line)}>
                {[['Bloeiperiode', v.bloei], ['Standplaats', v.standplaats], ['Max. hoogte', v.hoogte], ['Breedte', v.breedte], ['Groeisnelheid', v.groei], ['Winterhard', 'Ja']].map(([k, val]) => <div key={k}><dt className={cn('text-[12px]', m)}>{k}</dt><dd className={t}>{val}</dd></div>)}
              </dl>
              <fieldset>
                <legend className={cn('eyebrow mb-3', m)}>Maat (hoogte bij levering)</legend>
                <div className="grid grid-cols-2 gap-2">
                  {v.sizes.map((s, i) => (
                    <button key={s.label} type="button" onClick={() => { setSize(i); setAdded(false) }} aria-pressed={size === i} className={cn('flex items-center justify-between border px-4 py-3 text-left text-[14px] transition-colors rounded-field', size === i ? (dark ? 'border-white bg-white text-night' : 'border-fg bg-fg text-bg') : (dark ? 'border-white/35' : 'border-fg/30'))}>
                      <span>{s.label}</span><span className="font-medium">€ {s.price}</span>
                    </button>
                  ))}
                </div>
              </fieldset>
              <div className="flex flex-wrap items-center gap-4">
                <div className={cn('inline-flex h-12 items-center border rounded-field', dark ? 'border-white/35' : 'border-fg/30')} role="group" aria-label="Aantal">
                  <button type="button" onClick={() => { setQty((q) => Math.max(1, q - 1)); setAdded(false) }} aria-label="Minder" className="grid size-12 place-items-center"><Minus className="size-4" /></button>
                  <span className="w-8 text-center text-[15px] tabular-nums" aria-live="polite">{qty}</span>
                  <button type="button" onClick={() => { setQty((q) => q + 1); setAdded(false) }} aria-label="Meer" className="grid size-12 place-items-center"><Plus className="size-4" /></button>
                </div>
                <p className="font-display text-[26px]">{fmt(price)}</p>
                <Button as="button" variant={dark ? 'white' : 'solid'} size="lg" onClick={() => { addToCart({ slug: v.slug, name: v.name, size: v.sizes[size].label, price: v.sizes[size].price, qty }); setAdded(true) }} className="w-full sm:w-auto">
                  {added ? <><Check className="size-4" /> Toegevoegd</> : 'In winkelwagen'}
                </Button>
              </div>
              <ul className={cn('flex flex-col gap-1.5 text-[13.5px]', dark ? 'text-white/80' : 'text-fg-2')}>
                <li>Aangroeigarantie: niet aangeslagen in het eerste seizoen? Wij vervangen kosteloos.</li>
                <li>Vers gerooid voor uw bezorging. Eigen transport door heel Nederland; {company.pickup.toLowerCase()}</li>
                <li>Geen minimumbestelling. Vragen? Bel <a href={company.phone1Href} className="underline underline-offset-4">{company.phone1}</a>.</li>
              </ul>
              <p className={cn('text-[12px]', m)}>Demo: de winkelwagen is in de mockup nog niet gekoppeld aan een afrekenpagina.</p>
            </div>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  )
}
