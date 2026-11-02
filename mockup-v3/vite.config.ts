import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'
import { fileURLToPath, URL } from 'node:url'
const r = (p: string) => fileURLToPath(new URL(p, import.meta.url))

export default defineConfig({
  base: './',
  plugins: [react(), tailwindcss()],
  resolve: { alias: { '@': r('./src') } },
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    assetsInlineLimit: 0,
    rollupOptions: {
      input: {
        home: r('./index.html'),
        assortiment: r('./assortiment.html'),
        product: r('./product.html'),
        plantgids: r('./plantgids.html'),
        groothandel: r('./groothandel.html'),
      },
    },
  },
})
