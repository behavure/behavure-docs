---
title: Windows Event Log
description: Reference for the Windows Event Log component in Edge IQ's DSL
slug: inputs/windows-event-log
---

# Windows Event Log (`windows-event-log`)

Read events from Windows Event Log.


## Contents

- [Fields](#fields)




## Fields


| Field | Type | Required | Description |
|---|---|:---:|---|
| `channel` | `string` | ✅ | The publisher channel to read events from. |
| `query` | `string` | ✅ | The query to filter events. |
| `start-at-oldest` | `boolean` (`bool`) |  | Start with the oldest event available in the log. |
| `debug-event-payloads` | `boolean` (`bool`) |  | Dump expanded event log data (not recommended for production). |








---
Prev: [S3](s3.md)  
Next: [Worker Channel](worker-channel.md)  
