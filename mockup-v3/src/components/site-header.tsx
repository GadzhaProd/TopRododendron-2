// Header: a frosted paper bar from the very first pixel (AA contrast of logo and
// menu over any video frame), hairline underneath, no morphing capsule. The mobile
// menu is a real dialog (Escape, focus trap, inert page, measured top offset).
// Pattern adapted from 21st.dev "Header 1" (efferd) in round 2.
import * as React from 'react'
import { createPortal } from 'react-dom'
import { AnimatePresence, motion } from 'framer-motion'
import { Phone, ShoppingBag } from 'lucide-react'
import { cn, lockPage, trapTab } from '@/lib/utils'
import { Logo } from './logo'
import { Button } from './button'
import { company } from '@/data/content'
import { openCart, useCartCount } from '@/lib/store'

export type NavLink = { label: string; href: string; current?: boolean }

export const retailNav = (current?: string): NavLink[] => [
  { label: 'Assortiment', href: 'assortiment.html', current: current === 'assortiment' },
  { label: 'Plantgids', href: 'plantgids.html', current: current === 'plantgids' },
  { label: 'De kwekerij', href: 'index.html#kwekerij', current: false },
  { label: 'Contact', href: 'index.html#contact', current: false },
]

function useScrolled(threshold = 12) {
  const [s, setS] = React.useState(false)
  React.useEffect(() => {
    const h = () => setS(window.scrollY > threshold)
    h(); window.addEventListener('scroll', h, { passive: true })
    return () => window.removeEventListener('scroll', h)
  }, [threshold])
  return s
}

export function CartButton({ dark }: { dark?: boolean }) {
  const n = useCartCount()
  return (
    <button type="button" onClick={openCart} aria-label={`Winkelwagen, ${n} ${n === 1 ? 'artikel' : 'artikelen'}`} className={cn('relative flex h-11 items-center gap-2 rounded-ui px-2.5 text-[14px] font-medium transition-colors', dark ? 'text-white hover:bg-white/10' : 'text-ink hover:bg-ink/5')}>
      <ShoppingBag className="size-[18px]" strokeWidth={1.6} aria-hidden="true" />
      <span className="hidden sm:inline">Winkelwagen</span>
      {n > 0 && <span className={cn('num grid min-w-[20px] place-items-center rounded-full px-1.5 text-[11.5px] font-semibold leading-[20px]', dark ? 'bg-white text-ink' : 'bg-ink text-paper')}>{n}</span>}
    </button>
  )
}

