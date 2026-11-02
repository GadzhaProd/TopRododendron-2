// Forms of the old site, rebuilt: retail contact form (home), wholesale offerte
// form and the "ontvang de prijslijst" dialog (groothandel). Errors are bound
// to their fields (aria-invalid, aria-describedby) and focus goes to the first
// invalid field; the mockup does not send anything and says so.
import { useEffect, useId, useRef, useState, type FormEvent } from 'react'
import { AnimatePresence, motion, useReducedMotion } from 'framer-motion'
import { Check, X } from 'lucide-react'
import { cn, lockPage, trapTab, rememberFocus } from '@/lib/utils'
import { Button } from './button'
import { Field, Input, Select, Textarea, describe } from './fields'
import { varieties, monthsLong, b2b, company } from '@/data/content'
import { modal, closeModal } from '@/lib/store'

type Status = 'idle' | 'pending' | 'success'
type Errors = Record<string, string>
const emailOk = (s: string) => /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(s)

function focusFirst(form: HTMLFormElement, errs: Errors) {
  const first = Object.keys(errs)[0]
  if (first) (form.elements.namedItem(first) as HTMLElement | null)?.focus()
}
function Demo({ dark }: { dark?: boolean }) { return <p className={cn('text-[12px]', dark ? 'text-white/70' : 'text-muted')}>Demo: dit formulier verstuurt in de mockup nog niets.</p> }
function Summary({ errors, dark }: { errors: Errors; dark?: boolean }) {
  const n = Object.keys(errors).length
  if (!n) return null
  return <p role="alert" className={cn('rounded-field px-4 py-3 text-[14px] font-medium', dark ? 'bg-white/10 text-white' : 'bg-flower/10 text-ink')}>Controleer {n === 1 ? 'het gemarkeerde veld' : `de ${n} gemarkeerde velden`}.</p>
}

/* ---------------- Retail contact form ---------------- */
export function ContactForm({ className }: { className?: string }) {
  const id = useId()
  const [status, setStatus] = useState<Status>('idle')
  const [errors, setErrors] = useState<Errors>({})
  function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault()
    const f = e.currentTarget, d = new FormData(f), errs: Errors = {}
    if (String(d.get('naam') ?? '').trim().length < 2) errs.naam = 'Vul uw naam in.'
    if (!emailOk(String(d.get('email') ?? ''))) errs.email = 'Vul een geldig e-mailadres in.'
    if (String(d.get('bericht') ?? '').trim().length < 10) errs.bericht = 'Schrijf een bericht van minimaal 10 tekens.'
    setErrors(errs)
    if (Object.keys(errs).length) { focusFirst(f, errs); return }
    setStatus('pending'); setTimeout(() => { f.reset(); setStatus('success') }, 800)
  }
  if (status === 'success') {
    return (
      <div className={cn('flex flex-col items-start gap-3 rounded-panel bg-surface p-6', className)} role="status">
        <span className="grid size-10 place-items-center rounded-full bg-night text-white"><Check className="size-5" strokeWidth={2.5} /></span>
        <p className="text-[22px] font-semibold">Bedankt voor uw bericht!</p>
        <p className="text-[15px] text-ink-2">Wij nemen binnen 1 werkdag contact met u op.</p>
      </div>
    )
  }
  const n = (k: string) => `${id}-${k}`
  return (
    <form onSubmit={onSubmit} noValidate className={cn('flex flex-col gap-5', className)} aria-describedby={`${id}-req`}>
      <div className="grid grid-cols-1 gap-5 sm:grid-cols-2">
        <Field label="Naam" htmlFor={n('naam')} required error={errors.naam}><Input id={n('naam')} name="naam" autoComplete="name" placeholder="Uw naam" required invalid={!!errors.naam} aria-describedby={describe(n('naam'), errors.naam)} /></Field>
        <Field label="Telefoonnummer" htmlFor={n('tel')}><Input id={n('tel')} name="tel" type="tel" autoComplete="tel" placeholder="06 12 34 56 78" /></Field>
      </div>
      <Field label="E-mailadres" htmlFor={n('email')} required error={errors.email}><Input id={n('email')} name="email" type="email" autoComplete="email" placeholder="uw@email.nl" required invalid={!!errors.email} aria-describedby={describe(n('email'), errors.email)} /></Field>
      <Field label="Bericht" htmlFor={n('bericht')} required error={errors.bericht}><Textarea id={n('bericht')} name="bericht" rows={4} placeholder="Waar kunnen wij u mee helpen?" required invalid={!!errors.bericht} aria-describedby={describe(n('bericht'), errors.bericht)} /></Field>
      <Summary errors={errors} />
      <div className="flex flex-wrap items-center gap-4">
        <Button as="button" type="submit" variant="solid" size="lg" arrow className="w-full sm:w-auto">{status === 'pending' ? 'Versturen…' : 'Verstuur bericht'}</Button>
        <p id={`${id}-req`} className="text-[13px] text-muted">Velden met * zijn verplicht.</p>
      </div>
      <p className="text-[12.5px] text-muted">Door dit formulier te verzenden gaat u akkoord met ons <a href={company.privacy} target="_blank" rel="noopener noreferrer" className="underline underline-offset-4">privacybeleid</a>.</p>
      <Demo />
    </form>
  )
}

