// 21st.dev "Single Voice Spotlight Testimonial" (id 28169, olewandowski1/testimonials-2).
// Original markup kept 1:1; changes: props instead of the hard-coded Acme copy,
// RiDoubleQuotesR (remixicon) -> lucide Quote, avatar shown in colour.
import { Quote } from 'lucide-react'
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar'
import { Separator } from '@/components/ui/separator'
type T = { quote: string; name: string; role: string; company: string; initials: string; avatar: string }
export default function TestimonialsBlock({ testimonial, metrics }: { testimonial: T; metrics: { value: string; label: string }[] }) {
  return (
    <section className="flex w-full items-center justify-center bg-background px-6 py-24 text-foreground">
      <div className="mx-auto w-full max-w-2xl">
        <div className="relative rounded-xl border border-border bg-card p-10 sm:p-14">
          <div className="absolute top-10 left-0 h-16 w-[3px] bg-primary" aria-hidden="true" />
          <Quote className="mb-8 size-8 text-muted-foreground" aria-hidden="true" />
          <blockquote className="text-xl leading-[1.65] font-medium tracking-tight text-foreground sm:text-2xl">„{testimonial.quote}”</blockquote>
          <Separator className="my-10" />
          <div className="flex flex-col gap-6 sm:flex-row sm:items-center sm:justify-between">
            <div className="flex items-center gap-4">
              <Avatar className="size-14 border border-border"><AvatarImage src={testimonial.avatar} alt={testimonial.name} className="object-[50%_20%]" /><AvatarFallback className="text-sm font-semibold">{testimonial.initials}</AvatarFallback></Avatar>
              <div className="flex flex-col gap-1">
                <span className="text-sm leading-tight font-semibold text-foreground">{testimonial.name}</span>
                <span className="text-xs leading-tight text-muted-foreground">{testimonial.role}, <span className="font-medium text-foreground">{testimonial.company}</span></span>
              </div>
            </div>
            <div className="flex items-center gap-6 sm:gap-8">
              {metrics.map((m, i) => (
                <div key={i} className="flex flex-col items-center gap-0.5 text-center">
                  <span className="text-lg leading-none font-bold tracking-tight text-foreground">{m.value}</span>
                  <span className="text-[11px] leading-tight text-muted-foreground">{m.label}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
