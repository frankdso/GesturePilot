import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

export default defineConfig({
  plugins: [react()],
  root: '.',
  base: './', // <-- THIS is CRITICAL for production!
  build: {
    outDir: 'dist',
  },
  server: {
    port: 5173
  }
});
