---
title: macOS Server Installation
description: macOS Server Installation Guide for EdgeIQ
slug: install/macos/server
sidebar:
  label: Server Installation
  order: 10
---

## Installation using Package Installer

Installing EdgeIQ on macOS (Apple Silicon and Intel) is straightforward using the provided package installer (`.pkg` file).

1.  **Download the Installer**  
    Visit the [downloads page](https://docs.behavure.ai/start/downloads/) to get the latest macOS installer (`.pkg` file).

2.  **Run the Installer**  
    Double-click the downloaded `.pkg` file and follow the installation prompts. The installer will place the `edgeiq` binary in `/usr/local/bin`.

3.  **Verify Installation**  
    Open Terminal. The installer automatically adds `/usr/local/bin` to your system's `PATH`. You should be able to run the `edgeiq` command directly:

    ```bash
    edgeiq --version
    ```

    If the command is not found, ensure `/usr/local/bin` is included in your `$PATH` environment variable. You might need to restart your terminal session or source your shell profile file (e.g., `~/.zshrc` or `~/.bash_profile`).

    ```bash
    echo $PATH
    # If /usr/local/bin is missing, add it to your shell profile
    # For zsh: echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc
    # For bash: echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bash_profile && source ~/.bash_profile
    ```

4.  **Allow Execution (If Necessary)**  
    Depending on your macOS security settings, you might need to grant permission for the binary to run. If you encounter a security warning, go to **System Settings** → **Privacy & Security** and allow the application.

## Server Configuration and Startup

After installing the `edgeiq` binary, configure and start the server.

### Create a Data Directory

The Server requires a data directory to store Jobs, logs, and metric data.

Create a directory for EdgeIQ data:

```bash
mkdir -p ~/Library/Application\ Support/EdgeIQ
```

### Configure Environment Variables

The Server can be configured through environment variables. Create a shell script to set these variables, ensuring you have write permissions or use `sudo` if necessary:

```bash
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

### Start the Server

To start the server with the environment variables:

```bash
source ~/edgeiq-server.env
edgeiq run server
```

The Server will start and listen on `EDGEIQ_BIND_ADDRESS` (default `127.0.0.1:3000`).

The terminal will display the admin password (either the one you set or a randomly generated one) upon successful startup. Use this to log in as `admin` via your web browser at `http://localhost:3000`.

:::tip
The Server can be configured to use `TLS`, by providing a certificate and key file. See `edgeiq server run --help`.
When using a reverse proxy for TLS termination, like Caddy or Nginx, it's recommended to configure the appropriate `HTTP` client address headers, for logging purposes.
:::

### Resetting the Administrator Password

The `admin` user password may be reset upon relaunching Edge IQ using `edgeiq run server --reset-admin-password`


### More Information
For more details, visit the full [EdgeIQ Documentation](https://docs.behavure.ai/).
