// Adapted from 21st.dev "Contact Form" (kevingirelli): two-column contact section
// with native validation and pending/success states. Extended into a wholesale
// quote request (bedrijf, soorten, maten, aantal, leverdatum) with own primitives.
import { useId, useState, type FormEvent, type ReactNode } from 'react'
import { cn } from '@/lib/utils'
import { Button } from './button'
import { varieties } from '@/data/content'

const field = 'w-full border bg-transparent px-4 h-12 text-[15px] outline-none transition-colors focus:border-current rounded-ui'
export function Input(props: React.ComponentProps<'input'> & { dark?: boolean }) { const { dark, className, ...r } = props; return <input className={cn(field, dark ? 'border-white/25 text-white placeholder:text-white/40' : 'border-fg/20 text-fg placeholder:text-muted', className)} {...r} /> }
export function Textarea(props: React.ComponentProps<'textarea'> & { dark?: boolean }) { const { dark, className, ...r } = props; return <textarea className={cn(field, 'h-auto py-3', dark ? 'border-white/25 text-white placeholder:text-white/40' : 'border-fg/20 text-fg placeholder:text-muted', className)} {...r} /> }
export function Select(props: React.ComponentProps<'select'> & { dark?: boolean }) { const { dark, className, ...r } = props; return <select className={cn(field, 'appearance-none', dark ? 'border-white/25 text-white [&>option]:text-black' : 'border-fg/20 text-fg', className)} {...r} /> }
export function Field({ label, htmlFor, children, dark }: { label: ReactNode; htmlFor: string; children: ReactNode; dark?: boolean }) {
  return <div className="flex flex-col gap-2"><label htmlFor={htmlFor} className={cn('eyebrow', dark ? 'text-white/70' : 'text-fg-2')}>{label}</label>{children}</div>
}

export function OfferteForm({ dark = false, className, buttonVariant }: { dark?: boolean; className?: string; buttonVariant?: 'solid' | 'white' }) {
  const id = useId()
  const [status, setStatus] = useState<'idle' | 'pending' | 'success'>('idle')
  function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault()
    if (status === 'pending') return
    setStatus('pending')
    const form = e.currentTarget
    setTimeout(() => { form.reset(); setStatus('success') }, 900)
  }
  return (
    <form onSubmit={onSubmit} data-status={status} className={cn('flex flex-col gap-5', className)} noValidate={false}>
      <div className="grid gap-5 sm:grid-cols-2">
        <Field label="Bedrijfsnaam" htmlFor={`${id}-b`} dark={dark}><Input dark={dark} id={`${id}-b`} name="bedrijf" autoComplete="organization" required /></Field>
        <Field label="Contactpersoon" htmlFor={`${id}-n`} dark={dark}><Input dark={dark} id={`${id}-n`} name="naam" autoComplete="name" required /></Field>
        <Field label="E-mail" htmlFor={`${id}-e`} dark={dark}><Input dark={dark} id={`${id}-e`} name="email" type="email" autoComplete="email" required /></Field>
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
        <Field label="Aantal planten" htmlFor={`${id}-a`} dark={dark}><Input dark={dark} id={`${id}-a`} name="aantal" type="number" min={25} placeholder="vanaf 25" required /></Field>
        <Field label="Gewenste leverdatum" htmlFor={`${id}-d`} dark={dark}><Input dark={dark} id={`${id}-d`} name="datum" type="month" /></Field>
      </div>
      <Field label="Toelichting" htmlFor={`${id}-x`} dark={dark}><Textarea dark={dark} id={`${id}-x`} name="toelichting" rows={4} placeholder="Locatie, planning, plantservice gewenst?" /></Field>
      <div className="flex flex-wrap items-center gap-4 pt-1">
        <Button as="button" variant={buttonVariant ?? (dark ? 'white' : 'solid')} size="lg" arrow className="w-full sm:w-auto">{status === 'pending' ? 'Versturen…' : 'Offerte aanvragen'}</Button>
        <p className={cn('text-[13px]', dark ? 'text-white/60' : 'text-muted')}>Binnen 24 uur een gespecificeerde offerte.</p>
      </div>
      <p role="status" className={cn('text-[14px] empty:hidden', dark ? 'text-white' : 'text-fg')}>{status === 'success' ? 'Dank u. Wij nemen binnen één werkdag contact met u op.' : null}</p>
    </form>
  )
}
