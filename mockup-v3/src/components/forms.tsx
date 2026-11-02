// Forms of the old site, rebuilt: retail contact form (home), wholesale offerte
// form and the "ontvang de prijslijst" dialog (groothandel). Two-column layout
// idea from 21st.dev "Contact Form" (kevingirelli, 35258). Validation and errors
// in Dutch; the mockup does not send anything and says so.
import { useEffect, useId, useRef, useState, type FormEvent } from 'react'
import { AnimatePresence, motion, useReducedMotion } from 'framer-motion'
import { Check, X } from 'lucide-react'
import { cn, lockPage, trapTab } from '@/lib/utils'
import { Button } from './button'
import { Field, Input, Select, Textarea } from './fields'
import { varieties, monthsLong, b2b, company } from '@/data/content'
import { modal, closeModal } from '@/lib/store'

type Status = 'idle' | 'pending' | 'success' | 'error'
const emailOk = (s: string) => /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(s)

function Errors({ errors, dark }: { errors: string[]; dark?: boolean }) {
  if (!errors.length) return null
  return <ul role="alert" className={cn('flex flex-col gap-1 border-l-2 pl-4 text-[14px]', dark ? 'border-white text-white' : 'border-bloom text-ink')}>{errors.map((e) => <li key={e}>{e}</li>)}</ul>
}
function Demo({ dark }: { dark?: boolean }) { return <p className={cn('text-[12px]', dark ? 'text-white/70' : 'text-muted')}>Demo: dit formulier verstuurt in de mockup nog niets.</p> }

/* ---------------- Retail contact form ---------------- */
export function ContactForm({ className }: { className?: string }) {
  const id = useId()
  const [status, setStatus] = useState<Status>('idle')
  const [errors, setErrors] = useState<string[]>([])
  function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault()
    const f = e.currentTarget, d = new FormData(f), errs: string[] = []
    if (String(d.get('naam') ?? '').trim().length < 2) errs.push('Vul uw naam in.')
    if (!emailOk(String(d.get('email') ?? ''))) errs.push('Vul een geldig e-mailadres in.')
    if (String(d.get('bericht') ?? '').trim().length < 10) errs.push('Schrijf een bericht van minimaal 10 tekens.')
    setErrors(errs)
    if (errs.length) { setStatus('error'); return }
    setStatus('pending'); setTimeout(() => { f.reset(); setStatus('success') }, 800)
  }
  if (status === 'success') {
    return (
      <div className={cn('flex flex-col items-start gap-3 rounded-img border border-line bg-surface p-6', className)} role="status">
        <span className="grid size-10 place-items-center rounded-full bg-moss text-white"><Check className="size-5" strokeWidth={2.5} /></span>
        <p className="font-display text-[24px]">Bedankt voor uw bericht.</p>
        <p className="text-[15px] text-ink-2">Wij nemen binnen 1 werkdag contact met u op.</p>
      </div>
    )
  }
  return (
    <form onSubmit={onSubmit} noValidate className={cn('flex flex-col gap-5', className)} aria-describedby={`${id}-req`}>
      <div className="grid grid-cols-1 gap-5 sm:grid-cols-2">
        <Field label="Naam" htmlFor={`${id}-n`} required><Input id={`${id}-n`} name="naam" autoComplete="name" placeholder="Uw naam" required /></Field>
        <Field label="Telefoonnummer" htmlFor={`${id}-t`}><Input id={`${id}-t`} name="tel" type="tel" autoComplete="tel" placeholder="06 12 34 56 78" /></Field>
      </div>
      <Field label="E-mailadres" htmlFor={`${id}-e`} required><Input id={`${id}-e`} name="email" type="email" autoComplete="email" placeholder="uw@email.nl" required /></Field>
      <Field label="Bericht" htmlFor={`${id}-b`} required><Textarea id={`${id}-b`} name="bericht" rows={4} placeholder="Waar kunnen wij u mee helpen? Soort, maat, standplaats, aantal…" required /></Field>
      <Errors errors={errors} />
      <div className="flex flex-wrap items-center gap-4">
        <Button as="button" type="submit" variant="solid" size="lg" arrow className="w-full sm:w-auto">{status === 'pending' ? 'Versturen…' : 'Verstuur bericht'}</Button>
        <p id={`${id}-req`} className="text-[13px] text-muted">Velden met * zijn verplicht. Reactie binnen 1 werkdag.</p>
      </div>
      <p className="text-[12.5px] text-muted">Door dit formulier te verzenden gaat u akkoord met ons <a href={company.privacy} className="underline underline-offset-4">privacybeleid</a>.</p>
      <Demo />
    </form>
  )
}

