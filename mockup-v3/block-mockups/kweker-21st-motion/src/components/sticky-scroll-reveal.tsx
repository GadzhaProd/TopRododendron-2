// 21st.dev "Sticky Scroll Reveal" (Aceternity, id 952). Original mechanics kept:
// scroll progress picks the active card, titles/descriptions fade 1 / 0.3, a sticky
// panel shows the active card's content. Changes: it follows the page scroll instead
// of an inner 30rem scroll box, slate/gradient colours -> site tokens, larger panel
// (portrait-shaped) and it also shows on phones.
import { useRef, useState, type ReactNode } from 'react'
import { motion, useMotionValueEvent, useScroll } from 'framer-motion'
import { cn } from '@/lib'
export const StickyScroll = ({ content, contentClassName }: { content: { title: string; description: string; content?: ReactNode }[]; contentClassName?: string }) => {
  const [activeCard, setActiveCard] = useState(0)
  const ref = useRef<HTMLDivElement>(null)
  const { scrollYProgress } = useScroll({ target: ref, offset: ['start center', 'end center'] })
  const cardLength = content.length
  useMotionValueEvent(scrollYProgress, 'change', (latest) => {
    const bp = content.map((_, i) => i / cardLength)
    const closest = bp.reduce((acc, b, i) => (Math.abs(latest - b) < Math.abs(latest - bp[acc]) ? i : acc), 0)
    setActiveCard(closest)
  })
  return (
    <div ref={ref} className="relative mx-auto flex max-w-6xl justify-between gap-10 px-6 md:px-10">
      <div className="relative flex items-start">
        <div className="max-w-xl">
          {content.map((item, index) => (
            <div key={item.title + index} className="flex flex-col justify-center py-14 md:min-h-[70vh] md:py-0">
              <div className="relative mb-8 aspect-[4/5] w-full overflow-hidden rounded-xl md:hidden">{item.content}</div>
              <motion.h2 initial={{ opacity: 0 }} animate={{ opacity: activeCard === index ? 1 : 0.25 }} className="text-3xl font-semibold tracking-[-0.03em] text-foreground md:text-5xl">{item.title}</motion.h2>
              <motion.p initial={{ opacity: 0 }} animate={{ opacity: activeCard === index ? 1 : 0.25 }} className="mt-6 max-w-md text-lg leading-relaxed text-muted-foreground">{item.description}</motion.p>
            </div>
          ))}
        </div>
      </div>
      <div className={cn('sticky top-[12vh] hidden h-[76vh] w-[46%] shrink-0 overflow-hidden rounded-xl bg-muted md:block', contentClassName)}>
        {content.map((c, i) => (
          <motion.div key={i} className="absolute inset-0" initial={false} animate={{ opacity: activeCard === i ? 1 : 0, scale: activeCard === i ? 1 : 1.04 }} transition={{ duration: 0.6 }}>{c.content}</motion.div>
        ))}
      </div>
    </div>
  )
}
