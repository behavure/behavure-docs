---
title: Linux Worker Installation
description: Worker Installation
slug: install/linux/worker
sidebar:
  label: Worker Installation
  order: 20
---

This section assumes that you have downloaded the Edge IO binary, and that the Server is [configured](../server) and running.

:::note
For the current deployment scenario, the Server and external Workers **do not** share a single host.
Should you require the above, additional security precautions need to be taken. For example: separate system accounts for the Server and Worker need to be created. Contact support to learn more.
:::

Set up a new Worker as follows:

1. Create a Worker ID and API key on the Server.

2. Create a data directory.

3. Creat a `systemd` service unit file

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
A `EDGEIQ_URL` environment variable instructs the CLI where to locate the Server HTTP API.
:::

If you changed the default bind address of the Server, set `EDGEIQ_URL`, for example:
If you changed the default bind address of the Server, set `EDGEIQ_URL`, for example:

```sh
export EDGEIQ_URL="http://localhost:4000"
export EDGEIQ_URL="http://localhost:4000"
```

Log in to the Server:

```sh
edgeiq login admin
edgeiq login admin
```

:::note
On your first interaction with the CLI, you'll be prompted to accept the [EULA](/edge_iq/legal/eula/). Press `Enter` to scroll through the EULA and follow the prompts.
:::

After providing the password, you will see `Login successful`. Then add the new Worker:

```sh
edgeiq workers add worker1 --id worker1
edgeiq workers add worker1 --id worker1
```

Lastly, create an associated API key:

```sh
edgeiq api-key issue worker1
edgeiq api-key issue worker1
```

```sh
API-KEY(worker1;api_read;default) F4177-AM9PZIEW7MPI7IL28ERE
```

:::note Remember
Copy the key value (`F4177-AM9PZIEW7MPI7IL28ERE`) for later use.
:::

:::note
The API key name is unrelated to a Worker ID. For simplicity, we're using `worker1` for both.
:::

## Create a system account

Create a system account under which the Worker will run:

```
adduser --system --home /var/lib/edgeiq-worker --disabled-login --group edgeiq
adduser --system --home /var/lib/edgeiq-worker --disabled-login --group edgeiq
```

:::danger
**Do not** run the Worker with `root` privileges. The Worker can execute Jobs with `exec` inputs, which in turn can execute arbitrary commands on the host.
:::

## Create a data directory

A Worker requires a data directory to store Job definitions and some state information.

The `edgeiq` user home directory is `/var/lib/edgeiq-worker` and it will also serve as the data directory.
The `edgeiq` user home directory is `/var/lib/edgeiq-worker` and it will also serve as the data directory.

:::security
Secure environments require `0700` permissions on the data directory!
:::

If a different data directory is required, create it with the appropriate ownership and permissions. For example:

```sh
sudo mkdir /data/edgeiq
sudo mkdir /data/edgeiq
```

```sh
sudo chown edgeiq:edgeiq /data/edgeiq
sudo chown edgeiq:edgeiq /data/edgeiq
```

## Create `systemd` Files

Create a `systemd` service unit file:

```
vi /etc/systemd/system/edgeiq-worker1.service
vi /etc/systemd/system/edgeiq-worker1.service
```

The file must contain the following:

```sh
[Unit]
Description=edgeiq Worker
Description=edgeiq Worker
After=network.target auditd.service

[Service]
EnvironmentFile=/etc/default/edgeiq-worker
User=edgeiq
Group=edgeiq
ExecStart=/usr/sbin/edgeiq run worker
EnvironmentFile=/etc/default/edgeiq-worker
User=edgeiq
Group=edgeiq
ExecStart=/usr/sbin/edgeiq run worker
Restart=on-failure
RestartSec=60

[Install]
WantedBy=multi-user.target
```

Create an environment file for the `EnvironmentFile` setting:

```sh
sudo vi /etc/default/edgeiq-worker
sudo vi /etc/default/edgeiq-worker
```

Here, the Worker is configured through either `edgeiq run worker` options or `environment` variables. In this case, we'll be using the latter.

:::tip
See `edgeiq run worker --help` for startup options and their environment variable equivalents and the reference.
See `edgeiq run worker --help` for startup options and their environment variable equivalents and the reference.
:::

