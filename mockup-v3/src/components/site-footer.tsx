import { Instagram } from 'lucide-react'
import { Logo } from './logo'
import { company } from '@/data/content'

export function SiteFooter() {
  const year = new Date().getFullYear()
  const col = 'flex flex-col gap-2.5 text-[14.5px] text-white/80 [&_a]:transition-colors [&_a:hover]:text-white'
  const h = 'eyebrow mb-4 text-white/60'
  return (
    <footer className="bg-night text-white on-dark">
      <div className="wrap container-x py-14 md:py-20">
        <div className="grid grid-cols-1 gap-12 md:grid-cols-2 lg:grid-cols-[1.4fr_1fr_1fr_1.1fr] lg:gap-10">
          <div>
            <Logo dark size="md" caption />
            <p className="mt-6 max-w-[34ch] text-[14.5px] leading-relaxed text-white/75">{company.description}</p>
            <a href={company.instagram} target="_blank" rel="noopener noreferrer" className="mt-6 inline-flex items-center gap-2 text-[14px] text-white/80 hover:text-white"><Instagram className="size-4" strokeWidth={1.6} aria-hidden="true" />{company.instagramHandle}</a>
          </div>
          <div>
            <p className={h}>Navigatie</p>
            <div className={col}>
              <a href="index.html">Home</a>
              <a href="assortiment.html">Assortiment</a>
              <a href="plantgids.html">Plantgids</a>
              <a href="index.html#kwekerij">De kwekerij</a>
              <a href="groothandel.html">Groothandel</a>
              <a href="index.html#contact">Contact</a>
            </div>
          </div>
          <div>
            <p className={h}>Openingstijden</p>
            <dl className="flex flex-col gap-2 text-[14.5px]">
              {company.hours.map(([d, t]) => (
                <div key={d} className="flex justify-between gap-4 border-b border-white/10 pb-2"><dt className="text-white/70">{d}</dt><dd className={t === 'Gesloten' ? 'text-white/50' : 'num text-white'}>{t}</dd></div>
              ))}
            </dl>
          </div>
          <div>
            <p className={h}>Kwekerij &amp; kantoor</p>
            <div className={col}>
              <a href={company.maps} target="_blank" rel="noopener noreferrer">{company.street}<br />{company.postal}</a>
              <a href={`mailto:${company.email}`}>{company.email}</a>
              <a href={company.phone1Href} className="num">{company.phone1}</a>
              <a href={company.phone2Href} className="num">{company.phone2}</a>
            </div>
          </div>
        </div>
        <div className="mt-14 flex flex-col gap-3 border-t border-white/12 pt-6 text-[13px] text-white/60 sm:flex-row sm:items-center sm:justify-between">
          <p>© {year} {company.name} · KvK {company.kvk} · Otterlo, Veluwe</p>
          <div className="flex gap-6">
            <a href={company.voorwaarden} className="hover:text-white">Algemene voorwaarden</a>
            <a href={company.privacy} className="hover:text-white">Privacybeleid</a>
          </div>
        </div>
      </div>
    </footer>
  )
}