/* ---------------- Wholesale offerte form ---------------- */
export function OfferteForm({ className, dark = true }: { className?: string; dark?: boolean }) {
  const id = useId()
  const [status, setStatus] = useState<Status>('idle')
  const [errors, setErrors] = useState<string[]>([])
  const year = new Date().getFullYear()
  function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault()
    const f = e.currentTarget, d = new FormData(f), errs: string[] = []
    if (String(d.get('bedrijf') ?? '').trim().length < 2) errs.push('Vul uw bedrijfsnaam in.')
    if (String(d.get('naam') ?? '').trim().length < 2) errs.push('Vul de naam van de contactpersoon in.')
    if (!emailOk(String(d.get('email') ?? ''))) errs.push('Vul een geldig e-mailadres in.')
    if (String(d.get('omschrijving') ?? '').trim().length < 10) errs.push('Beschrijf uw project in minimaal 10 tekens.')
    setErrors(errs)
    if (errs.length) { setStatus('error'); return }
    setStatus('pending'); setTimeout(() => { f.reset(); setStatus('success') }, 900)
  }
  if (status === 'success') {
    return (
      <div className={cn('flex flex-col items-start gap-3', className)} role="status">
        <span className="grid size-10 place-items-center rounded-full bg-white text-moss"><Check className="size-5" strokeWidth={2.5} /></span>
        <p className="font-display text-[26px] text-white">Bedankt voor uw aanvraag.</p>
        <p className="text-[15px] text-white/80">Wij nemen binnen 24 uur contact met u op met een projectofferte op maat.</p>
      </div>
    )
  }
  const t = dark
  return (
    <form onSubmit={onSubmit} noValidate className={cn('flex flex-col gap-5', className)} aria-describedby={`${id}-req`}>
      <div className="grid grid-cols-1 gap-5 sm:grid-cols-2">
        <Field dark={t} label="Bedrijfsnaam" htmlFor={`${id}-b`} required><Input dark={t} id={`${id}-b`} name="bedrijf" autoComplete="organization" placeholder="Uw bedrijf" required /></Field>
        <Field dark={t} label="KVK-nummer" htmlFor={`${id}-k`}><Input dark={t} id={`${id}-k`} name="kvk" inputMode="numeric" placeholder="bijv. 12345678" /></Field>
        <Field dark={t} label="Contactpersoon" htmlFor={`${id}-n`} required><Input dark={t} id={`${id}-n`} name="naam" autoComplete="name" placeholder="Uw naam" required /></Field>
        <Field dark={t} label="Telefoonnummer" htmlFor={`${id}-t`}><Input dark={t} id={`${id}-t`} name="tel" type="tel" autoComplete="tel" placeholder="06 12 34 56 78" /></Field>
        <Field dark={t} label="E-mailadres" htmlFor={`${id}-e`} required className="sm:col-span-2"><Input dark={t} id={`${id}-e`} name="email" type="email" autoComplete="email" placeholder="uw@bedrijf.nl" required /></Field>
      </div>
      <div className="grid grid-cols-1 gap-5 sm:grid-cols-3">
        <Field dark={t} label="Projecttype" htmlFor={`${id}-p`}>
          <Select dark={t} id={`${id}-p`} name="projecttype" defaultValue=""><option value="">Kies een type</option>{b2b.projectTypes.map((p) => <option key={p}>{p}</option>)}</Select>
        </Field>
        <Field dark={t} label="Soort" htmlFor={`${id}-s`}>
          <Select dark={t} id={`${id}-s`} name="soort" defaultValue=""><option value="">Gemengd / nog niet bekend</option>{varieties.map((v) => <option key={v.slug} value={v.slug}>{v.name}</option>)}</Select>
        </Field>
        <Field dark={t} label="Gewenst aantal" htmlFor={`${id}-a`} hint="Partijprijzen vanaf 25 stuks; kleinere aantallen in overleg."><Input dark={t} id={`${id}-a`} name="aantal" inputMode="numeric" placeholder="bijv. 75 stuks" aria-describedby={`${id}-a-hint`} /></Field>
      </div>
      <div className="grid grid-cols-1 gap-5 sm:grid-cols-2">
        <Field dark={t} label="Maat" htmlFor={`${id}-m`}>
          <Select dark={t} id={`${id}-m`} name="maat" defaultValue=""><option value="">Alle maten</option>{['40–60 cm', '60–80 cm', '80–100 cm', '100–120 cm', '120 cm +'].map((m) => <option key={m}>{m}</option>)}</Select>
        </Field>
        <div className="flex flex-col gap-2">
          <span className="text-[13px] font-medium text-white/85" id={`${id}-d-l`}>Gewenste leverdatum</span>
          <div className="grid grid-cols-2 gap-3" role="group" aria-labelledby={`${id}-d-l`}>
            <Select dark={t} name="maand" defaultValue="" aria-label="Maand"><option value="">Maand</option>{monthsLong.map((m) => <option key={m}>{m}</option>)}</Select>
            <Select dark={t} name="jaar" defaultValue="" aria-label="Jaar"><option value="">Jaar</option>{[year, year + 1, year + 2].map((y) => <option key={y}>{y}</option>)}</Select>
          </div>
        </div>
      </div>
      <Field dark={t} label="Projectomschrijving" htmlFor={`${id}-o`} required><Textarea dark={t} id={`${id}-o`} name="omschrijving" rows={5} placeholder="Beschrijf uw project: gewenste soorten, maten, locatie, planning en eventuele vragen." required /></Field>
      <Errors errors={errors} dark={t} />
      <div className="flex flex-wrap items-center gap-4 pt-1">
        <Button as="button" type="submit" variant="paper" size="lg" arrow className="w-full sm:w-auto">{status === 'pending' ? 'Versturen…' : 'Projectofferte aanvragen'}</Button>
        <p id={`${id}-req`} className="text-[13px] text-white/75">Velden met * zijn verplicht. Reactie binnen 24 uur, direct van de kweker.</p>
      </div>
      <p className="text-[12.5px] text-white/60">Door dit formulier te verzenden gaat u akkoord met ons <a href={company.privacy} className="underline underline-offset-4">privacybeleid</a>.</p>
      <Demo dark={t} />
    </form>
  )
}

