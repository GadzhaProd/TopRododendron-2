// 21st.dev "Reading Text Reveal" (id 9386, waleedkibhen). The scroll logic is the
// original (eye-level progress, eased rAF, word-by-word reveal). Changes: content
// and section height via props instead of the hard-coded freelancer story, Inter ->
// site font, gray tones -> site tokens, footer removed, optional inline slot.
import { useEffect, useRef, useState, type ReactNode } from 'react'
export function ReadingTextReveal({ segments, minHeight = '170vh', className = '', after }: { segments: string[]; minHeight?: string; className?: string; after?: ReactNode }) {
  const containerRef = useRef<HTMLDivElement>(null)
  const [revealedWordCount, setRevealedWordCount] = useState(0)
  const allWords = segments.flatMap((s) => s.split(' '))
  const totalWords = allWords.length
  useEffect(() => {
    let rafId: number | null = null
    let targetProgress = 0
    let currentProgress = 0
    const smoothScroll = () => {
      const difference = targetProgress - currentProgress
      currentProgress += difference * 0.12
      if (Math.abs(targetProgress - currentProgress) > 0.001) { setRevealedWordCount(Math.floor(currentProgress * totalWords)); rafId = requestAnimationFrame(smoothScroll) }
      else setRevealedWordCount(Math.floor(targetProgress * totalWords))
    }
    const handleScroll = () => {
      if (!containerRef.current) return
      const rect = containerRef.current.getBoundingClientRect()
      const eyeLevel = window.innerHeight * 0.62
      const animationStart = rect.top + window.scrollY - eyeLevel
      const animationEnd = rect.top + window.scrollY + rect.height - eyeLevel
      const progress = (window.scrollY - animationStart) / (animationEnd - animationStart)
      targetProgress = Math.max(0, Math.min(1, progress))
      if (rafId) cancelAnimationFrame(rafId)
      rafId = requestAnimationFrame(smoothScroll)
    }
    window.addEventListener('scroll', handleScroll, { passive: true })
    handleScroll()
    return () => { window.removeEventListener('scroll', handleScroll); if (rafId) cancelAnimationFrame(rafId) }
  }, [totalWords])
  let wordIndex = 0
  return (
    <div ref={containerRef} className={`mx-auto max-w-5xl px-6 md:px-8 ${className}`} style={{ minHeight }}>
      <div className="space-y-10 md:space-y-14">
        {segments.map((segment, si) => {
          const words = segment.split(' ')
          const start = wordIndex
          wordIndex += words.length
          return (
            <p key={si} className="text-[34px] leading-[1.12] font-semibold tracking-[-0.03em] md:text-6xl">
              {words.map((w, i) => {
                const on = start + i < revealedWordCount
                return <span key={i} className={on ? 'text-foreground' : 'text-muted-foreground'} style={{ transition: 'all 0.3s ease-out', opacity: on ? 1 : 0.28 }}>{w}{' '}</span>
              })}
            </p>
          )
        })}
      </div>
      {after}
    </div>
  )
}
