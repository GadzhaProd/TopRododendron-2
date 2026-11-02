// Header: transparent over the hero (the hero carries a dark top scrim so the
// white logo and menu keep AA on every frame), a frosted night bar after
// scrolling and on all non-hero pages. Mobile menu is a real dialog.
import * as React from 'react'
import { createPortal } from 'react-dom'
import { AnimatePresence, motion } from 'framer-motion'
import { Phone, ShoppingBag } from 'lucide-react'
import { cn, lockPage, trapTab } from '@/lib/utils'
import { Logo } from './logo'
import { Button, ext } from './button'
import { WhatsAppIcon } from './whatsapp-float'
import { company } from '@/data/content'
import { openCart, useCartCount } from '@/lib/store'

export type NavLink = { label: string; href: string; current?: boolean }

function useScrolled(threshold = 40) {
  const [s, setS] = React.useState(false)
  React.useEffect(() => {
    const h = () => setS(window.scrollY > threshold)
    h(); window.addEventListener('scroll', h, { passive: true })
    return () => window.removeEventListener('scroll', h)
  }, [threshold])
  return s
}

export function CartButton() {
  const n = useCartCount()
  return (
    <button type="button" onClick={openCart} aria-label={`Winkelwagen, ${n} ${n === 1 ? 'artikel' : 'artikelen'}`} className="relative flex h-11 items-center gap-2 rounded-ui px-2.5 text-[14.5px] font-semibold text-white transition-colors hover:bg-white/12">
      <ShoppingBag className="size-[19px]" strokeWidth={1.7} aria-hidden="true" />
      <span className="hidden sm:inline">Winkelwagen</span>
      {n > 0 && <span className="num grid min-w-[20px] place-items-center rounded-full bg-white px-1.5 text-[11.5px] font-bold leading-[20px] text-ink">{n}</span>}
    </button>
  )
}

/** `hero`: page starts with a full-bleed dark hero (header transparent at top). `page`: 'home' | 'assortiment' | 'plantgids' | 'product'. */
export function SiteHeader({ variant = 'retail', page, hero = false }: { variant?: 'retail' | 'b2b'; page?: string; hero?: boolean }) {
  const [open, setOpen] = React.useState(false)
  const scrolled = useScrolled()
  const headerRef = React.useRef<HTMLElement>(null)
  const [top, setTop] = React.useState(64)
  const b2b = variant === 'b2b'
  const home = page === 'home'

  React.useEffect(() => {
    lockPage(open)
    if (open) setTop(headerRef.current?.getBoundingClientRect().bottom ?? 64)
    return () => lockPage(false)
  }, [open])

  // same-page anchors stay bare "#id" so they work inside the artifact viewer
  const links: NavLink[] = b2b
    ? [{ label: 'Afnemers', href: '#doelgroepen' }, { label: 'Werkwijze', href: '#werkwijze' }, { label: 'Voorraad', href: '#voorraad' }, { label: 'Tarieven', href: '#tarieven' }, { label: 'Vragen', href: '#faq' }]
    : [
        { label: 'Assortiment', href: 'assortiment.html', current: page === 'assortiment' || page === 'product' },
        { label: 'Plantgids', href: 'plantgids.html', current: page === 'plantgids' },
        { label: 'De kwekerij', href: home ? '#kwekerij' : 'index.html#kwekerij' },
        { label: 'Contact', href: home ? '#contact' : 'index.html#contact' },
      ]
  const solid = scrolled || !hero || open
  const linkCls = 'relative text-[14.5px] font-medium text-white/85 transition-colors hover:text-white after:absolute after:-bottom-1 after:left-0 after:h-px after:w-full after:origin-left after:scale-x-0 after:bg-current after:transition-transform hover:after:scale-x-100'

  return (
    <header ref={headerRef} className="on-dark fixed inset-x-0 top-0 z-50 text-white">
      <div className={cn('transition-colors duration-300', solid ? 'border-b border-white/10 bg-night/88 backdrop-blur-xl' : 'bg-transparent')}>
        <div className={cn('wrap container-x flex items-center justify-between transition-[height] duration-300', scrolled ? 'h-16' : 'h-[68px] md:h-20')}>
          <a href="index.html" aria-label="Top Rhododendrons, naar de homepage" className="flex items-center"><Logo size="sm" dark /></a>
          <nav className="hidden items-center gap-5 lg:flex xl:gap-7" aria-label="Hoofdnavigatie">
            {links.map((l) => <a key={l.label} href={l.href} aria-current={l.current ? 'page' : undefined} className={cn(linkCls, l.current && 'text-white after:scale-x-100')}>{l.label}</a>)}
            {!b2b && <a href="groothandel.html" className={cn(linkCls, 'font-semibold text-white')}>Groothandel</a>}
            {b2b && <a href="index.html" className={cn(linkCls, 'font-semibold text-white')}>Particulier</a>}
          </nav>
          <div className="flex items-center gap-0.5 sm:gap-1.5">
            <a href={company.whatsapp} {...ext} aria-label="WhatsApp" className="hidden size-11 place-items-center rounded-ui text-white hover:bg-white/12 xl:grid"><WhatsAppIcon className="size-5" /></a>
            <a href={company.phone1Href} aria-label={`Bel ${company.phone1}`} className="flex h-11 items-center gap-2 rounded-ui px-2.5 text-[14.5px] font-semibold text-white hover:bg-white/12">
              <Phone className="size-[18px]" strokeWidth={1.7} aria-hidden="true" /><span className="num hidden xl:inline">{company.phone1}</span>
            </a>
            {b2b ? <Button href="#offerte" variant="white" size="sm" className="hidden md:inline-flex">Offerte aanvragen</Button> : <CartButton />}
            <button type="button" onClick={() => setOpen(!open)} aria-expanded={open} aria-controls="mobile-menu" aria-label={open ? 'Menu sluiten' : 'Menu openen'} className="relative ml-1 flex size-11 items-center justify-center rounded-ui border border-white/40 text-white lg:hidden">
              <span className={cn('absolute h-px w-5 bg-current transition-transform duration-300', open ? 'rotate-45' : '-translate-y-[3px]')} />
              <span className={cn('absolute h-px w-5 bg-current transition-transform duration-300', open ? '-rotate-45' : 'translate-y-[3px]')} />
            </button>
          </div>
        </div>
      </div>
      <MobileMenu open={open} top={top} links={[...links, b2b ? { label: 'Particulier', href: 'index.html' } : { label: 'Groothandel', href: 'groothandel.html' }]} b2b={b2b} onClose={() => setOpen(false)} />
    </header>
  )
}

