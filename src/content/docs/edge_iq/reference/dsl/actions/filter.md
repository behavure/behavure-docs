---
title: Filter
description: Reference for the Filter component in Edge IQ's DSL
slug: actions/filter
---

# Filter (`filter`)

Only let certain events pass through.


## Contents

- [Fields](#fields)




## Fields


| Field | Type | Required | Description |
|---|---|:---:|---|
| `description` | `string` |  | describe this step. |
| `condition` | `string` |  | Only filter if this condition is true. |
| `discard-until` | `boolean` (`bool`) |  | if true, then we will discard events until the filter is green Thereafter, we pass all events through. |
| `how` | `filter:how` | ✅ | The four ways to filter events: by schema, by patterns matching, by patterns _not_ matching, or if empty. |







