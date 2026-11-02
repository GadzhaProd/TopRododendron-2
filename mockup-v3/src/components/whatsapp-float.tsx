// Floating WhatsApp button for the B2B page. Hidden while the hero, the offerte
// section or the footer is in view (IntersectionObserver), icon-only on phones.
import { useEffect, useState } from 'react'
import { cn } from '@/lib/utils'
import { company } from '@/data/content'

export function WhatsAppIcon({ className }: { className?: string }) {
  return <svg viewBox="0 0 24 24" className={className} fill="currentColor" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91S17.5 2 12.04 2m0 18.15c-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24 4.54 0 8.24 3.7 8.24 8.24.01 4.54-3.69 8.24-8.23 8.24m4.52-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.12-.17.25-.64.81-.78.97-.14.17-.29.19-.54.06-.25-.12-1.05-.39-1.99-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.02-.38.11-.51.11-.11.25-.29.37-.43s.17-.25.25-.41c.08-.17.04-.31-.02-.43s-.56-1.34-.76-1.84c-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.22.25-.86.85-.86 2.07 0 1.22.89 2.4 1.01 2.56.12.17 1.75 2.67 4.23 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.67-1.18.21-.58.21-1.07.14-1.18s-.22-.16-.47-.28" /></svg>
}

export function WhatsAppFloat({ hideNear = ['#hero', '#offerte', 'footer'] }: { hideNear?: string[] }) {
  const [hidden, setHidden] = useState(true)
  useEffect(() => {
    const els = hideNear.map((s) => document.querySelector(s)).filter(Boolean) as Element[]
    const vis = new Map<Element, boolean>()
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => vis.set(e.target, e.isIntersecting))
      setHidden(Array.from(vis.values()).some(Boolean))
    }, { threshold: 0.05 })
    els.forEach((el) => io.observe(el))
    return () => io.disconnect()
  }, [hideNear.join()])
  return (
    <a
      href={company.whatsapp}
      target="_blank"
      rel="noopener noreferrer"
      aria-label={`WhatsApp ${company.whatsappLabel}`}
      aria-hidden={hidden || undefined}
      tabIndex={hidden ? -1 : 0}
      className={cn('fixed bottom-4 right-4 z-40 flex h-12 items-center gap-2.5 rounded-full bg-[#176e3d] text-[14px] font-semibold text-white shadow-[0_10px_30px_-12px_rgba(0,0,0,.6)] transition-all duration-300 md:bottom-6 md:right-6', 'w-12 justify-center md:w-auto md:px-4', hidden ? 'pointer-events-none translate-y-3 opacity-0' : 'opacity-100')}
    >
      <WhatsAppIcon className="size-5" /><span className="hidden md:inline">WhatsApp</span>
    </a>
  )
}
