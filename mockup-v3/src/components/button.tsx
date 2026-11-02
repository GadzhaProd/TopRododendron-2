import * as React from 'react'
import { ArrowRight } from 'lucide-react'
import { cn } from '@/lib/utils'

type Variant = 'solid' | 'ink' | 'outline' | 'ghost' | 'paper' | 'outline-white' | 'link'
type Size = 'sm' | 'md' | 'lg'

const base = 'inline-flex items-center justify-center gap-2 whitespace-nowrap font-body font-medium transition-colors duration-200 disabled:opacity-60 disabled:pointer-events-none select-none rounded-ui'
const variants: Record<Variant, string> = {
  solid: 'bg-moss text-white hover:bg-moss-2',
  ink: 'bg-ink text-paper hover:bg-ink-2',
  outline: 'border border-ink/40 text-ink hover:border-ink hover:bg-ink hover:text-paper',
  ghost: 'text-ink hover:bg-ink/5',
  paper: 'bg-paper text-ink hover:bg-white',
  'outline-white': 'border border-white/70 text-white hover:bg-white hover:text-ink hover:border-white',
  link: 'text-ink underline underline-offset-4 decoration-line-2 hover:decoration-ink px-0',
}
const sizes: Record<Size, string> = {
  sm: 'h-10 px-4 text-[13.5px]',
  md: 'h-12 px-6 text-[14.5px]',
  lg: 'h-13 px-7 text-[15px] md:h-14 md:px-8',
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
