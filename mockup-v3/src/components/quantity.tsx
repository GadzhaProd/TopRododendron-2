// Quantity stepper (idea: 21st.dev "Quantity Stepper" 29940). A tap counts as
// one step on click; press-and-hold starts auto-repeat after 450 ms, and a
// scroll gesture that begins on a button changes nothing.
import { useEffect, useRef } from 'react'
import { Minus, Plus } from 'lucide-react'
import { cn } from '@/lib/utils'

export function Quantity({ value, onChange, min = 1, max = 999, label = 'Aantal', className, dark = false }: { value: number; onChange: (n: number) => void; min?: number; max?: number; label?: string; className?: string; dark?: boolean }) {
  const timer = useRef<ReturnType<typeof setTimeout> | null>(null)
  const repeat = useRef<ReturnType<typeof setInterval> | null>(null)
  const held = useRef(false)
  const latest = useRef(value)
  latest.current = value
  const clamp = (n: number) => Math.max(min, Math.min(max, n))
  const stop = () => { if (timer.current) clearTimeout(timer.current); if (repeat.current) clearInterval(repeat.current); timer.current = null; repeat.current = null }
  const down = (d: number) => {
    held.current = false
    timer.current = setTimeout(() => { held.current = true; onChange(clamp(latest.current + d)); repeat.current = setInterval(() => onChange(clamp(latest.current + d)), 110) }, 450)
  }
  const click = (d: number) => { if (held.current) { held.current = false; return } onChange(clamp(latest.current + d)) }
  useEffect(() => stop, [])
  const btn = 'grid size-12 place-items-center disabled:opacity-40'
  return (
    <div className={cn('inline-flex h-12 items-center rounded-field border', dark ? 'border-white/50 bg-white/6 text-white' : 'border-ink/45 bg-surface', className)} role="group" aria-label={label}>
      <button type="button" onPointerDown={() => down(-1)} onPointerUp={stop} onPointerLeave={stop} onPointerCancel={stop} onClick={() => click(-1)} aria-label="Minder" disabled={value <= min} className={btn}><Minus className="size-4" /></button>
      <input type="text" inputMode="numeric" role="spinbutton" aria-label={label} aria-valuenow={value} aria-valuemin={min} aria-valuemax={max} value={value} onChange={(e) => { const n = parseInt(e.target.value, 10); if (!Number.isNaN(n)) onChange(clamp(n)) }} onKeyDown={(e) => { if (e.key === 'ArrowUp') { e.preventDefault(); onChange(clamp(value + 1)) } if (e.key === 'ArrowDown') { e.preventDefault(); onChange(clamp(value - 1)) } }} className="num h-full w-10 bg-transparent text-center text-[15px] font-semibold outline-none" />
      <button type="button" onPointerDown={() => down(1)} onPointerUp={stop} onPointerLeave={stop} onPointerCancel={stop} onClick={() => click(1)} aria-label="Meer" className={btn}><Plus className="size-4" /></button>
    </div>
  )
}
