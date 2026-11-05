// Split Content Section (content-06) — 21st.dev id 28310, by felipemenezes098.
// Two-column frame: copy (title + description) left, media right. Kept: the
// section/container, the copy stack, the media wrapper. Changed: Manrope instead
// of serif, our tokens, the motion reveal is off (animation="none" path only),
// Balancer dropped (text-balance CSS instead), an eyebrow and a "reasons" slot
// added under the copy (grid areas in styles.css), CTA removed (no buttons here).
import * as React from 'react'
import { cn } from '@/lib'

export interface Content06Props {
  eyebrow?: React.ReactNode
  title?: React.ReactNode
  description?: React.ReactNode
  /** Another component's header can take the copy slot (variants 2 and 3). */
  copy?: React.ReactNode
  media: React.ReactNode
  reasons?: React.ReactNode
  className?: string
}

export function Content06({ eyebrow, title, description, copy, media, reasons, className }: Readonly<Content06Props>) {
  return (
    <section className={cn('pt-14 sm:pt-20 lg:pt-24', className)}>
      <div className="container">
        <div className="c06-grid">
          <div className="c06-copy order-1 flex w-full min-w-0 flex-col gap-5 self-start">
            {copy ?? (
              <>
                {eyebrow}
                <div className="flex flex-col gap-4">
                  <h2 className="text-balance text-[34px] font-semibold leading-[1.04] tracking-[-0.03em] text-foreground sm:text-[40px] lg:text-[52px]">{title}</h2>
                  <p className="max-w-[48ch] text-pretty text-[16px] leading-[1.6] text-foreground-2 sm:text-[17px] lg:text-[19px]">{description}</p>
                </div>
              </>
            )}
          </div>
          <div className="c06-media relative order-2 flex">{media}</div>
          {reasons && <div className="c06-reasons order-3">{reasons}</div>}
        </div>
      </div>
    </section>
  )
}

export default Content06
