---
title: macOS Server Installation
description: macOS Server Installation
slug: install/macos/server
sidebar:
  label: Server Installation
  order: 10
---

## Quick Start on macOS (Apple Silicon and Intel)

To quickly install and run EdgeIQ on macOS:

1. **Download the Latest Binary**  
   Visit the [downloads page](https://docs.behavure.ai/start/downloads/) or use this direct link for macOS:

   ```
   http://downloads.behavure.ai/latest/edgeiq-aarch64-apple-darwin.tar.xz
   ```

2. **Extract the Binary**  
   Open Terminal and run:

   ```
   tar -xf edgeiq-aarch64-apple-darwin.tar.xz
   ```

3. **Move the Binary to Your PATH**  
   Move the extracted binary to a folder in your `PATH`, such as `/usr/local/bin`:

   ```
   sudo mv edgeiq /usr/local/bin
   ```

4. **Run EdgeIQ**  
   Start the server with:

   ```
   edgeiq run server
   ```

   The server runs on `http://localhost:3000` by default.

5. **Log In**  
   After startup, the terminal will show a randomly generated admin password. Use this to log in as `admin` via the browser.

> **Tip:** You may need to allow the binary to run via System Preferences → Security & Privacy if macOS flags it as unverified.

## Manual Installation

If you prefer to set up the server manually, follow these steps:

1. Create a data directory
2. Configure environment variables
3. Start the Server

By the end of this section, you should be able to access the Server via a browser.

## Create a Data Directory

The Server requires a data directory to store Jobs, logs, and metric data.

Create a directory for EdgeIQ data:

```
mkdir -p ~/Library/Application\ Support/EdgeIQ
```

## Configure Environment Variables

The Server can be configured through environment variables. Create a shell script to set these variables:

```
cat > ~/edgeiq-server.env << EOF
EDGEIQ_STAGING_DIR=~/Library/Application\ Support/EdgeIQ
EDGEIQ_LICENSE_EULA_ACCEPT=yes
EDGEIQ_ADMIN_INIT_PASSWORD=ChangeMeVerySoon
EOF
```

:::tip
See `edgeiq run server --help` for startup options and their environment variable equivalents.
:::

We've added 2 additional environment variables:

- `EDGEIQ_LICENSE_EULA_ACCEPT=yes` prevents the one-time prompt for accepting the [EULA](/eula).
- `EDGEIQ_ADMIN_INIT_PASSWORD` provides an initial `password` for the Server `admin` user.

Upon first initialization of the Server user database, if `EDGEIQ_ADMIN_INIT_PASSWORD` is unset, a random `password` will be generated in the Server `STDOUT` output.

:::note
Whether using `EDGEIQ_ADMIN_INIT_PASSWORD`, or the randomly generated `password` on first run, change the `admin` `password` immediately!
:::

## Start the Server

To start the server with the environment variables:

```
source ~/edgeiq-server.env
edgeiq run server
```

The Server will be listening on `EDGEIQ_BIND_ADDRESS` (default `127.0.0.1:3000`).

:::tip
The Server can be configured to use `TLS`, by providing a certificate and key file. See `edgeiq server run --help`.
When using a reverse proxy for TLS termination, like Caddy or Nginx, it's recommended to configure the appropriate `HTTP` client address headers, for logging purposes.
:::

For more details, visit the full [EdgeIQ Documentation](https://docs.behavure.ai/).
