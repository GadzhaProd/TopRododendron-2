// Adapted from 21st.dev "Footer with Suite" (scrollxui): link columns and an
// oversized brand wordmark above the bottom bar. Extended with a compact mode for
// pages that already show the contact block, readable 14px links and real legal links.
import type { ReactNode } from 'react'
import { cn } from '@/lib/utils'
import { company } from '@/data/content'

export function FooterSuite({ links, wordmark, logo, dark = false, className, wordmarkClassName, wordmarkSize = 'clamp(2.6rem, 9.6vw, 11rem)', compact = false }: { links: { label: string; href: string }[]; wordmark: string; logo?: ReactNode; dark?: boolean; className?: string; wordmarkClassName?: string; wordmarkSize?: string; compact?: boolean }) {
  const t = dark ? 'text-white' : 'text-fg'
  const m = dark ? 'text-white/70' : 'text-muted'
  const l = dark ? 'border-white/15' : 'border-fg/10'
  const link = cn('py-1 text-[14px] transition-colors hover:opacity-60', t)
  return (
    <footer className={cn('relative w-full overflow-hidden', dark && 'on-dark', className)}>
      <div className={cn('container-x grid gap-10 pt-14 pb-6', compact ? 'md:grid-cols-[1.4fr_1fr_1fr]' : 'md:grid-cols-4')}>
        <div className="flex flex-col gap-4">{logo}<p className={cn('max-w-[30ch] text-[14px] leading-relaxed', m)}>Familiekwekerij van rhododendrons op de Veluwe. Veenrijke bodem, sterk wortelstelsel, aangroeigarantie.</p></div>
        <div className="flex flex-col"><p className={cn('eyebrow mb-2', m)}>Navigatie</p>{links.map((x) => <a key={x.label} href={x.href} className={link}>{x.label}</a>)}</div>
        {compact ? (
          <div className="flex flex-col gap-1">
            <p className={cn('eyebrow mb-2', m)}>Contact</p>
            <a href={company.phone1Href} className={cn('text-[14px]', t)}>{company.phone1}</a>
            <a href={`mailto:${company.email}`} className={cn('text-[14px]', t)}>{company.email}</a>
            <a href={company.instagram} className={cn('text-[14px]', t)}>Instagram · @toprhododendrons</a>
          </div>
        ) : (
          <>
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
          </>
        )}
      </div>
      <p aria-hidden="true" className={cn('container-x select-none font-display leading-[0.85] tracking-[-0.02em] whitespace-nowrap', t, wordmarkClassName)} style={{ fontSize: wordmarkSize }}>{wordmark}</p>
      <div className={cn('container-x mt-4 flex flex-wrap items-center justify-between gap-3 border-t py-4', l)}>
        <p className={cn('text-[13px]', m)}>© 2026 {company.name} · KvK {company.kvk}</p>
        <p className={cn('text-[13px]', m)}><a href={company.voorwaarden} className="hover:opacity-70">Voorwaarden</a> · <a href={company.privacy} className="hover:opacity-70">Privacy</a></p>
      </div>
    </footer>
  )
}
