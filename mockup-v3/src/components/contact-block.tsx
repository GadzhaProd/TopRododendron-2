import { cn } from '@/lib/utils'
import { company } from '@/data/content'

/** Address, phones, e-mail and opening hours as a calm three-column block. */
export function ContactBlock({ dark = false, className }: { dark?: boolean; className?: string }) {
  const t = dark ? 'text-white' : 'text-ink'
  const m = dark ? 'text-white/70' : 'text-muted'
  const line = dark ? 'border-white/12' : 'border-line'
  return (
    <div className={cn('grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3', t, className)}>
      <div>
        <p className={cn('eyebrow mb-3', m)}>Kwekerij &amp; kantoor</p>
        <a href={company.maps} target="_blank" rel="noopener noreferrer" className="font-display text-[22px] leading-tight">{company.street}<br />{company.postal}</a>
        <p className={cn('mt-2 text-[14px]', m)}>{company.region}. {company.pickup}</p>
      </div>
      <div>
        <p className={cn('eyebrow mb-3', m)}>Bereikbaar</p>
        <a href={company.phone1Href} className="num block font-display text-[22px] leading-tight">{company.phone1}</a>
        <a href={company.phone2Href} className="num block font-display text-[22px] leading-tight">{company.phone2}</a>
        <a href={`mailto:${company.email}`} className={cn('mt-2 block text-[14px] underline-offset-4 hover:underline', m)}>{company.email}</a>
        <a href={company.whatsapp} target="_blank" rel="noopener noreferrer" className={cn('mt-1 block text-[14px] underline-offset-4 hover:underline', m)}>WhatsApp {company.whatsappLabel}</a>
      </div>
      <div className="sm:col-span-2 lg:col-span-1">
        <p className={cn('eyebrow mb-3', m)}>Openingstijden</p>
        {company.hours.map(([d, h]) => <p key={d} className={cn('flex justify-between gap-6 border-b py-1.5 text-[14px]', line)}><span className={m}>{d}</span><span className="num">{h}</span></p>)}
      </div>
    </div>
  )
}
