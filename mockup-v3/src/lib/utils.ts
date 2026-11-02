import { clsx, type ClassValue } from 'clsx'
import { twMerge } from 'tailwind-merge'
import { showToast } from './store'
export function cn(...inputs: ClassValue[]) { return twMerge(clsx(inputs)) }

/** Lock page scroll and make <main> inert while a dialog (portaled to body) is open. */
export function lockPage(lock: boolean) {
  document.body.style.overflow = lock ? 'hidden' : ''
  const main = document.querySelector('main')
  if (lock) main?.setAttribute('inert', '')
  else main?.removeAttribute('inert')
}

export function trapTab(e: KeyboardEvent, root: HTMLElement | null) {
  if (e.key !== 'Tab' || !root) return
  const f = Array.from(root.querySelectorAll<HTMLElement>('a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex="0"]')).filter((el) => el.offsetParent !== null)
  if (!f.length) return
  const first = f[0], last = f[f.length - 1]
  if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus() }
  else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus() }
}

/** Remember the element that opened a dialog and give focus back to it on close. */
export function rememberFocus(): () => void {
  const el = document.activeElement as HTMLElement | null
  return () => { if (el && typeof el.focus === 'function') setTimeout(() => el.focus(), 0) }
}

/**
 * Artifact mode: the claude.ai viewer shows each page on its own and cannot
 * navigate between files. A click on a cross-page link then shows a quiet
 * notice instead of silently failing. Same-page links (#id) always work.
 */
const pageNames: Record<string, string> = { 'index.html': 'Home', 'assortiment.html': 'Assortiment', 'product.html': 'Plant', 'plantgids.html': 'Plantgids', 'groothandel.html': 'Groothandel' }
export function installArtifactLinkGuard() {
  if (typeof window === 'undefined') return
  const standalone = !/\.html?$/i.test(window.location.pathname) && window.location.protocol !== 'file:'
  if (!standalone) return
  document.addEventListener('click', (e) => {
    const a = (e.target as HTMLElement).closest?.('a[href]') as HTMLAnchorElement | null
    if (!a) return
    const href = a.getAttribute('href') || ''
    const m = href.match(/^([a-z]+\.html)(#.*)?$/i)
    if (!m) return
    e.preventDefault()
    showToast(`In de mockup: open de pagina «${pageNames[m[1].toLowerCase()] ?? m[1]}» apart.`)
  })
}
