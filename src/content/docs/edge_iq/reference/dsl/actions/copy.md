# Copy (`copy`)

Copy fields of an event using JSONPATH expressions.


## Contents

- [Fields](#fields)




## Fields


| Field | Type | Required | Description |
|---|---|:---:|---|
| `description` | `string` |  | describe this step. |
| `condition` | `lua-expression` (`string`) |  | Only run this action if the specified condition is met. |
| `jsonpath-fields` | `string` | ✅ | Fields to add to the event, where the values are the result of a JSONPath query For the query syntax see: https://www.ietf.org/archive/id/draft-ietf-jsonpath-base-12.html. |
| `overwrite` | `boolean` (`bool`) |  | Override existing fields. |








---
Prev: [Convert](convert.md)  
Next: [Csv](csv.md)  
