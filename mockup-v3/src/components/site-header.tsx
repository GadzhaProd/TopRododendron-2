// Header of concept C (round 2, post-audit): a translucent frosted light strip
// from the very first pixel (dark text, AA over the video), which compacts into a
// floating capsule after scrolling. The mobile menu is a real dialog (Escape,
// focus trap, inert page, measured top offset). Retail pages carry the cart CTA
// ("Bestellen" / "Winkelwagen (n)"), the B2B page "Offerte aanvragen".
import * as React from 'react'
import { createPortal } from 'react-dom'
import { AnimatePresence, motion } from 'framer-motion'
import { Phone } from 'lucide-react'
import { cn, lockPage, trapTab } from '@/lib/utils'
import { Logo } from './logo'
import { Button, ext } from './button'
import { WhatsAppIcon } from './whatsapp-float'
import { company } from '@/data/content'
import { openCart, useCartCount } from '@/lib/store'

export type NavLink = { label: string; href: string; strong?: boolean; current?: boolean }

export function useScrolled(threshold = 24) {
  const [s, setS] = React.useState(false)
  React.useEffect(() => {
    const h = () => setS(window.scrollY > threshold)
    h(); window.addEventListener('scroll', h, { passive: true })
    return () => window.removeEventListener('scroll', h)
  }, [threshold])
  return s
}

function CartCta({ home, onClick }: { home: boolean; onClick?: () => void }) {
  const n = useCartCount()
  if (n > 0 || !home) return <Button as="button" variant="solid" size="sm" onClick={() => { onClick?.(); openCart() }}>{n > 0 ? `Winkelwagen (${n})` : 'Winkelwagen'}</Button>
  return <Button href="#planten" variant="solid" size="sm" onClick={onClick}>Bestellen</Button>
}

/** `page`: 'home' | 'assortiment' | 'plantgids' | 'product'. `hero` is kept for API compatibility (the C bar is frosted everywhere). */
export function SiteHeader({ variant = 'retail', page }: { variant?: 'retail' | 'b2b'; page?: string; hero?: boolean }) {
  const [open, setOpen] = React.useState(false)
  const scrolled = useScrolled(24)
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
    ? [{ label: 'Projecten', href: '#doelgroepen' }, { label: 'Werkwijze', href: '#werkwijze' }, { label: 'Voorraad', href: '#voorraad' }, { label: 'Offerte', href: '#offerte' }, { label: 'Particulier', href: 'index.html', strong: true }]
    : home
      ? [{ label: 'Planten', href: '#planten' }, { label: 'Waarom wij', href: '#waarom' }, { label: 'De kweker', href: '#kweker' }, { label: 'Advies', href: '#advies' }, { label: 'Groothandel', href: 'groothandel.html', strong: true }]
      : [
          { label: 'Assortiment', href: 'assortiment.html', current: page === 'assortiment' || page === 'product' },
          { label: 'Plantgids', href: 'plantgids.html', current: page === 'plantgids' },
          { label: 'De kweker', href: 'index.html#kweker' },
          { label: 'Advies', href: 'index.html#advies' },
          { label: 'Groothandel', href: 'groothandel.html', strong: true },
        ]
  const cta = (onClick?: () => void) => (b2b ? <Button href="#offerte" variant="solid" size="sm" onClick={onClick}>Offerte aanvragen</Button> : <CartCta home={home} onClick={onClick} />)
  const linkCls = 'text-[14px] tracking-[0.01em] transition-colors text-fg-2 hover:text-fg'
  const capsule = scrolled && !open

  return (
    <header ref={headerRef} className="fixed inset-x-0 top-0 z-50">
      <div className={cn('transition-all duration-500', capsule && 'px-3 pt-3 md:px-6')}>
        <div
          className={cn(
            'mx-auto flex items-center justify-between border-b border-fg/10 bg-bg/90 text-fg backdrop-blur-xl transition-all duration-500 supports-[backdrop-filter]:bg-bg/80',
            capsule ? 'h-14 max-w-5xl rounded-full border px-4 shadow-[0_12px_40px_-24px_rgba(0,0,0,.5)] md:px-6' : cn('w-full container-x', scrolled ? 'h-14 md:h-16' : 'h-16 md:h-20'),
          )}
        >
          <a href="index.html" aria-label="Top Rhododendrons, naar de homepage" className="flex items-center"><Logo size="sm" /></a>
          <nav className="hidden items-center gap-7 lg:flex" aria-label="Hoofdnavigatie">
            {links.map((l) => <a key={l.label} href={l.href} aria-current={l.current ? 'page' : undefined} className={cn(linkCls, (l.strong || l.current) && 'font-medium text-fg')}>{l.label}</a>)}
          </nav>
          <div className="flex items-center gap-3">
            <div className="hidden lg:block">{cta()}</div>
            <button type="button" onClick={() => setOpen(!open)} aria-expanded={open} aria-controls="mobile-menu" aria-label={open ? 'Menu sluiten' : 'Menu openen'} className="relative flex size-11 items-center justify-center rounded-full border border-fg/25 text-fg lg:hidden">
              <span className={cn('absolute h-px w-5 bg-current transition-transform duration-300', open ? 'rotate-45' : '-translate-y-[3px]')} />
              <span className={cn('absolute h-px w-5 bg-current transition-transform duration-300', open ? '-rotate-45' : 'translate-y-[3px]')} />
            </button>
          </div>
        </div>
      </div>
      <MobileMenu open={open} top={top} links={links} cta={cta(() => setOpen(false))} onClose={() => setOpen(false)} />
    </header>
  )
}

function MobileMenu({ open, top, links, cta, onClose }: { open: boolean; top: number; links: NavLink[]; cta: React.ReactNode; onClose: () => void }) {
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
        <motion.div ref={ref} id="mobile-menu" role="dialog" aria-modal="true" aria-label="Menu" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} transition={{ duration: 0.2 }} style={{ top }} className="fixed inset-x-0 bottom-0 z-40 flex flex-col justify-between overflow-y-auto bg-bg px-6 pb-8 pt-4 text-fg lg:hidden">
          <nav className="flex flex-col" aria-label="Mobiele navigatie">
            {links.map((l, i) => (
              <motion.a key={l.label} href={l.href} onClick={onClose} initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.05 + i * 0.04 }} className="border-b border-fg/10 py-4 font-display text-[26px] leading-none">{l.label}</motion.a>
            ))}
          </nav>
          <div className="mt-6 flex flex-col gap-3 [&>a]:w-full [&>button]:w-full">
            {cta}
            <div className="grid grid-cols-2 gap-3">
              <Button href={company.phone1Href} variant="outline" size="md"><Phone className="size-4" aria-hidden="true" />Bel ons</Button>
              <Button href={company.whatsapp} {...ext} variant="outline" size="md"><WhatsAppIcon className="size-4" />WhatsApp</Button>
            </div>
          </div>
        </motion.div>
      )}
    </AnimatePresence>,
    document.body,
  )
}
