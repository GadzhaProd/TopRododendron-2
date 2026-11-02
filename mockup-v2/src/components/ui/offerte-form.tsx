// Adapted from 21st.dev "Contact Form" (kevingirelli): two-column contact section
// with native validation and pending/success states. Extended into a wholesale
// quote request with own primitives: visible select chevron, AA borders, required
// marks, Dutch error messages, month/year selects, no hard minimum quantity.
import { useId, useState, type FormEvent, type ReactNode } from 'react'
import { ChevronDown } from 'lucide-react'
import { cn } from '@/lib/utils'
import { Button } from './button'
import { varieties } from '@/data/content'

const field = 'w-full border bg-transparent px-4 h-12 text-[15px] outline-none transition-colors rounded-field'
const tone = (dark?: boolean) => (dark ? 'border-white/55 text-white placeholder:text-white/55 focus:border-white' : 'border-fg/45 text-fg placeholder:text-muted focus:border-fg')
export function Input(props: React.ComponentProps<'input'> & { dark?: boolean }) { const { dark, className, ...r } = props; return <input className={cn(field, tone(dark), className)} {...r} /> }
export function Textarea(props: React.ComponentProps<'textarea'> & { dark?: boolean }) { const { dark, className, ...r } = props; return <textarea className={cn(field, 'h-auto py-3', tone(dark), className)} {...r} /> }
export function Select(props: React.ComponentProps<'select'> & { dark?: boolean }) {
  const { dark, className, ...r } = props
  return (
    <span className="relative block">
      <select className={cn(field, 'appearance-none pr-11', tone(dark), dark ? '[&>option]:text-black' : '', className)} {...r} />
      <ChevronDown aria-hidden="true" className={cn('pointer-events-none absolute right-4 top-1/2 size-4 -translate-y-1/2', dark ? 'text-white/80' : 'text-fg-2')} />
    </span>
  )
}
export function Field({ label, htmlFor, children, dark, required, hint }: { label: ReactNode; htmlFor: string; children: ReactNode; dark?: boolean; required?: boolean; hint?: string }) {
  return (
    <div className="flex flex-col gap-2">
      <label htmlFor={htmlFor} className={cn('eyebrow', dark ? 'text-white/80' : 'text-fg-2')}>{label}{required && <span aria-hidden="true"> *</span>}</label>
      {children}
      {hint && <p id={`${htmlFor}-hint`} className={cn('text-[12.5px]', dark ? 'text-white/65' : 'text-muted')}>{hint}</p>}
    </div>
  )
}

const months = ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december']

