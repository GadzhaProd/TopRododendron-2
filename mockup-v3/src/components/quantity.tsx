// Quantity stepper (idea: 21st.dev "Quantity Stepper" 29940) — press-and-hold
// repeat, spinbutton semantics, no rolling-digit theatre.
import { useEffect, useRef } from 'react'
import { Minus, Plus } from 'lucide-react'
import { cn } from '@/lib/utils'

export function Quantity({ value, onChange, min = 1, max = 999, label = 'Aantal', className }: { value: number; onChange: (n: number) => void; min?: number; max?: number; label?: string; className?: string }) {
  const timer = useRef<ReturnType<typeof setTimeout> | null>(null)
  const repeat = useRef<ReturnType<typeof setInterval> | null>(null)
  const latest = useRef(value)
  latest.current = value
  const clamp = (n: number) => Math.max(min, Math.min(max, n))
  const stop = () => { if (timer.current) clearTimeout(timer.current); if (repeat.current) clearInterval(repeat.current); timer.current = null; repeat.current = null }
  const start = (d: number) => {
    onChange(clamp(latest.current + d))
    timer.current = setTimeout(() => { repeat.current = setInterval(() => onChange(clamp(latest.current + d)), 110) }, 420)
  }
  useEffect(() => stop, [])
  return (
    <div className={cn('inline-flex h-12 items-center rounded-field border border-ink/35 bg-surface', className)} role="group" aria-label={label}>
      <button type="button" onPointerDown={() => start(-1)} onPointerUp={stop} onPointerLeave={stop} onPointerCancel={stop} onKeyDown={(e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); onChange(clamp(value - 1)) } }} aria-label="Minder" disabled={value <= min} className="grid size-12 place-items-center disabled:opacity-40"><Minus className="size-4" /></button>
      <input type="text" inputMode="numeric" role="spinbutton" aria-label={label} aria-valuenow={value} aria-valuemin={min} aria-valuemax={max} value={value} onChange={(e) => { const n = parseInt(e.target.value, 10); if (!Number.isNaN(n)) onChange(clamp(n)) }} onKeyDown={(e) => { if (e.key === 'ArrowUp') { e.preventDefault(); onChange(clamp(value + 1)) } if (e.key === 'ArrowDown') { e.preventDefault(); onChange(clamp(value - 1)) } }} className="num h-full w-10 bg-transparent text-center text-[15px] outline-none" />
      <button type="button" onPointerDown={() => start(1)} onPointerUp={stop} onPointerLeave={stop} onPointerCancel={stop} onKeyDown={(e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); onChange(clamp(value + 1)) } }} aria-label="Meer" className="grid size-12 place-items-center"><Plus className="size-4" /></button>
    </div>
  )
}
