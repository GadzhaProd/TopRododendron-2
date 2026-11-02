// Accordion in the spirit of 21st.dev "Accordion with Plus/Minus Indicators"
// (cnippet-dev): plus/minus trigger, animated height. Panels stay in the DOM so
// aria-controls always resolves; reduced motion disables the height animation.
import { motion, useReducedMotion } from 'framer-motion'
import { useId, useState } from 'react'
import { Minus, Plus } from 'lucide-react'
import { cn } from '@/lib/utils'

export function Faq({ items, dark = false, className, defaultOpen = 0 }: { items: { q: string; a: string }[]; dark?: boolean; className?: string; defaultOpen?: number | null }) {
  const [open, setOpen] = useState<number | null>(defaultOpen)
  const id = useId()
  const reduce = useReducedMotion()
  const line = dark ? 'border-white/15' : 'border-fg/12'
  return (
    <div className={cn('flex flex-col border-t', line, className)}>
      {items.map((it, i) => {
        const isOpen = open === i
        return (
          <div key={it.q} className={cn('border-b', line)}>
            <h3 className="m-0">
              <button type="button" onClick={() => setOpen(isOpen ? null : i)} aria-expanded={isOpen} aria-controls={`${id}-${i}`} className={cn('flex w-full items-center justify-between gap-6 py-5 text-left font-display text-[20px] leading-snug md:text-[23px]', dark ? 'text-white' : 'text-fg')}>
                <span>{it.q}</span>
                <span className={cn('grid size-8 shrink-0 place-items-center rounded-full border', dark ? 'border-white/40' : 'border-fg/25')}>{isOpen ? <Minus className="size-4" /> : <Plus className="size-4" />}</span>
              </button>
            </h3>
            <motion.div id={`${id}-${i}`} role="region" aria-hidden={!isOpen} initial={false} animate={{ height: isOpen ? 'auto' : 0, opacity: isOpen ? 1 : 0 }} transition={{ duration: reduce ? 0 : 0.35, ease: [0.22, 1, 0.36, 1] }} className="overflow-hidden">
              <p className={cn('max-w-[62ch] pb-6 text-[15.5px] leading-relaxed', dark ? 'text-white/80' : 'text-fg-2')}>{it.a}</p>
            </motion.div>
          </div>
        )
      })}
    </div>
  )
}
