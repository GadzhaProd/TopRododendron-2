// Minimal shadcn/ui Badge (outline pill), used by Feature 8 (#26797) for its eyebrow.
import type { ReactNode } from 'react'
import { cn } from '@/lib'
export const Badge = ({ className, children, variant = 'outline' }: { className?: string; children: ReactNode; variant?: 'outline' | 'default' }) => (
  <span className={cn('inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-medium', variant === 'default' && 'border-transparent bg-primary text-primary-foreground', className)}>{children}</span>
)
