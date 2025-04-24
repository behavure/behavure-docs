---
title: Echo
description: Reference for the Echo component in Edge IQ's DSL
slug: inputs/echo
---

# Echo (`echo`)

Create a simple static event.


## Contents

- [Fields](#fields)




## Fields


| Field | Type | Required | Description |
|---|---|:---:|---|
| `trigger` | `trigger` |  | How and when to trigger runs of the job. |
| `event` | `multiline-text` (`string`) | ✅ | The static data to be used as input A message trigger can import data to be used here in ${} expressions. |
| `json` | `boolean` (`bool`) |  | Treat incoming data as JSON. |
| `ignore-linebreaks` | `boolean` (`bool`) |  | Do not treat separate lines as distinct events. |








---
Prev: [Azure Blob](azure-blob.md)  
Next: [Exec](exec.md)  
