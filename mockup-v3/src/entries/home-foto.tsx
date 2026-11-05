import { createRoot } from 'react-dom/client'
import '@/styles/base.css'
import Page from '@/pages/Home'
createRoot(document.getElementById('root')!).render(<Page heroMedia="photo" />)
