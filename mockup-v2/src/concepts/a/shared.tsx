import type { ReactNode } from 'react'
import { cn } from '@/lib/utils'
import { SiteHeader, useCartCount } from '@/components/ui/site-header'
import { Button } from '@/components/ui/button'
import { FooterSuite } from '@/components/ui/footer-suite'
import { company } from '@/data/content'

/* Logo A — "Truss": seven petals around a centre, a single hairline ring. */
export function MarkA({ className }: { className?: string }) {
  const petals = Array.from({ length: 7 }, (_, i) => (i * 360) / 7)
  return (
    <svg viewBox="0 0 48 48" className={className} aria-hidden="true" fill="none" stroke="currentColor" strokeWidth="1.1">
      <circle cx="24" cy="24" r="22.5" opacity=".55" />
      {petals.map((a) => <ellipse key={a} cx="24" cy="14.5" rx="4.2" ry="8.5" transform={`rotate(${a} 24 24)`} />)}
      <circle cx="24" cy="24" r="2.2" fill="currentColor" stroke="none" />
    </svg>
  )
}
export function LogoA({ dark = false, size = 'md', caption = false }: { dark?: boolean; size?: 'sm' | 'md' | 'lg'; caption?: boolean }) {
  const s = { sm: ['size-8', 'text-[19px]', 'text-[10px]'], md: ['size-9', 'text-[21px]', 'text-[10px]'], lg: ['size-12', 'text-[28px]', 'text-[11px]'] }[size]
  return (
    <span className={cn('inline-flex items-center gap-3', dark ? 'text-white' : 'text-fg')}>
      <MarkA className={s[0]} />
      <span className="flex flex-col leading-none">
        <span className={cn('font-display tracking-[0.01em]', s[1])}>Top Rhododendrons</span>
        {caption && <span className={cn('mt-1.5 tracking-[0.22em] uppercase opacity-80', s[2])}>Kwekerij · Otterlo · sinds 2001</span>}
      </span>
    </span>
  )
}

export const navHome = [
  { label: 'Assortiment', href: '#assortiment' },
  { label: 'De kwekerij', href: '#kwekerij' },
  { label: 'Advies', href: '#advies' },
  { label: 'Contact', href: '#contact' },
  { label: 'Groothandel', href: 'groothandel.html', strong: true },
]
export const navB2b = [
  { label: 'Doelgroepen', href: '#doelgroepen' },
  { label: 'Werkwijze', href: '#werkwijze' },
  { label: 'Maten & voorraad', href: '#maten' },
  { label: 'Offerte', href: '#offerte' },
  { label: 'Particulier', href: 'index.html', strong: true },
]

function CartCta() {
  const n = useCartCount()
  return <Button href="#assortiment" variant="outline" size="sm">{n > 0 ? `Winkelwagen (${n})` : 'Bestellen'}</Button>
}

export function HeaderA({ b2b = false }: { b2b?: boolean }) {
  return (
    <SiteHeader
      tone="light"
      logo={() => <LogoA size="sm" />}
      links={b2b ? navB2b : navHome}
      cta={() => (b2b ? <Button href="#offerte" variant="solid" size="sm">Offerte aanvragen</Button> : <CartCta />)}
    />
  )
}

export function FooterA({ compact = false }: { compact?: boolean }) {
  return (
    <FooterSuite
      compact={compact}
      logo={<LogoA size="sm" caption />}
      wordmark="Top Rhododendrons"
      wordmarkSize="clamp(2.4rem, 13.6vw, 14rem)"
      links={[{ label: 'Assortiment', href: 'index.html#assortiment' }, { label: 'De kwekerij', href: 'index.html#kwekerij' }, { label: 'Advies', href: 'index.html#advies' }, { label: 'Groothandel', href: 'groothandel.html' }, { label: 'Contact', href: 'index.html#contact' }]}
      className="border-t border-line bg-bg"
    />
  )
}

export function SectionHead({ eyebrow, title, text, className, align = 'left', dark = false }: { eyebrow?: string; title: ReactNode; text?: ReactNode; className?: string; align?: 'left' | 'center'; dark?: boolean }) {
  return (
    <div className={cn('flex flex-col gap-4', align === 'center' && 'items-center text-center', className)}>
      {eyebrow && <p className={cn('eyebrow', dark ? 'text-white/75' : 'text-muted')}>{eyebrow}</p>}
      <h2 className="max-w-[min(18ch,100%)] font-display text-[clamp(34px,4.4vw,60px)] text-balance leading-[1.02]">{title}</h2>
      {text && <p className={cn('max-w-[52ch] text-[16px] leading-relaxed md:text-[17px]', dark ? 'text-white/80' : 'text-fg-2')}>{text}</p>}
    </div>
  )
}

export function ContactStrip({ dark = false }: { dark?: boolean }) {
  const t = dark ? 'text-white' : 'text-fg'
  const m = dark ? 'text-white/75' : 'text-muted'
  return (
    <div className={cn('grid grid-cols-1 gap-8 md:grid-cols-3', t)}>
      <div><p className={cn('eyebrow mb-3', m)}>Kwekerij &amp; kantoor</p><a href={company.maps} className="font-display text-[24px] leading-tight">{company.street}<br />{company.postal}</a><p className={cn('mt-2 text-[14px]', m)}>{company.pickup}</p></div>
      <div><p className={cn('eyebrow mb-3', m)}>Bereikbaar</p><a href={company.phone1Href} className="block font-display text-[24px] leading-tight">{company.phone1}</a><a href={company.phone2Href} className="block font-display text-[24px] leading-tight">{company.phone2}</a><a href={`mailto:${company.email}`} className={cn('mt-2 block text-[14px]', m)}>{company.email}</a></div>
      <div><p className={cn('eyebrow mb-3', m)}>Openingstijden</p>{company.hours.map(([d, h]) => <p key={d} className="flex justify-between gap-6 border-b border-current/10 py-1.5 text-[14px]"><span className={m}>{d}</span><span>{h}</span></p>)}</div>
    </div>
  )
}
