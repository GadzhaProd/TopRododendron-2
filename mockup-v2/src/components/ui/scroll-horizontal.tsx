// Adapted from 21st.dev "Scroll Horizontal Gallery" (motiondotdev): a pinned
// section where vertical scrolling translates a horizontal track. Rewritten to
// use the window scroller, responsive item widths and a mobile swipe fallback.
import { motion, useScroll, useTransform, useReducedMotion } from 'framer-motion'
import { useEffect, useRef, useState, type ReactNode } from 'react'
import { cn } from '@/lib/utils'

export function ScrollHorizontal<T>({ items, render, itemWidth = 420, gap = 24, className, header, mobileWidth = 300 }: { items: T[]; render: (item: T, i: number) => ReactNode; itemWidth?: number; gap?: number; className?: string; header?: ReactNode; mobileWidth?: number }) {
  const targetRef = useRef<HTMLDivElement>(null)
  const reduce = useReducedMotion()
  const [vw, setVw] = useState(1440)
  useEffect(() => { const h = () => setVw(window.innerWidth); h(); window.addEventListener('resize', h); return () => window.removeEventListener('resize', h) }, [])
  const pad = Math.max(20, Math.min(64, vw * 0.04))
  const total = items.length * (itemWidth + gap) - gap + pad * 2 - vw
  const { scrollYProgress } = useScroll({ target: targetRef, offset: ['start start', 'end end'] })
  const x = useTransform(scrollYProgress, [0, 1], [0, -Math.max(0, total)])
  const desktop = vw >= 900 && !reduce

  if (!desktop) {
    return (
      <div className={className}>
        {header}
        <div className="no-scrollbar flex snap-x snap-mandatory gap-4 overflow-x-auto px-5 pb-4" style={{ scrollPaddingLeft: 20 }}>
          {items.map((it, i) => <div key={i} className="shrink-0 snap-start" style={{ width: mobileWidth }}>{render(it, i)}</div>)}
        </div>
      </div>
    )
  }
  const height = Math.max(0, total) + window.innerHeight
  return (
    <div ref={targetRef} className={className} style={{ height }}>
      <div className="sticky top-0 flex h-screen flex-col justify-center overflow-hidden">
        {header}
        <motion.div className="flex" style={{ x, gap, paddingLeft: pad, paddingRight: pad }}>
          {items.map((it, i) => <div key={i} className="shrink-0" style={{ width: itemWidth }}>{render(it, i)}</div>)}
        </motion.div>
      </div>
    </div>
  )
}

export { cn }