At a minimum, the Worker needs to know:

- A unique Worker ID (`EDGEIQ_WORKER_ID`).
- A unique Worker ID (`EDGEIQ_WORKER_ID`).

- An API key to authenticate against a Server (`EDGEIQ_WORKER_API_KEY`).
- An API key to authenticate against a Server (`EDGEIQ_WORKER_API_KEY`).

- The Server URL (`EDGEIQ_URL`).
- The Server URL (`EDGEIQ_URL`).

- A data directory to store Job definitions and other state data (`EDGEIQ_JOBS_DIR`).
- A data directory to store Job definitions and other state data (`EDGEIQ_JOBS_DIR`).

Additional configuration options are optional, but three should be mentioned here:

- `EDGEIQ_WORKER_POLL_INTERVAL` determines how often the Worker will poll the Server to check for updates. Default: `15` seconds..
- `EDGEIQ_WORKER_POLL_INTERVAL` determines how often the Worker will poll the Server to check for updates. Default: `15` seconds..

- `EDGEIQ_WORKER_LISTENER` determines which address and port the Worker will listen on for _internal_ updates. Default: `127.0.0.1:4040`.

- `EDGEIQ_LICENSE_EULA_ACCEPT=yes` prevents the one-time prompt for accepting the [End User License Agreement](/eula).
- `EDGEIQ_LICENSE_EULA_ACCEPT=yes` prevents the one-time prompt for accepting the [End User License Agreement](/eula).

:::note
It's possible to co-locate one or more workers on the same host with the Server. When the Server is started with the built-in Worker (`edgeiq run server`), the built-in Worker will bind to port `4040` on the host. This means that co-located Workers on the same host must be configured to listen on different ports.
It's possible to co-locate one or more workers on the same host with the Server. When the Server is started with the built-in Worker (`edgeiq run server`), the built-in Worker will bind to port `4040` on the host. This means that co-located Workers on the same host must be configured to listen on different ports.
:::

Therefore, the file should contain the following:

```
EDGEIQ_WORKER_ID=worker1
EDGEIQ_WORKER_API_KEY=F4177-AM9PZIEW7MPI7IL28ERE
EDGEIQ_JOBS_DIR=/var/lib/edgeiq-worker
EDGEIQ_URL=http://<server>:3000
EDGEIQ_LICENSE_EULA_ACCEPT=yes
EDGEIQ_WORKER_ID=worker1
EDGEIQ_WORKER_API_KEY=F4177-AM9PZIEW7MPI7IL28ERE
EDGEIQ_JOBS_DIR=/var/lib/edgeiq-worker
EDGEIQ_URL=http://<server>:3000
EDGEIQ_LICENSE_EULA_ACCEPT=yes
```

Change the `EDGEIQ_WORKER_API_KEY` to match the key you previously created.
Change the `EDGEIQ_WORKER_API_KEY` to match the key you previously created.

Change the `EDGEIQ_URL` to the Server address or hostname (confirm that your DNS is configured).
Change the `EDGEIQ_URL` to the Server address or hostname (confirm that your DNS is configured).

:::note
The value of `EDGEIQ_WORKER_ID` should match the Worker ID previously configured on the Server.
The value of `EDGEIQ_WORKER_ID` should match the Worker ID previously configured on the Server.
:::

Once you have saved the service unit file, reload `systemd`:

```sh
sudo systemctl daemon-reload
```

To start the Worker at boot, enable the service with:

```sh
sudo systemctl enable edgeiq-worker
sudo systemctl enable edgeiq-worker
```

Finally, start the Worker:

```sh
sudo systemctl start edgeiq-worker
sudo systemctl start edgeiq-worker
```

Verify that the Worker started successfully:

```sh
systemctl status edgeiq-worker
systemctl status edgeiq-worker
```

It's a good idea to inspect the startup output, which might contain an `error` or `warn`:

```sh
journalctl -u edgeiq-worker
journalctl -u edgeiq-worker
```

A Worker should now be running. It will register with the Server, using the specified API key.

The Server should indicate the Worker status on the Dashboard.

At this point, the Worker is ready to run received Jobs from the Server.
