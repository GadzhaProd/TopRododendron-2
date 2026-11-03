import { cn } from '@/lib/utils'

/* Logo of concept C — "Blad": a geometric leaf-monogram (T + leaf) in a soft square.
   The same geometry is used for the favicon and for public/logo.svg. */
export function Mark({ className }: { className?: string }) {
  return (
    <svg viewBox="0 0 40 40" className={className} aria-hidden="true" focusable="false">
      <rect x="1" y="1" width="38" height="38" rx="11" fill="currentColor" />
      <path d="M12 13h16" stroke="var(--color-bg)" strokeWidth="2.6" strokeLinecap="round" />
      <path d="M20 13v15" stroke="var(--color-bg)" strokeWidth="2.6" strokeLinecap="round" />
      <path d="M20 28c0-6 3.5-9.5 9-9.5 0 6-3.5 9.5-9 9.5Z" fill="var(--color-bg)" />
    </svg>
  )
}

export function Logo({ dark = false, size = 'md', caption = false, className }: { dark?: boolean; size?: 'sm' | 'md' | 'lg'; caption?: boolean; className?: string }) {
  const s = { sm: ['size-8', 'text-[17px]', 'text-[10px]'], md: ['size-10', 'text-[20px]', 'text-[10px]'], lg: ['size-14', 'text-[26px]', 'text-[11px]'] }[size]
  return (
    <span className={cn('inline-flex items-center gap-2.5', dark ? 'text-white' : 'text-fg', className)}>
      <Mark className={cn(s[0], 'shrink-0')} />
      <span className="flex flex-col leading-none">
        <span className={cn('whitespace-nowrap font-display font-semibold tracking-[-0.02em]', s[1])}>Top Rhododendrons</span>
        {caption && <span className={cn('mt-1.5 tracking-[0.18em] uppercase opacity-80', s[2])}>Kwekerij Otterlo · sinds 2001</span>}
      </span>
    </span>
  )
}
