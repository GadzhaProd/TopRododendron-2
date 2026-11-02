// Tiny page-level stores (no dependencies): the product sheet that is open and a
// mock cart counter. Both are mockup-only; nothing is persisted or sent.
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

export const sheetStore = createStore<string | null>(null)
export const openSheet = (slug: string) => sheetStore.set(slug)
export const closeSheet = () => sheetStore.set(null)

export type CartLine = { slug: string; name: string; size: string; price: string; qty: number }
export const cartStore = createStore<CartLine[]>([])
export const addToCart = (line: CartLine) => cartStore.set([...cartStore.get(), line])
export const cartCount = (lines: CartLine[]) => lines.reduce((n, l) => n + l.qty, 0)
