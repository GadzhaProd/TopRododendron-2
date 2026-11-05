// 21st.dev "About 3" by shadcnblocks (id 2202). Original markup kept; changes:
// our copy and photos, the client-logo row is only rendered when logos exist
// (we have none), grid overlay colour uses the site token, main image focus point.
import type { ReactNode } from 'react'
import { Button } from '@/components/ui/button'
type Img = { src: string; alt: string; className?: string }
interface About3Props {
  title: string; description: string; mainImage: Img; secondaryImage: Img
  breakout: { logo: ReactNode; title: ReactNode; description: string; buttonText: string; buttonUrl: string }
  companiesTitle?: string; companies?: { src: string; alt: string }[]
  achievementsTitle: string; achievementsDescription: string; achievements: { label: string; value: string }[]
}
export const About3 = ({ title, description, mainImage, secondaryImage, breakout, companiesTitle, companies = [], achievementsTitle, achievementsDescription, achievements }: About3Props) => {
  return (
    <section className="py-24">
      <div className="container mx-auto">
        <div className="mb-14 grid gap-5 text-center md:grid-cols-2 md:text-left">
          <h1 className="text-4xl font-semibold tracking-tight text-balance md:text-5xl">{title}</h1>
          <p className="text-muted-foreground md:text-lg">{description}</p>
        </div>
        <div className="grid gap-7 lg:grid-cols-3">
          <img src={mainImage.src} alt={mainImage.alt} className={`size-full max-h-[620px] rounded-xl object-cover lg:col-span-2 ${mainImage.className ?? ''}`} />
          <div className="flex flex-col gap-7 md:flex-row lg:flex-col">
            <div className="flex flex-col justify-between gap-6 rounded-xl bg-muted p-7 md:w-1/2 lg:w-auto">
              <div className="mr-auto h-12">{breakout.logo}</div>
              <div>
                <p className="mb-2 text-lg font-semibold">{breakout.title}</p>
                <p className="text-muted-foreground">{breakout.description}</p>
              </div>
              <Button variant="outline" className="mr-auto" asChild><a href={breakout.buttonUrl}>{breakout.buttonText}</a></Button>
            </div>
            <img src={secondaryImage.src} alt={secondaryImage.alt} className={`grow basis-0 rounded-xl object-cover md:w-1/2 lg:min-h-0 lg:w-auto ${secondaryImage.className ?? ''}`} />
          </div>
        </div>
        {companies.length > 0 && (
          <div className="py-32">
            <p className="text-center">{companiesTitle}</p>
            <div className="mt-8 flex flex-wrap justify-center gap-8">{companies.map((c, i) => <img key={c.src + i} src={c.src} alt={c.alt} className="h-6 w-auto md:h-8" />)}</div>
          </div>
        )}
        <div className="relative mt-16 overflow-hidden rounded-xl bg-muted p-10 md:p-16">
          <div className="flex flex-col gap-4 text-center md:text-left">
            <h2 className="text-3xl font-semibold tracking-tight md:text-4xl">{achievementsTitle}</h2>
            <p className="max-w-screen-sm text-muted-foreground">{achievementsDescription}</p>
          </div>
          <div className="mt-10 flex flex-wrap justify-between gap-10 text-center">
            {achievements.map((item, idx) => (
              <div className="flex flex-col gap-4" key={item.label + idx}>
                <p>{item.label}</p>
                <span className="text-4xl font-semibold md:text-5xl">{item.value}</span>
              </div>
            ))}
          </div>
          <div className="pointer-events-none absolute -top-1 right-1 z-10 hidden h-full w-full bg-[linear-gradient(to_right,var(--color-muted-foreground)_1px,transparent_1px),linear-gradient(to_bottom,var(--color-muted-foreground)_1px,transparent_1px)] bg-[size:80px_80px] opacity-15 [mask-image:linear-gradient(to_bottom_right,#000,transparent,transparent)] md:block"></div>
        </div>
      </div>
    </section>
  )
}