export function SiteHeader({ variant = 'retail', current }: { variant?: 'retail' | 'b2b'; current?: string }) {
  const [open, setOpen] = React.useState(false)
  const scrolled = useScrolled()
  const headerRef = React.useRef<HTMLElement>(null)
  const [top, setTop] = React.useState(64)
  const b2b = variant === 'b2b'
  const dark = b2b

  React.useEffect(() => {
    lockPage(open)
    if (open) setTop(headerRef.current?.getBoundingClientRect().bottom ?? 64)
    return () => lockPage(false)
  }, [open])

  const links: NavLink[] = b2b
    ? [
        { label: 'Afnemers', href: '#doelgroepen' },
        { label: 'Werkwijze', href: '#werkwijze' },
        { label: 'Voorraad', href: '#voorraad' },
        { label: 'Tarieven', href: '#tarieven' },
        { label: 'Vragen', href: '#faq' },
      ]
    : retailNav(current)
  const linkCls = cn('relative text-[14.5px] transition-colors after:absolute after:-bottom-1 after:left-0 after:h-px after:w-full after:origin-left after:scale-x-0 after:bg-current after:transition-transform hover:after:scale-x-100', dark ? 'text-white/85 hover:text-white' : 'text-ink-2 hover:text-ink')

  return (
    <header ref={headerRef} className={cn('fixed inset-x-0 top-0 z-50', dark && 'on-dark')}>
      <div className={cn('border-b backdrop-blur-xl transition-[height,background-color] duration-300', dark ? 'border-white/12 bg-night/85 text-white' : 'border-ink/10 bg-paper/88 text-ink', scrolled && (dark ? 'bg-night/92' : 'bg-paper/94'))}>
        <div className={cn('wrap container-x flex items-center justify-between transition-[height] duration-300', scrolled ? 'h-16' : 'h-16 md:h-[76px]')}>
          <a href="index.html" aria-label="Top Rhododendrons, naar de homepage" className="flex items-center">
            <Logo size="sm" dark={dark} />
          </a>
          <nav className="hidden items-center gap-5 lg:flex xl:gap-7" aria-label="Hoofdnavigatie">
            {links.map((l) => (
              <a key={l.label} href={l.href} aria-current={l.current ? 'page' : undefined} className={cn(linkCls, l.current && 'after:scale-x-100 font-medium')}>{l.label}</a>
            ))}
            {!b2b && <a href="groothandel.html" className={cn(linkCls, 'font-medium')}>Groothandel</a>}
            {b2b && <a href="index.html" className={cn(linkCls, 'font-medium')}>Particulier</a>}
          </nav>
          <div className="flex items-center gap-1 sm:gap-2">
            <a href={company.phone1Href} className={cn('hidden h-11 items-center gap-2 rounded-ui px-2.5 text-[14px] font-medium md:flex lg:hidden xl:flex', dark ? 'text-white hover:bg-white/10' : 'text-ink hover:bg-ink/5')}>
              <Phone className="size-4" strokeWidth={1.6} aria-hidden="true" /><span className="num">{company.phone1}</span>
            </a>
            {b2b ? (
              <Button href="#offerte" variant="paper" size="sm" className="hidden lg:inline-flex">Offerte aanvragen</Button>
            ) : (
              <CartButton dark={dark} />
            )}
            <button
              type="button"
              onClick={() => setOpen(!open)}
              aria-expanded={open}
              aria-controls="mobile-menu"
              aria-label={open ? 'Menu sluiten' : 'Menu openen'}
              className={cn('relative ml-1 flex size-11 items-center justify-center rounded-ui border lg:hidden', dark ? 'border-white/40 text-white' : 'border-ink/25 text-ink')}
            >
              <span className={cn('absolute h-px w-5 bg-current transition-transform duration-300', open ? 'rotate-45' : '-translate-y-[3px]')} />
              <span className={cn('absolute h-px w-5 bg-current transition-transform duration-300', open ? '-rotate-45' : 'translate-y-[3px]')} />
            </button>
          </div>
        </div>
      </div>
      <MobileMenu open={open} top={top} dark={dark} links={[...links, b2b ? { label: 'Particulier', href: 'index.html' } : { label: 'Groothandel', href: 'groothandel.html' }]} b2b={b2b} onClose={() => setOpen(false)} />
    </header>
  )
}

function MobileMenu({ open, top, dark, links, b2b, onClose }: { open: boolean; top: number; dark: boolean; links: NavLink[]; b2b: boolean; onClose: () => void }) {
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
        <motion.div
          ref={ref}
          id="mobile-menu"
          role="dialog" aria-modal="true" aria-label="Menu"
          initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} transition={{ duration: 0.18 }}
          style={{ top }}
          className={cn('fixed inset-x-0 bottom-0 z-40 flex flex-col justify-between overflow-y-auto px-6 pb-8 pt-3 lg:hidden', dark ? 'bg-night text-white on-dark' : 'bg-paper text-ink')}
        >
          <nav className="flex flex-col" aria-label="Mobiele navigatie">
            {links.map((l, i) => (
              <motion.a
                key={l.label} href={l.href} onClick={onClose}
                initial={{ opacity: 0, y: 6 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.04 + i * 0.035 }}
                className={cn('border-b py-4 font-display text-[28px] leading-none', dark ? 'border-white/15' : 'border-line')}
              >
                {l.label}
              </motion.a>
            ))}
          </nav>
          <div className="mt-8 flex flex-col gap-3">
            {b2b ? <Button href="#offerte" variant="paper" size="lg" onClick={onClose}>Offerte aanvragen</Button> : <Button href="assortiment.html" variant="solid" size="lg" onClick={onClose}>Bekijk het assortiment</Button>}
            <Button href={company.phone1Href} variant={dark ? 'outline-white' : 'outline'} size="lg">Bel {company.phone1}</Button>
            <Button href={company.whatsapp} variant={dark ? 'outline-white' : 'outline'} size="lg">WhatsApp</Button>
          </div>
        </motion.div>
      )}
    </AnimatePresence>,
    document.body,
  )
}
