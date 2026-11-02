import type { ReactNode } from 'react'
import { cn } from '@/lib/utils'
import { SiteHeader } from '@/components/ui/site-header'
import { Button } from '@/components/ui/button'
import { FooterSuite } from '@/components/ui/footer-suite'
import { company } from '@/data/content'

/* Logo B — "Zegel": a seal with the TR monogram, ring text OTTERLO · MMI. */
export function SealB({ className, id = 'sealB' }: { className?: string; id?: string }) {
  return (
    <svg viewBox="0 0 100 100" className={className} aria-hidden="true" fill="none">
      <defs><path id={`${id}-ring`} d="M50,50 m-36,0 a36,36 0 1,1 72,0 a36,36 0 1,1 -72,0" /></defs>
      <circle cx="50" cy="50" r="47" stroke="currentColor" strokeWidth="1" opacity=".8" />
      <circle cx="50" cy="50" r="27" stroke="currentColor" strokeWidth=".8" opacity=".7" />
      <text fontSize="7.4" letterSpacing="3.2" fill="currentColor" fontFamily="Figtree, system-ui, sans-serif" fontWeight="500">
        <textPath href={`#${id}-ring`} startOffset="2%">TOP RHODODENDRONS · OTTERLO · MMI ·</textPath>
      </text>
      <text x="50" y="59" textAnchor="middle" fontSize="25" fill="currentColor" fontFamily="Marcellus, Georgia, serif">TR</text>
    </svg>
  )
}
export function LogoB({ dark = true, size = 'md', stacked = false }: { dark?: boolean; size?: 'sm' | 'md' | 'lg'; stacked?: boolean }) {
  const s = { sm: ['size-10', 'text-[15px]', 'text-[8px]'], md: ['size-14', 'text-[19px]', 'text-[9px]'], lg: ['size-28', 'text-[26px]', 'text-[10px]'] }[size]
  return (
    <span className={cn('inline-flex items-center gap-3', stacked && 'flex-col gap-4 text-center', dark ? 'text-[#f1ece3]' : 'text-[#11130f]')}>
      <SealB className={cn(s[0], 'text-accent')} id={`seal-${size}-${stacked ? 's' : 'i'}`} />
      <span className="flex flex-col leading-none">
        <span className={cn('font-display uppercase tracking-[0.18em]', s[1])}>Top Rhododendrons</span>
        <span className={cn('mt-1.5 tracking-[0.3em] uppercase opacity-60', s[2])}>Kwekerij op de Veluwe</span>
      </span>
    </span>
  )
}

const navHome = [
  { label: 'Collectie', href: '#collectie' },
  { label: 'Het landgoed', href: '#kwekerij' },
  { label: 'Advies', href: '#advies' },
  { label: 'Bezoek', href: '#bezoek' },
  { label: 'Groothandel', href: 'groothandel.html', strong: true },
]
const navB2b = [
  { label: 'Projecten', href: '#doelgroepen' },
  { label: 'Werkwijze', href: '#werkwijze' },
  { label: 'Voorraad', href: '#maten' },
  { label: 'Offerte', href: '#offerte' },
  { label: 'Particulier', href: 'index.html', strong: true },
]

export function HeaderB({ b2b = false }: { b2b?: boolean }) {
  return (
    <SiteHeader
      logo={() => <LogoB size="sm" />}
      links={b2b ? navB2b : navHome}
      darkWhenSolid
      solidClassName="border-b border-white/10 bg-[#0f1412]/85 backdrop-blur-xl"
      cta={() => (b2b
        ? <Button href="#offerte" variant="solid" size="sm">Offerte aanvragen</Button>
        : <Button href="#collectie" variant="outline-white" size="sm">Bestellen</Button>)}
    />
  )
}

export function FooterB() {
  return (
    <FooterSuite
      dark
      logo={<LogoB size="sm" />}
      wordmark="TOP RHODODENDRONS"
      wordmarkSize="clamp(1.6rem, 7.4vw, 8.5rem)"
      wordmarkClassName="text-accent/90 uppercase tracking-[0.04em]"
      links={[{ label: 'Collectie', href: 'index.html#collectie' }, { label: 'Het landgoed', href: 'index.html#kwekerij' }, { label: 'Advies', href: 'index.html#advies' }, { label: 'Groothandel', href: 'groothandel.html' }, { label: 'Bezoek', href: 'index.html#bezoek' }]}
      className="border-t border-white/10 bg-[#0b0f0d] text-white"
    />
  )
}

export function Rule({ className }: { className?: string }) { return <div className={cn('gold-rule w-full', className)} aria-hidden="true" /> }

export function HeadB({ eyebrow, title, text, className, align = 'center' }: { eyebrow?: string; title: ReactNode; text?: ReactNode; className?: string; align?: 'left' | 'center' }) {
  return (
    <div className={cn('flex flex-col gap-5', align === 'center' && 'items-center text-center', className)}>
      {eyebrow && <p className="eyebrow text-accent">{eyebrow}</p>}
      <h2 className="font-display text-[clamp(30px,3.8vw,52px)] leading-[1.08] text-balance max-w-[22ch]">{title}</h2>
      {text && <p className="max-w-[56ch] text-[16px] leading-relaxed text-fg-2 md:text-[17px]">{text}</p>}
    </div>
  )
}

export function ContactB() {
  return (
    <div className="grid gap-10 md:grid-cols-3">
      <div><p className="eyebrow mb-3 text-accent">Landgoed &amp; kantoor</p><a href={company.maps} className="font-display text-[22px] leading-snug">{company.street}<br />{company.postal}</a><p className="mt-2 text-[14px] text-muted">{company.region}. Afhalen op afspraak.</p></div>
      <div><p className="eyebrow mb-3 text-accent">Bereikbaar</p><a href={company.phone1Href} className="block font-display text-[22px]">{company.phone1}</a><a href={company.phone2Href} className="block font-display text-[22px]">{company.phone2}</a><a href={`mailto:${company.email}`} className="mt-2 block text-[14px] text-muted">{company.email}</a></div>
      <div><p className="eyebrow mb-3 text-accent">Openingstijden</p>{company.hours.map(([d, h]) => <p key={d} className="flex justify-between gap-6 border-b border-white/10 py-1.5 text-[14px]"><span className="text-muted">{d}</span><span>{h}</span></p>)}</div>
    </div>
  )
}
