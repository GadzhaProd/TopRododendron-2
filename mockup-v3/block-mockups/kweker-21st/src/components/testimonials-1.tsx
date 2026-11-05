// 21st.dev "Centered Testimonial" (id 18914, efferd/testimonials-1). Original markup
// kept; changes: props instead of the Vercel copy, our logo mark instead of the
// Vercel icon, larger avatar (it is the founder, not a customer).
import type { ReactNode } from 'react'
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar'
export function TestimonialsSection({ logo, brand, quote, name, role, avatar }: { logo: ReactNode; brand: string; quote: ReactNode; name: string; role: string; avatar: string }) {
  return (
    <figure className="mx-auto flex w-full max-w-2xl flex-col items-center justify-center">
      <div className="mb-8 flex items-center gap-2">{logo}<span className="text-lg font-medium">{brand}</span></div>
      <blockquote className="text-center text-2xl leading-tight tracking-tight sm:text-3xl md:text-4xl">{quote}</blockquote>
      <div className="mx-auto my-6 h-px w-full max-w-sm bg-border [mask-image:linear-gradient(to_right,transparent,black,transparent)]" />
      <figcaption className="flex flex-col items-center gap-5">
        <div className="space-y-0.5 text-center">
          <cite className="text-xl font-medium text-foreground not-italic">{name}</cite>
          <div className="text-lg text-muted-foreground">{role}</div>
        </div>
        <Avatar className="size-24 rounded-full border object-cover"><AvatarImage alt={`${name}`} src={avatar} className="object-[50%_20%]" /><AvatarFallback>GT</AvatarFallback></Avatar>
      </figcaption>
    </figure>
  )
}
