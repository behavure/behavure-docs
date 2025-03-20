// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// Helper function to convert kebab-case to Title Case
function toTitleCase(str) {
	return str
	  .split('-')
	  .map(word => word.charAt(0).toUpperCase() + word.slice(1))
	  .join(' ');
  }


// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'Behavure Docs',
			social: {
				github: 'https://github.com/withastro/starlight',
			},
			sidebar: [

				{
					label: 'Edge IQ',
					autogenerate: { directory: 'edge_iq', collapsed: true },
				},
				{
					label: 'Measure IQ',
					autogenerate: { directory: 'measure_iq', collapsed: true },
				},
			],
		}),
	],
});
