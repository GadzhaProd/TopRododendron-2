// Adapted from 21st.dev "Footer with Suite" (scrollxui): uppercase micro-links in
// two columns and an oversized brand wordmark above the bottom bar. Extended with
// address / hours columns and a logo slot.
import type { ReactNode } from 'react'
import { cn } from '@/lib/utils'
import { company } from '@/data/content'

export function FooterSuite({ links, wordmark, logo, dark = false, className, wordmarkClassName }: { links: { label: string; href: string }[]; wordmark: string; logo?: ReactNode; dark?: boolean; className?: string; wordmarkClassName?: string }) {
  const t = dark ? 'text-white' : 'text-fg'
  const m = dark ? 'text-white/55' : 'text-muted'
  const l = dark ? 'border-white/15' : 'border-fg/10'
  const link = cn('eyebrow py-1 transition-colors hover:opacity-60', t)
  return (
    <footer className={cn('relative w-full overflow-hidden', dark && 'on-dark', className)}>
      <div className="container-x grid gap-10 pt-16 pb-6 md:grid-cols-4">
        <div className="flex flex-col gap-4">{logo}<p className={cn('max-w-[28ch] text-[13px] leading-relaxed', m)}>Familiekwekerij van rhododendrons op de Veluwe. Veenrijke bodem, sterk wortelstelsel, aangroeigarantie.</p></div>
        <div className="flex flex-col">{links.map((x) => <a key={x.label} href={x.href} className={link}>{x.label}</a>)}</div>
        <div className="flex flex-col gap-1">
          <p className={cn('eyebrow mb-2', m)}>Kwekerij</p>
          <a href={company.maps} className={cn('text-[14px] leading-relaxed', t)}>{company.street}<br />{company.postal}</a>
          <a href={`mailto:${company.email}`} className={cn('mt-2 text-[14px]', t)}>{company.email}</a>
          <a href={company.phone1Href} className={cn('text-[14px]', t)}>{company.phone1}</a>
          <a href={company.phone2Href} className={cn('text-[14px]', t)}>{company.phone2}</a>
        </div>
        <div className="flex flex-col gap-1">
          <p className={cn('eyebrow mb-2', m)}>Open</p>
          {company.hours.map(([d, h]) => <p key={d} className={cn('flex justify-between gap-4 text-[14px]', t)}><span className={m}>{d}</span><span>{h}</span></p>)}
          <a href={company.instagram} className={cn('mt-3 text-[14px]', t)}>Instagram · @toprhododendrons</a>
        </div>
      </div>
      <p aria-hidden="true" className={cn('container-x select-none font-display leading-[0.85] tracking-[-0.02em] whitespace-nowrap', t, wordmarkClassName)} style={{ fontSize: 'clamp(2.6rem, 9.6vw, 11rem)' }}>{wordmark}</p>
      <div className={cn('container-x mt-4 flex flex-wrap items-center justify-between gap-3 border-t py-4', l)}>
        <p className={cn('text-[11px] tracking-[0.14em] uppercase', m)}>© 2026 {company.name} · KvK {company.kvk}</p>
        <p className={cn('text-[11px] tracking-[0.14em] uppercase', m)}><a href="#" className="hover:opacity-70">Voorwaarden</a> · <a href="#" className="hover:opacity-70">Privacy</a></p>
      </div>
    </footer>
  )
}
