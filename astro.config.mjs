// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

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
					autogenerate: { directory: 'edge_iq' },
				},
				{
					label: 'Measure IQ',
					autogenerate: { directory: 'measure_iq' },
				},
			],
		}),
	],
});
