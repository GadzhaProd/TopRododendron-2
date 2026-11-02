// Form primitives: visible chevron on select, AA borders, required marks,
// optional hint text. Dark variant for the moss offerte block.
import { forwardRef, type ReactNode } from 'react'
import { ChevronDown, Check } from 'lucide-react'
import { cn } from '@/lib/utils'

const field = 'w-full border bg-transparent px-3.5 h-12 text-[15px] outline-none transition-colors rounded-field font-body'
const tone = (dark?: boolean) => (dark ? 'border-white/60 text-white placeholder:text-white/65 focus:border-white bg-white/5' : 'border-ink/55 text-ink placeholder:text-muted focus:border-ink bg-surface')

export const Input = forwardRef<HTMLInputElement, React.ComponentProps<'input'> & { dark?: boolean }>(function Input(props, ref) { const { dark, className, ...r } = props; return <input ref={ref} className={cn(field, tone(dark), className)} {...r} /> })
export function Textarea(props: React.ComponentProps<'textarea'> & { dark?: boolean }) { const { dark, className, ...r } = props; return <textarea className={cn(field, 'h-auto py-3', tone(dark), className)} {...r} /> }
export function Select(props: React.ComponentProps<'select'> & { dark?: boolean }) {
  const { dark, className, ...r } = props
  return (
    <span className="relative block">
      <select className={cn(field, 'appearance-none pr-11', tone(dark), dark ? '[&>option]:text-ink' : '', className)} {...r} />
      <ChevronDown aria-hidden="true" className={cn('pointer-events-none absolute right-3.5 top-1/2 size-4 -translate-y-1/2', dark ? 'text-white/80' : 'text-ink-2')} />
    </span>
  )
}
export function Field({ label, htmlFor, children, dark, required, hint, className }: { label: ReactNode; htmlFor: string; children: ReactNode; dark?: boolean; required?: boolean; hint?: string; className?: string }) {
  return (
    <div className={cn('flex flex-col gap-2', className)}>
      <label htmlFor={htmlFor} className={cn('text-[13px] font-medium', dark ? 'text-white/85' : 'text-ink-2')}>{label}{required && <span aria-hidden="true"> *</span>}</label>
      {children}
      {hint && <p id={`${htmlFor}-hint`} className={cn('text-[12.5px]', dark ? 'text-white/65' : 'text-muted')}>{hint}</p>}
    </div>
  )
}

export function Checkbox({ id, checked, onChange, children, dark }: { id: string; checked: boolean; onChange: (v: boolean) => void; children: ReactNode; dark?: boolean }) {
  return (
    <label htmlFor={id} className={cn('flex cursor-pointer items-start gap-3 text-[14.5px]', dark ? 'text-white/90' : 'text-ink')}>
      <span className="relative mt-0.5 inline-flex size-5 shrink-0 items-center justify-center">
        <input id={id} type="checkbox" checked={checked} onChange={(e) => onChange(e.target.checked)} className="peer absolute inset-0 size-5 cursor-pointer appearance-none rounded-[3px] border border-ink/55 bg-surface checked:border-moss checked:bg-moss" />
        <Check aria-hidden="true" className="pointer-events-none relative size-3.5 text-white opacity-0 peer-checked:opacity-100" strokeWidth={3} />
      </span>
      <span>{children}</span>
    </label>
  )
}

export function Segmented<T extends string>({ options, value, onChange, label }: { options: { value: T; label: string }[]; value: T; onChange: (v: T) => void; label: string }) {
  return (
    <div role="radiogroup" aria-label={label} className="inline-flex rounded-ui border border-ink/50 bg-surface p-1">
      {options.map((o) => (
        <button key={o.value} type="button" role="radio" aria-checked={value === o.value} onClick={() => onChange(o.value)} className={cn('h-9 rounded-[2px] px-4 text-[13.5px] font-medium transition-colors', value === o.value ? 'bg-ink text-paper' : 'text-ink-2 hover:text-ink')}>{o.label}</button>
      ))}
    </div>
  )
}
