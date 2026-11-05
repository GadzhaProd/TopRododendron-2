// Gallery Grid with Captions (gallery-02) — 21st.dev id 26909, by ln-dev7.
// Only its tile is used: <figure> with a rounded, bordered image and a
// <figcaption> beneath (caption line + smaller sub line). Changed: tokens, our
// 28px radius, a real portrait instead of the gradient tile, no hover scale,
// height:auto + aspect-ratio so the <img> width/height attributes never stretch it.
import type { ReactNode } from 'react'
import { cn } from '@/lib'

export function CaptionedFigure({ src, alt, caption, sub, className, below }: { src: string; alt: string; caption?: ReactNode; sub?: ReactNode; className?: string; below?: ReactNode }) {
  return (
    <figure className={cn('group flex w-full flex-col gap-3', className)}>
      <img src={src} alt={alt} width={1200} height={1418} className="aspect-[4/4.6] w-full overflow-hidden rounded-img border border-border object-cover object-[50%_22%] sm:aspect-[4/5]" />
      {caption && (
        <figcaption className="flex flex-col gap-0.5 px-1">
          <p className="text-[17px] font-semibold tracking-[-0.01em] text-foreground">{caption}</p>
          <p className="text-[14px] leading-[1.5] text-muted-foreground">{sub}</p>
        </figcaption>
      )}
      {below}
    </figure>
  )
}