/* ---------------- Wholesale offerte form ---------------- */
export function OfferteForm({ className }: { className?: string }) {
  const id = useId()
  const [status, setStatus] = useState<Status>('idle')
  const [errors, setErrors] = useState<Errors>({})
  const year = new Date().getFullYear()
  const t = true
  function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault()
    const f = e.currentTarget, d = new FormData(f), errs: Errors = {}
    if (String(d.get('bedrijf') ?? '').trim().length < 2) errs.bedrijf = 'Vul uw bedrijfsnaam in.'
    if (String(d.get('naam') ?? '').trim().length < 2) errs.naam = 'Naam moet minimaal 2 tekens bevatten.'
    if (!emailOk(String(d.get('email') ?? ''))) errs.email = 'Vul een geldig e-mailadres in.'
    if (String(d.get('omschrijving') ?? '').trim().length < 10) errs.omschrijving = 'Beschrijf uw project in minimaal 10 tekens.'
    setErrors(errs)
    if (Object.keys(errs).length) { focusFirst(f, errs); return }
    setStatus('pending'); setTimeout(() => { f.reset(); setStatus('success') }, 900)
  }
  if (status === 'success') {
    return (
      <div className={cn('flex flex-col items-start gap-3', className)} role="status">
        <span className="grid size-10 place-items-center rounded-full bg-white text-moss"><Check className="size-5" strokeWidth={2.5} /></span>
        <p className="text-[24px] font-semibold text-white">Bedankt voor uw aanvraag!</p>
        <p className="text-[15px] text-white/80">Wij nemen binnen 24 uur contact met u op met een projectofferte op maat.</p>
      </div>
    )
  }
  const n = (k: string) => `${id}-${k}`
  return (
    <form onSubmit={onSubmit} noValidate className={cn('flex flex-col gap-5', className)} aria-describedby={`${id}-req`}>
      <div className="grid grid-cols-1 gap-5 sm:grid-cols-2">
        <Field dark label="Bedrijfsnaam" htmlFor={n('bedrijf')} required error={errors.bedrijf}><Input dark id={n('bedrijf')} name="bedrijf" autoComplete="organization" placeholder="Uw bedrijf" required invalid={!!errors.bedrijf} aria-describedby={describe(n('bedrijf'), errors.bedrijf)} /></Field>
        <Field dark label="KVK-nummer" htmlFor={n('kvk')}><Input dark id={n('kvk')} name="kvk" inputMode="numeric" placeholder="bijv. 12345678" /></Field>
        <Field dark label="Contactpersoon" htmlFor={n('naam')} required error={errors.naam}><Input dark id={n('naam')} name="naam" autoComplete="name" placeholder="Uw naam" required invalid={!!errors.naam} aria-describedby={describe(n('naam'), errors.naam)} /></Field>
        <Field dark label="Telefoonnummer" htmlFor={n('tel')}><Input dark id={n('tel')} name="tel" type="tel" autoComplete="tel" placeholder="06 12 34 56 78" /></Field>
        <Field dark label="E-mailadres" htmlFor={n('email')} required error={errors.email} className="sm:col-span-2"><Input dark id={n('email')} name="email" type="email" autoComplete="email" placeholder="uw@bedrijf.nl" required invalid={!!errors.email} aria-describedby={describe(n('email'), errors.email)} /></Field>
      </div>
      <div className="grid grid-cols-1 gap-5 sm:grid-cols-3">
        <Field dark label="Projecttype" htmlFor={n('projecttype')}>
          <Select dark id={n('projecttype')} name="projecttype" defaultValue=""><option value="">Kies een type</option>{b2b.projectTypes.map((p) => <option key={p}>{p}</option>)}</Select>
        </Field>
        <Field dark label="Soort" htmlFor={n('soort')}>
          <Select dark id={n('soort')} name="soort" defaultValue=""><option value="">Gemengd / nog niet bekend</option>{varieties.map((v) => <option key={v.slug} value={v.slug}>{v.name}</option>)}</Select>
        </Field>
        <Field dark label="Gewenst aantal" htmlFor={n('aantal')} hint="Partijprijzen vanaf 25 stuks; kleinere aantallen in overleg."><Input dark id={n('aantal')} name="aantal" inputMode="numeric" placeholder="bijv. 75 stuks" aria-describedby={describe(n('aantal'), undefined, 'x')} /></Field>
      </div>
      <div className="grid grid-cols-1 gap-5 sm:grid-cols-2">
        <Field dark label="Maat" htmlFor={n('maat')}>
          <Select dark id={n('maat')} name="maat" defaultValue=""><option value="">Alle maten</option>{['40–60 cm', '60–80 cm', '80–100 cm', '100–120 cm', '120 cm +'].map((m) => <option key={m}>{m}</option>)}</Select>
        </Field>
        <div className="flex flex-col gap-2">
          <span className="label text-white/90" id={n('d-l')}>Gewenste leverdatum</span>
          <div className="grid grid-cols-2 gap-3" role="group" aria-labelledby={n('d-l')}>
            <Select dark name="maand" defaultValue="" aria-label="Maand"><option value="">Maand</option>{monthsLong.map((m) => <option key={m}>{m}</option>)}</Select>
            <Select dark name="jaar" defaultValue="" aria-label="Jaar"><option value="">Jaar</option>{[year, year + 1, year + 2].map((y) => <option key={y}>{y}</option>)}</Select>
          </div>
        </div>
      </div>
      <Field dark label="Projectomschrijving" htmlFor={n('omschrijving')} required error={errors.omschrijving}><Textarea dark id={n('omschrijving')} name="omschrijving" rows={5} placeholder="Beschrijf uw project: gewenste soorten, maten, locatie, en eventuele vragen." required invalid={!!errors.omschrijving} aria-describedby={describe(n('omschrijving'), errors.omschrijving)} /></Field>
      <Summary errors={errors} dark={t} />
      <div className="flex flex-wrap items-center gap-4 pt-1">
        <Button as="button" type="submit" variant="white" size="lg" arrow className="w-full sm:w-auto">{status === 'pending' ? 'Versturen…' : 'Projectofferte aanvragen'}</Button>
        <p id={`${id}-req`} className="text-[13px] text-white/75">Velden met * zijn verplicht. Reactie binnen 24 uur, direct van de kweker.</p>
      </div>
      <p className="text-[12.5px] text-white/65">Door dit formulier te verzenden gaat u akkoord met ons <a href={company.privacy} target="_blank" rel="noopener noreferrer" className="underline underline-offset-4">privacybeleid</a>.</p>
      <Demo dark />
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
  const [errors, setErrors] = useState<Errors>({})
  const [email, setEmail] = useState('')

  useEffect(() => {
    if (!open) { setStatus('idle'); setErrors({}); return }
    const restore = rememberFocus()
    lockPage(true)
    setTimeout(() => first.current?.focus(), 30)
    const onKey = (e: KeyboardEvent) => { if (e.key === 'Escape') closeModal(); trapTab(e, panel.current) }
    document.addEventListener('keydown', onKey)
    return () => { document.removeEventListener('keydown', onKey); lockPage(false); restore() }
  }, [open])

  function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault()
    const f = e.currentTarget, d = new FormData(f), errs: Errors = {}
    if (String(d.get('naam') ?? '').trim().length < 2) errs.naam = 'Vul uw naam in.'
    const em = String(d.get('email') ?? '')
    if (!emailOk(em)) errs.email = 'Vul een geldig e-mailadres in.'
    setErrors(errs)
    if (Object.keys(errs).length) { focusFirst(f, errs); return }
    setEmail(em); setStatus('pending'); setTimeout(() => setStatus('success'), 700)
  }
  const n = (k: string) => `${id}-${k}`
  return (
    <AnimatePresence>
      {open && (
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} transition={{ duration: reduce ? 0 : 0.2 }} className="fixed inset-0 z-[80] flex items-end justify-center bg-night/65 p-0 sm:items-center sm:p-6" onClick={(e) => { if (e.target === e.currentTarget) closeModal() }}>
          <motion.div ref={panel} role="dialog" aria-modal="true" aria-labelledby={n('t')} initial={reduce ? false : { y: 30, opacity: 0 }} animate={{ y: 0, opacity: 1 }} exit={reduce ? undefined : { y: 30, opacity: 0 }} transition={{ duration: 0.3, ease: [0.22, 1, 0.36, 1] }} className="relative w-full max-w-md rounded-t-panel bg-bg p-6 text-ink sm:rounded-panel md:p-8">
            <button type="button" onClick={closeModal} aria-label="Sluiten" className="absolute right-4 top-4 grid size-10 place-items-center rounded-full bg-ink/8 hover:bg-ink/15"><X className="size-4" /></button>
            {status === 'success' ? (
              <div className="flex flex-col items-start gap-3" role="status">
                <span className="grid size-10 place-items-center rounded-full bg-night text-white"><Check className="size-5" strokeWidth={2.5} /></span>
                <p className="text-[24px] font-semibold">Aanvraag ontvangen</p>
                <p className="text-[15px] text-ink-2">De prijslijst wordt binnen 24 uur naar <span className="font-semibold text-ink">{email}</span> gestuurd. Heeft u vragen? Bel ons direct: <a href={company.phone1Href} className="num font-semibold underline underline-offset-4">{company.phone1}</a>.</p>
                <Button as="button" variant="outline" size="md" onClick={closeModal} className="mt-2">Sluiten</Button>
              </div>
            ) : (
              <form onSubmit={onSubmit} noValidate className="flex flex-col gap-4">
                <div>
                  <h2 id={n('t')} className="pr-10 text-[26px] font-semibold tracking-[-0.02em] leading-tight">Ontvang de prijslijst</h2>
                  <p className="mt-2 text-[14.5px] text-ink-2">Vul uw gegevens in, de prijslijst wordt direct per e-mail toegestuurd. Geen spam, geen verplichtingen.</p>
                </div>
                <Field label="Naam" htmlFor={n('naam')} required error={errors.naam}><Input ref={first} id={n('naam')} name="naam" autoComplete="name" required invalid={!!errors.naam} aria-describedby={describe(n('naam'), errors.naam)} /></Field>
                <Field label="E-mailadres" htmlFor={n('email')} required error={errors.email}><Input id={n('email')} name="email" type="email" autoComplete="email" required invalid={!!errors.email} aria-describedby={describe(n('email'), errors.email)} /></Field>
                <Field label="Bedrijfsnaam (optioneel)" htmlFor={n('bedrijf')}><Input id={n('bedrijf')} name="bedrijf" autoComplete="organization" /></Field>
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
