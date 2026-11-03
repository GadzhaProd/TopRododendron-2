// Concept C "Split Feature Section" (adapted from 21st.dev, uiable): two panels,
// each with eyebrow, heading, copy and CTA over a photo with a dark gradient.
import type { ReactNode } from 'react'
import { cn } from '@/lib/utils'

export type SplitPanel = { id?: string; eyebrow: string; title: string; text: string; action: ReactNode; className?: string; image?: string; imageSrcSet?: string; position?: string; dark?: boolean }

export function SplitCta({ panels, className, minH = 'min-h-[460px]' }: { panels: [SplitPanel, SplitPanel]; className?: string; minH?: string }) {
  return (
    <section id="doors" className={cn('grid grid-cols-1 md:grid-cols-2', className)}>
      {panels.map((p) => (
        <div key={p.title} data-door={p.id} className={cn('relative flex flex-col justify-end overflow-hidden p-8 md:p-12', minH, p.dark && 'on-dark text-white', p.className)}>
          {p.image && (<><img src={p.image} srcSet={p.imageSrcSet} sizes="(min-width: 768px) 50vw, 100vw" alt="" aria-hidden="true" loading="lazy" className="absolute inset-0 h-full w-full object-cover img-treat" style={{ objectPosition: p.position }} /><div className="absolute inset-0 bg-gradient-to-t from-black/90 from-10% via-black/85 via-55% to-black/25" /></>)}
          <div className="relative max-w-md">
            {/* eyebrow at 100 % white and the heavier gradient: AA on the bright flowers (audit В2) */}
            <p className={cn('eyebrow mb-4', p.dark ? 'text-white' : 'text-muted')}>{p.eyebrow}</p>
            <h2 className="font-display text-[clamp(30px,3.6vw,46px)] leading-[1.02] text-balance">{p.title}</h2>
            <p className={cn('mt-4 text-[15.5px] leading-relaxed', p.dark ? 'text-white/80' : 'text-fg-2')}>{p.text}</p>
            <div className="mt-7">{p.action}</div>
          </div>
        </div>
      ))}
    </section>
  )
}
