// Comparison of the varieties (old /plantgids table, pattern of 21st.dev
// "Sortable Table" 22166 without TanStack). From md up: a sortable table with
// thumbnails, sticky name column and a scroll cue above it. On phones: one
// card per variety with all eight values and a sort <select>.
import { useMemo, useState } from 'react'
import { ChevronDown, ChevronUp, ChevronsUpDown } from 'lucide-react'
import { cn } from '@/lib/utils'
import { Swatch } from './section-head'
import { Select } from './fields'
import { varieties, popularOrder, img, type Variety } from '@/data/content'

type Key = 'popular' | 'name' | 'color' | 'bloei' | 'hoogte' | 'breedte' | 'groei' | 'standplaats' | 'zone'
const cols: { key: Key; label: string }[] = [
  { key: 'name', label: 'Variëteit' }, { key: 'color', label: 'Kleur' }, { key: 'bloei', label: 'Bloei' },
  { key: 'hoogte', label: 'Hoogte' }, { key: 'breedte', label: 'Breedte' }, { key: 'groei', label: 'Groei per jaar' },
  { key: 'standplaats', label: 'Standplaats' }, { key: 'zone', label: 'Winterhard' },
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
const cellsOf = (v: Variety): [string, string][] => [['Bloei', v.bloei], ['Hoogte', v.hoogte], ['Breedte', v.breedte], ['Groei per jaar', v.groeiCm.replace(' per jaar', '')], ['Standplaats', v.standplaats], ['Winterhard', `Ja, zone ${v.zone}`]]

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
    <div className={className}>
      {/* phones: cards + sort select */}
      <div className="md:hidden">
        <label className="flex items-center gap-3 text-[14px] text-ink-2"><span className="shrink-0 font-medium">Sorteer op</span>
          <Select value={`${key}:${dir}`} onChange={(e) => { const [k, d] = e.target.value.split(':'); setKey(k as Key); setDir(d as 'asc' | 'desc') }} className="h-10 text-[14px]" aria-label="Sorteren">
            <option value="popular:asc">Populair</option><option value="name:asc">Naam A–Z</option><option value="bloei:asc">Vroegste bloei</option><option value="hoogte:asc">Hoogte, laag–hoog</option><option value="hoogte:desc">Hoogte, hoog–laag</option><option value="groei:asc">Groei, langzaam–snel</option><option value="zone:asc">Winterhard, zone</option>
          </Select>
        </label>
        <ul className="mt-4 flex flex-col gap-3">
          {rows.map((v) => (
            <li key={v.slug} className="rounded-img bg-surface p-4">
              <a href={`product.html#${v.slug}`} className="flex items-center gap-3">
                <img src={img(`${v.slug}-sm`)} alt="" className="size-14 shrink-0 rounded-[10px] object-cover" loading="lazy" />
                <span className="min-w-0"><span className="block text-[17px] font-semibold leading-tight">{v.name}</span><span className="mt-1 flex items-center gap-2 text-[13px] text-muted"><Swatch hex={v.hex} light={v.light} />{v.color}</span></span>
              </a>
              <dl className="mt-3 grid grid-cols-2 gap-x-4 gap-y-2 border-t border-line pt-3 text-[13.5px]">
                {cellsOf(v).map(([k, x]) => <div key={k} className={k === 'Standplaats' ? 'col-span-2' : ''}><dt className="text-muted">{k}</dt><dd className="num font-medium text-ink">{x}</dd></div>)}
              </dl>
            </li>
          ))}
        </ul>
      </div>

      {/* ≥ md: table */}
      <div className="hidden md:block">
        <p className="mb-2 text-[12.5px] text-muted lg:hidden" aria-hidden="true">← schuif voor meer kolommen →</p>
        <div className="overflow-x-auto rounded-img bg-surface">
          <table className="w-full min-w-[900px] border-collapse text-left text-[14.5px]">
            <thead>
              <tr className="border-b border-line">
                {cols.map((c) => {
                  const active = c.key === key
                  const Icon = active ? (dir === 'asc' ? ChevronUp : ChevronDown) : ChevronsUpDown
                  return (
                    <th key={c.key} scope="col" aria-sort={active ? (dir === 'asc' ? 'ascending' : 'descending') : 'none'} className={cn('p-0 align-bottom', c.key === 'name' && 'sticky left-0 z-10 bg-surface')}>
                      <button type="button" onClick={() => sort(c.key)} className={cn('flex min-h-12 w-full items-center gap-1.5 px-4 py-2 text-[13px] font-semibold transition-colors hover:text-ink', active ? 'text-ink' : 'text-muted')}>
                        {c.label}<Icon aria-hidden="true" className={cn('size-3.5', active ? 'text-flower' : 'text-muted/60')} />
                      </button>
                    </th>
                  )
                })}
              </tr>
            </thead>
            <tbody>
              {rows.map((v) => (
                <tr key={v.slug} className="group border-b border-line last:border-b-0 transition-colors hover:bg-bg/60">
                  <td className="sticky left-0 z-10 bg-surface px-4 py-2.5 group-hover:bg-[#edefe9]"><a href={`product.html#${v.slug}`} className="flex items-center gap-3 font-semibold underline-offset-4 hover:underline"><img src={img(`${v.slug}-sm`)} alt="" className="size-11 shrink-0 rounded-[8px] object-cover" loading="lazy" /><span className="whitespace-nowrap">{v.name}</span></a></td>
                  <td className="whitespace-nowrap px-4 py-2.5"><span className="inline-flex items-center gap-2"><Swatch hex={v.hex} light={v.light} />{v.color}</span></td>
                  <td className="whitespace-nowrap px-4 py-2.5">{v.bloei}</td>
                  <td className="num whitespace-nowrap px-4 py-2.5">{v.hoogte}</td>
                  <td className="num whitespace-nowrap px-4 py-2.5">{v.breedte}</td>
                  <td className="num whitespace-nowrap px-4 py-2.5">{v.groeiCm.replace(' per jaar', '')}</td>
                  <td className="px-4 py-2.5">{v.standplaats}</td>
                  <td className="num whitespace-nowrap px-4 py-2.5">Ja, zone {v.zone}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  )
}
