import type { ReactNode } from 'react'
import { cn } from '@/lib/utils'
import { SiteHeader, useCartCount } from '@/components/ui/site-header'
import { Button } from '@/components/ui/button'
import { FooterSuite } from '@/components/ui/footer-suite'
import { company } from '@/data/content'

/* Logo B — "Zegel": TR monogram in a double ring; the full seal carries a ring
   text fitted to the path length (textLength), the simple seal is used small. */
export function SealB({ className, id = 'sealB', simple = false }: { className?: string; id?: string; simple?: boolean }) {
  return (
    <svg viewBox="0 0 100 100" className={className} aria-hidden="true" fill="none">
      <defs><path id={`${id}-ring`} d="M50,50 m-36,0 a36,36 0 1,1 72,0 a36,36 0 1,1 -72,0" /></defs>
      <circle cx="50" cy="50" r="47" stroke="currentColor" strokeWidth="1.2" />
      <circle cx="50" cy="50" r={simple ? 40 : 27} stroke="currentColor" strokeWidth=".9" opacity=".8" />
      {!simple && (
        <text fontSize="7.6" fill="currentColor" fontFamily="Figtree, system-ui, sans-serif" fontWeight="500" textLength="222" lengthAdjust="spacing">
          <textPath href={`#${id}-ring`} startOffset="0" textLength="222" lengthAdjust="spacing">TOP RHODODENDRONS · OTTERLO · 2001 ·</textPath>
        </text>
      )}
      <text x="50" y={simple ? 61 : 59} textAnchor="middle" fontSize={simple ? 30 : 25} fill="currentColor" fontFamily="Marcellus, Georgia, serif">TR</text>
    </svg>
  )
}
export function LogoB({ dark = false, size = 'md', caption = false }: { dark?: boolean; size?: 'sm' | 'md' | 'lg'; caption?: boolean }) {
  const s = { sm: ['size-9', 'text-[15px]', 'text-[10px]'], md: ['size-12', 'text-[18px]', 'text-[10px]'], lg: ['size-24', 'text-[24px]', 'text-[11px]'] }[size]
  return (
    <span className={cn('inline-flex items-center gap-3', dark ? 'text-[#f1ece3]' : 'text-fg')}>
      <SealB simple className={cn(s[0], dark ? 'text-brass' : 'text-accent-2')} id={`seal-${size}-${dark ? 'd' : 'l'}`} />
      <span className="flex flex-col leading-none">
        <span className={cn('font-display tracking-[0.12em]', s[1])}>Top Rhododendrons</span>
        {caption && <span className={cn('mt-1.5 tracking-[0.24em] uppercase opacity-80', s[2])}>Kwekerij op de Veluwe · 2001</span>}
      </span>
    </span>
  )
}

const navHome = [
  { label: 'Collectie', href: '#collectie' },
  { label: 'De kwekerij', href: '#kwekerij' },
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

function CartCta() {
  const n = useCartCount()
  return <Button href="#collectie" variant="outline" size="sm">{n > 0 ? `Winkelwagen (${n})` : 'Bestellen'}</Button>
}

export function HeaderB({ b2b = false }: { b2b?: boolean }) {
  return (
    <SiteHeader
      tone="light"
      logo={() => <LogoB size="sm" />}
      links={b2b ? navB2b : navHome}
      cta={() => (b2b ? <Button href="#offerte" variant="solid" size="sm">Offerte aanvragen</Button> : <CartCta />)}
    />
  )
}

export function FooterB({ compact = false }: { compact?: boolean }) {
  return (
    <FooterSuite
      dark
      compact={compact}
      logo={<LogoB dark size="sm" caption />}
      wordmark="Top Rhododendrons"
      wordmarkSize="clamp(2rem, 8.9vw, 9.4rem)"
      wordmarkClassName="text-brass/90 tracking-[0.06em]"
      links={[{ label: 'Collectie', href: 'index.html#collectie' }, { label: 'De kwekerij', href: 'index.html#kwekerij' }, { label: 'Advies', href: 'index.html#advies' }, { label: 'Groothandel', href: 'groothandel.html' }, { label: 'Bezoek', href: 'index.html#bezoek' }]}
      className="night border-t border-white/10"
    />
  )
}

export function Rule({ className, dark = false }: { className?: string; dark?: boolean }) { return <div className={cn('gold-rule w-full', dark && 'opacity-80', className)} aria-hidden="true" /> }

export function HeadB({ eyebrow, title, text, className, align = 'center', dark = false }: { eyebrow?: string; title: ReactNode; text?: ReactNode; className?: string; align?: 'left' | 'center'; dark?: boolean }) {
  return (
    <div className={cn('flex flex-col gap-5', align === 'center' && 'items-center text-center', className)}>
      {eyebrow && <p className={cn('eyebrow', dark ? 'text-brass' : 'text-accent-2')}>{eyebrow}</p>}
      <h2 className="max-w-[min(22ch,100%)] font-display text-[clamp(30px,3.8vw,52px)] text-balance leading-[1.1]">{title}</h2>
      {text && <p className={cn('max-w-[56ch] text-[16px] leading-relaxed md:text-[17px]', dark ? 'text-white/80' : 'text-fg-2')}>{text}</p>}
    </div>
  )
}

export function ContactB() {
  return (
    <div className="grid grid-cols-1 gap-10 md:grid-cols-3">
      <div><p className="eyebrow mb-3 text-accent-2">Kwekerij &amp; kantoor</p><a href={company.maps} className="font-display text-[22px] leading-snug">{company.street}<br />{company.postal}</a><p className="mt-2 text-[14px] text-muted">{company.region}. {company.pickup}</p></div>
      <div><p className="eyebrow mb-3 text-accent-2">Bereikbaar</p><a href={company.phone1Href} className="block font-display text-[22px]">{company.phone1}</a><a href={company.phone2Href} className="block font-display text-[22px]">{company.phone2}</a><a href={`mailto:${company.email}`} className="mt-2 block text-[14px] text-muted">{company.email}</a></div>
      <div><p className="eyebrow mb-3 text-accent-2">Openingstijden</p>{company.hours.map(([d, h]) => <p key={d} className="flex justify-between gap-6 border-b border-fg/10 py-1.5 text-[14px]"><span className="text-muted">{d}</span><span>{h}</span></p>)}</div>
    </div>
  )
}
