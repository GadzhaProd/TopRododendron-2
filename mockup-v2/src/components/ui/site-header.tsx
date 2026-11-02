// Adapted from 21st.dev "Header 1" (efferd) — sticky header with scroll blur and
// portal mobile menu — merged with the floating-capsule idea of "Morphing Scroll
// Navbar" (laziekiki). Transparent over the video hero, solid after scrolling.
import * as React from 'react'
import { createPortal } from 'react-dom'
import { AnimatePresence, motion } from 'framer-motion'
import { cn } from '@/lib/utils'

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
  variant?: 'overlay' | 'solid'
  mode?: 'bar' | 'capsule'
  solidClassName?: string
  darkWhenSolid?: boolean
}

export function SiteHeader({ logo, links, cta, variant = 'overlay', mode = 'bar', solidClassName, darkWhenSolid = false }: SiteHeaderProps) {
  const [open, setOpen] = React.useState(false)
  const scrolled = useScrolled(24)
  const overlay = variant === 'overlay' && !scrolled && !open
  const dark = overlay || darkWhenSolid

  React.useEffect(() => {
    document.body.style.overflow = open ? 'hidden' : ''
    return () => { document.body.style.overflow = '' }
  }, [open])

  const linkCls = cn('text-[13.5px] tracking-[0.02em] transition-colors', dark ? 'text-white/85 hover:text-white' : 'text-fg-2 hover:text-fg')

  return (
    <header className={cn('fixed inset-x-0 top-0 z-50', dark && 'on-dark')}>
      <div className={cn('transition-all duration-500', mode === 'capsule' && scrolled && 'px-3 pt-3 md:px-6')}>
        <div
          className={cn(
            'mx-auto flex items-center justify-between transition-all duration-500',
            mode === 'capsule'
              ? scrolled
                ? cn('h-14 max-w-5xl rounded-full border px-4 backdrop-blur-xl md:px-6', solidClassName ?? 'border-fg/10 bg-bg/85 shadow-[0_12px_40px_-24px_rgba(0,0,0,.5)]')
                : 'h-20 w-full container-x'
              : cn('h-16 w-full container-x md:h-20', scrolled || open ? (solidClassName ?? 'border-b border-fg/10 bg-bg/90 backdrop-blur-xl') : 'border-b border-transparent'),
          )}
        >
          <a href="index.html" aria-label="Top Rhododendrons, naar de homepage" className="flex items-center">
            {logo({ dark })}
          </a>
          <nav className="hidden items-center gap-7 md:flex" aria-label="Hoofdnavigatie">
            {links.map((l) => (
              <a key={l.label} href={l.href} className={cn(linkCls, l.strong && 'font-medium')}>{l.label}</a>
            ))}
          </nav>
          <div className="flex items-center gap-3">
            <div className="hidden md:block">{cta?.({ dark })}</div>
            <button
              type="button"
              onClick={() => setOpen(!open)}
              aria-expanded={open}
              aria-controls="mobile-menu"
              aria-label={open ? 'Menu sluiten' : 'Menu openen'}
              className={cn('relative flex size-11 items-center justify-center rounded-full border md:hidden', dark ? 'border-white/40 text-white' : 'border-fg/20 text-fg')}
            >
              <span className={cn('absolute h-px w-5 bg-current transition-transform duration-300', open ? 'rotate-45' : '-translate-y-[3px]')} />
              <span className={cn('absolute h-px w-5 bg-current transition-transform duration-300', open ? '-rotate-45' : 'translate-y-[3px]')} />
            </button>
          </div>
        </div>
      </div>
      <MobileMenu open={open} links={links} cta={cta?.({ dark: false })} onNavigate={() => setOpen(false)} />
    </header>
  )
}

function MobileMenu({ open, links, cta, onNavigate }: { open: boolean; links: NavLink[]; cta?: React.ReactNode; onNavigate: () => void }) {
  if (typeof window === 'undefined') return null
  return createPortal(
    <AnimatePresence>
      {open && (
        <motion.div
          id="mobile-menu"
          initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} transition={{ duration: 0.25 }}
          className="fixed inset-x-0 top-16 bottom-0 z-40 flex flex-col justify-between bg-bg px-6 pb-8 pt-6 md:hidden"
        >
          <nav className="flex flex-col" aria-label="Mobiele navigatie">
            {links.map((l, i) => (
              <motion.a
                key={l.label} href={l.href} onClick={onNavigate}
                initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.05 + i * 0.05 }}
                className="border-b border-fg/10 py-4 font-display text-[28px] leading-none text-fg"
              >
                {l.label}
              </motion.a>
            ))}
          </nav>
          <div className="flex flex-col gap-3">{cta}</div>
        </motion.div>
      )}
    </AnimatePresence>,
    document.body,
  )
}
