import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

const backendUrl = process.env.VITE_API_URL ?? 'http://localhost:8000'
const port = parseInt(process.env.FRONTEND_CONTAINER_PORT ?? '5173')

export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',
    port,
    proxy: {
      '/api': {
        target: backendUrl,
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  },
})
