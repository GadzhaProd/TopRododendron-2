// Footer of concept C ("Footer with Suite", round 2, post-audit): link columns,
// an oversized brand wordmark and a bottom bar. Compact on the homepage (the
// contact block sits right above it), full on the other pages.
import { cn } from '@/lib/utils'
import { Logo } from './logo'
import { ext } from './button'
import { company } from '@/data/content'

export function SiteFooter({ home = false }: { home?: boolean }) {
  const compact = home
  const p = home ? '' : 'index.html'
  const links = [
    { label: 'Planten', href: home ? '#planten' : 'assortiment.html' },
    { label: 'De kweker', href: `${p}#kweker` },
    { label: 'Advies', href: `${p}#advies` },
    { label: 'Plantgids', href: 'plantgids.html' },
    { label: 'Groothandel', href: 'groothandel.html' },
  ]
  const t = 'text-fg', m = 'text-muted'
  const link = cn('py-1 text-[14px] transition-colors hover:opacity-60', t)
  return (
    <footer className="relative w-full overflow-hidden bg-bg-2">
      <div className={cn('container-x grid gap-10 pt-14 pb-6', compact ? 'md:grid-cols-[1.4fr_1fr_1fr]' : 'md:grid-cols-4')}>
        <div className="flex flex-col gap-4"><Logo size="sm" caption /><p className={cn('max-w-[30ch] text-[14px] leading-relaxed', m)}>Familiekwekerij van rhododendrons op de Veluwe. Veenrijke bodem, sterk wortelstelsel, aangroeigarantie.</p></div>
        <div className="flex flex-col"><p className={cn('eyebrow mb-2', m)}>Navigatie</p>{links.map((x) => <a key={x.label} href={x.href} className={link}>{x.label}</a>)}</div>
        {compact ? (
          <div className="flex flex-col gap-1">
            <p className={cn('eyebrow mb-2', m)}>Contact</p>
            <a href={company.phone1Href} className={cn('text-[14px]', t)}>{company.phone1}</a>
            <a href={`mailto:${company.email}`} className={cn('text-[14px]', t)}>{company.email}</a>
            <a href={company.instagram} {...ext} className={cn('text-[14px]', t)}>Instagram · {company.instagramHandle}</a>
          </div>
        ) : (
          <>
            <div className="flex flex-col gap-1">
              <p className={cn('eyebrow mb-2', m)}>Kwekerij</p>
              <a href={company.maps} {...ext} className={cn('text-[14px] leading-relaxed', t)}>{company.street}<br />{company.postal}</a>
              <a href={`mailto:${company.email}`} className={cn('mt-2 text-[14px]', t)}>{company.email}</a>
              <a href={company.phone1Href} className={cn('text-[14px]', t)}>{company.phone1}</a>
              <a href={company.phone2Href} className={cn('text-[14px]', t)}>{company.phone2}</a>
            </div>
            <div className="flex flex-col gap-1">
              <p className={cn('eyebrow mb-2', m)}>Open</p>
              {company.hours.map(([d, h]) => <p key={d} className={cn('flex justify-between gap-4 text-[14px]', t)}><span className={m}>{d}</span><span>{h}</span></p>)}
              <a href={company.instagram} {...ext} className={cn('mt-3 text-[14px]', t)}>Instagram · {company.instagramHandle}</a>
            </div>
          </>
        )}
      </div>
      <p aria-hidden="true" className={cn('container-x select-none font-display font-semibold leading-[0.85] tracking-[-0.05em] whitespace-nowrap', t)} style={{ fontSize: 'clamp(2.2rem, 10.6vw, 11.2rem)' }}>Top Rhododendrons</p>
      <div className="container-x mt-4 flex flex-wrap items-center justify-between gap-3 border-t border-fg/10 py-4">
        <p className={cn('text-[13px]', m)}>© 2026 {company.name} · KvK {company.kvk}</p>
        <p className={cn('text-[13px]', m)}><a href={company.voorwaarden} {...ext} className="hover:opacity-70">Voorwaarden</a> · <a href={company.privacy} {...ext} className="hover:opacity-70">Privacy</a></p>
      </div>
    </footer>
  )
}
