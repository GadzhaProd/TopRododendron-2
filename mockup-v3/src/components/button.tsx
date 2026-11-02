import * as React from 'react'
import { ArrowRight } from 'lucide-react'
import { cn } from '@/lib/utils'

type Variant = 'solid' | 'moss' | 'outline' | 'ghost' | 'white' | 'outline-white' | 'flower' | 'link'
type Size = 'sm' | 'md' | 'lg'

const base = 'inline-flex items-center justify-center gap-2 whitespace-nowrap font-semibold transition-colors duration-200 disabled:opacity-50 disabled:pointer-events-none select-none rounded-ui'
const variants: Record<Variant, string> = {
  solid: 'bg-night text-white hover:bg-moss-2',
  moss: 'bg-moss text-white hover:bg-moss-2',
  outline: 'border border-ink/35 text-ink hover:border-ink hover:bg-ink hover:text-white',
  ghost: 'text-ink hover:bg-ink/6',
  white: 'bg-white text-ink hover:bg-bg',
  'outline-white': 'border border-white/60 text-white hover:bg-white hover:text-ink hover:border-white',
  flower: 'bg-flower text-white hover:bg-[#a92c60]',
  link: 'text-ink underline underline-offset-4 decoration-ink/40 hover:decoration-ink px-0',
}
const sizes: Record<Size, string> = {
  sm: 'h-10 px-4 text-[14px]',
  md: 'h-12 px-5 text-[15px]',
  lg: 'h-13 px-6 text-[15.5px] md:h-14 md:px-7',
}

export interface ButtonProps extends Omit<React.ComponentProps<'a'>, 'onClick'> {
  variant?: Variant
  size?: Size
  arrow?: boolean
  as?: 'a' | 'button'
  type?: 'button' | 'submit'
  disabled?: boolean
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
