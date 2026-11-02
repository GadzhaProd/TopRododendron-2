import type { ReactNode } from 'react'
import { cn } from '@/lib/utils'

/** Section heading: big title + lead. An optional `label` chip is used at most once or twice per page. */
export function SectionHead({ label, title, text, className, align = 'left', dark = false, size = 'md', as: Tag = 'h2', children }: { label?: ReactNode; title: ReactNode; text?: ReactNode; className?: string; align?: 'left' | 'center'; dark?: boolean; size?: 'sm' | 'md' | 'lg' | 'xl'; as?: 'h1' | 'h2' | 'h3'; children?: ReactNode }) {
  const sz = { sm: 'text-[clamp(24px,2.6vw,32px)]', md: 'text-[clamp(30px,3.6vw,46px)]', lg: 'text-[clamp(36px,4.6vw,60px)]', xl: 'text-[clamp(40px,6vw,84px)]' }[size]
  return (
    <div className={cn('flex flex-col gap-4', align === 'center' && 'items-center text-center', className)}>
      {label && <Chip dark={dark}>{label}</Chip>}
      <Tag className={cn('title max-w-[20ch] text-balance', sz, dark ? 'text-white' : 'text-ink')}>{title}</Tag>
      {text && <p className={cn('max-w-[58ch] text-[16px] leading-relaxed md:text-[17.5px]', dark ? 'text-white/78' : 'text-ink-2')}>{text}</p>}
      {children}
    </div>
  )
}

export function Chip({ children, dark, className }: { children: ReactNode; dark?: boolean; className?: string }) {
  return <span className={cn('label inline-flex h-7 w-fit items-center rounded-full px-3', dark ? 'bg-white/12 text-white' : 'bg-ink/8 text-ink', className)}>{children}</span>
}

export function Swatch({ hex, light, className }: { hex: string; light?: boolean; className?: string }) {
  return <span aria-hidden="true" className={cn('swatch inline-block size-2.5 shrink-0 rounded-full', className)} style={{ background: hex, boxShadow: light ? 'inset 0 0 0 1px rgba(15,26,20,.35)' : undefined }} />
}
