// Comparison Section (comparison-03) — 21st.dev id 26826, by mohammadshehadeh (Hirael, MIT).
// Kept: the two panels on a 1px border grid (old way muted with "minus" rows, new
// way ticked), each with an icon + small uppercase label and a list; the closing
// outcome strip as a <dl> of value + label pairs. Changed: tokens and Manrope,
// no mono/serif, no strike-through on the muted list (factual, not mocking),
// the "See what ships" button removed (no CTAs in this block), panels exposed
// as separate parts so they can sit in the left column while the outcome strip
// spans the full width.
import { Check, CircleAlert, CircleCheck, Minus } from 'lucide-react'
import { cn } from '@/lib'

export type Outcome = { value: string; label: string }

export function ComparisonPanels({ before, after, className }: { before: { title: string; items: readonly string[] }; after: { title: string; items: readonly string[] }; className?: string }) {
  return (
    <div className={cn('cmp-panels overflow-hidden rounded-[20px] border border-border bg-border', className)}>
      <div className="bg-background p-6 sm:p-7">
        <div className="flex items-center gap-2">
          <CircleAlert aria-hidden className="size-4 text-muted-foreground" />
          <h3 className="text-[11px] font-semibold uppercase tracking-[0.12em] text-muted-foreground">{before.title}</h3>
        </div>
        <ul className="mt-5 flex flex-col gap-3.5">
          {before.items.map((item) => (
            <li key={item} className="flex gap-3 text-[15px] leading-[1.45] text-muted-foreground">
              <Minus aria-hidden className="mt-[3px] size-4 shrink-0 text-muted-foreground/60" />
              <span>{item}</span>
            </li>
          ))}
        </ul>
      </div>
      <div className="bg-card p-6 sm:p-7">
        <div className="flex items-center gap-2">
          <CircleCheck aria-hidden className="size-4 text-primary" />
          <h3 className="text-[11px] font-semibold uppercase tracking-[0.12em] text-primary">{after.title}</h3>
        </div>
        <ul className="mt-5 flex flex-col gap-3.5">
          {after.items.map((item) => (
            <li key={item} className="flex gap-3 text-[15px] leading-[1.45] text-foreground">
              <Check aria-hidden className="mt-[3px] size-4 shrink-0 text-primary" />
              <span>{item}</span>
            </li>
          ))}
        </ul>
      </div>
    </div>
  )
}

export function ComparisonOutcomes({ outcomes, className }: { outcomes: readonly Outcome[]; className?: string }) {
  return (
    <div className={cn('mt-12 flex flex-col items-start justify-between gap-6 border-t border-border pt-7 sm:flex-row sm:items-center lg:mt-14', className)}>
      <dl className="cmp-outcomes w-full items-baseline">
        {outcomes.map((o) => (
          <div key={o.value} className="flex flex-wrap items-baseline gap-x-2.5 gap-y-0.5">
            <dt className="text-[14px] text-muted-foreground">{o.label}</dt>
            <dd className="order-first whitespace-nowrap text-[20px] font-semibold tracking-[-0.02em] text-foreground">{o.value}</dd>
          </div>
        ))}
      </dl>
    </div>
  )
}
