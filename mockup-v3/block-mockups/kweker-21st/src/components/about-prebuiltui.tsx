// 21st.dev "About" by prebuiltui (id 6907, "About Section with Image").
// Original structure kept: centered title + subtitle, image beside a heading,
// text and a list of FeatureItems. Changes: our copy and photo, Poppins -> Manrope,
// the PNG icons -> lucide icons, slate/indigo -> site tokens, optional actions.
import type { ReactNode } from 'react'
type Feature = { icon: ReactNode; title: string; desc: string }
export function AboutPrebuiltui({ title, subtitle, image, imageAlt, heading, text, features, actions }: { title: string; subtitle: string; image: string; imageAlt: string; heading: string; text: string; features: Feature[]; actions?: ReactNode }) {
  return (
    <div className="flex flex-col items-center justify-center px-4 py-24 text-center">
      <h1 className="max-w-2xl text-3xl font-semibold tracking-tight md:text-4xl">{title}</h1>
      <p className="mt-3 max-w-lg text-sm text-muted-foreground md:text-base">{subtitle}</p>
      <div className="mt-10 flex max-w-5xl flex-col items-center justify-center gap-10 md:flex-row">
        <img className="w-full max-w-sm rounded-xl" src={image} alt={imageAlt} />
        <div className="max-w-md text-left md:text-left">
          <h2 className="text-2xl font-semibold tracking-tight md:text-3xl">{heading}</h2>
          <p className="mt-2 text-sm text-muted-foreground md:text-base">{text}</p>
          <div className="mt-6 flex flex-col gap-8">
            {features.map((f) => <FeatureItem key={f.title} {...f} />)}
          </div>
          {actions && <div className="mt-8 flex flex-wrap gap-3">{actions}</div>}
        </div>
      </div>
    </div>
  )
}
function FeatureItem({ icon, title, desc }: Feature) {
  return (
    <div className="flex items-start gap-4">
      <div className="flex size-10 shrink-0 items-center justify-center rounded border border-primary/25 bg-accent-soft text-primary">{icon}</div>
      <div>
        <h3 className="text-base font-medium text-foreground">{title}</h3>
        <p className="text-sm text-muted-foreground">{desc}</p>
      </div>
    </div>
  )
}
