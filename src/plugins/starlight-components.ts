import type { StarlightPlugin } from '@astrojs/starlight/types';

export const starlightComponents: StarlightPlugin = {
  name: 'custom-components-plugin',
  hooks: {
    setup({ config, updateConfig }) {
      updateConfig({
        components: {
          ...config.components,
          Sidebar: './src/components/Sidebar.astro',
          // Dark mode only components will be added in astro.config.mjs
          // This ensures that they're not added twice
        },
      });
    },
  },
};