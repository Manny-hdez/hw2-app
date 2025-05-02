/// <reference types="vitest" />
import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vite.dev/config/
export default defineConfig(({ mode }) => ({
  plugins: [svelte()],
  test: { // vitest config
    globals: true,
    environment: 'jsdom',
    setupFiles: './src/setupTests.js', // You may need to create this setup file
    include: ['src/**/*.{test,spec}.{js,ts,svelte}'],
  },
  server: mode === 'development' ? {
    proxy: {
      '/api': {
        target: 'http://backend:8000',
        changeOrigin: true,
        secure: false,
        configure: (proxy, options) => {
          proxy.on('proxyReq', (proxyReq, req, res) => {
            console.log('Proxying request:', req.url)
          })
        }
      },
    },
  } : undefined,
}))
