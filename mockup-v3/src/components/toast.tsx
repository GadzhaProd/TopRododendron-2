// Quiet notice at the bottom of the screen (used when a cross-page link is
// clicked inside the artifact viewer, where pages cannot navigate to each other).
import { useEffect } from 'react'
import { AnimatePresence, motion } from 'framer-motion'
import { toast } from '@/lib/store'
import { installArtifactLinkGuard } from '@/lib/utils'

export function Toast() {
  const msg = toast.use()
  useEffect(() => { installArtifactLinkGuard() }, [])
  return (
    <AnimatePresence>
      {msg && (
        <motion.p role="status" initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: 12 }} transition={{ duration: 0.2 }} className="fixed bottom-5 left-1/2 z-[95] w-[calc(100%-32px)] max-w-md -translate-x-1/2 rounded-ui bg-night px-4 py-3 text-center text-[14px] font-medium text-white shadow-xl">{msg}</motion.p>
      )}
    </AnimatePresence>
  )
}
