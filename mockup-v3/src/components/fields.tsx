// Form primitives: visible chevron on select, AA borders, required marks,
// hint text, and per-field error binding (aria-invalid + aria-describedby).
import { forwardRef, type ReactNode } from 'react'
import { ChevronDown, Check } from 'lucide-react'
import { cn } from '@/lib/utils'

const field = 'w-full border bg-transparent px-3.5 h-12 text-[15px] outline-none transition-colors rounded-field'
const tone = (dark?: boolean, invalid?: boolean) => cn(
  dark ? 'border-white/60 text-white placeholder:text-white/65 focus:border-white bg-white/6' : 'border-ink/45 text-ink placeholder:text-muted focus:border-ink bg-surface',
  invalid && (dark ? 'border-flower-2' : 'border-flower'),
)

type Extra = { dark?: boolean; invalid?: boolean }
export const Input = forwardRef<HTMLInputElement, React.ComponentProps<'input'> & Extra>(function Input(props, ref) { const { dark, invalid, className, ...r } = props; return <input ref={ref} aria-invalid={invalid || undefined} className={cn(field, tone(dark, invalid), className)} {...r} /> })
export const Textarea = forwardRef<HTMLTextAreaElement, React.ComponentProps<'textarea'> & Extra>(function Textarea(props, ref) { const { dark, invalid, className, ...r } = props; return <textarea ref={ref} aria-invalid={invalid || undefined} className={cn(field, 'h-auto py-3', tone(dark, invalid), className)} {...r} /> })
export function Select(props: React.ComponentProps<'select'> & Extra) {
  const { dark, invalid, className, ...r } = props
  return (
    <span className="relative block">
      <select aria-invalid={invalid || undefined} className={cn(field, 'appearance-none pr-11', tone(dark, invalid), dark ? '[&>option]:text-ink' : '', className)} {...r} />
      <ChevronDown aria-hidden="true" className={cn('pointer-events-none absolute right-3.5 top-1/2 size-4 -translate-y-1/2', dark ? 'text-white/80' : 'text-ink-2')} />
    </span>
  )
}

/** Field wrapper. `error` renders the message under the control with id `${htmlFor}-err` (bind via aria-describedby). */
export function Field({ label, htmlFor, children, dark, required, hint, error, className }: { label: ReactNode; htmlFor: string; children: ReactNode; dark?: boolean; required?: boolean; hint?: string; error?: string; className?: string }) {
  return (
    <div className={cn('flex flex-col gap-2', className)}>
      <label htmlFor={htmlFor} className={cn('label', dark ? 'text-white/90' : 'text-ink-2')}>{label}{required && <span aria-hidden="true"> *</span>}</label>
      {children}
      {hint && !error && <p id={`${htmlFor}-hint`} className={cn('text-[12.5px]', dark ? 'text-white/65' : 'text-muted')}>{hint}</p>}
      {error && <p id={`${htmlFor}-err`} className={cn('text-[13px] font-medium', dark ? 'text-flower-2' : 'text-flower')}>{error}</p>}
    </div>
  )
}
export const describe = (id: string, error?: string, hint?: string) => (error ? `${id}-err` : hint ? `${id}-hint` : undefined)

export function Checkbox({ id, checked, onChange, children }: { id: string; checked: boolean; onChange: (v: boolean) => void; children: ReactNode }) {
  return (
    <label htmlFor={id} className="flex cursor-pointer items-start gap-3 text-[14.5px] text-ink">
      <span className="relative mt-0.5 inline-flex size-5 shrink-0 items-center justify-center">
        <input id={id} type="checkbox" checked={checked} onChange={(e) => onChange(e.target.checked)} className="peer absolute inset-0 size-5 cursor-pointer appearance-none rounded-[5px] border border-ink/50 bg-surface checked:border-night checked:bg-night" />
        <Check aria-hidden="true" className="pointer-events-none relative size-3.5 text-white opacity-0 peer-checked:opacity-100" strokeWidth={3} />
      </span>
      <span>{children}</span>
    </label>
  )
}
