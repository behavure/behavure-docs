---
title: Server Installation
description: Server Installation
slug: install/linux/server
sidebar:
  label: Server Installation
  order: 10
---

The Lyftdata binary is installed and available on the system, set up the Server as follows:

1. Create a system account.

2. Create a data directory.

3. Create `systemd` files.

4. Start the Server.

By the end of this section, you should be able to access the Server via a browser.

## Create a system account

Create a system account for the Server to run under:

```sh
sudo adduser --system --home /var/lib/lyftdata-server --disabled-login --group lyftdata
```

:::danger
**Do not** run the Server with `root` user privileges.
:::

## Create a Data Directory

The Server requires a data directory to store Jobs, logs, and metric data.

The `lyftdata` user home directory is `/var/lib/lyftdata-server` and it will also serve as the data directory.

:::danger
Secure environments require `0700` permissions on the data directory!
:::

If a different data directory is required, create it with the appropriate ownership and permissions. For example:

```sh
sudo mkdir -p /data/lyftdata
```

```sh
sudo chown lyftdata:lyftdata /data/lyftdata
```

## Create `systemd` Files

Create a `systemd` service unit file:

```sh
sudo vi /etc/systemd/system/lyftdata-server.service
```

The file must contain the following:

:::note
This `systemd` unit file assumes the binary is installed in `/usr/sbin/`.
If the binary is installed elsewhere, adjust the `ExecStart` section path accordingly.
:::


```sh
[Unit]
Description=lyftdata Server
After=network.target auditd.service

[Service]
EnvironmentFile=/etc/default/lyftdata-server
User=lyftdata
Group=lyftdata
ExecStart=/usr/sbin/lyftdata run server
Restart=on-failure
RestartSec=60

[Install]
WantedBy=multi-user.target
```

Create an environment file for the `EnvironmentFile` setting:

```sh
sudo vi /etc/default/lyftdata-server
```

Here, the Server is configured through either `lyftdata run server` options or environment variables. In this case, we'll be using the latter.

:::tip
See `lyftdata run server --help` for startup options and their environment variable equivalents and the reference.
:::

At a minimum, the Server needs `LYFTDATA_STAGING_DIR`:

```sh
LYFTDATA_STAGING_DIR=/var/lib/lyftdata-server
LYFTDATA_LICENSE_EULA_ACCEPT=yes
LYFTDATA_ADMIN_INIT_PASSWORD=ChangeMeVerySoon
```

:::note
If `lyftdata` user home directory is not `LYFTDATA_STAGING_DIR`, set accordingly.
:::

We've added 2 additional environment variables:

- `LYFTDATA_LICENSE_EULA_ACCEPT=yes` prevents the one-time prompt for accepting the [EULA](/eula).

- `LYFTDATA_ADMIN_INIT_PASSWORD` provides an initial `password` for the Server `admin` user.

Upon first initialization of the Server user database, if `LYFTDATA_ADMIN_INIT_PASSWORD` is unset, a random `password` will be generated in the Server `STDOUT` output (see `journalctl -u lyftdata-server`).

:::note
Whether using `LYFTDATA_ADMIN_INIT_PASSWORD`, or the randomly generated `password` on first run, change the `admin` `password` immediately!
:::

:::note
Besides the configured data directory (`LYFTDATA_STAGING_DIR`), the Server will persist some minimal state information to the home directory of the user that the Server runs as (`~/.local/share/lyftdata*/`). This directory must be writable by the Server.
:::

Once you have saved the service unit file, reload `systemd`:

```sh
sudo systemctl daemon-reload
```

To start the Server at boot, enable the service with:

```sh
sudo systemctl enable lyftdata-server
```

Finally, start the Server:

```sh
sudo systemctl start lyftdata-server
```

Verify that the Server started successfully:

```sh
systemctl status lyftdata-server
```

It's a good idea to inspect the startup output, which will contain the `admin` user `password` if it wasn't set with `LYFTDATA_ADMIN_INIT_PASSWORD`:

```sh
journalctl -u lyftdata-server
```

The Server will be listening on `LYFTDATA_BIND_ADDRESS` (default `127.0.0.1:3000`).

:::tip
The Server can be configured to use `TLS`, by providing a certificate and key file. See `lyftdata server run --help`.
When using a reverse proxy for TLS termination, like Caddy or Nginx, it's recommended to configure the appropriate `HTTP` client address headers, for logging purposes.
:::

If your cert uses `subjectAltName`, you **must** have an entry matching the cert `CN`. In the below `CSR` it is `server.lyftdata.local`:

```sh
openssl req -new -nodes -out server.lyftdata.local.csr -newkey rsa:4096 -keyout server.lyftdata.local.key -subj '/CN=server.lyftdata.local/C=ZA/ST=Gauteng/L=Johannesburg/O=Lyftdata'
```

The matching entry `DNS.1 = server.lyftdata.local`:

```sh
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names
[alt_names]
DNS.1 = server.lyftdata.local
IP.1 = 192.168.235.10
```

If no `subjectAltName`, the `CN` will suffice for successful cert verification, else an error occurs (see `journalctl -u lyftdata-server`):

```plaintext
...X509VerifyResult { code: 62, error: "**_Hostname mismatch_**" }
```

When testing with `curl -v`, the output _is_ indicative of what failed:

```plaintext
* subjectAltName does not match server.lyftdata.local
```

`openssl s_client` works without issues.

Go to `http://localhost:3000` in a browser. Log in with the username `admin` and the appropriate `password`.

At this point, the Server is ready to start serving Workers.