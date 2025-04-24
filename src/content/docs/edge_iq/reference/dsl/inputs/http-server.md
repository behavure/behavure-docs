---
title: HTTP Server
description: Reference for the HTTP Server component in Edge IQ's DSL
slug: inputs/http-server
---

# HTTP Server (`http-server`)

Run an HTTP server and output any received requests.


## Contents

- [Fields](#fields)




## Fields


| Field | Type | Required | Description |
|---|---|:---:|---|
| `address` | `string` | ✅ | server listens on this address:port. |
| `path` | `string` |  | and optionally only on this path. |
| `content-type` | `string` |  | Optional type of this body. |
| `tls` | [`Tls`](#tls-fields) |  | Optional TLS certificate and key. |
| `only-body` | `boolean` (`bool`) |  | only print out body, assumed to be JSON. |
| `query` | `string` |  | only print out given query var. |
| `json` | `boolean` (`bool`) |  | data is assumed to be already JSON. |
| `ignore-linebreaks` | `boolean` (`bool`) |  | data is assumed to be already JSON. |
| `custom-response` | `multiline-text` (`string`) |  | respond using this text. |
| `source-ip-field` | `event-field` (`string`) |  | If specified the source IP address for the http request to the server will be stored in the specified field. |
| `timeout` | `string` |  | timeout. |





### Tls Fields

| Field | Type | Required | Description |
|---|---|:---:|---|
| `cert` | `string` | ✅ | . |
| `key` | `string` | ✅ | . |





