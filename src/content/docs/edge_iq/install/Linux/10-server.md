---
title: Server Installation
description: Server Installation
slug: install/linux/server
sidebar:
  label: Server Installation
  order: 10
---

The Edge IQ binary is installed and available on the system, set up the Server as follows:

## Quick Installation

For a quick setup, you can use the following installation script. Save it as `install-server.sh`, make it executable with `chmod +x install-server.sh`, and run it with `sudo ./install-server.sh`:

```sh
#!/bin/bash

# Edge IQ Server Installation Script
# This script automates the systemd setup process for Edge IQ server

# Check if running as root
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root (use sudo)"
  exit 1
fi

# Create system account
echo "Creating system account..."
useradd --system --home /var/lib/edgeiq-server --disabled-login --group edgeiq || true

# Create data directory
echo "Creating data directory..."
mkdir -p /var/lib/edgeiq-server
chown edgeiq:edgeiq /var/lib/edgeiq-server
chmod 700 /var/lib/edgeiq-server

# Create systemd service file
echo "Creating systemd service file..."
cat > /etc/systemd/system/edgeiq-server.service << EOF
[Unit]
Description=edgeiq Server
After=network.target auditd.service

[Service]
EnvironmentFile=/etc/default/edgeiq-server
User=edgeiq
Group=edgeiq
ExecStart=/usr/sbin/edgeiq run server
Restart=on-failure
RestartSec=60

[Install]
WantedBy=multi-user.target
EOF

# Create environment file
echo "Creating environment file..."
cat > /etc/default/edgeiq-server << EOF
EDGEIQ_STAGING_DIR=/var/lib/edgeiq-server
EDGEIQ_LICENSE_EULA_ACCEPT=yes
EDGEIQ_ADMIN_INIT_PASSWORD=ChangeMeVerySoon
EOF

# Set proper permissions
chmod 600 /etc/default/edgeiq-server

# Reload systemd
echo "Reloading systemd..."
systemctl daemon-reload

# Enable and start the service
echo "Enabling and starting Edge IQ server..."
systemctl enable edgeiq-server
systemctl start edgeiq-server

echo ""
echo "=== Installation Complete ==="
echo "Edge IQ server is now running at http://127.0.0.1:3000"
echo "Login with username: admin"
echo "Password: ChangeMeVerySoon"
echo ""
echo "IMPORTANT: Change the admin password immediately after first login!"
```

## Manual Installation

If you prefer to set up the server manually, follow these steps:

1. Create a system account.

2. Create a data directory.

3. Create `systemd` files.

4. Start the Server.

By the end of this section, you should be able to access the Server via a browser.

## Create a system account

Create a system account for the Server to run under:

```sh
sudo adduser --system --home /var/lib/edgeiq-server --disabled-login --group edgeiq
```

:::danger
**Do not** run the Server with `root` user privileges.
:::

## Create a Data Directory

The Server requires a data directory to store Jobs, logs, and metric data.

The `edgeiq` user home directory is `/var/lib/edgeiq-server` and it will also serve as the data directory.

:::danger
Secure environments require `0700` permissions on the data directory!
:::

If a different data directory is required, create it with the appropriate ownership and permissions. For example:

```sh
sudo mkdir -p /data/edgeiq
```

```sh
sudo chown edgeiq:edgeiq /data/edgeiq
```

## Create `systemd` Files

Create a `systemd` service unit file:

```sh
sudo vi /etc/systemd/system/edgeiq-server.service
```

The file must contain the following:

:::note
This `systemd` unit file assumes the binary is installed in `/usr/sbin/`.
If the binary is installed elsewhere, adjust the `ExecStart` section path accordingly.
:::

```sh
[Unit]
Description=edgeiq Server
After=network.target auditd.service

[Service]
EnvironmentFile=/etc/default/edgeiq-server
User=edgeiq
Group=edgeiq
ExecStart=/usr/sbin/edgeiq run server
Restart=on-failure
RestartSec=60

[Install]
WantedBy=multi-user.target
```

