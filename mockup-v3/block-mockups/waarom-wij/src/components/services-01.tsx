// Services List (services-01) — 21st.dev id 33903, by balick.
// Kept: SectionHeader (eyebrow, title, description, left-aligned) and the
// numbered list with divide-y/border-y rows, each a grid of index | title + small
// line | description + a wrap of pill chips. Changed: tokens and Manrope, rows
// are not links and the arrow button is gone (no CTAs in this block), the
// 4-column row only above 1280px because the list sits in the left column.
import * as React from 'react'

export type Service = { title: string; sub: string; description: string; deliverables: readonly string[] }

export function SectionHeader({ eyebrow, title, description }: { eyebrow: string; title: React.ReactNode; description: React.ReactNode }) {
  return (
    <div className="flex max-w-3xl flex-col items-start gap-4">
      <p className="text-[12px] font-semibold uppercase tracking-[0.14em] text-primary">{eyebrow}</p>
      <h2 className="text-balance text-[34px] font-semibold leading-[1.04] tracking-[-0.03em] sm:text-[40px] lg:text-[52px]">{title}</h2>
      <p className="max-w-[48ch] text-pretty text-[16px] leading-[1.6] text-foreground-2 sm:text-[17px] lg:text-[19px]">{description}</p>
    </div>
  )
}

export function ServicesList({ services }: { services: readonly Service[] }) {
  return (
    <ul className="divide-y border-y">
      {services.map((s, index) => (
        <li key={s.title}>
          <div className="svc-row py-6 lg:py-7">
            <span className="pt-[5px] text-[13px] font-semibold tracking-[0.06em] text-primary">{String(index + 1).padStart(2, '0')}</span>
            <div>
              <h3 className="text-[20px] font-semibold leading-[1.2] tracking-[-0.02em]">{s.title}</h3>
              <p className="mt-1.5 text-[14px] text-muted-foreground">{s.sub}</p>
            </div>
            <div className="svc-desc">
              <p className="text-pretty text-[15px] leading-[1.5] text-foreground-2">{s.description}</p>
              <ul aria-label="Kenmerken" className="mt-3.5 flex flex-wrap gap-2">
                {s.deliverables.map((d) => (
                  <li key={d} className="rounded-full border border-border bg-card px-3 py-1 text-[12.5px] text-foreground-2">{d}</li>
                ))}
              </ul>
            </div>
          </div>
        </li>
      ))}
    </ul>
  )
}
