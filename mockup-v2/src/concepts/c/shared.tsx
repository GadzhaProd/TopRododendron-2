import type { ReactNode } from 'react'
import { cn } from '@/lib/utils'
import { SiteHeader } from '@/components/ui/site-header'
import { Button } from '@/components/ui/button'
import { FooterSuite } from '@/components/ui/footer-suite'
import { company } from '@/data/content'

/* Logo C — "Blad": a geometric leaf-monogram (T + leaf) in a soft square. */
export function MarkC({ className }: { className?: string }) {
  return (
    <svg viewBox="0 0 40 40" className={className} aria-hidden="true">
      <rect x="1" y="1" width="38" height="38" rx="11" fill="currentColor" />
      <path d="M12 13h16" stroke="var(--color-bg)" strokeWidth="2.6" strokeLinecap="round" />
      <path d="M20 13v15" stroke="var(--color-bg)" strokeWidth="2.6" strokeLinecap="round" />
      <path d="M20 28c0-6 3.5-9.5 9-9.5 0 6-3.5 9.5-9 9.5Z" fill="var(--color-bg)" />
    </svg>
  )
}
export function LogoC({ dark = false, size = 'md' }: { dark?: boolean; size?: 'sm' | 'md' | 'lg' }) {
  const s = { sm: ['size-8', 'text-[17px]'], md: ['size-10', 'text-[20px]'], lg: ['size-14', 'text-[26px]'] }[size]
  return (
    <span className={cn('inline-flex items-center gap-2.5', dark ? 'text-white' : 'text-fg')}>
      <MarkC className={s[0]} />
      <span className={cn('font-display font-semibold tracking-[-0.03em]', s[1])}>top rhododendrons</span>
    </span>
  )
}

const navHome = [
  { label: 'Planten', href: '#planten' },
  { label: 'Waarom wij', href: '#waarom' },
  { label: 'De kweker', href: '#kweker' },
  { label: 'Plantgids', href: '#plantgids' },
  { label: 'Groothandel', href: 'groothandel.html', strong: true },
]
const navB2b = [
  { label: 'Projecten', href: '#doelgroepen' },
  { label: 'Werkwijze', href: '#werkwijze' },
  { label: 'Voorraad', href: '#maten' },
  { label: 'Offerte', href: '#offerte' },
  { label: 'Particulier', href: 'index.html', strong: true },
]

export function HeaderC({ b2b = false }: { b2b?: boolean }) {
  return (
    <SiteHeader
      mode="capsule"
      logo={({ dark }) => <LogoC dark={dark} size="sm" />}
      links={b2b ? navB2b : navHome}
      solidClassName="border-fg/10 bg-surface/85 shadow-[0_16px_50px_-28px_rgba(0,0,0,.45)]"
      cta={({ dark }) => (b2b
        ? <Button href="#offerte" variant={dark ? 'white' : 'solid'} size="sm">Offerte aanvragen</Button>
        : <Button href="#planten" variant={dark ? 'white' : 'solid'} size="sm">Bestellen</Button>)}
    />
  )
}

export function FooterC() {
  return (
    <FooterSuite
      logo={<LogoC size="sm" />}
      wordmark="top rhododendrons"
      wordmarkClassName="font-semibold tracking-[-0.05em]"
      links={[{ label: 'Planten', href: 'index.html#planten' }, { label: 'Waarom wij', href: 'index.html#waarom' }, { label: 'De kweker', href: 'index.html#kweker' }, { label: 'Plantgids', href: 'index.html#plantgids' }, { label: 'Groothandel', href: 'groothandel.html' }]}
      className="bg-bg-2"
    />
  )
}

export function HeadC({ eyebrow, title, text, className, align = 'left', dark = false, size = 'md' }: { eyebrow?: string; title: ReactNode; text?: ReactNode; className?: string; align?: 'left' | 'center'; dark?: boolean; size?: 'md' | 'lg' }) {
  return (
    <div className={cn('flex flex-col gap-4', align === 'center' && 'items-center text-center', className)}>
      {eyebrow && <p className={cn('eyebrow', dark ? 'text-white/60' : 'text-muted')}>{eyebrow}</p>}
      <h2 className={cn('font-display text-balance max-w-[20ch] leading-[1.02]', size === 'lg' ? 'text-[clamp(36px,5vw,68px)]' : 'text-[clamp(30px,3.8vw,52px)]')}>{title}</h2>
      {text && <p className={cn('max-w-[52ch] text-[16px] leading-relaxed md:text-[17px]', dark ? 'text-white/70' : 'text-fg-2')}>{text}</p>}
    </div>
  )
}

export function Pill({ children, className }: { children: ReactNode; className?: string }) {
  return <span className={cn('inline-flex h-8 items-center rounded-full border border-fg/12 bg-surface px-3.5 text-[12.5px] font-medium text-fg-2', className)}>{children}</span>
}

export function ContactC({ dark = false }: { dark?: boolean }) {
  const t = dark ? 'text-white' : 'text-fg'
  const m = dark ? 'text-white/60' : 'text-muted'
  return (
    <div className={cn('grid gap-8 md:grid-cols-3', t)}>
      <div><p className={cn('eyebrow mb-3', m)}>Kwekerij &amp; kantoor</p><a href={company.maps} className="font-display text-[22px] leading-tight">{company.street}<br />{company.postal}</a><p className={cn('mt-2 text-[14px]', m)}>Afhalen op afspraak.</p></div>
      <div><p className={cn('eyebrow mb-3', m)}>Bereikbaar</p><a href={company.phone1Href} className="block font-display text-[22px] leading-tight">{company.phone1}</a><a href={company.phone2Href} className="block font-display text-[22px] leading-tight">{company.phone2}</a><a href={`mailto:${company.email}`} className={cn('mt-2 block text-[14px]', m)}>{company.email}</a></div>
      <div><p className={cn('eyebrow mb-3', m)}>Openingstijden</p>{company.hours.map(([d, h]) => <p key={d} className={cn('flex justify-between gap-6 border-b py-1.5 text-[14px]', dark ? 'border-white/10' : 'border-fg/10')}><span className={m}>{d}</span><span>{h}</span></p>)}</div>
    </div>
  )
}
