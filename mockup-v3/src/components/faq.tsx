// Accordion (in the spirit of 21st.dev "Accordion with Plus/Minus", cnippet-dev):
// panels stay in the DOM so aria-controls always resolves.
import { motion, useReducedMotion } from 'framer-motion'
import { useId, useState } from 'react'
import { Minus, Plus } from 'lucide-react'
import { cn } from '@/lib/utils'

export function Faq({ items, dark = false, className, defaultOpen = 0 }: { items: { q: string; a: string }[]; dark?: boolean; className?: string; defaultOpen?: number | null }) {
  const [open, setOpen] = useState<number | null>(defaultOpen)
  const id = useId()
  const reduce = useReducedMotion()
  return (
    <div className={cn('flex flex-col gap-2.5', className)}>
      {items.map((it, i) => {
        const isOpen = open === i
        return (
          <div key={it.q} className={cn('rounded-img border transition-colors', dark ? 'border-white/12 bg-white/5' : 'border-line bg-surface', isOpen && (dark ? 'bg-white/8' : 'bg-white'))}>
            <h3 className="m-0">
              <button type="button" onClick={() => setOpen(isOpen ? null : i)} aria-expanded={isOpen} aria-controls={`${id}-${i}`} className={cn('flex w-full items-start justify-between gap-5 px-5 py-4 text-left text-[17px] font-semibold leading-snug md:px-6 md:text-[18px]', dark ? 'text-white' : 'text-ink')}>
                <span>{it.q}</span>
                <span className={cn('mt-0.5 grid size-7 shrink-0 place-items-center rounded-full', dark ? 'bg-white/12' : 'bg-bg')}>{isOpen ? <Minus className="size-3.5" /> : <Plus className="size-3.5" />}</span>
              </button>
            </h3>
            <motion.div id={`${id}-${i}`} role="region" aria-hidden={!isOpen} initial={false} animate={{ height: isOpen ? 'auto' : 0, opacity: isOpen ? 1 : 0 }} transition={{ duration: reduce ? 0 : 0.3, ease: [0.22, 1, 0.36, 1] }} className="overflow-hidden">
              <p className={cn('max-w-[64ch] px-5 pb-5 text-[15.5px] leading-relaxed md:px-6', dark ? 'text-white/80' : 'text-ink-2')}>{it.a}</p>
            </motion.div>
          </div>
        )
      })}
    </div>
  )
}
