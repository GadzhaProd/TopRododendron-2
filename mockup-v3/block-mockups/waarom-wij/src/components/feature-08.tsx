// Feature Grid Spotlight Cards (feature-08) — 21st.dev id 26797, by mohammadshehadeh (Hirael, MIT).
// Kept: FeatureCard on hairline rails (the four 1px lines that run 16px past the
// card), the corner crosshair marks, the icon box + title + description stack,
// the pointer-follow spotlight on hover, and the header (outline pill badge,
// h2, p). Changed: tokens and Manrope, header left-aligned, 2x2 grid instead of
// 3 columns (it lives in the left column), glow tinted with our moss accent.
import type { LucideIcon } from 'lucide-react'
import * as React from 'react'
import { cn } from '@/lib'
import { Badge } from '@/components/ui/badge'

export type Feature = { icon: LucideIcon; title: string; description: string }

/** Corner crosshair, drawn half outside the card edge like a survey mark. */
const CrossDecor = ({ position }: { position: 'top-start' | 'bottom-end' }) => (
  <svg aria-hidden viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1" strokeLinecap="round"
    className={cn('pointer-events-none absolute z-10 size-3.5 shrink-0 text-muted-foreground',
      position === 'top-start' && 'start-0 top-0 -translate-y-1/2 -translate-x-1/2',
      position === 'bottom-end' && 'bottom-0 end-0 translate-y-1/2 translate-x-1/2')}>
    <path d="M5 12h14" /><path d="M12 5v14" />
  </svg>
)

const FeatureCard = ({ className, children, ...props }: React.ComponentProps<'div'>) => {
  const handlePointerMove = (e: React.PointerEvent<HTMLDivElement>) => {
    const rect = e.currentTarget.getBoundingClientRect()
    e.currentTarget.style.setProperty('--mx', `${e.clientX - rect.left}px`)
    e.currentTarget.style.setProperty('--my', `${e.clientY - rect.top}px`)
  }
  return (
    <div onPointerMove={handlePointerMove} data-slot="feature-card"
      className={cn('group relative flex h-full flex-col justify-start gap-5 bg-card px-5 pb-5 pt-6 sm:px-6 sm:pb-6 sm:pt-7',
        'bg-[radial-gradient(50%_80%_at_25%_0%,var(--warm-glow),transparent)]', className)} {...props}>
      <div aria-hidden className="pointer-events-none absolute inset-0 opacity-0 transition-opacity duration-300 group-hover:opacity-100 bg-[radial-gradient(circle_200px_at_var(--mx)_var(--my),color-mix(in_oklch,var(--color-warm)_14%,transparent),transparent_70%)]" />
      <div className="absolute -inset-y-4 -start-px w-px bg-border" />
      <div className="absolute -inset-y-4 -end-px w-px bg-border" />
      <div className="absolute -inset-x-4 -top-px h-px bg-border" />
      <div className="absolute -inset-x-4 -bottom-px h-px bg-border" />
      {children}
    </div>
  )
}

export function Feature08Header({ badge, title, description }: { badge: string; title: React.ReactNode; description: React.ReactNode }) {
  return (
    <div data-slot="feature-header" className="flex max-w-3xl flex-col items-start gap-4 text-left">
      <Badge variant="outline" className="rounded-full bg-card/70 px-3.5 py-1.5 text-[11px] font-semibold uppercase tracking-[0.14em] text-primary">{badge}</Badge>
      <h2 className="text-balance text-[34px] font-semibold leading-[1.04] tracking-[-0.03em] sm:text-[40px] lg:text-[52px]">{title}</h2>
      <p className="max-w-[48ch] text-pretty text-[16px] leading-[1.6] text-foreground-2 sm:text-[17px] lg:text-[19px]">{description}</p>
    </div>
  )
}

export function Feature08Grid({ features }: { features: readonly Feature[] }) {
  return (
    <div className="grid w-full grid-cols-1 gap-8 px-4 py-4 sm:grid-cols-2">
      {features.map((f) => (
        <FeatureCard key={f.title}>
          <CrossDecor position="top-start" />
          <CrossDecor position="bottom-end" />
          <div data-slot="feature-card-icon" className="relative z-10 flex w-fit items-center justify-center rounded-[8px] border border-border bg-muted/40 p-2.5 transition-colors duration-300 group-hover:border-warm/60">
            <f.icon aria-hidden className="size-5 stroke-[1.5] text-primary" />
          </div>
          <div className="relative z-10 flex flex-col gap-1.5">
            <h3 className="text-[17px] font-semibold leading-[1.25] tracking-[-0.015em] text-foreground">{f.title}</h3>
            <p className="text-pretty text-[14.5px] leading-[1.5] text-muted-foreground">{f.description}</p>
          </div>
        </FeatureCard>
      ))}
    </div>
  )
}
