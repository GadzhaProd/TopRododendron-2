import { cn } from '@/lib/utils'

/**
 * Brand mark: a five-lobed rhododendron floret drawn as a thin line, the way a
 * nursery catalogue would draw it. The same geometry is used for the favicon
 * (filled) and for public/logo.svg.
 */
const PETAL = 'M24 24C19.2 19.4 17.4 10.4 24 5.2c6.6 5.2 4.8 14.2 0 18.8Z'

export function Mark({ className, filled = false }: { className?: string; filled?: boolean }) {
  return (
    <svg viewBox="0 0 48 48" className={className} aria-hidden="true" focusable="false">
      {[0, 72, 144, 216, 288].map((r) => (
        <path key={r} d={PETAL} transform={`rotate(${r} 24 24)`} fill={filled ? 'currentColor' : 'none'} stroke="currentColor" strokeWidth={filled ? 1 : 1.5} strokeLinejoin="round" />
      ))}
      <circle cx="24" cy="24" r={filled ? 2.6 : 2.1} fill={filled ? 'var(--color-paper)' : 'currentColor'} />
    </svg>
  )
}

export function Logo({ dark = false, size = 'md', caption = false, className }: { dark?: boolean; size?: 'sm' | 'md' | 'lg'; caption?: boolean; className?: string }) {
  const s = { sm: ['size-8', 'text-[19px]', 'text-[9.5px]'], md: ['size-10', 'text-[22px]', 'text-[10px]'], lg: ['size-12', 'text-[26px]', 'text-[11px]'] }[size]
  return (
    <span className={cn('inline-flex items-center gap-2.5', dark ? 'text-white' : 'text-ink', className)}>
      <Mark className={cn(s[0], 'shrink-0')} />
      <span className="flex flex-col leading-none">
        <span className={cn('font-display-tight whitespace-nowrap', s[1])} style={{ fontVariationSettings: '"opsz" 24', letterSpacing: '-0.015em' }}>Top Rhododendrons</span>
        {caption && <span className={cn('mt-1.5 font-body font-medium uppercase tracking-[0.18em]', s[2], dark ? 'text-white/75' : 'text-muted')}>Kwekerij · Otterlo · sinds 2001</span>}
      </span>
    </span>
  )
}
