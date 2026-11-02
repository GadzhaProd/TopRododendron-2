// Adapted from 21st.dev "Scroll Horizontal Gallery" (motiondotdev): a pinned
// section where vertical scrolling translates a horizontal track. Rewritten to
// use the window scroller, pin below the fixed header, size cards from the
// viewport height (nothing clipped at 1366×768) and fall back to swipe on mobile.
import { motion, useScroll, useTransform, useReducedMotion } from 'framer-motion'
import { useEffect, useRef, useState, type ReactNode } from 'react'

const HEADER = 80

export function ScrollHorizontal<T>({ items, render, maxItemWidth = 460, gap = 24, className, header, mobileWidth = 290, captionHeight = 150 }: { items: T[]; render: (item: T, i: number, width: number) => ReactNode; maxItemWidth?: number; gap?: number; className?: string; header?: ReactNode; mobileWidth?: number; captionHeight?: number }) {
  const targetRef = useRef<HTMLDivElement>(null)
  const reduce = useReducedMotion()
  const [vp, setVp] = useState({ w: 1440, h: 900 })
  useEffect(() => { const h = () => setVp({ w: window.innerWidth, h: window.innerHeight }); h(); window.addEventListener('resize', h); return () => window.removeEventListener('resize', h) }, [])
  const pad = Math.max(20, Math.min(64, vp.w * 0.04))
  // available height for the image (4:5) under the header block and above the caption
  const avail = vp.h - HEADER - 150 - captionHeight
  const itemWidth = Math.max(260, Math.min(maxItemWidth, avail / 1.25))
  const total = items.length * (itemWidth + gap) - gap + pad * 2 - vp.w
  const { scrollYProgress } = useScroll({ target: targetRef, offset: ['start start', 'end end'] })
  const x = useTransform(scrollYProgress, [0, 1], [0, -Math.max(0, total)])
  const progressW = useTransform(scrollYProgress, [0, 1], ['0%', '100%'])
  const desktop = vp.w >= 1024 && !reduce

  if (!desktop) {
    return (
      <div className={className}>
        {header}
        <div className="no-scrollbar flex snap-x snap-mandatory gap-4 overflow-x-auto px-5 pb-4" style={{ scrollPaddingLeft: 20 }}>
          {items.map((it, i) => <div key={i} className="shrink-0 snap-start" style={{ width: mobileWidth }}>{render(it, i, mobileWidth)}</div>)}
        </div>
      </div>
    )
  }
  const height = Math.max(0, total) + vp.h
  return (
    <div ref={targetRef} className={className} style={{ height }}>
      <div className="sticky flex flex-col justify-center overflow-hidden" style={{ top: HEADER, height: `calc(100svh - ${HEADER}px)` }}>
        {header}
        <motion.div className="flex" style={{ x, gap, paddingLeft: pad, paddingRight: pad }}>
          {items.map((it, i) => <div key={i} className="shrink-0" style={{ width: itemWidth }}>{render(it, i, itemWidth)}</div>)}
        </motion.div>
        <motion.div aria-hidden="true" className="mx-auto mt-6 h-px w-40 bg-fg/15"><motion.div className="h-px bg-fg/70" style={{ width: progressW }} /></motion.div>
      </div>
    </div>
  )
}
