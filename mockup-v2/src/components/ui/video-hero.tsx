// Adapted from 21st.dev "PrismaHero" (rahil1202): full-screen cinematic video hero
// with staggered word reveal. Reworked for a vertical/landscape source pair,
// prefers-reduced-motion, poster fallback, in-flow content (no absolute
// positioning, so short phones never overlap the header) and a heavier text scrim.
import { motion, useInView, useReducedMotion } from 'framer-motion'
import { useEffect, useRef, useState, type ReactNode } from 'react'
import { cn } from '@/lib/utils'
import { hero } from '@/data/content'

export function WordsPullUp({ text, className = '', delay = 0 }: { text: string; className?: string; delay?: number }) {
  const ref = useRef<HTMLSpanElement>(null)
  const isInView = useInView(ref, { once: true })
  const reduce = useReducedMotion()
  const words = text.split(' ')
  return (
    <span ref={ref} className={cn('inline-flex flex-wrap', className)}>
      {words.map((word, i) => (
        <motion.span
          key={i}
          initial={reduce ? false : { y: 24, opacity: 0 }}
          animate={isInView ? { y: 0, opacity: 1 } : {}}
          transition={{ duration: 0.7, delay: delay + i * 0.07, ease: [0.16, 1, 0.3, 1] }}
          className="inline-block"
          style={{ marginRight: i === words.length - 1 ? 0 : '0.26em' }}
        >
          {word}
        </motion.span>
      ))}
    </span>
  )
}

export function useIsMobile(bp = 768) {
  const [m, setM] = useState(() => (typeof window !== 'undefined' ? window.innerWidth < bp : false))
  useEffect(() => {
    const mq = window.matchMedia(`(max-width: ${bp - 1}px)`)
    const h = () => setM(mq.matches)
    h(); mq.addEventListener('change', h)
    return () => mq.removeEventListener('change', h)
  }, [bp])
  return m
}

export function HeroVideo({ className, position = '50% 50%', mobilePosition = '50% 40%' }: { className?: string; position?: string; mobilePosition?: string }) {
  const mobile = useIsMobile()
  const reduce = useReducedMotion()
  const src = mobile ? hero.mobile : hero.desktop
  const poster = mobile ? hero.mobilePoster : hero.desktopPoster
  if (reduce) {
    return <img src={poster} alt="" aria-hidden="true" className={cn('absolute inset-0 h-full w-full object-cover', className)} style={{ objectPosition: mobile ? mobilePosition : position }} />
  }
  return (
    <video key={src} autoPlay loop muted playsInline poster={poster} aria-hidden="true" className={cn('absolute inset-0 h-full w-full object-cover', className)} style={{ objectPosition: mobile ? mobilePosition : position }}>
      <source src={src} type="video/mp4" />
    </video>
  )
}

export interface VideoHeroProps {
  eyebrow?: ReactNode
  title: string
  titleClassName?: string
  text?: ReactNode
  actions?: ReactNode
  align?: 'left' | 'center'
  above?: ReactNode
  bottomBar?: ReactNode
  className?: string
  position?: string
  leading?: string
}

export function VideoHero({ eyebrow, title, titleClassName, text, actions, align = 'left', above, bottomBar, className, position, leading = 'leading-[0.98]' }: VideoHeroProps) {
  const reduce = useReducedMotion()
  const fade = (d: number) => ({ initial: reduce ? false : { y: 18, opacity: 0 }, animate: { y: 0, opacity: 1 }, transition: { duration: 0.8, delay: d, ease: [0.16, 1, 0.3, 1] as any } })
  return (
    <section className={cn('relative flex min-h-[100svh] w-full flex-col justify-end overflow-hidden bg-black text-white on-dark', className)}>
      <HeroVideo position={position} />
      {/* scrim: light at the top, heavy under the text block */}
      <div className="pointer-events-none absolute inset-0 bg-black/15" />
      <div className="pointer-events-none absolute inset-x-0 bottom-0 h-[78%] bg-gradient-to-t from-black/90 via-black/55 to-transparent md:h-[70%] md:via-black/40" />
      <div className={cn('relative container-x pt-28 pb-8 md:pb-12 short:pt-24 short:pb-6', align === 'center' && 'text-center')}>
        <div className={cn('flex flex-col gap-4 md:gap-5', align === 'center' ? 'mx-auto max-w-3xl items-center' : 'max-w-4xl items-start')}>
          {above}
          {eyebrow && <motion.div {...fade(0.1)} className="eyebrow text-white/85">{eyebrow}</motion.div>}
          <h1 className={cn('font-display text-balance', titleClassName ?? 'text-[clamp(40px,7vw,100px)]', leading)}>
            <WordsPullUp text={title} delay={0.2} className={align === 'center' ? 'justify-center' : ''} />
          </h1>
          {text && <motion.p {...fade(0.7)} className="max-w-xl text-[16px] leading-relaxed text-white/90 md:text-lg">{text}</motion.p>}
          {actions && <motion.div {...fade(0.85)} className={cn('mt-1 flex flex-wrap gap-3', align === 'center' && 'justify-center')}>{actions}</motion.div>}
        </div>
        {bottomBar && <motion.div {...fade(1.0)} className="mt-8 hidden border-t border-white/20 pt-5 md:block">{bottomBar}</motion.div>}
      </div>
    </section>
  )
}
