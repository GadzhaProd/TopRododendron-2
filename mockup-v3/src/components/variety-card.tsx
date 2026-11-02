import { ArrowUpRight } from 'lucide-react'
import { cn } from '@/lib/utils'
import { Swatch } from './section-head'
import { img, srcset, type Variety } from '@/data/content'

/** Catalogue card: numbered, photo, name, colour, bloom, height, price from. */
export function VarietyCard({ v, index, className, sizes = '(min-width: 1024px) 25vw, (min-width: 640px) 50vw, 100vw', photo = 'bush' }: { v: Variety; index?: number; className?: string; sizes?: string; photo?: 'bush' | 'flower' }) {
  const name = photo === 'bush' ? `${v.slug}-2` : v.slug
  return (
    <a href={`product.html#${v.slug}`} className={cn('group/p flex h-full flex-col', className)}>
      <div className="relative aspect-[4/5] overflow-hidden rounded-img bg-paper-2">
        <img src={img(name)} srcSet={srcset(name)} sizes={sizes} alt={`Rhododendron ${v.name}, ${v.color.toLowerCase()}`} loading="lazy" className="h-full w-full object-cover img-treat transition-transform duration-[900ms] ease-[cubic-bezier(.22,1,.36,1)] group-hover/p:scale-[1.035]" />
        {index !== undefined && <span className="num absolute left-3 top-3 rounded-[2px] bg-paper/90 px-2 py-1 text-[11.5px] font-semibold tracking-[0.08em] text-ink">{String(index).padStart(2, '0')}</span>}
      </div>
      <div className="flex flex-1 flex-col pt-4">
        <div className="flex items-start justify-between gap-3">
          <h3 className="font-display text-[18px] leading-tight sm:text-[22px] md:text-[24px]">{v.name}</h3>
          <span className="mt-1 hidden size-7 shrink-0 sm:grid place-items-center rounded-full border border-ink/25 text-ink transition-colors group-hover/p:border-ink group-hover/p:bg-ink group-hover/p:text-paper"><ArrowUpRight className="size-3.5" /></span>
        </div>
        <p className="mt-1.5 flex flex-wrap items-center gap-x-2 gap-y-0.5 text-[12.5px] text-muted sm:text-[13.5px]"><Swatch hex={v.hex} light={v.light} />{v.color}<span aria-hidden="true">·</span>{v.bloei}<span aria-hidden="true">·</span>{v.hoogte}</p>
        <p className="mt-3 hidden text-[14.5px] leading-relaxed text-ink-2 sm:block">{v.short}</p>
        <p className="num mt-auto pt-4 text-[14.5px]"><span className="text-muted">vanaf</span> <span className="font-semibold text-ink">€ {v.from},–</span></p>
      </div>
    </a>
  )
}
