// Bold Stats (stats-bold) — 21st.dev id 18908, by uilayout.contact.
// Kept: headline metric row (huge number + title + short text, supporting image
// on the right, hairline underneath) followed by a row of key figures with small
// uppercase labels. Changed: tokens and Manrope, the image is a real variety
// photo with our 28px radius, the number is smaller (calm, not a SaaS counter),
// the figures row wraps to 2x2 on phones.
import * as React from 'react'

export type Figure = { value: string; label: string }

export function BoldStats({ big, title, text, image, imageAlt, figures }: { big: string; title: string; text: string; image: string; imageAlt: string; figures: readonly Figure[] }) {
  return (
    <section className="mt-12 flex flex-col justify-center lg:mt-14">
      <div className="container flex w-full flex-col gap-10 sm:gap-12">
        <div className="items-center justify-between gap-8 border-b border-border pb-8 md:flex">
          <div className="flex flex-col items-start gap-3 md:flex-row md:items-baseline md:gap-6">
            <span className="shrink-0 text-[64px] font-semibold leading-none tracking-[-0.04em] text-foreground sm:text-[80px] lg:text-[104px]">{big}</span>
            <div className="max-w-sm">
              <h3 className="text-[19px] font-semibold tracking-[-0.015em] text-foreground">{title}</h3>
              <p className="mt-1 text-pretty text-[15px] leading-[1.5] text-muted-foreground">{text}</p>
            </div>
          </div>
          <img src={image} alt={imageAlt} width={672} height={900} className="mt-6 h-48 w-full shrink-0 rounded-img object-cover object-[50%_60%] sm:w-80 md:mt-0 lg:h-52 lg:w-96" />
        </div>
        <div className="grid grid-cols-2 gap-x-5 gap-y-8 md:flex md:items-center md:justify-between">
          {figures.map((f) => (
            <div key={f.label}>
              <p className="mb-1.5 text-[32px] font-semibold leading-none tracking-[-0.03em] text-foreground sm:text-[40px]">{f.value}</p>
              <p className="text-[11.5px] font-semibold uppercase tracking-[0.12em] text-muted-foreground">{f.label}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}

export default BoldStats
