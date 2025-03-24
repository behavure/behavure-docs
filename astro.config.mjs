// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { starlightComponents } from './src/plugins/starlight-components';

// https://astro.build/config
export default defineConfig({
  integrations: [
    starlight({
      title: 'Docs',
      logo: {
        src: './src/assets/behavure-logo.svg',
      },
      social: {
        github: 'https://github.com/behavure/behavure-docs',
      },
      customCss: [
        './src/styles/custom.css',
      ],
      sidebar: [
        {
          label: 'Getting Started',
          items: [
            { label: 'Introduction', link: '/introduction' },
          ],
        },
        {
          label: 'Measure IQ',
          collapsed: true,
          items: [
            {
              label: 'Overview',
              link: '/measure_iq'
            },
            {
              label: 'Key Concepts',
              collapsed: true,
              items: [
                { label: 'Overview', link: '/measure_iq/key-concepts-and-terminology' },
                { label: 'Event Data', link: '/measure_iq/key-concepts-and-terminology/what-is-event-data' },
                { label: 'Actor Properties', link: '/measure_iq/key-concepts-and-terminology/actor-properties' },
                { label: 'Data Sampling', link: '/measure_iq/key-concepts-and-terminology/how-does-scuba-perform-data-sampling' },
                {
                  label: 'Data Pipeline',
                  collapsed: true,
                  autogenerate: {
                    directory: 'measure_iq/key-concepts-and-terminology/data-pipeline',
                    collapsed: true,
                  },
                },
              ],
            },
            {
              label: 'Measure Guides',
              collapsed: true,
              items: [
                { label: 'Overview', link: '/measure_iq/measure-guides' },
                { label: 'String Resolution & Hash Collisions', link: '/measure_iq/measure-guides/string-resolution-and-hash-collisions' },
              ],
            },
            {
              label: 'SCUBA User Guides',
              collapsed: true,
              items: [
                { label: 'Overview', link: '/measure_iq/scuba-user-guides' },
                {
                  label: 'Learn About SCUBA Concepts',
                  collapsed: true,
                  autogenerate: {
                    directory: 'measure_iq/scuba-user-guides/learn-about-scuba-concepts',
                    collapsed: true,
                  },
                },
                {
                  label: 'Build Queries and Visualizations',
                  collapsed: true,
                  autogenerate: {
                    directory: 'measure_iq/scuba-user-guides/build-queries-and-visualizations',
                    collapsed: true,
                  },
                },
                {
                  label: 'Analyze User Paths with Flows',
                  collapsed: true,
                  autogenerate: {
                    directory: 'measure_iq/scuba-user-guides/analyze-user-paths-with-flows',
                    collapsed: true,
                  },
                },
                {
                  label: 'Enrich Your Data with Properties',
                  collapsed: true,
                  autogenerate: {
                    directory: 'measure_iq/scuba-user-guides/enrich-your-data-with-properties',
                    collapsed: true,
                  },
                },
                {
                  label: 'Manage Your Created Objects',
                  collapsed: true,
                  autogenerate: {
                    directory: 'measure_iq/scuba-user-guides/manage-your-created-objects',
                    collapsed: true,
                  },
                },
                {
                  label: 'Streamline Analysis with Additional Explorations',
                  collapsed: true,
                  autogenerate: {
                    directory: 'measure_iq/scuba-user-guides/streamline-analysis-with-additional-explorations',
                    collapsed: true,
                  },
                },
                {
                  label: 'API: Programmatically Querying SCUBA',
                  collapsed: true,
                  autogenerate: {
                    directory: 'measure_iq/scuba-user-guides/api-programmatically-querying-scuba',
                    collapsed: true,
                  },
                },
              ],
            },
            {
              label: 'SCUBA Tutorials',
              collapsed: true,
              autogenerate: {
                directory: 'measure_iq/scuba-tutorials',
                collapsed: true,
              },
            },
            {
              label: 'Admin Guides',
              collapsed: true,
              autogenerate: {
                directory: 'measure_iq/admin-guides',
                collapsed: true,
              },
            },
            {
              label: 'Glossary',
              collapsed: true,
              autogenerate: {
                directory: 'measure_iq/glossary',
                collapsed: true,
              },
            }
          ]
        },
        {
          label: 'Edge IQ',
          collapsed: true,
          autogenerate: { 
            directory: 'edge_iq', 
            collapsed: true 
          },
        },
      ],
      plugins: [starlightComponents],
      
      // Custom settings
      pagefind: true, // Enable search
      defaultLocale: 'root',
      editLink: {
        baseUrl: 'https://github.com/behavure/behavure-docs/edit/main/',
      },
      lastUpdated: true,
      
      // Theme configuration is now handled through component overrides
      // See src/components/ThemeProvider.astro and src/components/ThemeSelect.astro
      // To re-enable light mode, delete these component override files and remove the
      // components configuration below
      components: {
        // Override the theme components to force dark mode
        ThemeProvider: './src/components/ThemeProvider.astro',
        ThemeSelect: './src/components/ThemeSelect.astro',
      },
    }),
  ],
});