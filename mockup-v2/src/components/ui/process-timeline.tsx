// Adapted from 21st.dev "Vertical How It Works Timeline" (ln-dev7, how-it-works-02):
// numbered nodes on a dashed rail. Icons removed, cards flattened to hairlines,
// optional horizontal layout on large screens.
import { cn } from '@/lib/utils'

export function ProcessTimeline({ steps, horizontal = false, dark = false, className }: { steps: { title: string; text: string }[]; horizontal?: boolean; dark?: boolean; className?: string }) {
  const line = dark ? 'border-white/20' : 'border-fg/15'
  const node = dark ? 'border-white/30 bg-transparent text-white' : 'border-fg/20 bg-surface text-fg'
  const muted = dark ? 'text-white/70' : 'text-fg-2'
  if (horizontal) {
    return (
      <ol className={cn('grid gap-8 md:grid-cols-4', className)}>
        {steps.map((s, i) => (
          <li key={s.title} className="relative">
            <div className="flex items-center gap-4">
              <span className={cn('grid size-10 shrink-0 place-items-center rounded-full border font-display text-[18px]', node)}>{String(i + 1).padStart(2, '0')}</span>
              <span className={cn('hidden h-px flex-1 border-t border-dashed md:block', line)} />
            </div>
            <h3 className="mt-5 font-display text-[22px] leading-tight">{s.title}</h3>
            <p className={cn('mt-2 text-[15px] leading-relaxed', muted)}>{s.text}</p>
          </li>
        ))}
      </ol>
    )
  }
  return (
    <ol className={cn('relative flex flex-col gap-8 border-l border-dashed pl-10 sm:pl-12', line, className)}>
      {steps.map((s, i) => (
        <li key={s.title} className="relative">
          <span className={cn('absolute -left-[3.3rem] top-0 grid size-10 place-items-center rounded-full border font-display text-[17px] sm:-left-[3.8rem]', node)}>{String(i + 1).padStart(2, '0')}</span>
          <h3 className="font-display text-[22px] leading-tight">{s.title}</h3>
          <p className={cn('mt-2 max-w-[52ch] text-[15px] leading-relaxed', muted)}>{s.text}</p>
        </li>
      ))}
    </ol>
  )
}
