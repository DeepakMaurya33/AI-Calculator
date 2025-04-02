import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

import * as path from "node:path"; // Ensure compatibility with newer Node.js versions

export default defineConfig({
  plugins: [
    react(),
  ],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "src"), // Ensure correct alias resolution
    },
  },
});
