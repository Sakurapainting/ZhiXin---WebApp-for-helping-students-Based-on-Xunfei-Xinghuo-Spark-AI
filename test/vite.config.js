import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import Components from 'unplugin-vue-components/vite'

import Pages from 'vite-plugin-pages'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(), 
    Pages(),
    Components()],
  server: {
    host:'0.0.0.0'
  }
})