/* ---------------- Prijslijst dialog ---------------- */
export function PrijslijstModal() {
  const which = modal.use()
  const open = which === 'prijslijst'
  const reduce = useReducedMotion()
  const panel = useRef<HTMLDivElement>(null)
  const first = useRef<HTMLInputElement>(null)
  const id = useId()
  const [status, setStatus] = useState<Status>('idle')
  const [errors, setErrors] = useState<string[]>([])
  const [email, setEmail] = useState('')

  useEffect(() => {
    lockPage(open)
    if (!open) { setStatus('idle'); setErrors([]); return }
    setTimeout(() => first.current?.focus(), 30)
    const onKey = (e: KeyboardEvent) => { if (e.key === 'Escape') closeModal(); trapTab(e, panel.current) }
    document.addEventListener('keydown', onKey)
    return () => { document.removeEventListener('keydown', onKey); lockPage(false) }
  }, [open])

  function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault()
    const d = new FormData(e.currentTarget), errs: string[] = []
    if (String(d.get('naam') ?? '').trim().length < 2) errs.push('Vul uw naam in.')
    const em = String(d.get('email') ?? '')
    if (!emailOk(em)) errs.push('Vul een geldig e-mailadres in.')
    setErrors(errs)
    if (errs.length) return
    setEmail(em); setStatus('pending'); setTimeout(() => setStatus('success'), 700)
  }

  return (
    <AnimatePresence>
      {open && (
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} transition={{ duration: reduce ? 0 : 0.2 }} className="fixed inset-0 z-[80] flex items-end justify-center bg-ink/55 p-0 sm:items-center sm:p-6" onClick={(e) => { if (e.target === e.currentTarget) closeModal() }}>
          <motion.div ref={panel} role="dialog" aria-modal="true" aria-labelledby={`${id}-t`} initial={reduce ? false : { y: 30, opacity: 0 }} animate={{ y: 0, opacity: 1 }} exit={reduce ? undefined : { y: 30, opacity: 0 }} transition={{ duration: 0.3, ease: [0.22, 1, 0.36, 1] }} className="relative w-full max-w-md rounded-t-img bg-paper p-6 text-ink sm:rounded-img md:p-8">
            <button type="button" onClick={closeModal} aria-label="Sluiten" className="absolute right-4 top-4 grid size-10 place-items-center rounded-ui border border-ink/25"><X className="size-4" /></button>
            {status === 'success' ? (
              <div className="flex flex-col items-start gap-3" role="status">
                <span className="grid size-10 place-items-center rounded-full bg-moss text-white"><Check className="size-5" strokeWidth={2.5} /></span>
                <p className="font-display text-[26px]">Aanvraag ontvangen.</p>
                <p className="text-[15px] text-ink-2">De prijslijst wordt binnen 24 uur naar <span className="text-ink">{email}</span> gestuurd. Vragen? Bel <a href={company.phone1Href} className="num underline underline-offset-4">{company.phone1}</a>.</p>
                <Button as="button" variant="outline" size="md" onClick={closeModal} className="mt-2">Sluiten</Button>
              </div>
            ) : (
              <form onSubmit={onSubmit} noValidate className="flex flex-col gap-4">
                <div>
                  <p className="eyebrow text-bloom">Groothandel</p>
                  <h2 id={`${id}-t`} className="mt-2 font-display text-[28px] leading-tight">Ontvang de prijslijst</h2>
                  <p className="mt-2 text-[14.5px] text-ink-2">Vul uw gegevens in; de prijslijst wordt per e-mail toegestuurd. Geen verplichtingen.</p>
                </div>
                <Field label="Naam" htmlFor={`${id}-n`} required><Input ref={first} id={`${id}-n`} name="naam" autoComplete="name" required /></Field>
                <Field label="E-mailadres" htmlFor={`${id}-e`} required><Input id={`${id}-e`} name="email" type="email" autoComplete="email" required /></Field>
                <Field label="Bedrijfsnaam" htmlFor={`${id}-b`}><Input id={`${id}-b`} name="bedrijf" autoComplete="organization" /></Field>
                <Errors errors={errors} />
                <Button as="button" type="submit" variant="solid" size="lg" className="w-full">{status === 'pending' ? 'Versturen…' : 'Prijslijst ontvangen'}</Button>
                <p className="text-center text-[12.5px] text-muted">Uw gegevens worden niet gedeeld met derden.</p>
                <Demo />
              </form>
            )}
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  )
}
