// Pill button of concept C (round 2, post-audit). The v3 variant names `moss`
// and `flower` stay as aliases so the other pages keep working.
import * as React from 'react'
import { ArrowRight } from 'lucide-react'
import { cn } from '@/lib/utils'

type Variant = 'solid' | 'moss' | 'outline' | 'ghost' | 'white' | 'outline-white' | 'flower' | 'link'
type Size = 'sm' | 'md' | 'lg'

const base = 'inline-flex items-center justify-center gap-2 whitespace-nowrap font-medium transition-all duration-300 disabled:opacity-60 disabled:pointer-events-none select-none'
const variants: Record<Variant, string> = {
  solid: 'bg-accent text-accent-fg hover:opacity-90',
  moss: 'bg-accent text-accent-fg hover:opacity-90',
  outline: 'border border-fg/35 text-fg hover:bg-fg hover:text-bg hover:border-fg',
  ghost: 'text-fg hover:bg-fg/5',
  white: 'bg-white text-[#141414] hover:bg-white/90',
  'outline-white': 'border border-white/70 text-white hover:bg-white hover:text-[#141414] hover:border-white',
  flower: 'bg-fg text-bg hover:opacity-90',
  link: 'text-fg underline-offset-4 hover:underline px-0',
}
const sizes: Record<Size, string> = {
  sm: 'h-10 px-4 text-[13px] rounded-ui',
  md: 'h-12 px-6 text-[14px] rounded-ui',
  lg: 'h-13 px-7 text-[15px] rounded-ui md:h-14 md:px-8',
}

export interface ButtonProps extends Omit<React.ComponentProps<'a'>, 'onClick'> {
  variant?: Variant
  size?: Size
  arrow?: boolean
  as?: 'a' | 'button'
  type?: 'button' | 'submit'
  disabled?: boolean
  tabIndex?: number
  onClick?: React.MouseEventHandler<HTMLElement>
}

export function Button({ className, variant = 'solid', size = 'md', arrow, as = 'a', children, onClick, type, disabled, ...props }: ButtonProps) {
  const cls = cn(base, variants[variant], sizes[size], 'group/btn', className)
  const inner = (
    <>
      {children}
      {arrow && <ArrowRight className="size-4 transition-transform duration-300 group-hover/btn:translate-x-1" aria-hidden="true" />}
    </>
  )
  if (as === 'button') return <button type={type ?? 'button'} className={cls} onClick={onClick as any} disabled={disabled} {...(props as any)}>{inner}</button>
  return <a className={cls} onClick={onClick as any} {...props}>{inner}</a>
}

/** External link helper: every https link opens in a new tab (artifact viewer sandbox). */
export const ext = { target: '_blank', rel: 'noopener noreferrer' } as const