Create an environment file for the `EnvironmentFile` setting:

```sh
sudo vi /etc/default/edgeiq-server
```

Here, the Server is configured through either `edgeiq run server` options or environment variables. In this case, we'll be using the latter.

:::tip
See `edgeiq run server --help` for startup options and their environment variable equivalents and the reference.
:::

At a minimum, the Server needs `EDGE_IQ_STAGING_DIR`:

```sh
EDGEIQ_STAGING_DIR=/var/lib/edgeiq-server
EDGEIQ_LICENSE_EULA_ACCEPT=yes
EDGEIQ_ADMIN_INIT_PASSWORD=ChangeMeVerySoon
```

:::note
If `edgeiq` user home directory is not `EDGEIQ_STAGING_DIR`, set accordingly.
:::

We've added 2 additional environment variables:

- `EDGEIQ_LICENSE_EULA_ACCEPT=yes` prevents the one-time prompt for accepting the [EULA](/eula).

- `EDGEIQ_ADMIN_INIT_PASSWORD` provides an initial `password` for the Server `admin` user.

Upon first initialization of the Server user database, if `EDGEIQ_ADMIN_INIT_PASSWORD` is unset, a random `password` will be generated in the Server `STDOUT` output (see `journalctl -u EDGEIQ-server`).

:::note
Whether using `edgeiq_ADMIN_INIT_PASSWORD`, or the randomly generated `password` on first run, change the `admin` `password` immediately!
:::

:::note
Besides the configured data directory (`EDGEIQ_STAGING_DIR`), the Server will persist some minimal state information to the home directory of the user that the Server runs as (`~/.local/share/edgeiq*/`). This directory must be writable by the Server.
:::

Once you have saved the service unit file, reload `systemd`:

```sh
sudo systemctl daemon-reload
```

To start the Server at boot, enable the service with:

```sh
sudo systemctl enable edgeiq-server
```

Finally, start the Server:

```sh
sudo systemctl start edgeiq-server
```

Verify that the Server started successfully:

```sh
systemctl status edgeiq-server
```

It's a good idea to inspect the startup output, which will contain the `admin` user `password` if it wasn't set with `EDGEIQ_ADMIN_INIT_PASSWORD`:

```sh
journalctl -u edgeiq-server
```

The Server will be listening on `EDGEIQ_BIND_ADDRESS` (default `127.0.0.1:3000`).

:::tip
The Server can be configured to use `TLS`, by providing a certificate and key file. See `edgeiq server run --help`.
When using a reverse proxy for TLS termination, like Caddy or Nginx, it's recommended to configure the appropriate `HTTP` client address headers, for logging purposes.
:::

If your cert uses `subjectAltName`, you **must** have an entry matching the cert `CN`. In the below `CSR` it is `server.edgeiq.local`:

```sh
openssl req -new -nodes -out server.edgeiq.local.csr -newkey rsa:4096 -keyout server.edgeiq.local.key -subj '/CN=server.edgeiq.local/C=ZA/ST=Gauteng/L=Johannesburg/O=edgeiq'
```

The matching entry `DNS.1 = server.edgeiq.local`:

```sh
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names
[alt_names]
DNS.1 = server.edgeiq.local
IP.1 = 192.168.235.10
```

If no `subjectAltName`, the `CN` will suffice for successful cert verification, else an error occurs (see `journalctl -u edgeiq-server`):

```plaintext
...X509VerifyResult { code: 62, error: "**_Hostname mismatch_**" }
```

When testing with `curl -v`, the output _is_ indicative of what failed:

```plaintext
* subjectAltName does not match server.edgeiq.local
```

`openssl s_client` works without issues.

Go to `http://localhost:3000` in a browser. Log in with the username `admin` and the appropriate `password`.

At this point, the Server is ready to start serving Workers.
