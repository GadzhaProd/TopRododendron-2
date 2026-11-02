// Adapted from 21st.dev "Scroll 01" (felipemenezes098): sticky media on one side
// that swaps as the reader scrolls through the items. Extended with meta rows,
// price, link, image treatment and a mobile fallback list.
import { motion, useScroll, useTransform, useMotionValueEvent, useReducedMotion } from 'framer-motion'
import { useRef, useState, type Dispatch, type ReactNode, type SetStateAction } from 'react'
import { cn } from '@/lib/utils'

export type StickyItem = { title: string; description: string; media: string; meta?: string[]; price?: string; href?: string; swatch?: string }

function ScrollItem({ item, index, setActive, render }: { item: StickyItem; index: number; setActive: Dispatch<SetStateAction<number>>; render: (i: StickyItem, active: boolean) => ReactNode }) {
  const ref = useRef<HTMLDivElement | null>(null)
  const reduce = useReducedMotion()
  const { scrollYProgress } = useScroll({ target: ref, offset: ['start 85%', 'end 20%'] })
  const y = useTransform(scrollYProgress, [0, 1], reduce ? [0, 0] : [16, -16])
  const opacity = useTransform(scrollYProgress, [0, 0.25, 0.75, 1], index === 0 ? [1, 1, 1, 0.25] : [0.25, 1, 1, 0.25])
  const isActive = useTransform(scrollYProgress, (v) => v > 0.3 && v < 0.7)
  const [active, setA] = useState(index === 0)
  useMotionValueEvent(isActive, 'change', (v) => { if (v) { setActive((p) => (p === index ? p : index)); setA(true) } else setA(false) })
  return (
    <motion.article ref={ref} style={{ opacity, y }} className="min-h-[38vh] flex flex-col justify-center">
      {render(item, active)}
    </motion.article>
  )
}

export function StickyScroll({ items, render, mobileRender, imgClassName, side = 'left', className }: {
  items: StickyItem[]
  render: (i: StickyItem, active: boolean) => ReactNode
  mobileRender: (i: StickyItem, index: number) => ReactNode
  imgClassName?: string
  side?: 'left' | 'right'
  className?: string
}) {
  const [activeIndex, setActiveIndex] = useState(0)
  return (
    <div className={className}>
      <div className="flex flex-col gap-10 md:hidden">{items.map((it, i) => <div key={it.title}>{mobileRender(it, i)}</div>)}</div>
      <div className={cn('hidden gap-12 md:grid md:grid-cols-2 lg:gap-20', side === 'right' && '[&>*:first-child]:order-2')}>
        <div className="sticky top-24 h-[calc(100vh-7rem)] max-h-[820px] overflow-hidden">
          <div className={cn('relative h-full w-full overflow-hidden', imgClassName)}>
            {items.map((it, i) => (
              <motion.img
                key={it.title} src={it.media} alt={it.title}
                className="absolute inset-0 h-full w-full object-cover img-treat"
                initial={{ opacity: i === 0 ? 1 : 0 }}
                animate={{ opacity: activeIndex === i ? 1 : 0, scale: activeIndex === i ? 1 : 1.04 }}
                transition={{ duration: 0.6, ease: [0.22, 1, 0.36, 1] }}
              />
            ))}
          </div>
        </div>
        <div className="py-[12vh]">
          <div className="flex flex-col gap-[8vh]">
            {items.map((it, i) => <ScrollItem key={it.title} item={it} index={i} setActive={setActiveIndex} render={render} />)}
          </div>
        </div>
      </div>
    </div>
  )
}
