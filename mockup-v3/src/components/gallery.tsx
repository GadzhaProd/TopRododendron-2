// Product gallery: main photo, keyboard-navigable thumbnail strip, lightbox
// (pattern from 21st.dev "Thumbnail image viewer" 37501). The lightbox is
// portaled to document.body so the inert <main> never swallows its buttons;
// focus returns to the "Foto vergroten" button on close.
import { useCallback, useEffect, useRef, useState } from 'react'
import { createPortal } from 'react-dom'
import { AnimatePresence, motion, useReducedMotion } from 'framer-motion'
import { ChevronLeft, ChevronRight, X, Maximize2 } from 'lucide-react'
import { cn, lockPage, trapTab } from '@/lib/utils'
import { img, srcset } from '@/data/content'

export type Photo = { name: string; alt: string }

export function Gallery({ photos, className }: { photos: Photo[]; className?: string }) {
  const [active, setActive] = useState(0)
  const [open, setOpen] = useState(false)
  const reduce = useReducedMotion()
  const panel = useRef<HTMLDivElement>(null)
  const closeRef = useRef<HTMLButtonElement>(null)
  const openerRef = useRef<HTMLButtonElement>(null)
  const n = photos.length
  const prev = useCallback(() => setActive((i) => (i - 1 + n) % n), [n])
  const next = useCallback(() => setActive((i) => (i + 1) % n), [n])
  const key = photos.map((p) => p.name).join()
  useEffect(() => { setActive(0) }, [key])
  useEffect(() => {
    lockPage(open)
    if (!open) return
    setTimeout(() => closeRef.current?.focus(), 20)
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') setOpen(false)
      else if (e.key === 'ArrowLeft') prev()
      else if (e.key === 'ArrowRight') next()
      trapTab(e, panel.current)
    }
    document.addEventListener('keydown', onKey)
    return () => { document.removeEventListener('keydown', onKey); lockPage(false); setTimeout(() => openerRef.current?.focus(), 0) }
  }, [open, prev, next])
  const cur = photos[active]
  const nav = 'absolute top-1/2 grid size-11 -translate-y-1/2 place-items-center rounded-full bg-white/90 text-ink shadow-sm hover:bg-white'
  return (
    <div className={className}>
      <div className="relative overflow-hidden rounded-panel bg-bg-2">
        <button ref={openerRef} type="button" onClick={() => setOpen(true)} aria-label="Foto vergroten" className="group/g block aspect-[4/3] w-full cursor-zoom-in sm:aspect-[4/5] lg:aspect-[4/5]">
          <img key={cur.name} src={img(cur.name)} srcSet={srcset(cur.name)} sizes="(min-width: 1024px) 56vw, 100vw" alt={cur.alt} className="h-full w-full object-cover img-treat" />
          <span className="absolute bottom-3 right-3 grid size-10 place-items-center rounded-full bg-white/90 text-ink opacity-90 transition-opacity group-hover/g:opacity-100"><Maximize2 className="size-4" aria-hidden="true" /></span>
        </button>
        {n > 1 && (
          <>
            <button type="button" onClick={prev} aria-label="Vorige foto" className={cn(nav, 'left-3')}><ChevronLeft className="size-5" /></button>
            <button type="button" onClick={next} aria-label="Volgende foto" className={cn(nav, 'right-3')}><ChevronRight className="size-5" /></button>
          </>
        )}
      </div>
      {n > 1 && (
        <div className="mt-3 flex gap-2.5" role="tablist" aria-label="Foto's">
          {photos.map((p, i) => (
            <button key={p.name} type="button" role="tab" aria-selected={i === active} aria-label={`Foto ${i + 1}: ${p.alt}`} onClick={() => setActive(i)} onKeyDown={(e) => { if (e.key === 'ArrowRight') next(); if (e.key === 'ArrowLeft') prev() }} className={cn('aspect-square w-[64px] overflow-hidden rounded-[10px] transition-opacity', i === active ? 'ring-2 ring-ink ring-offset-2 ring-offset-bg' : 'opacity-65 hover:opacity-100')}>
              <img src={img(`${p.name}-sm`) ?? img(p.name)} alt="" className="h-full w-full object-cover" />
            </button>
          ))}
        </div>
      )}
      {typeof document !== 'undefined' && createPortal(
        <AnimatePresence>
          {open && (
            <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} transition={{ duration: reduce ? 0 : 0.2 }} className="fixed inset-0 z-[90] flex items-center justify-center bg-night/96 p-3 on-dark sm:p-6" onClick={(e) => { if (e.target === e.currentTarget) setOpen(false) }}>
              <div ref={panel} role="dialog" aria-modal="true" aria-label={cur.alt} className="relative flex h-full w-full items-center justify-center">
                <img src={img(cur.name)} srcSet={srcset(cur.name)} sizes="100vw" alt={cur.alt} className="max-h-full max-w-full rounded-img object-contain" />
                <button ref={closeRef} type="button" onClick={() => setOpen(false)} aria-label="Sluiten" className="absolute right-0 top-0 grid size-12 place-items-center rounded-full bg-white/12 text-white hover:bg-white/25"><X className="size-5" /></button>
                {n > 1 && (
                  <>
                    <button type="button" onClick={prev} aria-label="Vorige foto" className="absolute left-0 top-1/2 grid size-12 -translate-y-1/2 place-items-center rounded-full bg-white/12 text-white hover:bg-white/25"><ChevronLeft className="size-5" /></button>
                    <button type="button" onClick={next} aria-label="Volgende foto" className="absolute right-0 top-1/2 grid size-12 -translate-y-1/2 place-items-center rounded-full bg-white/12 text-white hover:bg-white/25"><ChevronRight className="size-5" /></button>
                  </>
                )}
                <p className="num absolute bottom-0 left-1/2 -translate-x-1/2 text-[13px] text-white/80">{active + 1} / {n}</p>
              </div>
            </motion.div>
          )}
        </AnimatePresence>,
        document.body,
      )}
    </div>
  )
}
