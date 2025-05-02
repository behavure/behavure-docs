---
title: macOS Worker Installation
description: macOS Worker Installation Guide for EdgeIQ
slug: install/macos/worker
sidebar:
  label: Worker Installation
  order: 20
---

This section assumes you have installed EdgeIQ using the [macOS package installer](./10-server#installation-using-package-installer), which places the `edgeiq` binary in `/usr/local/bin` and makes it available in your `PATH`. It also assumes the Server is [configured](./10-server) and running.

:::note
For the current deployment scenario, the Server and external Workers **do not** share a single host.
Should you require the above, additional security precautions need to be taken. Contact support to learn more.
:::

Set up a new Worker as follows:

1.  Generate a Worker ID and API key on the Server
2.  Create a data directory for the Worker
3.  Configure environment variables for the Worker
4.  Start the Worker

:::note
The evaluation license allows 1 Worker instance, used by the built-in worker.
:::

## Generate an API key

A Worker ID and API key are required before the Worker can connect to the Server. This can be done either via the web-based UI or the `edgeiq` CLI.

### Via web-based UI

Log in to the Server UI (usually `http://localhost:3000`). Go to **Workers** in the top navigation, then select **NEW WORKER**.

Create a new Worker with a specified name and ID.

The Worker name is a human-readable designation (a label), while the Worker ID will be used in the Worker configuration.

:::note
A `Worker ID` must be unique, and may contain only `ASCII` letters, numbers, periods (`.`), and hyphens (`-`).
:::

Next, create an API key for the Worker. Go to **Manage > Keys** in the top navigation.

Then create a name for the new API key, select **Add** and copy the key value for later use.

:::note
Key names must be between at least 5 and 50 characters in length and comprised solely of letters, numbers, dashes, and hyphens.
:::

### Via the CLI

Adding a Worker via the CLI is a two-step process, similar to the UI method.

:::note
The CLI is a wrapper for the Server HTTP API.
By default, the CLI assumes a Server is listening on `http://localhost:3000`.
If your server is running elsewhere, set the `EDGEIQ_URL` environment variable to instruct the CLI where to locate the Server HTTP API.
:::

If you changed the default bind address of the Server or it's on a different host, set `EDGEIQ_URL`:

```bash
export EDGEIQ_URL="http://<your-server-ip-or-hostname>:3000"
```

Log in to the Server using the CLI:

```bash
edgeiq login admin
```

:::note
On your first interaction with the CLI, you'll be prompted to accept the [EULA](/edge_iq/legal/eula/). Press `Enter` to scroll through the EULA and follow the prompts.
:::

After providing the admin password, you will see `Login successful`. Then add the new Worker:

```bash
edgeiq workers add worker1 --id worker1
```

Lastly, create an associated API key for the worker:

```bash
edgeiq api-key issue worker1
```

```text
API-KEY(worker1;api_read;default) F4177-AM9PZIEW7MPI7IL28ERE
```

:::note
Copy the generated key value (e.g., `F4177-AM9PZIEW7MPI7IL28ERE`) for later use. Remember that this key is just an example!
:::

## Create a Data Directory

A Worker requires a data directory to store Job definitions and some state information.

Create a directory for EdgeIQ worker data:

```bash
mkdir -p ~/Library/Application\ Support/EdgeIQ/worker
```

## Configure Environment Variables

The Worker is configured through environment variables. Create a shell script to set these variables:

```bash
cat > ~/edgeiq-worker.env << EOF
EDGEIQ_WORKER_ID=worker1
EDGEIQ_WORKER_API_KEY=PASTE_YOUR_API_KEY_HERE
EDGEIQ_JOBS_DIR=~/Library/Application\ Support/EdgeIQ/worker
EDGEIQ_URL=http://<your-server-ip-or-hostname>:3000
EDGEIQ_LICENSE_EULA_ACCEPT=yes
EOF
```

:::tip
See `edgeiq run worker --help` for startup options and their environment variable equivalents.
:::

**Important:**

- Replace `PASTE_YOUR_API_KEY_HERE` with the actual API key you generated.
- Replace `<your-server-ip-or-hostname>` with the correct IP address or hostname where your EdgeIQ Server is accessible.
- Ensure the `EDGEIQ_WORKER_ID` matches the ID you created on the Server.

At a minimum, the Worker needs:

- A unique Worker ID (`EDGEIQ_WORKER_ID`)
- An API key to authenticate against the Server (`EDGEIQ_WORKER_API_KEY`)
- The Server URL (`EDGEIQ_URL`)
- A data directory (`EDGEIQ_JOBS_DIR`)

Optional environment variables include:

- `EDGEIQ_WORKER_POLL_INTERVAL`: How often (in seconds) the Worker checks the Server for updates (default: `15`).
- `EDGEIQ_WORKER_LISTENER`: The address and port the Worker listens on for _internal_ updates (default: `127.0.0.1:4040`).
- `EDGEIQ_LICENSE_EULA_ACCEPT=yes`: Prevents the one-time prompt for accepting the [End User License Agreement](/eula).

:::note
When the Server is started with its built-in Worker (`edgeiq run server`), that worker binds to port `4040` by default. If you co-locate additional Workers on the same host as the Server, each additional Worker must be configured with a unique `EDGEIQ_WORKER_LISTENER` port (e.g., `127.0.0.1:4041`).
:::

## Start the Worker

To start the worker using the configured environment variables:

```bash
source ~/edgeiq-worker.env
edgeiq run worker
```

The Worker will connect to the Server using the provided `EDGEIQ_URL` and API key, and begin processing assigned Jobs.

For more details, visit the full [EdgeIQ Documentation](https://docs.behavure.ai/).
