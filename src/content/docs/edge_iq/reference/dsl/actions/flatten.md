---
title: Flatten
description: Reference for the Flatten component in Edge IQ's DSL
slug: actions/flatten
---

# Flatten (`flatten`)

Flatten nested JSON Objects and Arrays into a single JSON Object containing only top-level fields.


## Contents

- [Fields](#fields)




## Fields


| Field | Type | Required | Description |
|---|---|:---:|---|
| `description` | `string` |  | describe this step. |
| `condition` | `lua-expression` (`string`) |  | Only run this action if the specified condition is met. |
| `fields` | `flatten:fields` | ✅ | The fields that should be flattened (all or a subset). |
| `preserve-empty-arrays` | `boolean` (`bool`) |  | Preserve empty arrays. |
| `preserve-empty-objects` | `boolean` (`bool`) |  | Preserve empty objects. |
| `separator` | `string` |  | Set the string to separate keys in the flattened object. |







