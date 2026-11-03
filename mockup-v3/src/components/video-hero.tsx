// Hero. Desktop and tablets in landscape ("split" media query): a solid dark panel
// in concept C's moss accent with the text on the left, the video at full viewport
// height on the right, edge to edge, cut from the vertical source so that the
// woman's face and hands stay in frame for the whole loop (source y 90–930).
// Phones and tablets in portrait: the video fills the viewport (source y 0–1200,
// the figure in the upper ~65 %, a soft dark ground below); the text block sits
// compact at the bottom over a gradient scrim (phones) or top-left (tablets in
// portrait), never over the face or the hands. prefers-reduced-motion: poster
// frame (t ≈ 6.5 s, hands on the flowers). The "Veo" mark (source y ≥ 1222) is
// outside both cuts.
import { motion, useInView, useReducedMotion } from 'framer-motion'
import { useEffect, useRef, useState, type ReactNode } from 'react'
import { cn } from '@/lib/utils'
import { hero } from '@/data/content'

export const SPLIT_QUERY = '(min-width: 1024px), (min-width: 768px) and (orientation: landscape)'

export function useMedia(query: string) {
  const [m, setM] = useState(() => (typeof window !== 'undefined' ? window.matchMedia(query).matches : false))
  useEffect(() => {
    const mq = window.matchMedia(query)
    const h = () => setM(mq.matches)
    h(); mq.addEventListener('change', h)
    return () => mq.removeEventListener('change', h)
  }, [query])
  return m
}
export const useIsMobile = (bp = 768) => useMedia(`(max-width: ${bp - 1}px)`)

export function WordsPullUp({ text, className = '', delay = 0 }: { text: string; className?: string; delay?: number }) {
  const ref = useRef<HTMLSpanElement>(null)
  const isInView = useInView(ref, { once: true })
  const reduce = useReducedMotion()
  const words = text.split(' ')
  return (
    <span ref={ref} className={cn('inline-flex flex-wrap', className)}>
      {words.map((word, i) => (
        <motion.span key={i} initial={reduce ? false : { y: 24, opacity: 0 }} animate={isInView ? { y: 0, opacity: 1 } : {}} transition={{ duration: 0.7, delay: delay + i * 0.07, ease: [0.16, 1, 0.3, 1] }} className="inline-block" style={{ marginRight: i === words.length - 1 ? 0 : '0.26em' }}>
          {word}
        </motion.span>
      ))}
    </span>
  )
}

export function HeroVideo({ className }: { className?: string }) {
  const split = useMedia(SPLIT_QUERY)
  const reduce = useReducedMotion()
  const src = split ? hero.split : hero.portrait
  const poster = split ? hero.splitPoster : hero.portraitPoster
  // portrait: top-aligned, so short phones crop the dark ground, never the face
  const pos = split ? '50% 50%' : '50% 0%'
  const cls = cn('absolute inset-0 h-full w-full object-cover', className)
  if (reduce) return <img src={poster} alt="" aria-hidden="true" className={cls} style={{ objectPosition: pos }} />
  return (
    <video key={src} autoPlay loop muted playsInline poster={poster} aria-hidden="true" className={cls} style={{ objectPosition: pos }}>
      <source src={src} type="video/mp4" />
    </video>
  )
}

export function VideoHero({ eyebrow, title, text, actions }: { eyebrow?: ReactNode; title: string; text?: ReactNode; actions?: ReactNode }) {
  const reduce = useReducedMotion()
  const fade = (d: number) => ({ initial: reduce ? false : { y: 18, opacity: 0 }, animate: { y: 0, opacity: 1 }, transition: { duration: 0.8, delay: d, ease: [0.16, 1, 0.3, 1] as any } })
  return (
    <section id="hero" className="relative flex min-h-[100svh] w-full flex-col justify-end overflow-hidden bg-black text-white on-dark tabp:justify-start split:grid split:grid-cols-[54fr_46fr] split:items-stretch split:bg-accent">
      <div className="absolute inset-0 split:relative split:col-start-2 split:row-start-1 split:h-full split:min-h-[100svh]">
        <HeroVideo />
        {/* phones: light veil + scrim under the text block (lower 55 %); tablets in portrait: scrim at the top */}
        <div className="pointer-events-none absolute inset-0 bg-black/10 split:hidden" />
        <div className="pointer-events-none absolute inset-x-0 bottom-0 h-[55%] bg-gradient-to-t from-black/90 via-black/55 to-transparent tabp:hidden split:hidden" />
        <div className="pointer-events-none absolute inset-x-0 top-0 hidden h-[62%] bg-gradient-to-b from-black/80 via-black/45 to-transparent tabp:block" />
      </div>
      <div className="relative w-full container-x pt-28 pb-7 shortphone:pb-5 tabp:pt-32 split:col-start-1 split:row-start-1 split:flex split:flex-col split:justify-center split:py-28">
        <div className="flex max-w-4xl flex-col items-start gap-3 md:gap-5 tabp:max-w-[21.5rem] split:max-w-[36rem]">
          {eyebrow && <motion.div {...fade(0.1)} className="eyebrow text-white/85">{eyebrow}</motion.div>}
          <h1 className="font-display text-balance text-[clamp(30px,8.4vw,38px)] font-medium leading-[0.98] tracking-[-0.04em] tabp:text-[36px] split:text-[clamp(38px,4.6vw,72px)]">
            <WordsPullUp text={title} delay={0.2} />
          </h1>
          {text && <motion.p {...fade(0.7)} className="max-w-xl text-[15px] leading-relaxed text-white/90 shortphone:hidden md:text-lg split:text-[17px]">{text}</motion.p>}
          {actions && <motion.div {...fade(0.85)} className="mt-1 flex flex-wrap gap-3">{actions}</motion.div>}
        </div>
      </div>
    </section>
  )
}
