// Demo cart: side sheet on desktop, bottom sheet on phones (pattern from
// 21st.dev "Drawer" 31360, rebuilt without Base UI). Focus returns to the
// opener on close. Shipping note uses the old site's wording.
import { useEffect, useRef } from 'react'
import { AnimatePresence, motion, useReducedMotion } from 'framer-motion'
import { X, Minus, Plus, Trash2 } from 'lucide-react'
import { cn, lockPage, trapTab, rememberFocus } from '@/lib/utils'
import { Button } from './button'
import { cartOpen, closeCart, useCart, setQty, removeLine, cartTotal, cartCount } from '@/lib/store'
import { company, fmtEur, img } from '@/data/content'

export function CartDrawer() {
  const open = cartOpen.use()
  const lines = useCart()
  const reduce = useReducedMotion()
  const panel = useRef<HTMLDivElement>(null)
  const closeRef = useRef<HTMLButtonElement>(null)

  useEffect(() => {
    if (!open) return
    const restore = rememberFocus()
    lockPage(true)
    setTimeout(() => closeRef.current?.focus(), 20)
    const onKey = (e: KeyboardEvent) => { if (e.key === 'Escape') closeCart(); trapTab(e, panel.current) }
    document.addEventListener('keydown', onKey)
    return () => { document.removeEventListener('keydown', onKey); lockPage(false); restore() }
  }, [open])

  const n = cartCount(lines)
  return (
    <AnimatePresence>
      {open && (
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} transition={{ duration: reduce ? 0 : 0.2 }} className="fixed inset-0 z-[80] flex items-end justify-end bg-night/60 md:items-stretch" onClick={(e) => { if (e.target === e.currentTarget) closeCart() }}>
          <motion.div
            ref={panel} role="dialog" aria-modal="true" aria-labelledby="cart-title"
            initial={reduce ? false : { y: 40, opacity: 0 }} animate={{ y: 0, opacity: 1 }} exit={reduce ? undefined : { y: 40, opacity: 0 }} transition={{ duration: 0.3, ease: [0.22, 1, 0.36, 1] }}
            className="flex max-h-[92svh] w-full flex-col rounded-t-panel bg-bg text-ink shadow-2xl md:h-full md:max-h-none md:w-[460px] md:rounded-none"
          >
            <div className="flex items-center justify-between px-5 py-4 md:px-6">
              <h2 id="cart-title" className="text-[22px] font-semibold tracking-[-0.01em]">Winkelwagen <span className="num text-[15px] font-medium text-muted">({n})</span></h2>
              <button ref={closeRef} type="button" onClick={closeCart} aria-label="Sluiten" className="grid size-10 place-items-center rounded-full bg-ink/8 hover:bg-ink/15"><X className="size-4" /></button>
            </div>
            <div className="flex-1 overflow-y-auto px-5 pb-4 md:px-6">
              {lines.length === 0 ? (
                <div className="flex h-full flex-col items-start justify-center gap-4 py-10">
                  <p className="text-[22px] font-semibold">Uw winkelwagen is leeg.</p>
                  <p className="max-w-[36ch] text-[14.5px] text-ink-2">Zeven winterharde soorten, in vier maten. Vers gerooid voor uw levering.</p>
                  <Button href="assortiment.html" variant="outline" size="md" arrow>Bekijk het assortiment</Button>
                </div>
              ) : (
                <ul className="flex flex-col gap-2.5">
                  {lines.map((l) => (
                    <li key={l.slug + l.size} className="flex gap-4 rounded-img bg-surface p-3">
                      <div className="size-[76px] shrink-0 overflow-hidden rounded-[10px] bg-bg-2">{l.image && <img src={img(l.image)} alt="" className="h-full w-full object-cover" />}</div>
                      <div className="min-w-0 flex-1">
                        <p className="text-[16px] font-semibold leading-tight">{l.name}</p>
                        <p className="mt-0.5 text-[13px] text-muted">{l.size}</p>
                        <div className="mt-2.5 flex items-center justify-between gap-3">
                          <div className="inline-flex h-9 items-center rounded-field border border-ink/35 bg-white" role="group" aria-label={`Aantal ${l.name} ${l.size}`}>
                            <button type="button" onClick={() => setQty(l.slug, l.size, l.qty - 1)} aria-label="Minder" className="grid size-9 place-items-center"><Minus className="size-3.5" /></button>
                            <span className="num w-7 text-center text-[14px] font-semibold">{l.qty}</span>
                            <button type="button" onClick={() => setQty(l.slug, l.size, l.qty + 1)} aria-label="Meer" className="grid size-9 place-items-center"><Plus className="size-3.5" /></button>
                          </div>
                          <p className="num text-[15px] font-semibold">{fmtEur(l.qty * parseFloat(l.price.replace(',', '.')))}</p>
                          <button type="button" onClick={() => removeLine(l.slug, l.size)} aria-label={`${l.name} verwijderen`} className="grid size-9 place-items-center rounded-full text-muted hover:bg-ink/8 hover:text-ink"><Trash2 className="size-4" strokeWidth={1.7} /></button>
                        </div>
                      </div>
                    </li>
                  ))}
                </ul>
              )}
            </div>
            {lines.length > 0 && (
              <div className="border-t border-line bg-surface px-5 py-5 md:px-6">
                <div className="flex items-baseline justify-between"><span className="text-[14px] text-ink-2">Subtotaal</span><span className="num text-[26px] font-semibold tracking-[-0.02em]">{fmtEur(cartTotal(lines))}</span></div>
                <p className="mt-1 text-[12.5px] text-muted">Verzendkosten worden berekend bij afrekenen.</p>
                <div className="mt-4 flex flex-col gap-2">
                  <Button as="button" variant="solid" size="lg" disabled className="w-full">Afrekenen</Button>
                  <p className="text-center text-[12.5px] text-muted">Online betalen komt binnenkort beschikbaar. Bestellen kan nu telefonisch of per e-mail.</p>
                  <div className="grid grid-cols-2 gap-2">
                    <Button href={company.phone1Href} variant="outline" size="md">Bel ons</Button>
                    <Button href={`mailto:${company.email}?subject=Bestelling%20rhododendrons`} variant="outline" size="md">E-mail</Button>
                  </div>
                </div>
                <p className="mt-4 border-t border-line pt-3 text-[13px] text-ink-2">Hovenier of groothandel? <a href="groothandel.html#offerte" className="font-semibold underline underline-offset-4">Vraag een partijprijs aan</a>.</p>
              </div>
            )}
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  )
}
