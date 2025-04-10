# Behavure Documentation

This repository contains the documentation website for Behavure products (Measure IQ and Edge IQ), built using [Astro](https://astro.build).

## Overview

The documentation site is organized into several main sections:
- Introduction
- Measure IQ documentation
- Edge IQ documentation
- Glossary
- Admin guides
- User guides
- Tutorials

The site is built with Astro, a modern static site generator optimized for content-focused websites.

## Prerequisites

> [!TIP]
> If you skip ahead and install [Flox](https://flox.dev), you simply need to activate the environment to get NodeJS and don't need NPM.


Before you begin, ensure you have the following installed:
- [Node.js](https://nodejs.org/) (v16.x or higher recommended)
- [npm](https://www.npmjs.com/) (comes with Node.js)
- [Git](https://git-scm.com/)



## Getting Started with Development

### Setting Up Your Local Environment

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd behavure-docs
   ```

2. Install dependencies (if not using Flox):
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. Open your browser and navigate to `http://localhost:4321` to see the site (or whatever the `npm run dev` output lists - it's right there).

## Working with Astro

[Astro](https://astro.build) is a modern static site generator that allows you to build faster websites with less client-side JavaScript. 

### Key Concepts

- **Content Collections**: Content is stored in the `src/content` directory and organized into collections.
- **Markdown/MDX**: Most content is written in Markdown or MDX (Markdown with JSX) files.
- **Components**: Reusable UI elements are stored in `src/components`.
- **Pages**: Page templates are located in the appropriate directories under `src/pages`.

### Project Structure

```
behavure-docs/
├── src/                      # Source files
│   ├── assets/               # Static assets
│   ├── components/           # Reusable components
│   ├── content/              # Documentation content
│   │   └── docs/             # Main documentation 
│   │       ├── measure_iq/   # Measure IQ documentation
│   │       ├── edge_iq/      # Edge IQ documentation
│   │       └── ...           # Other doc sections
│   ├── styles/               # CSS and styling
│   └── plugins/              # Astro plugins
├── public/                   # Public assets (copied as-is)
├── dist/                     # Build output directory
├── astro.config.mjs          # Astro configuration
└── package.json              # Project dependencies
```

## Updating Documentation

### Adding or Modifying Content

1. Navigate to the appropriate directory in `src/content/docs/`.
2. Create or edit the Markdown (`.md`) or MDX (`.mdx`) files.
3. Images and other attachments should be placed in an `attachments` folder within the same directory.

### File Naming Conventions

- Use kebab-case for filenames (e.g., `getting-started.md`).
- Index files (`index.md`) serve as the main page for a directory.
- Each content page should include frontmatter with at least a title.

Example of a content file:

```markdown
---
title: Getting Started with Measure IQ
description: Learn how to use Measure IQ to analyze your data
---

# Getting Started

Content goes here...
```

### Building for Production

To create a production build:

```bash
npm run build
```

This will generate the static site in the `dist/` directory.

## Using Conventional Commits

This project follows the [Conventional Commits](https://www.conventionalcommits.org/) specification for commit messages. This provides a clear structure for commit messages and makes it easier to generate changelogs and understand the project history.

### Commit Message Format

Each commit message should be structured as follows:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Types

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, etc.)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `build`: Changes that affect the build system or external dependencies
- `ci`: Changes to CI configuration files and scripts
- `chore`: Other changes that don't modify src or test files

### Examples

```
feat(user-guide): add new section on flow properties

fix(glossary): correct definition of actor property

docs: update Measure IQ installation instructions
```

For more details, visit the [Conventional Commits website](https://www.conventionalcommits.org/).

## Using Flox.dev for Development

[Flox](https://flox.dev) is a development environment manager that ensures consistent environments across team members.

### Installing Flox

1. Visit [flox.dev](https://flox.dev) to download and install Flox.

2. Follow the installation instructions on the website.

3. Verify the installation:
   ```bash
   flox --version
   ```

### Using Flox with this Project

1. Navigate to the project directory:
   ```bash
   cd behavure-docs
   ```

2. Activate the Flox environment:
   ```bash
   flox activate
   ```
3. Exit the environment when done:
   ```bash
   exit
   ```

### Benefits of Using Flox

- Ensures consistent development environments across the team
- Isolates project dependencies
- Makes onboarding new developers easier
- Avoids "works on my machine" problems

## Deployment

The site is built into static HTML in the `dist/` directory. When pushed to Github, [Vercel](https://vercel.com/behavure/behavure-docs) will handle publishing the site:

1. Build the project:
   ```bash
   npm run build
   ```

2. Deploy the contents of the `dist/` directory to your hosting service. Vercel handles this automatically for us. 

## Troubleshooting

- If you encounter issues with the build, try clearing the cache:
  ```bash
  npm run clean
  ```

- For dependency issues, try removing node_modules and reinstalling:
  ```bash
  rm -rf node_modules
  npm install
  ```

## Contributing

Please follow these guidelines when contributing to the documentation:

1. Create a new branch for your changes
2. Make your changes in the appropriate files
3. Test your changes locally using `npm run dev`
4. Use conventional commit messages for your commits
5. Submit a pull request for review
6. Once approved & merged, the site will be quickly deployed with changes

