import * as React from 'react'
import { ArrowRight } from 'lucide-react'
import { cn } from '@/lib/utils'

type Variant = 'solid' | 'outline' | 'ghost' | 'white' | 'outline-white' | 'link'
type Size = 'sm' | 'md' | 'lg'

const base = 'inline-flex items-center justify-center gap-2 whitespace-nowrap font-medium transition-all duration-300 disabled:opacity-60 disabled:pointer-events-none select-none'
const variants: Record<Variant, string> = {
  solid: 'bg-accent text-accent-fg hover:opacity-90',
  outline: 'border border-fg/25 text-fg hover:bg-fg hover:text-bg hover:border-fg',
  ghost: 'text-fg hover:bg-fg/5',
  white: 'bg-white text-[#141414] hover:bg-white/90',
  'outline-white': 'border border-white/50 text-white hover:bg-white hover:text-[#141414] hover:border-white',
  link: 'text-fg underline-offset-4 hover:underline px-0',
}
const sizes: Record<Size, string> = {
  sm: 'h-10 px-4 text-[13px] rounded-ui',
  md: 'h-12 px-6 text-[14px] rounded-ui',
  lg: 'h-14 px-8 text-[15px] rounded-ui',
}

export interface ButtonProps extends React.ComponentProps<'a'> {
  variant?: Variant
  size?: Size
  arrow?: boolean
  as?: 'a' | 'button'
}

export function Button({ className, variant = 'solid', size = 'md', arrow, as = 'a', children, ...props }: ButtonProps) {
  const cls = cn(base, variants[variant], sizes[size], 'group/btn', className)
  const inner = (
    <>
      {children}
      {arrow && <ArrowRight className="size-4 transition-transform duration-300 group-hover/btn:translate-x-1" aria-hidden="true" />}
    </>
  )
  if (as === 'button') return <button type="submit" className={cls} {...(props as any)}>{inner}</button>
  return <a className={cls} {...props}>{inner}</a>
}
