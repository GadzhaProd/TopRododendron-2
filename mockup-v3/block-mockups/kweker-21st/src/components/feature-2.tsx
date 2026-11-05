// 21st.dev "Feature 2" by shadcnblocks (id 2219). Original markup kept; changes:
// our copy and photo, links without target=_blank (internal/tel), optional extra content.
import type { ReactNode } from 'react'
import { Button } from '@/components/ui/button'
interface Feature2Props { title: string; description?: string; imageSrc: string; imageAlt: string; buttonPrimary: { label: string; href: string }; buttonSecondary: { label: string; href: string }; children?: ReactNode }
export const Feature2 = ({ title, description, imageSrc, imageAlt, buttonPrimary, buttonSecondary, children }: Feature2Props) => {
  return (
    <section className="py-24">
      <div className="container">
        <div className="grid items-center gap-8 md:gap-16 lg:grid-cols-2">
          <img src={imageSrc} alt={imageAlt} className="max-h-96 w-full rounded-md object-cover lg:max-h-[30rem] lg:rounded-xl" />
          <div className="flex flex-col items-center text-center lg:items-start lg:text-left">
            <h1 className="my-6 mt-0 text-4xl font-semibold tracking-tight text-balance lg:text-5xl">{title}</h1>
            <p className="mb-8 max-w-xl text-muted-foreground lg:text-lg">{description}</p>
            {children}
            <div className="flex w-full flex-col justify-center gap-2 sm:flex-row lg:justify-start">
              <Button asChild><a href={buttonPrimary.href}>{buttonPrimary.label}</a></Button>
              <Button variant="outline" asChild><a href={buttonSecondary.href} target="_blank" rel="noopener">{buttonSecondary.label}</a></Button>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
