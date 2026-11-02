// Full-screen video hero. Adapted in round 2 from 21st.dev "PrismaHero"
// (rahil1202); here reduced to what the brand needs: a vertical source on
// phones, a landscape band on larger screens (both cut without the watermark),
// poster under prefers-reduced-motion, content in flow at the bottom-left,
// a scrim only where the text sits.
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
  const reduce = useReducedMotion()
  const src = mobile ? hero.mobile : hero.desktop
  const poster = mobile ? hero.mobilePoster : hero.desktopPoster
  const pos = mobile ? '50% 35%' : '50% 40%'
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
        <motion.span
          key={i}
          initial={reduce ? false : { y: 22, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ duration: 0.75, delay: delay + i * 0.08, ease: [0.16, 1, 0.3, 1] }}
          className="inline-block"
          style={{ marginRight: i === words.length - 1 ? 0 : '0.25em' }}
        >
          {word}
        </motion.span>
      ))}
    </span>
  )
}

export function VideoHero({ eyebrow, title, text, actions, bottomBar }: { eyebrow?: ReactNode; title: string; text?: ReactNode; actions?: ReactNode; bottomBar?: ReactNode }) {
  const reduce = useReducedMotion()
  const fade = (d: number) => ({ initial: reduce ? false : { y: 14, opacity: 0 }, animate: { y: 0, opacity: 1 }, transition: { duration: 0.8, delay: d, ease: [0.16, 1, 0.3, 1] as any } })
  return (
    <section className="relative flex min-h-[100svh] w-full flex-col justify-end overflow-hidden bg-night text-white on-dark">
      <HeroVideo />
      <div className="pointer-events-none absolute inset-0 bg-ink/10" />
      <div className="pointer-events-none absolute inset-x-0 bottom-0 h-[82%] bg-gradient-to-t from-[#0b120e]/92 via-[#0b120e]/55 to-transparent md:h-[72%] md:via-[#0b120e]/38" />
      <div className="relative wrap container-x w-full pb-8 pt-28 md:pb-10 short:pt-24 short:pb-6">
        <div className="flex max-w-[46rem] flex-col items-start gap-5 md:gap-6">
          {eyebrow && <motion.p {...fade(0.1)} className="eyebrow text-white/85">{eyebrow}</motion.p>}
          <h1 className="font-display-tight text-balance text-[clamp(44px,8.2vw,112px)] leading-[0.95] short:text-[clamp(36px,6vw,72px)]">
            <Words text={title} delay={0.25} />
          </h1>
          {text && <motion.p {...fade(0.8)} className="max-w-[40rem] text-[16px] leading-relaxed text-white/88 md:text-[18px]">{text}</motion.p>}
          {actions && <motion.div {...fade(0.95)} className="mt-1 flex flex-wrap gap-3">{actions}</motion.div>}
        </div>
        {bottomBar && <motion.div {...fade(1.1)} className="mt-10 hidden border-t border-white/22 pt-5 md:block">{bottomBar}</motion.div>}
      </div>
    </section>
  )
}
