// Adapted from 21st.dev "Header 1" (efferd) — sticky header with scroll blur and a
// portal mobile menu — merged with the floating-capsule idea of "Morphing Scroll
// Navbar" (laziekiki). The bar is a translucent frosted strip from the very first
// pixel (AA contrast over the video), compacts after scrolling; the mobile menu is
// a real dialog (Escape, focus trap, inert page, measured top offset).
import * as React from 'react'
import { createPortal } from 'react-dom'
import { AnimatePresence, motion } from 'framer-motion'
import { cn } from '@/lib/utils'
import { cartStore, cartCount } from '@/lib/store'

export function useScrolled(threshold = 24) {
  const [s, setS] = React.useState(false)
  React.useEffect(() => {
    const h = () => setS(window.scrollY > threshold)
    h(); window.addEventListener('scroll', h, { passive: true })
    return () => window.removeEventListener('scroll', h)
  }, [threshold])
  return s
}

export type NavLink = { label: string; href: string; strong?: boolean }

export interface SiteHeaderProps {
  logo: (opts: { dark: boolean }) => React.ReactNode
  links: NavLink[]
  cta?: (opts: { dark: boolean }) => React.ReactNode
  /** light: frosted light bar with dark text; dark: frosted night bar with light text */
  tone?: 'light' | 'dark'
  mode?: 'bar' | 'capsule'
  barClassName?: string
}

export function useCartCount() { return cartCount(cartStore.use()) }

export function SiteHeader({ logo, links, cta, tone = 'light', mode = 'bar', barClassName }: SiteHeaderProps) {
  const [open, setOpen] = React.useState(false)
  const scrolled = useScrolled(24)
  const dark = tone === 'dark'
  const headerRef = React.useRef<HTMLElement>(null)
  const [top, setTop] = React.useState(64)

  React.useEffect(() => {
    document.body.style.overflow = open ? 'hidden' : ''
    const main = document.querySelector('main')
    if (open) { main?.setAttribute('inert', ''); setTop(headerRef.current?.getBoundingClientRect().bottom ?? 64) } else main?.removeAttribute('inert')
    return () => { document.body.style.overflow = ''; main?.removeAttribute('inert') }
  }, [open])

  const bar = dark
    ? 'bg-night/85 text-white border-white/10 supports-[backdrop-filter]:bg-night/75'
    : 'bg-bg/90 text-fg border-fg/10 supports-[backdrop-filter]:bg-bg/80'
  const linkCls = cn('text-[14px] tracking-[0.01em] transition-colors', dark ? 'text-white/85 hover:text-white' : 'text-fg-2 hover:text-fg')

  return (
    <header ref={headerRef} className={cn('fixed inset-x-0 top-0 z-50', dark && 'on-dark')}>
      <div className={cn('transition-all duration-500', mode === 'capsule' && scrolled && !open && 'px-3 pt-3 md:px-6')}>
        <div
          className={cn(
            'mx-auto flex items-center justify-between border-b backdrop-blur-xl transition-all duration-500',
            bar, barClassName,
            mode === 'capsule' && scrolled && !open
              ? 'h-14 max-w-5xl rounded-full border px-4 shadow-[0_12px_40px_-24px_rgba(0,0,0,.5)] md:px-6'
              : cn('w-full container-x', scrolled ? 'h-14 md:h-16' : 'h-16 md:h-20'),
          )}
        >
          <a href="index.html" aria-label="Top Rhododendrons, naar de homepage" className="flex items-center">
            {logo({ dark })}
          </a>
          <nav className="hidden items-center gap-7 lg:flex" aria-label="Hoofdnavigatie">
            {links.map((l) => (
              <a key={l.label} href={l.href} className={cn(linkCls, l.strong && 'font-medium')}>{l.label}</a>
            ))}
          </nav>
          <div className="flex items-center gap-3">
            <div className="hidden lg:block">{cta?.({ dark })}</div>
            <button
              type="button"
              onClick={() => setOpen(!open)}
              aria-expanded={open}
              aria-controls="mobile-menu"
              aria-label={open ? 'Menu sluiten' : 'Menu openen'}
              className={cn('relative flex size-11 items-center justify-center rounded-full border lg:hidden', dark ? 'border-white/40 text-white' : 'border-fg/25 text-fg')}
            >
              <span className={cn('absolute h-px w-5 bg-current transition-transform duration-300', open ? 'rotate-45' : '-translate-y-[3px]')} />
              <span className={cn('absolute h-px w-5 bg-current transition-transform duration-300', open ? '-rotate-45' : 'translate-y-[3px]')} />
            </button>
          </div>
        </div>
      </div>
      <MobileMenu open={open} top={top} dark={dark} links={links} cta={cta?.({ dark })} onClose={() => setOpen(false)} />
    </header>
  )
}

function MobileMenu({ open, top, dark, links, cta, onClose }: { open: boolean; top: number; dark: boolean; links: NavLink[]; cta?: React.ReactNode; onClose: () => void }) {
  const ref = React.useRef<HTMLDivElement>(null)
  React.useEffect(() => {
    if (!open) return
    const el = ref.current
    const focusables = () => Array.from(el?.querySelectorAll<HTMLElement>('a[href], button:not([disabled])') ?? [])
    focusables()[0]?.focus()
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') { e.preventDefault(); onClose(); document.querySelector<HTMLElement>('[aria-controls="mobile-menu"]')?.focus(); return }
      if (e.key !== 'Tab') return
      const f = focusables(); if (!f.length) return
      const first = f[0], last = f[f.length - 1]
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus() }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus() }
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
          initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} transition={{ duration: 0.2 }}
          style={{ top }}
          className={cn('fixed inset-x-0 bottom-0 z-40 flex flex-col justify-between overflow-y-auto px-6 pb-8 pt-4 lg:hidden', dark ? 'bg-night text-white on-dark' : 'bg-bg text-fg')}
        >
          <nav className="flex flex-col" aria-label="Mobiele navigatie">
            {links.map((l, i) => (
              <motion.a
                key={l.label} href={l.href} onClick={onClose}
                initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.05 + i * 0.04 }}
                className={cn('border-b py-4 font-display text-[26px] leading-none', dark ? 'border-white/15' : 'border-fg/10')}
              >
                {l.label}
              </motion.a>
            ))}
          </nav>
          <div className="mt-6 flex flex-col gap-3 [&>a]:w-full">{cta}</div>
        </motion.div>
      )}
    </AnimatePresence>,
    document.body,
  )
}
