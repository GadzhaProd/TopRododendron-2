// Single Voice Spotlight Testimonial (testimonials-2) — 21st.dev id 28169, by olewandowski1.
// Used here for the grower's own line under his portrait (not a customer review).
// Kept: the card with the vertical bar at the top-left, blockquote, Separator,
// and the author row (avatar + name + role). Changed: tokens, Manrope, the
// quote-mark icon from @remixicon replaced by an inline SVG of the same mark,
// the three metrics replaced by one plain-text phone line (no buttons), the
// avatar dropped because the big portrait sits directly above the card.
import { Separator } from '@/components/ui/separator'

export function QuoteCard({ quote, name, role, noteLabel, note }: { quote: string; name: string; role: string; noteLabel: string; note: string }) {
  return (
    <div className="relative rounded-[20px] border border-border bg-card p-6 sm:p-7">
      <div className="absolute left-0 top-7 h-10 w-[3px] bg-primary" aria-hidden="true" />
      <svg aria-hidden="true" viewBox="0 0 24 24" fill="currentColor" className="mb-4 size-6 text-accent-2"><path d="M9.983 3v7.391c0 5.704-3.731 9.57-8.983 10.609l-.995-2.151c2.432-.917 3.995-3.638 3.995-5.849h-4v-10h9.983zm14.017 0v7.391c0 5.704-3.748 9.571-9 10.609l-.996-2.151c2.433-.917 3.996-3.638 3.996-5.849h-3.983v-10h9.983z" /></svg>
      <blockquote className="text-pretty text-[18px] font-medium leading-[1.45] tracking-[-0.01em] text-foreground">&ldquo;{quote}&rdquo;</blockquote>
      <Separator className="my-5" />
      <div className="flex items-end justify-between gap-4">
        <div className="flex flex-col gap-1">
          <span className="text-[15px] font-semibold leading-tight text-foreground">{name}</span>
          <span className="text-[13px] leading-tight text-muted-foreground">{role}</span>
        </div>
        <div className="flex flex-col items-end gap-1 text-right">
          <span className="text-[12px] leading-tight text-muted-foreground">{noteLabel}</span>
          <span className="whitespace-nowrap text-[15px] font-semibold leading-tight text-foreground">{note}</span>
        </div>
      </div>
    </div>
  )
}
