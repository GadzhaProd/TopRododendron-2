// Adapted from 21st.dev "Shop by Category Grid" (ziegfiroyt, ecommerce4):
// image tiles with hover zoom and bottom overlay text. Generalised (no badges,
// configurable aspect ratio and columns, heavier scrim, srcset).
import { ArrowRight } from 'lucide-react'
import { cn } from '@/lib/utils'

export type ImageCard = { name: string; description?: string; image: string; srcSet?: string; href: string; meta?: string; position?: string; onClick?: () => void }

export function ImageCardGrid({ cards, cols = 3, aspect = 'aspect-[4/5]', radius = 'rounded-img', className, titleClassName }: { cards: ImageCard[]; cols?: 2 | 3 | 4; aspect?: string; radius?: string; className?: string; titleClassName?: string }) {
  const grid = { 2: 'md:grid-cols-2', 3: 'md:grid-cols-3', 4: 'md:grid-cols-2 lg:grid-cols-4' }[cols]
  return (
    <div className={cn('grid gap-4 md:gap-5', grid, className)}>
      {cards.map((c) => (
        <a key={c.name} href={c.href} onClick={c.onClick ? (e) => { e.preventDefault(); c.onClick?.() } : undefined} className={cn('group/card relative block overflow-hidden bg-bg-2', radius)}>
          <div className={cn('overflow-hidden', aspect)}>
            <img src={c.image} srcSet={c.srcSet} sizes="(min-width: 768px) 33vw, 100vw" alt={c.name} loading="lazy" className="size-full object-cover img-treat transition-transform duration-[900ms] ease-[cubic-bezier(.22,1,.36,1)] group-hover/card:scale-[1.04]" style={{ objectPosition: c.position }} />
            <div className="absolute inset-0 bg-gradient-to-t from-black/85 via-black/35 to-black/5" />
          </div>
          <div className="absolute inset-x-0 bottom-0 p-5 text-white md:p-6 on-dark">
            {c.meta && <p className="eyebrow mb-2 text-white/80">{c.meta}</p>}
            <h3 className={cn('font-display text-[26px] leading-none md:text-[30px]', titleClassName)}>{c.name}</h3>
            {c.description && <p className="mt-2 max-w-[32ch] text-[14px] leading-relaxed text-white/85">{c.description}</p>}
            <div className="mt-4 flex items-center gap-2 text-[13px] text-white/90"><span className="h-px w-8 bg-white/60 transition-all duration-500 group-hover/card:w-12" /><ArrowRight className="size-4" aria-hidden="true" /></div>
          </div>
        </a>
      ))}
    </div>
  )
}
