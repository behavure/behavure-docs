---
title: Worker Installation
description: macOS Worker Installation
slug: install/macos/worker
sidebar:
  label: Worker Installation
  order: 20
---

This section assumes that you have downloaded the Edge IQ binary, and that the Server is [configured](../server) and running.

:::note
For the current deployment scenario, the Server and external Workers **do not** share a single host.
Should you require the above, additional security precautions need to be taken. Contact support to learn more.
:::

Set up a new Worker as follows:

1. Create a Worker ID and API key on the Server
2. Create a data directory
3. Configure environment variables
4. Start the Worker

:::note
The evaluation license allows 1 external Worker.
:::

## Generate an API key

A Worker ID and API key are required for the Worker before it can connect to the Server. This can be done either via the web-based UI or the CLI.

### Via web-based UI

Log in to the Server. Go to **Workers** in the top navigation, then select **NEW WORKER**.

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

Adding a Worker via the CLI is a two-step process, much like the method above that uses the web-based UI.

:::note
The CLI is a wrapper to the Server HTTP API.
By default, the CLI assumes a Server is listening on `http://localhost:3000`.
A `EDGEIQ_URL` environment variable instructs the CLI where to locate the Server HTTP API.
:::

If you changed the default bind address of the Server, set `EDGEIQ_URL`, for example:

```
export EDGEIQ_URL="http://localhost:4000"
```

Log in to the Server:

```
edgeiq login admin
```

:::note
On your first interaction with the CLI, you'll be prompted to accept the [EULA](/edge_iq/legal/eula/). Press `Enter` to scroll through the EULA and follow the prompts.
:::

After providing the password, you will see `Login successful`. Then add the new Worker:

```
edgeiq workers add worker1 --id worker1
```

Lastly, create an associated API key:

```
edgeiq api-key issue worker1
```

```
API-KEY(worker1;api_read;default) F4177-AM9PZIEW7MPI7IL28ERE
```

:::note
Copy the key value (`F4177-AM9PZIEW7MPI7IL28ERE`) for later use. Remember that key is just an example!
:::

## Create a Data Directory

A Worker requires a data directory to store Job definitions and some state information.

Create a directory for EdgeIQ worker data:

```
mkdir -p ~/Library/Application\ Support/EdgeIQ/worker
```

## Configure Environment Variables

The Worker can be configured through environment variables. Create a shell script to set these variables:

```
cat > ~/edgeiq-worker.env << EOF
EDGEIQ_WORKER_ID=worker1
EDGEIQ_WORKER_API_KEY=F4177-AM9PZIEW7MPI7IL28ERE
EDGEIQ_JOBS_DIR=~/Library/Application\ Support/EdgeIQ/worker
EDGEIQ_URL=http://<server>:3000
EDGEIQ_LICENSE_EULA_ACCEPT=yes
EOF
```

:::tip
See `edgeiq run worker --help` for startup options and their environment variable equivalents.
:::

At a minimum, the Worker needs to know:

- A unique Worker ID (`EDGEIQ_WORKER_ID`)
- An API key to authenticate against a Server (`EDGEIQ_WORKER_API_KEY`)
- The Server URL (`EDGEIQ_URL`)
- A data directory to store Job definitions and other state data (`EDGEIQ_JOBS_DIR`)

Additional configuration options are optional, but three should be mentioned here:

- `EDGEIQ_WORKER_POLL_INTERVAL` determines how often the Worker will poll the Server to check for updates. Default: `15` seconds.
- `EDGEIQ_WORKER_LISTENER` determines which address and port the Worker will listen on for _internal_ updates. Default: `127.0.0.1:4040`.
- `EDGEIQ_LICENSE_EULA_ACCEPT=yes` prevents the one-time prompt for accepting the [End User License Agreement](/eula).

:::note
It's possible to co-locate one or more workers on the same host with the Server. When the Server is started with the built-in Worker (`edgeiq run server`), the built-in Worker will bind to port `4040` on the host. This means that co-located Workers on the same host must be configured to listen on different ports.
:::

Change the `EDGEIQ_WORKER_API_KEY` to match the key you previously created.

Change the `EDGEIQ_URL` to the Server address or hostname (confirm that your DNS is configured).

:::note
The value of `EDGEIQ_WORKER_ID` should match the Worker ID previously configured on the Server.
:::

## Start the Worker

To start the worker with the environment variables:

```
source ~/edgeiq-worker.env
edgeiq run worker
```

The Worker will connect to the Server and begin processing Jobs.

For more details, visit the full [EdgeIQ Documentation](https://docs.behavure.ai/).
