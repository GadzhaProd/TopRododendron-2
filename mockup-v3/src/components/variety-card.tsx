import { ArrowUpRight } from 'lucide-react'
import { cn } from '@/lib/utils'
import { Swatch } from './section-head'
import { img, srcset, type Variety } from '@/data/content'

/**
 * Showcase card: big photo, name, colour, price-from. `href` defaults to the
 * product page; on the product page itself pass `#slug` so it stays in-page.
 * `compact` shows only the colour (small grids), `dark` is for night sections.
 */
export function VarietyCard({ v, className, sizes = '(min-width: 1024px) 33vw, (min-width: 640px) 50vw, 100vw', photo = 'bush', href, compact = false, dark = false, eager = false }: { v: Variety; className?: string; sizes?: string; photo?: 'bush' | 'flower'; href?: string; compact?: boolean; dark?: boolean; eager?: boolean }) {
  const name = photo === 'bush' ? `${v.slug}-2` : v.slug
  return (
    <a href={href ?? `product.html#${v.slug}`} className={cn('group/p flex h-full flex-col', className)}>
      <div className={cn('relative aspect-[4/5] overflow-hidden rounded-img', dark ? 'bg-moss-3' : 'bg-bg-2')}>
        <img src={img(name)} srcSet={srcset(name)} sizes={sizes} alt={`Rhododendron ${v.name}, ${v.color.toLowerCase()}`} loading={eager ? 'eager' : 'lazy'} className="h-full w-full object-cover img-treat transition-transform duration-[900ms] ease-[cubic-bezier(.22,1,.36,1)] group-hover/p:scale-[1.035]" />
        <span className={cn('num absolute bottom-3 left-3 rounded-full px-3 py-1.5 text-[13px] font-semibold backdrop-blur', dark ? 'bg-night/70 text-white' : 'bg-white/85 text-ink')}>vanaf € {v.from},–</span>
      </div>
      <div className="flex flex-1 flex-col pt-3.5">
        <div className="flex items-start justify-between gap-3">
          <h3 className={cn('text-[17px] font-semibold leading-tight tracking-[-0.01em] sm:text-[20px]', dark ? 'text-white' : 'text-ink')}>{v.name}</h3>
          {!compact && <span className={cn('mt-0.5 hidden size-7 shrink-0 place-items-center rounded-full transition-colors sm:grid', dark ? 'bg-white/12 text-white group-hover/p:bg-white group-hover/p:text-ink' : 'bg-ink/8 text-ink group-hover/p:bg-ink group-hover/p:text-white')}><ArrowUpRight className="size-3.5" /></span>}
        </div>
        <p className={cn('mt-1 flex items-center gap-2 text-[13.5px]', dark ? 'text-white/70' : 'text-muted')}><Swatch hex={v.hex} light={v.light} /><span className="truncate">{v.color}{!compact && <span className="hidden sm:inline"> · {v.bloei} · {v.hoogte}</span>}</span></p>
        {!compact && <p className={cn('mt-2.5 hidden text-[14.5px] leading-relaxed sm:block', dark ? 'text-white/75' : 'text-ink-2')}>{v.short}</p>}
      </div>
    </a>
  )
}