function MobileMenu({ open, top, links, b2b, onClose }: { open: boolean; top: number; links: NavLink[]; b2b: boolean; onClose: () => void }) {
  const ref = React.useRef<HTMLDivElement>(null)
  React.useEffect(() => {
    if (!open) return
    const el = ref.current
    el?.querySelector<HTMLElement>('a[href]')?.focus()
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') { e.preventDefault(); onClose(); document.querySelector<HTMLElement>('[aria-controls="mobile-menu"]')?.focus(); return }
      trapTab(e, el)
    }
    document.addEventListener('keydown', onKey)
    return () => document.removeEventListener('keydown', onKey)
  }, [open, onClose])
  if (typeof window === 'undefined') return null
  return createPortal(
    <AnimatePresence>
      {open && (
        <motion.div ref={ref} id="mobile-menu" role="dialog" aria-modal="true" aria-label="Menu" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} transition={{ duration: 0.18 }} style={{ top }} className="on-dark fixed inset-x-0 bottom-0 z-40 flex flex-col justify-between overflow-y-auto bg-night px-6 pb-8 pt-2 text-white lg:hidden">
          <nav className="flex flex-col" aria-label="Mobiele navigatie">
            {links.map((l, i) => (
              <motion.a key={l.label} href={l.href} onClick={onClose} initial={{ opacity: 0, y: 6 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.04 + i * 0.035 }} className="border-b border-white/12 py-4 text-[28px] font-semibold tracking-[-0.02em] leading-none">{l.label}</motion.a>
            ))}
          </nav>
          <div className="mt-8 flex flex-col gap-2.5">
            {b2b ? <Button href="#offerte" variant="white" size="lg" onClick={onClose}>Offerte aanvragen</Button> : <Button href="assortiment.html" variant="white" size="lg" onClick={onClose}>Bekijk het assortiment</Button>}
            <div className="grid grid-cols-2 gap-2.5">
              <Button href={company.phone1Href} variant="outline-white" size="lg"><Phone className="size-4" aria-hidden="true" />Bel ons</Button>
              <Button href={company.whatsapp} {...ext} variant="outline-white" size="lg"><WhatsAppIcon className="size-4" />WhatsApp</Button>
            </div>
          </div>
        </motion.div>
      )}
    </AnimatePresence>,
    document.body,
  )
}
