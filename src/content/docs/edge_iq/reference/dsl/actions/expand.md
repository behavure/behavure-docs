---
title: Expand
description: Reference for the Expand component in Edge IQ's DSL
slug: actions/expand
---

# Expand (`expand`)

expand data in various ways: events, XML, multiline events.


## Contents

- [Fields](#fields)




## Fields


| Field | Type | Required | Description |
|---|---|:---:|---|
| `description` | `string` |  | . |
| `condition` | `lua-expression` (`string`) |  | Only run this action if the condition the specified condition is met. |
| `delim` | `string` |  | . |
| `suppress-warnings` | `boolean` (`bool`) |  | Suppress warnings generated by this action. |
| `input-field` | `event-field` (`string`) |  | . |
| `document-mode` | `boolean` (`bool`) |  | . |
| `remove` | `boolean` (`bool`) |  | . |
| `mode` | `expand:mode` | ✅ | . |







