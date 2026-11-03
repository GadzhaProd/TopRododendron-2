// Concept C "Reveal" (adapted from 21st.dev, asanshay): fade + un-blur into view, staggered.
import { motion, useReducedMotion, type Variants } from 'framer-motion'
import type { ReactNode } from 'react'
import { cn } from '@/lib/utils'

const VARIANTS: Variants = {
  hidden: { opacity: 0, y: 28, filter: 'blur(8px)' },
  show: (i: number = 0) => ({ opacity: 1, filter: 'blur(0px)', y: 0, transition: { delay: i * 0.12, duration: 0.7, ease: [0.22, 1, 0.36, 1] } }),
}

export function Reveal({ children, className, index = 0, as = 'div', style }: { children: ReactNode; className?: string; index?: number; as?: 'div' | 'section' | 'li' | 'article'; style?: React.CSSProperties }) {
  const reduce = useReducedMotion()
  const M = (motion as any)[as]
  if (reduce) { const T = as as any; return <T className={className} style={style}>{children}</T> }
  return (
    <M variants={VARIANTS} initial="hidden" whileInView="show" viewport={{ once: true, amount: 0.2 }} custom={index} className={cn(className)} style={style}>
      {children}
    </M>
  )
}
