// Adapted from 21st.dev "Split Feature Section" (uiable, block-content-4): a
// two-panel section, one coloured, one neutral, each with heading, copy and CTA.
// Icons removed; optional background image per panel.
import type { ReactNode } from 'react'
import { cn } from '@/lib/utils'

export type SplitPanel = { eyebrow: string; title: string; text: string; action: ReactNode; className?: string; image?: string; dark?: boolean }

export function SplitCta({ panels, className, minH = 'min-h-[460px]' }: { panels: [SplitPanel, SplitPanel]; className?: string; minH?: string }) {
  return (
    <section className={cn('grid md:grid-cols-2', className)}>
      {panels.map((p) => (
        <div key={p.title} className={cn('relative flex flex-col justify-end overflow-hidden p-8 md:p-12', minH, p.dark && 'on-dark text-white', p.className)}>
          {p.image && (<><img src={p.image} alt="" aria-hidden="true" className="absolute inset-0 h-full w-full object-cover img-treat" /><div className="absolute inset-0 bg-gradient-to-t from-black/75 via-black/30 to-black/10" /></>)}
          <div className="relative max-w-md">
            <p className={cn('eyebrow mb-4', p.dark ? 'text-white/70' : 'text-muted')}>{p.eyebrow}</p>
            <h2 className="font-display text-[clamp(30px,3.6vw,46px)] leading-[1.02] text-balance">{p.title}</h2>
            <p className={cn('mt-4 text-[15.5px] leading-relaxed', p.dark ? 'text-white/80' : 'text-fg-2')}>{p.text}</p>
            <div className="mt-7">{p.action}</div>
          </div>
        </div>
      ))}
    </section>
  )
}
