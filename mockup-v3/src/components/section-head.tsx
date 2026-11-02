import type { ReactNode } from 'react'
import { cn } from '@/lib/utils'

/** Section heading: small index/eyebrow, serif title, optional lead paragraph. */
export function SectionHead({ eyebrow, title, text, className, align = 'left', dark = false, size = 'md', as: Tag = 'h2' }: { eyebrow?: ReactNode; title: ReactNode; text?: ReactNode; className?: string; align?: 'left' | 'center'; dark?: boolean; size?: 'sm' | 'md' | 'lg' | 'xl'; as?: 'h1' | 'h2' | 'h3' }) {
  const sz = { sm: 'text-[clamp(26px,3vw,34px)]', md: 'text-[clamp(30px,3.8vw,46px)]', lg: 'text-[clamp(36px,4.8vw,62px)]', xl: 'text-[clamp(40px,6vw,80px)]' }[size]
  return (
    <div className={cn('flex flex-col gap-4', align === 'center' && 'items-center text-center', className)}>
      {eyebrow && <p className={cn('eyebrow', dark ? 'text-white/70' : 'text-bloom')}>{eyebrow}</p>}
      <Tag className={cn('font-display max-w-[22ch] text-balance leading-[1.04]', sz, dark ? 'text-white' : 'text-ink')} style={{ fontVariationSettings: '"opsz" 72' }}>{title}</Tag>
      {text && <p className={cn('max-w-[56ch] text-[16px] leading-relaxed md:text-[17.5px]', dark ? 'text-white/80' : 'text-ink-2')}>{text}</p>}
    </div>
  )
}

export function Swatch({ hex, light, className }: { hex: string; light?: boolean; className?: string }) {
  return <span aria-hidden="true" className={cn('inline-block size-2.5 shrink-0 rounded-full', className)} style={{ background: hex, boxShadow: light ? 'inset 0 0 0 1px rgba(27,31,27,.3)' : undefined }} />
}
