// Key Value List (key-value-list) — 21st.dev id 25162, by corr.
// Kept: a <dl> in the "bordered" variant (rounded, 1px border, border-t between
// rows), each row a grid of label | value with an optional small description.
// Changed: tokens and Manrope, no truncate (values wrap), our 28px radius and
// card background, two columns on wide screens (kv-grid in styles.css).
import type { ReactNode } from 'react'
import { cn } from '@/lib'

export type KeyValueListItem = { label: ReactNode; value: ReactNode; description?: ReactNode }

export function KeyValueList({ items, className }: { items: KeyValueListItem[]; className?: string }) {
  return (
    <dl className={cn('kv-grid mt-12 overflow-hidden rounded-img border border-border bg-card text-[15px] lg:mt-14', className)}>
      {items.map((item, index) => (
        <div key={index} className={cn('grid gap-1 px-5 py-4 sm:grid-cols-[9rem_minmax(0,1fr)] sm:gap-4 sm:px-7 sm:py-[18px]', index > 0 && 'border-t border-border')}>
          <dt className="text-muted-foreground">{item.label}</dt>
          <dd className="min-w-0 font-semibold text-foreground">
            <div>{item.value}</div>
            {item.description ? <div className="mt-0.5 text-[13.5px] font-normal text-muted-foreground">{item.description}</div> : null}
          </dd>
        </div>
      ))}
    </dl>
  )
}

export default KeyValueList
