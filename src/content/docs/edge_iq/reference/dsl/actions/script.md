# Script (`script`)

Calculated fields.


## Contents

- [Fields](#fields)




## Fields


| Field | Type | Required | Description |
|---|---|:---:|---|
| `description` | `string` |  | describe this step. |
| `condition` | `lua-expression` (`string`) |  | Only run this action if the condition is met. |
| `overwrite` | `boolean` (`bool`) |  | Overwrite a field if it already exists. |
| `let` | `string` |  | field-expression pairs, like 'c: count()'. |
| `load` | `path` (`string`) |  | Load a file containing Lua functions into the current context 'init.lua' is loaded by default. |
| `run` | `multiline-text` (`string`) |  | Run the code on each action. |








---
Prev: [Rename](rename.md)  
Next: [Time](time.md)  
