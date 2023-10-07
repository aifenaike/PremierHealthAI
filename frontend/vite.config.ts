import { sveltekit } from '@sveltejs/kit/vite'; // SvelteKit plugin for Vite, used to build Svelte applications with Vite
import { build, defineConfig } from 'vite'; // configuring Vite build process
import UnoCSS from 'unocss/vite' // For optimizing and purging CSS in the project


export default defineConfig({
	plugins: [
		UnoCSS(),
		sveltekit()
	],
	build: {
		sourcemap: true
	}
});
