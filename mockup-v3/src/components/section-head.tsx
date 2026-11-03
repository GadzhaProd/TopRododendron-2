import type { ReactNode } from 'react'
import { cn } from '@/lib/utils'

/** Section heading of concept C (HeadC): tracked uppercase eyebrow, display title, lead. `label` / `eyebrow` are the same thing. */
export function SectionHead({ label, eyebrow, title, text, className, align = 'left', dark = false, size = 'md', as: Tag = 'h2', children }: { label?: ReactNode; eyebrow?: ReactNode; title: ReactNode; text?: ReactNode; className?: string; align?: 'left' | 'center'; dark?: boolean; size?: 'sm' | 'md' | 'lg' | 'xl'; as?: 'h1' | 'h2' | 'h3'; children?: ReactNode }) {
  const sz = { sm: 'text-[clamp(24px,2.6vw,32px)]', md: 'text-[clamp(30px,3.8vw,52px)]', lg: 'text-[clamp(36px,5vw,68px)]', xl: 'text-[clamp(40px,6vw,84px)]' }[size]
  const eb = eyebrow ?? label
  return (
    <div className={cn('flex flex-col gap-4', align === 'center' && 'items-center text-center', className)}>
      {eb && <p className={cn('eyebrow', dark ? 'text-white/75' : 'text-muted')}>{eb}</p>}
      <Tag className={cn('max-w-[min(20ch,100%)] font-display text-balance', sz, 'leading-[1.02]', dark ? 'text-white' : 'text-fg')}>{title}</Tag>
      {text && <p className={cn('max-w-[52ch] text-[16px] leading-relaxed md:text-[17px]', dark ? 'text-white/80' : 'text-fg-2')}>{text}</p>}
      {children}
    </div>
  )
}
export const HeadC = SectionHead

export function Chip({ children, dark, className }: { children: ReactNode; dark?: boolean; className?: string }) {
  return <span className={cn('inline-flex h-8 w-fit items-center rounded-full border px-3.5 text-[12.5px] font-medium', dark ? 'border-white/40 bg-white/15 text-white' : 'border-fg/15 bg-surface text-fg-2', className)}>{children}</span>
}

export function Swatch({ hex, light, className }: { hex: string; light?: boolean; className?: string }) {
  return <span aria-hidden="true" className={cn('swatch inline-block size-2.5 shrink-0 rounded-full', className)} style={{ background: hex, boxShadow: light ? 'inset 0 0 0 1px rgba(0,0,0,.12)' : undefined }} />
}
