// In the spirit of 21st.dev "Reveal" (asanshay): a quiet fade + rise into view.
// No blur (it reads as "template"), respects prefers-reduced-motion.
import { motion, useReducedMotion, type Variants } from 'framer-motion'
import type { ReactNode } from 'react'

const VARIANTS: Variants = {
  hidden: { opacity: 0, y: 18 },
  show: (i: number = 0) => ({ opacity: 1, y: 0, transition: { delay: i * 0.08, duration: 0.6, ease: [0.22, 1, 0.36, 1] } }),
}

export function Reveal({ children, className, index = 0, as = 'div', style }: { children: ReactNode; className?: string; index?: number; as?: 'div' | 'section' | 'li' | 'article'; style?: React.CSSProperties }) {
  const reduce = useReducedMotion()
  const M = (motion as any)[as]
  if (reduce) { const T = as as any; return <T className={className} style={style}>{children}</T> }
  return (
    <M variants={VARIANTS} initial="hidden" whileInView="show" viewport={{ once: true, amount: 0.15 }} custom={index} className={className} style={style}>
      {children}
    </M>
  )
}
