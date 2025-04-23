# Add (`add`)

Add fields to the event.


## Contents

- [Fields](#fields)




## Fields


| Field | Type | Required | Description |
|---|---|:---:|---|
| `description` | `string` |  | describe this step. |
| `condition` | `lua-expression` (`string`) |  | Only run this action if the specified condition is met. |
| `output-fields` | [`Output Fields`](#output-fields-fields) | ✅ | Add these output fields (may be arbitrary values). |
| `overwrite` | `boolean` (`bool`) |  | Override existing fields. |








---
Prev: [Abort](abort.md)  
Next: [Assert](assert.md)  
