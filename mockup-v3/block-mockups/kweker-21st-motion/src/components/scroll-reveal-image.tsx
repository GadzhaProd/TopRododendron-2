// 21st.dev "Scroll Reveal Image" (id 24466, unlumen). Component logic kept 1:1
// (useScroll -> width / scale / radius with spring smoothing); next/image -> <img>.
import { useRef } from 'react'
import { motion, useScroll, useTransform, useSpring } from 'framer-motion'
export interface ScrollRevealImageProps {
  src: string; alt: string; height?: string; fromWidth?: string; toWidth?: string; fromRadius?: string; toRadius?: string
  radiusStart?: number; innerWidth?: string; fromScale?: number; toScale?: number; stiffness?: number; damping?: number
  scrollOffset?: NonNullable<Parameters<typeof useScroll>[0]>['offset']; className?: string; imageClassName?: string
}
export default function ScrollRevealImage({ src, alt, height = '80vh', fromWidth = '40vw', toWidth = '95vw', fromRadius = '0px', toRadius = '22px', radiusStart = 0.5, innerWidth = '95vw', fromScale = 1.6, toScale = 1, stiffness = 120, damping = 80, scrollOffset = ['start end', 'start start'] as const, className, imageClassName }: ScrollRevealImageProps) {
  const containerRef = useRef<HTMLDivElement>(null)
  const { scrollYProgress } = useScroll({ target: containerRef, offset: scrollOffset })
  // springs smooth the scroll progress; unit strings (vw/px) are interpolated from it
  // (springing the unit strings directly collapsed the width in this build)
  const p = useSpring(scrollYProgress, { stiffness, damping })
  const smoothWidth = useTransform(p, [0, 1], [fromWidth, toWidth])
  const smoothScale = useTransform(p, [0, 1], [fromScale, toScale])
  const smoothRadius = useTransform(p, [radiusStart, 1], [fromRadius, toRadius])
  return (
    <motion.div ref={containerRef} className={className} style={{ width: smoothWidth, position: 'relative', height, borderRadius: smoothRadius, overflow: 'hidden', margin: '0 auto' }}>
      <motion.div style={{ position: 'absolute', left: '50%', x: '-50%', width: innerWidth, height: '100%', scale: smoothScale, originX: 0.5, originY: 0.5 }}>
        <img src={src} alt={alt} className={`absolute inset-0 h-full w-full object-cover${imageClassName ? ` ${imageClassName}` : ''}`} />
      </motion.div>
    </motion.div>
  )
}
