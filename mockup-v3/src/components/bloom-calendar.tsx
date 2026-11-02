// Bloei- & plantkalender. A Gantt-style month grid (idea from 21st.dev "Gantt
// Chart" 38523, rebuilt as plain CSS grid): one row per variety, bloom months as
// a thin bar in the real bloom colour of that variety, ideal planting months as a
// hatched bar, the current month marked. On phones each variety becomes a
// stacked block with its own 12-month strip, so nothing needs horizontal scroll.
// The comparison table on the plantgids is the table twin of this chart.
import { cn } from '@/lib/utils'
import { months, monthsLong, plantMonths, type Variety } from '@/data/content'

const today = new Date().getMonth() + 1

function rowLabel(v: Variety, showPlant: boolean) {
  const bloom = v.bloomMonths.map((m) => monthsLong[m - 1]).join(' en ')
  const plant = plantMonths.map((m) => monthsLong[m - 1]).join(', ')
  return `${v.name}: bloeit in ${bloom}${showPlant ? `; ideaal plantmoment ${plant}` : ''}.`
}

function Cell({ v, m, showPlant, tall = false }: { v: Variety; m: number; showPlant: boolean; tall?: boolean }) {
  const isBloom = v.bloomMonths.includes(m)
  const first = isBloom && !v.bloomMonths.includes(m - 1)
  const last = isBloom && !v.bloomMonths.includes(m + 1)
  const isPlant = showPlant && plantMonths.includes(m)
  const pFirst = isPlant && !plantMonths.includes(m - 1)
  const pLast = isPlant && !plantMonths.includes(m + 1)
  const h = tall ? 'h-3' : 'h-2.5'
  return (
    <div className={cn('relative flex items-center', tall ? 'h-12' : 'h-9', m === today && 'bg-moss/[0.07]')} aria-hidden="true">
      {isBloom ? (
        <div className={cn(h, 'w-full', first && 'ml-[2px] rounded-l-[3px]', last && 'mr-[2px] rounded-r-[3px]')} style={{ background: v.hex, boxShadow: v.light ? 'inset 0 0 0 1.5px rgba(27,31,27,.45)' : undefined }} />
      ) : isPlant ? (
        <div className={cn(h, 'hatch w-full', pFirst && 'ml-[2px] rounded-l-[3px]', pLast && 'mr-[2px] rounded-r-[3px]')} />
      ) : (
        <span className="mx-auto block size-[3px] rounded-full bg-ink/25" />
      )}
    </div>
  )
}

export function BloomCalendar({ rows, showPlant = true, className, compact = false }: { rows: Variety[]; showPlant?: boolean; className?: string; compact?: boolean }) {
  return (
    <div className={cn('w-full', className)}>
      {/* ≥ md: one grid */}
      <div className={cn('hidden md:block', compact && 'md:hidden')}>
        <div className="grid grid-cols-[minmax(190px,250px)_repeat(12,minmax(0,1fr))] border-b border-line pb-2">
          <div className="eyebrow self-end pb-1 text-muted">Soort</div>
          {months.map((mo, i) => {
            const m = i + 1
            return (
              <div key={mo} className={cn('relative flex flex-col items-center justify-end', m === today && 'bg-moss/[0.07] rounded-t-[3px]')}>
                {m === today && <span className="eyebrow mb-1 rounded-[2px] bg-moss px-1.5 py-0.5 text-[9.5px] text-white">Vandaag</span>}
                <span className={cn('num text-[12.5px] uppercase tracking-[0.08em]', m === today ? 'font-semibold text-moss' : 'text-muted')}>{mo}</span>
              </div>
            )
          })}
        </div>
        {rows.map((v) => (
          <div key={v.slug} role="img" aria-label={rowLabel(v, showPlant)} className="grid grid-cols-[minmax(190px,250px)_repeat(12,minmax(0,1fr))] border-b border-line last:border-b-0">
            <div className="flex items-center gap-2.5 py-1 pr-3">
              <span className="size-2.5 shrink-0 rounded-full" style={{ background: v.hex, boxShadow: v.light ? 'inset 0 0 0 1px rgba(27,31,27,.3)' : undefined }} />
              <span className="min-w-0"><span className="block font-display text-[17px] leading-tight">{v.name}</span><span className="block text-[12px] text-muted">{v.color}</span></span>
            </div>
            {months.map((_, i) => <Cell key={i} v={v} m={i + 1} showPlant={showPlant} tall />)}
          </div>
        ))}
      </div>

      {/* phones (and compact mode): stacked strips */}
      <div className={cn('md:hidden', compact && 'md:block')}>
        <div className="grid grid-cols-12 border-b border-line pb-1.5">
          {months.map((mo, i) => (
            <span key={mo} className={cn('num text-center text-[11px] uppercase', i + 1 === today ? 'font-semibold text-moss' : 'text-muted')}>{mo[0]}</span>
          ))}
        </div>
        {rows.map((v) => (
          <div key={v.slug} role="img" aria-label={rowLabel(v, showPlant)} className="border-b border-line py-2.5 last:border-b-0">
            {!compact && (
              <div className="mb-1 flex items-baseline justify-between gap-3">
                <span className="flex min-w-0 items-center gap-2"><span className="size-2 shrink-0 rounded-full" style={{ background: v.hex, boxShadow: v.light ? 'inset 0 0 0 1px rgba(27,31,27,.3)' : undefined }} /><span className="truncate font-display text-[17px]">{v.name}</span></span>
                <span className="shrink-0 text-[12.5px] text-muted">{v.bloei}</span>
              </div>
            )}
            <div className="grid grid-cols-12">{months.map((_, i) => <Cell key={i} v={v} m={i + 1} showPlant={showPlant} />)}</div>
          </div>
        ))}
      </div>
    </div>
  )
}

export function BloomLegend({ showPlant = true, className }: { showPlant?: boolean; className?: string }) {
  return (
    <ul className={cn('flex flex-wrap items-center gap-x-7 gap-y-2 text-[13px] text-ink-2', className)}>
      <li className="flex items-center gap-2.5"><span className="h-2.5 w-7 rounded-[3px]" style={{ background: 'linear-gradient(90deg,#b9293d,#d9679a,#9a6cc4)' }} />Bloeiperiode, in de bloemkleur van de soort</li>
      {showPlant && <li className="flex items-center gap-2.5"><span className="hatch h-2.5 w-7 rounded-[3px]" />Ideaal plantmoment</li>}
      <li className="flex items-center gap-2.5"><span className="h-5 w-7 rounded-[3px] bg-moss/[0.1]" />Huidige maand</li>
    </ul>
  )
}
