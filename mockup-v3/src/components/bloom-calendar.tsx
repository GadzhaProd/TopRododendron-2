// Bloei- & plantkalender. A Gantt-style month grid (idea from 21st.dev "Gantt
// Chart" 38523, rebuilt as a CSS grid): one row per variety, bloom months as a
// bar in the real bloom colour, ideal planting months hatched, current month
// marked. Styled in concept C's language (tracked uppercase month labels, display
// names, charcoal "Vandaag" pill); `dark` keeps a night variant. On phones every
// variety is a stacked block with its own 12-month strip, so nothing needs
// horizontal scroll. Data: the old site's bloom-section / bloom-timeline.
import { cn } from '@/lib/utils'
import { months, monthsLong, plantMonths, img, type Variety } from '@/data/content'

const today = new Date().getMonth() + 1

function rowLabel(v: Variety, showPlant: boolean) {
  const bloom = v.bloomMonths.map((m) => monthsLong[m - 1]).join(' en ')
  const plant = plantMonths.map((m) => monthsLong[m - 1]).join(', ')
  return `${v.name}: bloeit in ${bloom}${showPlant ? `; ideaal plantmoment ${plant}` : ''}.`
}

function Cell({ v, m, showPlant, tall = false, dark }: { v: Variety; m: number; showPlant: boolean; tall?: boolean; dark: boolean }) {
  const isBloom = v.bloomMonths.includes(m)
  const first = isBloom && !v.bloomMonths.includes(m - 1)
  const last = isBloom && !v.bloomMonths.includes(m + 1)
  const isPlant = showPlant && plantMonths.includes(m)
  const pFirst = isPlant && !plantMonths.includes(m - 1)
  const pLast = isPlant && !plantMonths.includes(m + 1)
  const h = tall ? 'h-3.5' : 'h-3'
  return (
    <div className={cn('relative flex items-center', tall ? 'h-14' : 'h-10', m === today && (dark ? 'bg-white/8' : 'bg-fg/6'))} aria-hidden="true">
      {isBloom ? (
        <div className={cn(h, 'w-full', first && 'ml-[2px] rounded-l-full', last && 'mr-[2px] rounded-r-full')} style={{ background: v.hex, boxShadow: v.light && !dark ? 'inset 0 0 0 1.5px rgba(20,20,19,.35)' : undefined }} />
      ) : isPlant ? (
        <div className={cn(h, 'hatch w-full', pFirst && 'ml-[2px] rounded-l-full', pLast && 'mr-[2px] rounded-r-full')} />
      ) : (
        <span className={cn('mx-auto block size-[3px] rounded-full', dark ? 'bg-white/30' : 'bg-fg/25')} />
      )}
    </div>
  )
}

export function BloomCalendar({ rows, showPlant = true, className, compact = false, dark = false, photos = false }: { rows: Variety[]; showPlant?: boolean; className?: string; compact?: boolean; dark?: boolean; photos?: boolean }) {
  const t = dark ? 'text-white' : 'text-fg'
  const m = dark ? 'text-white/65' : 'text-muted'
  const line = dark ? 'border-white/12' : 'border-fg/10'
  const cols = photos ? 'grid-cols-[minmax(220px,280px)_repeat(12,minmax(0,1fr))]' : 'grid-cols-[minmax(180px,240px)_repeat(12,minmax(0,1fr))]'
  const month = 'text-[11.5px] font-medium uppercase tracking-[0.14em]'
  return (
    <div className={cn('w-full', dark && 'on-dark', className)}>
      {/* ≥ md: one grid */}
      <div className={cn('hidden md:block', compact && 'md:hidden')}>
        <div className={cn('grid border-b pb-2', cols, line)}>
          <div className={cn('eyebrow self-end pb-1', m)}>Soort</div>
          {months.map((mo, i) => {
            const mm = i + 1
            return (
              <div key={mo} className={cn('relative flex flex-col items-center justify-end rounded-t-md', mm === today && (dark ? 'bg-white/8' : 'bg-fg/6'))}>
                {mm === today && <span className={cn('mb-1 rounded-full px-2 py-0.5 text-[10px] font-medium uppercase tracking-[0.12em]', dark ? 'bg-white text-fg' : 'bg-fg text-bg')}>Vandaag</span>}
                <span className={cn('num', month, mm === today ? t : m)}>{mo}</span>
              </div>
            )
          })}
        </div>
        {rows.map((v) => (
          <div key={v.slug} role="img" aria-label={rowLabel(v, showPlant)} className={cn('grid border-b last:border-b-0', cols, line)}>
            <div className="flex items-center gap-3 py-1 pr-3">
              {photos ? <img src={img(`${v.slug}-sm`)} alt="" className="size-10 shrink-0 rounded-[12px] object-cover img-treat" loading="lazy" /> : <span className="size-2.5 shrink-0 rounded-full" style={{ background: v.hex, boxShadow: v.light && !dark ? 'inset 0 0 0 1px rgba(0,0,0,.12)' : undefined }} />}
              <span className="min-w-0"><span className={cn('block font-display text-[17px] leading-tight', t)}>{v.name}</span><span className={cn('block text-[12.5px]', m)}>{v.color}</span></span>
            </div>
            {months.map((_, i) => <Cell key={i} v={v} m={i + 1} showPlant={showPlant} tall dark={dark} />)}
          </div>
        ))}
      </div>

      {/* phones (and compact mode): stacked strips */}
      <div className={cn('md:hidden', compact && 'md:block')}>
        <div className={cn('grid grid-cols-12 border-b pb-1.5', line)}>
          {months.map((mo, i) => (
            <span key={mo} className={cn('num text-center text-[11px] font-medium uppercase', i + 1 === today ? t : m)}>{mo[0]}</span>
          ))}
        </div>
        {rows.map((v) => (
          <div key={v.slug} role="img" aria-label={rowLabel(v, showPlant)} className={cn('border-b py-2.5 last:border-b-0', line)}>
            {!compact && (
              <div className="mb-1 flex items-baseline justify-between gap-3">
                <span className="flex min-w-0 items-center gap-2"><span className="size-2 shrink-0 rounded-full" style={{ background: v.hex, boxShadow: v.light && !dark ? 'inset 0 0 0 1px rgba(0,0,0,.12)' : undefined }} /><span className={cn('truncate font-display text-[16px]', t)}>{v.name}</span></span>
                <span className={cn('shrink-0 text-[12.5px]', m)}>{v.bloei}</span>
              </div>
            )}
            <div className="grid grid-cols-12">{months.map((_, i) => <Cell key={i} v={v} m={i + 1} showPlant={showPlant} dark={dark} />)}</div>
          </div>
        ))}
      </div>
    </div>
  )
}

export function BloomLegend({ showPlant = true, className, dark = false }: { showPlant?: boolean; className?: string; dark?: boolean }) {
  return (
    <ul className={cn('flex flex-wrap items-center gap-x-6 gap-y-2 text-[13px]', dark ? 'on-dark text-white/75' : 'text-fg-2', className)}>
      <li className="flex items-center gap-2.5"><span className="h-3 w-8 rounded-full" style={{ background: 'linear-gradient(90deg,#b9293d,#d9679a,#9a6cc4)' }} />Bloeiperiode, in de bloemkleur van de soort</li>
      {showPlant && <li className="flex items-center gap-2.5"><span className="hatch h-3 w-8 rounded-full" />Ideaal plantmoment</li>}
      <li className="flex items-center gap-2.5"><span className={cn('h-5 w-8 rounded-md', dark ? 'bg-white/10' : 'bg-fg/8')} />Huidige maand</li>
    </ul>
  )
}
