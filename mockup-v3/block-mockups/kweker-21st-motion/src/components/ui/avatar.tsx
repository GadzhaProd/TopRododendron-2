// Minimal shadcn/ui Avatar.
import type { ReactNode } from 'react'
import { cn } from '@/lib'
export const Avatar = ({ className, children }: { className?: string; children: ReactNode }) => <span className={cn('relative flex shrink-0 overflow-hidden rounded-full', className)}>{children}</span>
export const AvatarImage = ({ src, alt, className }: { src: string; alt: string; className?: string }) => <img src={src} alt={alt} className={cn('aspect-square size-full object-cover', className)} />
export const AvatarFallback = ({ className, children }: { className?: string; children: ReactNode }) => <span className={cn('hidden', className)}>{children}</span>
