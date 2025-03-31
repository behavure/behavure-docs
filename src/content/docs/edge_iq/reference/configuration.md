---
title: Configuration
description: Configuration
sidebar:
  label: Configuration
  order: 2
  # badge:
  #   text: New
  #   variant: tip
---

# Environment Variables

Here we cover environment variables used to configure the Server, Workers and CLI.

:::note
Some configuration and/or startup options do not have environment variable
equivalents. Use `--help` for additional parameters on the relevant CLI
commands.
:::

## Server

Settings here apply to `lyftdata run server` and `lyftdata run worker`. Options without environment variables are omitted:

| CLI/Environment Variable                                       |      Default      | Description                                                                                                    |
| -------------------------------------------------------------- | :---------------: |----------------------------------------------------------------------------------------------------------------|
| --staging-dir<br/>LYFTDATA_STAGING_DIR                           | `~/.local/lyftdata` | The data/working directory                                                                                     |
| --auto-enrollment-key<br/>LYFTDATA_AUTO_ENROLLMENT_KEY           |       none        | The shared secret for Worker enrollments                                                                       |
| --bind-address<br/>LYFTDATA_BIND_ADDRESS                         |  127.0.0.1:3000   | The Server HTTP API will be served on this address and port. Use `0.0.0.0:3000` for all network interfaces     |
| --disk-usage-max-percentage<br/>LYFTDATA_DB_DISK_USE_MAX_PERCENT |        80         | Logs and metric data will be removed when the staging directory volume exceeds this threshold                  |
| --jwt-psk<br/>LYFTDATA_JWT_PSK                                   |  Auto-generated   | Preshared JWT signing key                                                                                      |
| --log-retention-days<br/>LYFTDATA_LOG_RETENTION_DAYS             |        30         | The maximum number of days that logs should be retained                                                        |
| --tls-cert<br/>LYFTDATA_TLS_CERT                                 |       none        | Path to TLS certificate file (if using TLS)                                                                    |
| --tls-key<br/>LYFTDATA_TLS_KEY                                   |       none        | Path to TLS key (if using TLS)                                                                                 |
| n/a<br/>LYFTDATA_LICENSE                                         |       none        | Used to provide the Server with a license key. If present, it will override existing licenses on every startup |
| n/a<br/>LYFTDATA_LICENSE_EULA_ACCEPT                                         |       none        | Used to accept the EULA on startup. Sometimes needed for automation and other operational requirements         |

## Worker

Settings here apply to worker. Options without environment variables are omitted:

| CLI/Environment Variable                                    |        Default        | Description                                                                                                                            |
| ----------------------------------------------------------- | :-------------------: |----------------------------------------------------------------------------------------------------------------------------------------|
| --lyftdata-worker-api-key<br/>LYFTDATA_WORKER_API_KEY             |          n/a          | API key for this Worker                                                                                                                |
| --lyftdata-worker-id<br/>LYFTDATA_WORKER_ID                       |    auto-generated     | Unique ID. Used to identify this Worker                                                                                                |
| --worker-api-bind-address<br/>LYFTDATA_WORKER_API_BIND_ADDRESS  |    127.0.0.1:4041<br/>127.0.0.1:3041 | Listening address for new _internal_ job-worker protocol.<br/>Port 3041 by default on the Server's built-in Worker.<br/>Otherwise 4041 |
| --lyftdata-worker-name<br/>LYFTDATA_WORKER_NAME                   |          n/a          | Name for this Worker                                                                                                                   |
| --lyftdata-url<br/>LYFTDATA_URL                                 | http://localhost:3000 | URL where the Server API can be reached                                                                                                |
| --auto-enrollment-key<br/>LYFTDATA_AUTO_ENROLLMENT_KEY        |          n/a          | Enrollment secret if auto-enrollment is enabled on the Server                                                                          |
| --jobs-dir<br/>LYFTDATA_JOBS_DIR                            |          n/a          | Directory where jobs are stored, defaulting to user cache directory                                                                    |
| --metrics-interval<br/>LYFTDATA_WORKER_METRICS_INTERVAL        |          60           | Send metrics to Server at this interval (seconds)                                                                                      |
| --tags<br/>LYFTDATA_WORKER_LABELS                                |          n/a          | Labels to attach to Worker system information                                                                                          |

## CLI

Settings here apply to administrative commands. These commands are a CLI wrapper to the Server HTTP API:

| Environment Variable |        Default        | Description |
| -------------------- | :-------------------: | ----------- |
| LYFTDATA_URL           | http://localhost:3000 | Server URL  |