export function OfferteForm({ dark = false, className, buttonVariant }: { dark?: boolean; className?: string; buttonVariant?: 'solid' | 'white' }) {
  const id = useId()
  const [status, setStatus] = useState<'idle' | 'pending' | 'success' | 'error'>('idle')
  const [errors, setErrors] = useState<string[]>([])
  function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault()
    if (status === 'pending') return
    const form = e.currentTarget
    const data = new FormData(form)
    const errs: string[] = []
    if (!String(data.get('bedrijf') ?? '').trim()) errs.push('Vul uw bedrijfsnaam in.')
    if (!String(data.get('naam') ?? '').trim()) errs.push('Vul de naam van de contactpersoon in.')
    const email = String(data.get('email') ?? '')
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) errs.push('Vul een geldig e-mailadres in.')
    if (!String(data.get('aantal') ?? '').trim()) errs.push('Vul het gewenste aantal planten in.')
    setErrors(errs)
    if (errs.length) { setStatus('error'); return }
    setStatus('pending')
    setTimeout(() => { form.reset(); setStatus('success') }, 900)
  }
  const year = new Date().getFullYear()
  return (
    <form onSubmit={onSubmit} noValidate data-status={status} className={cn('flex flex-col gap-5', className)} aria-describedby={`${id}-req`}>
      <p id={`${id}-req`} className={cn('text-[13px]', dark ? 'text-white/70' : 'text-muted')}>Velden met * zijn verplicht.</p>
      <div className="grid grid-cols-1 gap-5 sm:grid-cols-2">
        <Field label="Bedrijfsnaam" htmlFor={`${id}-b`} dark={dark} required><Input dark={dark} id={`${id}-b`} name="bedrijf" autoComplete="organization" required aria-required="true" /></Field>
        <Field label="Contactpersoon" htmlFor={`${id}-n`} dark={dark} required><Input dark={dark} id={`${id}-n`} name="naam" autoComplete="name" required aria-required="true" /></Field>
        <Field label="E-mail" htmlFor={`${id}-e`} dark={dark} required><Input dark={dark} id={`${id}-e`} name="email" type="email" autoComplete="email" required aria-required="true" /></Field>
        <Field label="Telefoon" htmlFor={`${id}-t`} dark={dark}><Input dark={dark} id={`${id}-t`} name="tel" type="tel" autoComplete="tel" /></Field>
        <Field label="Soort" htmlFor={`${id}-s`} dark={dark}>
          <Select dark={dark} id={`${id}-s`} name="soort" defaultValue="">
            <option value="">Nog niet bekend / gemengd</option>
            {varieties.map((v) => <option key={v.slug} value={v.slug}>{v.name}</option>)}
          </Select>
        </Field>
        <Field label="Maat" htmlFor={`${id}-m`} dark={dark}>
          <Select dark={dark} id={`${id}-m`} name="maat" defaultValue="">
            <option value="">Alle maten</option>
            {['40–60 cm', '60–80 cm', '80–100 cm', '100–120 cm', '120 cm +'].map((m) => <option key={m}>{m}</option>)}
          </Select>
        </Field>
        <Field label="Aantal planten" htmlFor={`${id}-a`} dark={dark} required hint="Partijprijzen vanaf 25 stuks; kleinere aantallen in overleg."><Input dark={dark} id={`${id}-a`} name="aantal" type="number" min={1} inputMode="numeric" placeholder="bijv. 60" required aria-required="true" aria-describedby={`${id}-a-hint`} /></Field>
        <div className="flex flex-col gap-2">
          <span className={cn('eyebrow', dark ? 'text-white/80' : 'text-fg-2')} id={`${id}-d-l`}>Gewenste levering</span>
          <div className="grid grid-cols-2 gap-3" role="group" aria-labelledby={`${id}-d-l`}>
            <Select dark={dark} name="maand" defaultValue="" aria-label="Maand"><option value="">Maand</option>{months.map((m) => <option key={m}>{m}</option>)}</Select>
            <Select dark={dark} name="jaar" defaultValue="" aria-label="Jaar"><option value="">Jaar</option>{[year, year + 1, year + 2].map((y) => <option key={y}>{y}</option>)}</Select>
          </div>
        </div>
      </div>
      <Field label="Toelichting" htmlFor={`${id}-x`} dark={dark}><Textarea dark={dark} id={`${id}-x`} name="toelichting" rows={4} placeholder="Locatie, planning, plantservice gewenst?" /></Field>
      {errors.length > 0 && (
        <ul role="alert" className={cn('flex flex-col gap-1 border-l-2 pl-4 text-[14px]', dark ? 'border-white text-white' : 'border-fg text-fg')}>{errors.map((e) => <li key={e}>{e}</li>)}</ul>
      )}
      <div className="flex flex-wrap items-center gap-4 pt-1">
        <Button as="button" variant={buttonVariant ?? (dark ? 'white' : 'solid')} size="lg" arrow className="w-full sm:w-auto">{status === 'pending' ? 'Versturen…' : 'Offerte aanvragen'}</Button>
        <p className={cn('text-[13px]', dark ? 'text-white/70' : 'text-muted')}>Binnen 24 uur een gespecificeerde offerte.</p>
      </div>
      <p role="status" aria-live="polite" className={cn('text-[14px] empty:hidden', dark ? 'text-white' : 'text-fg')}>{status === 'success' ? 'Dank u. Binnen 24 uur ontvangt u een gespecificeerde offerte.' : null}</p>
      <p className={cn('text-[12px]', dark ? 'text-white/55' : 'text-muted')}>Demo: dit formulier verstuurt in de mockup nog niets.</p>
    </form>
  )
}
