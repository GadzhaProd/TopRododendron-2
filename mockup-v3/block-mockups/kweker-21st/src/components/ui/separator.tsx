// Minimal shadcn/ui Separator.
import { cn } from '@/lib'
export const Separator = ({ className }: { className?: string }) => <div role="separator" className={cn('h-px w-full shrink-0 bg-border', className)} />
