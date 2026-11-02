// Adapted from 21st.dev "Scroll 01" (felipemenezes098): sticky media on one side
// that swaps as the reader scrolls through the items. Extended with meta rows,
// price, an index scale beside the photo, reduced-motion, and a single render
// branch per breakpoint (the hidden mobile list is no longer rendered on desktop).
import { motion, useScroll, useTransform, useMotionValueEvent, useReducedMotion } from 'framer-motion'
import { useRef, useState, type Dispatch, type ReactNode, type SetStateAction } from 'react'
import { cn } from '@/lib/utils'
import { useIsMobile } from './video-hero'

export type StickyItem = { title: string; description: string; media: string; srcSet?: string; meta?: string[]; price?: string; slug: string; swatch?: string }

function ScrollItem({ item, index, setActive, render }: { item: StickyItem; index: number; setActive: Dispatch<SetStateAction<number>>; render: (i: StickyItem, active: boolean) => ReactNode }) {
  const ref = useRef<HTMLDivElement | null>(null)
  const reduce = useReducedMotion()
  const { scrollYProgress } = useScroll({ target: ref, offset: ['start 85%', 'end 20%'] })
  const y = useTransform(scrollYProgress, [0, 1], reduce ? [0, 0] : [12, -12])
  const opacity = useTransform(scrollYProgress, [0, 0.25, 0.75, 1], index === 0 ? [1, 1, 1, 0.6] : [0.6, 1, 1, 0.6])
  const isActive = useTransform(scrollYProgress, (v) => v > 0.3 && v < 0.7)
  const [active, setA] = useState(index === 0)
  useMotionValueEvent(isActive, 'change', (v) => { if (v) { setActive((p) => (p === index ? p : index)); setA(true) } else setA(false) })
  return (
    <motion.article ref={ref} style={{ opacity, y }} className="flex min-h-[28vh] flex-col justify-center">
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
  const mobile = useIsMobile(768)
  const reduce = useReducedMotion()
  if (mobile) return <div className={cn('flex flex-col gap-10', className)}>{items.map((it, i) => <div key={it.slug}>{mobileRender(it, i)}</div>)}</div>
  return (
    <div className={cn('grid grid-cols-1 gap-12 md:grid-cols-2 lg:gap-20', side === 'right' && '[&>*:first-child]:order-2', className)}>
      <div className="sticky top-24 h-[calc(100svh-7rem)] max-h-[820px]">
        <div className="flex h-full gap-4">
          <div className={cn('relative h-full flex-1 overflow-hidden bg-bg-2', imgClassName)}>
            {items.map((it, i) => (
              <motion.img
                key={it.slug} src={it.media} srcSet={it.srcSet} sizes="(min-width: 1024px) 40vw, 50vw" alt={it.title}
                loading={i === 0 ? 'eager' : 'lazy'}
                className="absolute inset-0 h-full w-full object-cover img-treat"
                initial={{ opacity: i === 0 ? 1 : 0 }}
                animate={{ opacity: activeIndex === i ? 1 : 0, scale: reduce ? 1 : activeIndex === i ? 1 : 1.04 }}
                transition={{ duration: reduce ? 0 : 0.6, ease: [0.22, 1, 0.36, 1] }}
              />
            ))}
          </div>
          <ol className="flex flex-col justify-center gap-3" aria-hidden="true">
            {items.map((it, i) => <li key={it.slug} className={cn('h-px w-5 transition-all duration-300', activeIndex === i ? 'w-8 bg-fg' : 'bg-fg/25')} />)}
          </ol>
        </div>
      </div>
      <div className="py-[10vh]">
        <div className="flex flex-col gap-[6vh]">
          {items.map((it, i) => <ScrollItem key={it.slug} item={it} index={i} setActive={setActiveIndex} render={render} />)}
        </div>
      </div>
    </div>
  )
}
