// Sortable comparison of the varieties (old /plantgids table, pattern of
// 21st.dev "Sortable Table" 22166 without TanStack). Sticky first column,
// horizontal scroll on narrow screens, aria-sort on the active header.
import { useMemo, useState } from 'react'
import { ChevronDown, ChevronUp, ChevronsUpDown } from 'lucide-react'
import { cn } from '@/lib/utils'
import { Swatch } from './section-head'
import { varieties, popularOrder, type Variety } from '@/data/content'

type Key = 'popular' | 'name' | 'color' | 'bloei' | 'hoogte' | 'breedte' | 'groei' | 'standplaats' | 'zone'
const cols: { key: Key; label: string; num?: boolean }[] = [
  { key: 'name', label: 'Variëteit' }, { key: 'color', label: 'Kleur' }, { key: 'bloei', label: 'Bloei' },
  { key: 'hoogte', label: 'Hoogte', num: true }, { key: 'breedte', label: 'Breedte', num: true }, { key: 'groei', label: 'Groei per jaar', num: true },
  { key: 'standplaats', label: 'Standplaats' }, { key: 'zone', label: 'Winterhard', num: true },
]
function val(v: Variety, k: Key): string | number {
  switch (k) {
    case 'popular': return popularOrder.indexOf(v.slug)
    case 'name': return v.name
    case 'color': return v.color
    case 'bloei': return v.bloeiStart
    case 'hoogte': return v.hoogteNum
    case 'breedte': return v.breedteNum
    case 'groei': return v.groeiMax
    case 'standplaats': return v.standplaats
    case 'zone': return v.zone
  }
}

export function CompareTable({ className }: { className?: string }) {
  const [key, setKey] = useState<Key>('popular')
  const [dir, setDir] = useState<'asc' | 'desc'>('asc')
  const rows = useMemo(() => {
    const c = [...varieties]
    c.sort((a, b) => { const x = val(a, key), y = val(b, key); const r = typeof x === 'number' && typeof y === 'number' ? x - y : String(x).localeCompare(String(y), 'nl'); return dir === 'asc' ? r : -r })
    return c
  }, [key, dir])
  const sort = (k: Key) => { if (k === key) setDir(dir === 'asc' ? 'desc' : 'asc'); else { setKey(k); setDir('asc') } }
  return (
    <div className={cn('-mx-5 overflow-x-auto px-5 md:mx-0 md:px-0', className)}>
      <table className="w-full min-w-[860px] border-collapse text-left text-[14.5px]">
        <thead>
          <tr className="border-b border-line-2">
            {cols.map((c) => {
              const active = c.key === key
              const Icon = active ? (dir === 'asc' ? ChevronUp : ChevronDown) : ChevronsUpDown
              return (
                <th key={c.key} scope="col" aria-sort={active ? (dir === 'asc' ? 'ascending' : 'descending') : 'none'} className={cn('p-0 align-bottom', c.key === 'name' && 'sticky left-0 z-10 bg-paper')}>
                  <button type="button" onClick={() => sort(c.key)} className={cn('flex min-h-11 w-full items-center gap-1.5 py-2 pr-4 text-[12px] font-semibold uppercase tracking-[0.12em] transition-colors hover:text-ink', active ? 'text-ink' : 'text-muted')}>
                    {c.label}<Icon aria-hidden="true" className={cn('size-3.5', active ? 'text-bloom' : 'text-muted/60')} />
                  </button>
                </th>
              )
            })}
          </tr>
        </thead>
        <tbody>
          {rows.map((v) => (
            <tr key={v.slug} className="group border-b border-line transition-colors hover:bg-paper-2/60">
              <td className="sticky left-0 z-10 bg-paper py-3 pr-4 group-hover:bg-[#efece4]"><a href={`product.html#${v.slug}`} className="font-display text-[18px] underline-offset-4 hover:underline">{v.name}</a></td>
              <td className="whitespace-nowrap py-3 pr-4"><span className="inline-flex items-center gap-2"><Swatch hex={v.hex} light={v.light} />{v.color}</span></td>
              <td className="whitespace-nowrap py-3 pr-4">{v.bloei}</td>
              <td className="num whitespace-nowrap py-3 pr-4">{v.hoogte}</td>
              <td className="num whitespace-nowrap py-3 pr-4">{v.breedte}</td>
              <td className="num whitespace-nowrap py-3 pr-4">{v.groeiCm.replace(' per jaar', '')}</td>
              <td className="py-3 pr-4">{v.standplaats}</td>
              <td className="num whitespace-nowrap py-3 pr-4">Ja, zone {v.zone}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <p className="mt-3 text-center text-[12.5px] text-muted md:hidden" aria-hidden="true">← schuif voor meer kolommen →</p>
    </div>
  )
}
