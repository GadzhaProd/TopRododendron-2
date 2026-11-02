// Adapted from 21st.dev "CTA Section With Floating Gallery" (scrollxui): headline
// + copy on one side, a two-column staggered gallery that animates in on the other.
// OrbButton replaced with the site Button; images and copy passed in as props.
import { motion, useReducedMotion } from 'framer-motion'
import type { ReactNode } from 'react'
import { cn } from '@/lib/utils'

export function CtaFloatingGallery({ eyebrow, title, description, actions, images, dark = false, className, radius = 'rounded-img' }: { eyebrow?: string; title: string; description: string; actions: ReactNode; images: { src: string; alt: string }[]; dark?: boolean; className?: string; radius?: string }) {
  const reduce = useReducedMotion()
  const words = title.split(' ')
  const left = images.slice(0, 3), right = images.slice(3, 6)
  const fade = dark ? 'from-[var(--color-bg)]' : 'from-[var(--color-bg)]'
  const item = (im: { src: string; alt: string }, d: number) => (
    <motion.div key={im.alt} initial={reduce ? false : { opacity: 0, scale: 0.92, y: 16 }} whileInView={{ opacity: 1, scale: 1, y: 0 }} viewport={{ once: true }} transition={{ duration: 0.7, delay: d, ease: [0.22, 1, 0.36, 1] }} className={cn('overflow-hidden', radius)}>
      <img src={im.src} alt={im.alt} loading="lazy" className="h-44 w-full object-cover img-treat md:h-52" />
    </motion.div>
  )
  return (
    <section className={cn('container-x grid items-center gap-12 py-20 md:grid-cols-2 md:gap-16 md:py-28', dark && 'on-dark', className)}>
      <div className="max-w-xl">
        {eyebrow && <p className={cn('eyebrow mb-5', dark ? 'text-white/60' : 'text-muted')}>{eyebrow}</p>}
        <h2 className="font-display text-[clamp(34px,4.2vw,56px)] leading-[1.02] text-balance">
          {words.map((w, i) => (
            <motion.span key={i} initial={reduce ? false : { opacity: 0, filter: 'blur(6px)', y: 10 }} whileInView={{ opacity: 1, filter: 'blur(0px)', y: 0 }} viewport={{ once: true }} transition={{ duration: 0.45, delay: i * 0.06 }} className="mr-[0.25em] inline-block">{w}</motion.span>
          ))}
        </h2>
        <motion.p initial={reduce ? false : { opacity: 0 }} whileInView={{ opacity: 1 }} viewport={{ once: true }} transition={{ duration: 0.6, delay: 0.4 }} className={cn('mt-6 max-w-lg text-[16px] leading-relaxed md:text-[17px]', dark ? 'text-white/75' : 'text-fg-2')}>{description}</motion.p>
        <motion.div initial={reduce ? false : { opacity: 0, y: 8 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} transition={{ duration: 0.6, delay: 0.5 }} className="mt-8 flex flex-wrap gap-3">{actions}</motion.div>
      </div>
      <div className="relative overflow-hidden">
        <div className={cn('pointer-events-none absolute inset-x-0 top-0 z-10 h-16 bg-gradient-to-b to-transparent', fade)} />
        <div className={cn('pointer-events-none absolute inset-x-0 bottom-0 z-10 h-16 bg-gradient-to-t to-transparent', fade)} />
        <div className="grid grid-cols-2 gap-3 md:gap-4">
          <div className="flex flex-col gap-3 md:gap-4">{left.map((im, i) => item(im, i * 0.1))}</div>
          <div className="mt-10 flex flex-col gap-3 md:gap-4">{right.map((im, i) => item(im, 0.15 + i * 0.1))}</div>
        </div>
      </div>
    </section>
  )
}
