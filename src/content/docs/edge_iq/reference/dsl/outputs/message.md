---
title: Message
description: Reference for the Message component in Edge IQ's DSL
slug: outputs/message
---



# Message (`message`)

Create a message to the internal message subsystem.


## Contents

- [Fields](#fields)




## Fields


| Field | Type | Required | Description |
|---|---|:---:|---|
| `tag` | `string` |  | A user-defined tag that's attached to the output message type for filtering. |
| `input-field` | `event-field` (`string`) |  | Send only the content of the specified field to the message subsystem. |
| `set-variable-name` | `string` |  | Use the input to set the value of a variable. |








---
Prev: [Log Files](file.md)  
Next: [Print](print.md)  
