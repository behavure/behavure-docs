// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
  integrations: [
    starlight({
      title: 'Docs',
      logo: {
        src: './src/assets/behavure-logo.svg',
      },
      social: [
        {
          icon: 'github',
          label: 'GitHub',
          href: 'https://github.com/behavure/behavure-docs',
        },
      ],
      customCss: [
        './src/styles/custom.css',
      ],
      sidebar: [
        {
          label: 'Home',
          link: '/'
        },
        {
          label: 'Edge IQ',
          items: [
            {
              label: "Overview",
              link: "edge_iq/",
            },
            {
              label: "Get Started",
              autogenerate: { directory: "edge_iq/start" },
            },
            {
              label: "Install",
              collapsed: true,
              items: [
                { label: "Overview", link: "/edge_iq/install/overview" },
                {
                  label: "macOS",
                  autogenerate: { directory: "edge_iq/install/macOS" }
                },
                {
                  label: "Linux",
                  autogenerate: { directory: "edge_iq/install/Linux" }
                }
              ]
            },
            {
              label: "Jobs",
              autogenerate: { directory: "edge_iq/jobs" },
            },
            {
              label: "Product Integrations",
              collapsed: true,
              autogenerate: { directory: "edge_iq/product_integrations", collapsed: true },
            },
            {
              label: "Guides",
              collapsed: false,
              autogenerate: { directory: "edge_iq/guides", collapsed: true },
            },
            {
              label: "Reference",
              collapsed: true,
              items: [
                {
                  label: "DSL Reference",
                  collapsed: true,
                  items: [
                    {
                      label: "Overview",
                      link: "/edge_iq/reference/dsl"
                    },
                    {
                      label: "Inputs",
                      autogenerate: { directory: "edge_iq/reference/dsl/inputs" }
                    },
                    {
                      label: "Actions",
                      autogenerate: { directory: "edge_iq/reference/dsl/actions" }
                    },
                    {
                      label: "Outputs",
                      autogenerate: { directory: "edge_iq/reference/dsl/outputs" }
                    }
                  ]
                }
              ]
            },
            {
              label: "Legal",
              collapsed: true,
              autogenerate: { directory: "edge_iq/legal", collapsed: true },
            },
          ]
        },
        {
          label: 'Measure IQ',
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
                { label: 'Data Sampling', link: '/measure_iq/key-concepts-and-terminology/how-does-measure-iq-perform-data-sampling' },
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
              label: 'Admin Guide',
              collapsed: true,
              items: [
                { label: 'Overview', link: '/measure_iq/admin-guides' },
                {
                  label: 'Managing Your Data',
                  collapsed: true,
                  autogenerate: {
                    directory: 'measure_iq/admin-guides/managing-your-data',
                    collapsed: true
                  }
                },
                {
                  label: 'Security & Compliance',
                  collapsed: true,
                  autogenerate: {
                    directory: 'measure_iq/admin-guides/security-compliance',
                    collapsed: true
                  }
                },
                {
                  label: 'Set Up Authentication Provider (SSO)',
                  collapsed: true,
                  autogenerate: {
                    directory: 'measure_iq/admin-guides/set-up-an-authentication-provider-sso',
                    collapsed: true
                  }
                },
                {
                  label: 'Configuring Azure for Clusters',
                  collapsed: true,
                  autogenerate: {
                    directory: 'measure_iq/admin-guides/configuring-azure-for-measure-iq-clusters',
                    collapsed: true
                  }
                }
              ]
            },
            {
              label: 'User Guide',
              collapsed: true,
              items: [
                { label: 'Overview', link: '/measure_iq/measure-user-guides' },
                {
                  label: 'Learn About Measure IQ Concepts',
                  collapsed: true,
                  autogenerate: {
                    directory: 'measure_iq/measure-user-guides/learn-about-measure-iq-concepts',
                    collapsed: true
                  }
                },
                {
                  label: 'Build Queries and Visualizations',
                  collapsed: true,
                  autogenerate: {
                    directory: 'measure_iq/measure-user-guides/build-queries-and-visualizations',
                    collapsed: true
                  }
                },
                {
                  label: 'Analyze User Paths with Flows',
                  collapsed: true,
                  autogenerate: {
                    directory: 'measure_iq/measure-user-guides/analyze-user-paths-with-flows',
                    collapsed: true
                  }
                },
                {
                  label: 'Enrich Your Data with Properties',
                  collapsed: true,
                  autogenerate: {
                    directory: 'measure_iq/measure-user-guides/enrich-your-data-with-properties',
                    collapsed: true
                  }
                },
                {
                  label: 'Manage Your Created Objects',
                  collapsed: true,
                  autogenerate: {
                    directory: 'measure_iq/measure-user-guides/manage-your-created-objects',
                    collapsed: true
                  }
                },
                {
                  label: 'Queries',
                  collapsed: true,
                  autogenerate: {
                    directory: 'measure_iq/measure-user-guides/queries',
                    collapsed: true
                  }
                },
                {
                  label: 'Streamline Analysis',
                  collapsed: true,
                  autogenerate: {
                    directory: 'measure_iq/measure-user-guides/streamline-analysis-with-additional-explorations',
                    collapsed: true
                  }
                },
                {
                  label: 'API: Programmatically Querying Measure IQ',
                  collapsed: true,
                  autogenerate: {
                    directory: 'measure_iq/measure-user-guides/api-programmatically-querying-measure-iq',
                    collapsed: true
                  }
                }
              ]
            },
            {
              label: 'Tutorials',
              collapsed: true,
              items: [
                { label: 'Overview', link: '/measure_iq/measure-tutorials' },
                {
                  label: 'Create a Board with Queries & Panels',
                  link: '/measure_iq/measure-tutorials/create-a-board-with-queries-and-panels'
                },
                {
                  label: 'Create an Actor Property',
                  link: '/measure_iq/measure-tutorials/create-an-actor-property'
                },
                {
                  label: 'Create an Event Property',
                  link: '/measure_iq/measure-tutorials/create-an-event-property'
                },
                {
                  label: 'Event Properties vs. Actor Properties',
                  link: '/measure_iq/measure-tutorials/event-properties-vs-actor-properties'
                },
                {
                  label: 'Manage Objects and Queries',
                  collapsed: true,
                  autogenerate: {
                    directory: 'measure_iq/measure-tutorials/manage-objects-and-queries',
                    collapsed: true
                  }
                },
                {
                  label: 'Work with Flows',
                  collapsed: true,
                  autogenerate: {
                    directory: 'measure_iq/measure-tutorials/work-with-flows',
                    collapsed: true
                  }
                },
                {
                  label: 'Work with Queries',
                  collapsed: true,
                  autogenerate: {
                    directory: 'measure_iq/measure-tutorials/work-with-queries',
                    collapsed: true
                  }
                }
              ]
            },
            {
              label: 'Glossary',
              collapsed: true,
              autogenerate: {
                directory: 'measure_iq/glossary',
                collapsed: true
              }
            }
          ]
        }
      ],

      // Custom settings
      pagefind: true, // Enable search
      defaultLocale: 'root',
      editLink: {
        baseUrl: 'https://github.com/behavure/behavure-docs/edit/main/',
      },
      lastUpdated: true,

      // Theme configuration is now handled through component overrides
      components: {
        ThemeProvider: './src/components/ThemeProvider.astro',
        ThemeSelect: './src/components/ThemeSelect.astro',
        Header: './src/components/Header.astro',
      },
    }),
  ],
});
