// Minimal shadcn/ui Button (default + outline, asChild), pill-shaped like the site.
import { cloneElement, isValidElement, type ReactElement, type ReactNode } from 'react'
import { cn } from '@/lib'
type Props = { variant?: 'default' | 'outline'; asChild?: boolean; className?: string; children: ReactNode }
export function Button({ variant = 'default', asChild, className, children }: Props) {
  const cls = cn(
    'inline-flex h-11 items-center justify-center gap-2 rounded-full px-6 text-[15px] font-medium transition-colors',
    variant === 'default' ? 'bg-primary text-primary-foreground hover:bg-primary/90' : 'border border-foreground/25 bg-transparent text-foreground hover:bg-foreground/5',
    className,
  )
  if (asChild && isValidElement(children)) { const el = children as ReactElement<{ className?: string }>; return cloneElement(el, { className: cn(cls, el.props.className) }) }
  return <button className={cls}>{children}</button>
}
