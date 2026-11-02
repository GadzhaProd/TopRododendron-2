// Demo cart: a side sheet on desktop, a bottom sheet on phones (pattern from
// 21st.dev "Drawer" (31360), rebuilt without Base UI). Lines, quantities,
// subtotal, and an honest note that online payment is not live yet.
import { useEffect, useRef } from 'react'
import { AnimatePresence, motion, useReducedMotion } from 'framer-motion'
import { X, Minus, Plus, Trash2 } from 'lucide-react'
import { cn, lockPage, trapTab } from '@/lib/utils'
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
    lockPage(open)
    if (!open) return
    closeRef.current?.focus()
    const onKey = (e: KeyboardEvent) => { if (e.key === 'Escape') closeCart(); trapTab(e, panel.current) }
    document.addEventListener('keydown', onKey)
    return () => { document.removeEventListener('keydown', onKey); lockPage(false) }
  }, [open])

  const n = cartCount(lines)
  return (
    <AnimatePresence>
      {open && (
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} transition={{ duration: reduce ? 0 : 0.2 }} className="fixed inset-0 z-[80] flex items-end justify-end bg-ink/50 md:items-stretch" onClick={(e) => { if (e.target === e.currentTarget) closeCart() }}>
          <motion.div
            ref={panel} role="dialog" aria-modal="true" aria-labelledby="cart-title"
            initial={reduce ? false : { y: 40, x: 0, opacity: 0 }} animate={{ y: 0, x: 0, opacity: 1 }} exit={reduce ? undefined : { y: 40, opacity: 0 }} transition={{ duration: 0.3, ease: [0.22, 1, 0.36, 1] }}
            className="flex max-h-[92svh] w-full flex-col bg-paper text-ink shadow-2xl md:h-full md:max-h-none md:w-[440px]"
          >
            <div className="flex items-center justify-between border-b border-line px-5 py-4 md:px-6">
              <h2 id="cart-title" className="font-display text-[24px]">Winkelwagen <span className="num text-[15px] text-muted">({n})</span></h2>
              <button ref={closeRef} type="button" onClick={closeCart} aria-label="Sluiten" className="grid size-10 place-items-center rounded-ui border border-ink/25"><X className="size-4" /></button>
            </div>
            <div className="flex-1 overflow-y-auto px-5 py-4 md:px-6">
              {lines.length === 0 ? (
                <div className="flex h-full flex-col items-start justify-center gap-4 py-10">
                  <p className="font-display text-[22px]">Uw winkelwagen is leeg.</p>
                  <p className="max-w-[36ch] text-[14.5px] text-ink-2">Zeven winterharde soorten, in vier maten. Vers gerooid voor uw levering.</p>
                  <Button href="assortiment.html" variant="outline" size="md" arrow>Bekijk het assortiment</Button>
                </div>
              ) : (
                <ul className="divide-y divide-line">
                  {lines.map((l) => (
                    <li key={l.slug + l.size} className="flex gap-4 py-4">
                      <div className="size-[72px] shrink-0 overflow-hidden rounded-img bg-paper-2">{l.image && <img src={img(l.image)} alt="" className="h-full w-full object-cover" />}</div>
                      <div className="min-w-0 flex-1">
                        <p className="font-display text-[18px] leading-tight">{l.name}</p>
                        <p className="mt-0.5 text-[13px] text-muted">{l.size}</p>
                        <div className="mt-2.5 flex items-center justify-between gap-3">
                          <div className="inline-flex h-9 items-center rounded-field border border-ink/30" role="group" aria-label={`Aantal ${l.name} ${l.size}`}>
                            <button type="button" onClick={() => setQty(l.slug, l.size, l.qty - 1)} aria-label="Minder" className="grid size-9 place-items-center"><Minus className="size-3.5" /></button>
                            <span className="num w-7 text-center text-[14px]">{l.qty}</span>
                            <button type="button" onClick={() => setQty(l.slug, l.size, l.qty + 1)} aria-label="Meer" className="grid size-9 place-items-center"><Plus className="size-3.5" /></button>
                          </div>
                          <p className="num text-[15px] font-medium">{fmtEur(l.qty * parseFloat(l.price.replace(',', '.')))}</p>
                          <button type="button" onClick={() => removeLine(l.slug, l.size)} aria-label={`${l.name} verwijderen`} className="grid size-9 place-items-center text-muted hover:text-ink"><Trash2 className="size-4" strokeWidth={1.6} /></button>
                        </div>
                      </div>
                    </li>
                  ))}
                </ul>
              )}
            </div>
            {lines.length > 0 && (
              <div className="border-t border-line bg-surface px-5 py-5 md:px-6">
                <div className="flex items-baseline justify-between"><span className="text-[14px] text-ink-2">Subtotaal</span><span className="num font-display text-[26px]">{fmtEur(cartTotal(lines))}</span></div>
                <p className="mt-1 text-[12.5px] text-muted">Inclusief btw. Bezorgkosten en leverdatum stemmen wij persoonlijk met u af.</p>
                <div className="mt-4 flex flex-col gap-2">
                  <Button as="button" variant="solid" size="lg" disabled className="w-full">Afrekenen</Button>
                  <p className="text-center text-[12.5px] text-muted">Online betalen komt binnenkort. Bestellen kan nu al telefonisch of per e-mail.</p>
                  <div className="grid grid-cols-2 gap-2">
                    <Button href={company.phone1Href} variant="outline" size="md">Bel ons</Button>
                    <Button href={`mailto:${company.email}?subject=Bestelling%20rhododendrons`} variant="outline" size="md">E-mail</Button>
                  </div>
                </div>
                <p className="mt-4 border-t border-line pt-3 text-[13px] text-ink-2">Hovenier of groothandel? <a href="groothandel.html#offerte" className="underline underline-offset-4">Vraag een partijprijs aan</a>.</p>
              </div>
            )}
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  )
}
