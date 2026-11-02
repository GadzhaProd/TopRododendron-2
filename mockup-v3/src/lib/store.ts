// Tiny page-level stores (no dependencies). The demo cart is kept in
// localStorage so the count survives navigation between the five pages; every
// read/write is guarded because storage can be unavailable (private mode, viewer).
import { useSyncExternalStore } from 'react'

type Listener = () => void
function createStore<T>(initial: T) {
  let state = initial
  const subs = new Set<Listener>()
  return {
    get: () => state,
    set: (next: T) => { state = next; subs.forEach((l) => l()) },
    use: () => useSyncExternalStore((l) => { subs.add(l); return () => { subs.delete(l) } }, () => state, () => state),
  }
}

export type CartLine = { slug: string; name: string; size: string; price: string; qty: number; image?: string }
const KEY = 'tr-cart-v3'
function load(): CartLine[] {
  try { const raw = localStorage.getItem(KEY); return raw ? (JSON.parse(raw) as CartLine[]) : [] } catch { return [] }
}
function save(lines: CartLine[]) { try { localStorage.setItem(KEY, JSON.stringify(lines)) } catch { /* ignore */ } }

export const cartStore = createStore<CartLine[]>(load())
export const cartOpen = createStore<boolean>(false)
export const openCart = () => cartOpen.set(true)
export const closeCart = () => cartOpen.set(false)

function commit(lines: CartLine[]) { cartStore.set(lines); save(lines) }
export const addToCart = (line: CartLine) => {
  const lines = [...cartStore.get()]
  const i = lines.findIndex((l) => l.slug === line.slug && l.size === line.size)
  if (i >= 0) lines[i] = { ...lines[i], qty: lines[i].qty + line.qty }
  else lines.push(line)
  commit(lines)
}
export const setQty = (slug: string, size: string, qty: number) => {
  const lines = cartStore.get().map((l) => (l.slug === slug && l.size === size ? { ...l, qty } : l)).filter((l) => l.qty > 0)
  commit(lines)
}
export const removeLine = (slug: string, size: string) => commit(cartStore.get().filter((l) => !(l.slug === slug && l.size === size)))
export const cartCount = (lines: CartLine[]) => lines.reduce((n, l) => n + l.qty, 0)
export const cartTotal = (lines: CartLine[]) => lines.reduce((n, l) => n + l.qty * parseFloat(l.price.replace(',', '.')), 0)
export const useCart = () => cartStore.use()
export const useCartCount = () => cartCount(cartStore.use())

/** Which product the product page shows: taken from the URL hash. */
export const productSlug = createStore<string>(typeof window !== 'undefined' && window.location.hash ? window.location.hash.slice(1) : 'nova-zembla')
if (typeof window !== 'undefined') {
  window.addEventListener('hashchange', () => { productSlug.set(window.location.hash.slice(1) || 'nova-zembla'); window.scrollTo({ top: 0 }) })
}

/** Modal dialogs (prijslijst). */
export const modal = createStore<string | null>(null)
export const openModal = (id: string) => modal.set(id)
export const closeModal = () => modal.set(null)
