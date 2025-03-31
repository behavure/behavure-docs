---
title: Worker authentication
description: Worker authentication
sidebar:
  label: Worker authentication
  order: 1
---

Two available strategies can be used to authenticate Workers against a Server.

| Strategy            | Features                                                                          |
| ------------------- | --------------------------------------------------------------------------------- |
| **API key**         | Requires explicit initial setup on Server for each Worker                          |
| **Auto-Enrollment** | Server is configured once with a shared secret, which is re-used by Worker        |

:::note
Both of these authentication strategies can be used in tandem on the Server. However, each Worker can only use one of these strategies.
:::

## API Key Authentication

Known as the default strategy, API key authentication is useful when further control is needed over Worker authentication. It's especially useful for Workers running on untrusted (or less-trusted) systems. With this strategy, Workers must be configured and authorized on the Server *before* they are allowed to connect to the Server.

Adding a new Worker involves the following two steps, as well as specific configuration:

**Server Configuration**

1. Create a new Worker with a name. As an option, customize the Worker ID.

2. Create a new API key on the Server, or re-use an existing API key.

**Worker Configuration**

Under the Worker startup settings:

3. Configure the Worker ID (`LYFTDATA_WORKER_ID`) and API key (`LYFTDATA_WORKER_API_KEY`) as per the Server configuration above.

:::note
The Worker name is optional when using API key authentication.
:::

## Auto-Enrollment Authentication

Auto-Enrollment uses a shared secret, configured once on the Server and then re-used among Workers. Unlike the API key strategy, adding new Workers does not require initial Server configuration. Because of the shared secret, it's recommended to only use this strategy for Workers running on trusted or self-managed systems. 

The Auto-Enrollment strategy is disabled by default on the Server. Enable it as follows:

**Server**

1. Configure a shared secret in the Server startup settings (`LYFTDATA_AUTO_ENROLLMENT_KEY`).

**Worker**

2. Configure an Worker with a name (`LYFTDATA_WORKER_NAME`) and the Server shared secret (`LYFTDATA_AUTO_ENROLLMENT_KEY`).

3. Do **not** give the Worker an ID or API key (`LYFTDATA_WORKER_ID`).

The Server will automatically create Worker entries for any connecting Workers using the Server Auto-Enrollment secret.

:::note SecuRity
Use a randomly generated value of at least 32 characters for the shared secret, for example: `c3s3R0s1T5QAQr7lz1KsT00pKh3adnma`.
:::

:::danger
If the Auto-Enrollment secret is known, anyone with network access to the Server can add new Workers, without having access to the Server itself.
:::
