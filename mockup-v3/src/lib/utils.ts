import { clsx, type ClassValue } from 'clsx'
import { twMerge } from 'tailwind-merge'
export function cn(...inputs: ClassValue[]) { return twMerge(clsx(inputs)) }

/** Lock page scroll and make <main> inert while a dialog is open. */
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
