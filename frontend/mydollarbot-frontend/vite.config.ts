import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000', // replace with your backend server URL
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '') // if you want to remove /api prefix
      }
    }
  }
})
