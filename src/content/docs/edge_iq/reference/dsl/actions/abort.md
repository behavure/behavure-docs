---
title: Abort
description: Reference for the Abort component in Edge IQ's DSL
slug: actions/abort
---

# Abort (`abort`)

Abort the job if the condition is met.


## Contents

- [Fields](#fields)




## Fields


| Field | Type | Required | Description |
|---|---|:---:|---|
| `description` | `string` |  | describe this step. |
| `condition` | `lua-expression` (`string`) | ✅ | Run this action if the specified condition is met. |
| `message` | `string` | ✅ | Emit this log warning when the job aborts. |








---

Next: [Add](add.md)  
