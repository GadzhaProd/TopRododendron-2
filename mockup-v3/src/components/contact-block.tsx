import { cn } from '@/lib/utils'
import { ext } from './button'
import { company } from '@/data/content'

/** Contact block of concept C (ContactC): address, phones/e-mail, opening hours in three columns. */
export function ContactBlock({ dark = false, className }: { dark?: boolean; className?: string }) {
  const t = dark ? 'text-white' : 'text-fg'
  const m = dark ? 'text-white/75' : 'text-muted'
  return (
    <div className={cn('grid grid-cols-1 gap-8 md:grid-cols-3', t, className)}>
      <div><p className={cn('eyebrow mb-3', m)}>Kwekerij &amp; kantoor</p><a href={company.maps} {...ext} className="font-display text-[22px] leading-tight">{company.street}<br />{company.postal}</a><p className={cn('mt-2 text-[14px]', m)}>{company.pickup}</p></div>
      <div><p className={cn('eyebrow mb-3', m)}>Bereikbaar</p><a href={company.phone1Href} className="block font-display text-[22px] leading-tight">{company.phone1}</a><a href={company.phone2Href} className="block font-display text-[22px] leading-tight">{company.phone2}</a><a href={`mailto:${company.email}`} className={cn('mt-2 block text-[14px]', m)}>{company.email}</a></div>
      <div><p className={cn('eyebrow mb-3', m)}>Openingstijden</p>{company.hours.map(([d, h]) => <p key={d} className={cn('flex justify-between gap-6 border-b py-1.5 text-[14px]', dark ? 'border-white/10' : 'border-fg/10')}><span className={m}>{d}</span><span>{h}</span></p>)}</div>
    </div>
  )
}
