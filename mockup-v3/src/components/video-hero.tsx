// Full-screen video hero (adapted from 21st.dev "PrismaHero" in round 2).
// Vertical source on phones, landscape band on larger screens (both without the
// watermark), poster under prefers-reduced-motion. Dark scrim at the top (for
// the transparent header) and a heavier one under the text; text-shadow on the
// small lines so AA holds on bright frames.
import { motion, useReducedMotion } from 'framer-motion'
import { useEffect, useState, type ReactNode } from 'react'
import { cn } from '@/lib/utils'
import { hero } from '@/data/content'

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

export function HeroVideo({ className }: { className?: string }) {
  const mobile = useIsMobile()
  const narrowDesktop = useIsMobile(1280) && !mobile
  const reduce = useReducedMotion()
  const src = mobile ? hero.mobile : hero.desktop
  const poster = mobile ? hero.mobilePoster : hero.desktopPoster
  // on 768–1279 the band is cropped at the sides: keep the right side (the face
  // lives there in the second half of the loop) away from the headline
  const pos = mobile ? '50% 35%' : narrowDesktop ? '90% 40%' : '50% 40%'
  if (reduce) return <img src={poster} alt="" aria-hidden="true" className={cn('absolute inset-0 h-full w-full object-cover', className)} style={{ objectPosition: pos }} />
  return (
    <video key={src} autoPlay loop muted playsInline poster={poster} aria-hidden="true" className={cn('absolute inset-0 h-full w-full object-cover', className)} style={{ objectPosition: pos }}>
      <source src={src} type="video/mp4" />
    </video>
  )
}

export function Words({ text, className = '', delay = 0 }: { text: string; className?: string; delay?: number }) {
  const reduce = useReducedMotion()
  const words = text.split(' ')
  return (
    <span className={cn('inline', className)}>
      {words.map((word, i) => (
        <motion.span key={i} initial={reduce ? false : { y: 22, opacity: 0 }} animate={{ y: 0, opacity: 1 }} transition={{ duration: 0.75, delay: delay + i * 0.08, ease: [0.16, 1, 0.3, 1] }} className="inline-block" style={{ marginRight: i === words.length - 1 ? 0 : '0.24em' }}>{word}</motion.span>
      ))}
    </span>
  )
}

export function VideoHero({ eyebrow, title, text, actions, bottomBar }: { eyebrow?: ReactNode; title: string; text?: ReactNode; actions?: ReactNode; bottomBar?: ReactNode }) {
  const reduce = useReducedMotion()
  const fade = (d: number) => ({ initial: reduce ? false : { y: 14, opacity: 0 }, animate: { y: 0, opacity: 1 }, transition: { duration: 0.8, delay: d, ease: [0.16, 1, 0.3, 1] as any } })
  return (
    <section id="hero" className="relative flex min-h-[100svh] w-full flex-col justify-end overflow-hidden bg-night text-white on-dark">
      <HeroVideo />
      <div className="pointer-events-none absolute inset-x-0 top-0 h-[32%] bg-gradient-to-b from-night/75 via-night/30 to-transparent" />
      <div className="pointer-events-none absolute inset-x-0 bottom-0 h-[88%] bg-gradient-to-t from-night/95 via-night/65 to-transparent md:h-[82%] md:via-night/60" />
      <div className="relative wrap container-x w-full pb-8 pt-28 md:pb-10 short:pt-24 short:pb-6">
        <div className="flex max-w-[48rem] flex-col items-start gap-5 md:gap-6">
          {eyebrow && <motion.p {...fade(0.1)} className="label text-shadow text-white">{eyebrow}</motion.p>}
          <h1 className="display text-shadow text-balance text-[clamp(46px,8.6vw,124px)] short:text-[clamp(38px,6vw,76px)]"><Words text={title} delay={0.25} /></h1>
          {text && <motion.p {...fade(0.8)} className="text-shadow max-w-[38rem] text-[16.5px] font-medium leading-relaxed text-white md:text-[19px]">{text}</motion.p>}
          {actions && <motion.div {...fade(0.95)} className="mt-1 flex flex-wrap gap-3">{actions}</motion.div>}
        </div>
        {bottomBar && <motion.div {...fade(1.1)} className="mt-10 hidden border-t border-white/20 pt-5 md:block">{bottomBar}</motion.div>}
      </div>
    </section>
  )
}
