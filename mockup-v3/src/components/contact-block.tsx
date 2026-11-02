import { cn } from '@/lib/utils'
import { ext } from './button'
import { company } from '@/data/content'

/** Address, phones, e-mail; opening hours only from md up (the footer has them on phones). */
export function ContactBlock({ dark = false, className, hours = true }: { dark?: boolean; className?: string; hours?: boolean }) {
  const t = dark ? 'text-white' : 'text-ink'
  const m = dark ? 'text-white/70' : 'text-muted'
  const line = dark ? 'border-white/12' : 'border-line'
  return (
    <div className={cn('grid grid-cols-1 gap-8 sm:grid-cols-2', t, className)}>
      <div>
        <p className={cn('label mb-2', m)}>Kwekerij &amp; kantoor</p>
        <a href={company.maps} {...ext} className="text-[20px] font-semibold leading-tight tracking-[-0.01em]">{company.street}<br />{company.postal}</a>
        <p className={cn('mt-2 text-[14px]', m)}>{company.region}. {company.pickup}</p>
      </div>
      <div>
        <p className={cn('label mb-2', m)}>Bereikbaar</p>
        <a href={company.phone1Href} className="num block text-[20px] font-semibold leading-tight">{company.phone1}</a>
        <a href={company.phone2Href} className="num block text-[20px] font-semibold leading-tight">{company.phone2}</a>
        <a href={`mailto:${company.email}`} className={cn('mt-2 block text-[14px] underline-offset-4 hover:underline', m)}>{company.email}</a>
        <a href={company.whatsapp} {...ext} className={cn('mt-1 block text-[14px] underline-offset-4 hover:underline', m)}>WhatsApp {company.whatsappLabel}</a>
      </div>
      {hours && (
        <div className="hidden sm:col-span-2 md:block">
          <p className={cn('label mb-2', m)}>Openingstijden</p>
          <div className="grid grid-cols-1 gap-x-8 sm:grid-cols-3">
            {company.hours.map(([d, h]) => <p key={d} className={cn('flex justify-between gap-4 border-b py-1.5 text-[14px] sm:flex-col sm:gap-0 sm:border-b-0', line)}><span className={m}>{d}</span><span className="num font-medium">{h}</span></p>)}
          </div>
        </div>
      )}
    </div>
  )
}
