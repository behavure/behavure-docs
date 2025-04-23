# Message (`message`)

Conditionally generate a message when an event meets the provided condition.


## Contents

- [Fields](#fields)




## Fields


| Field | Type | Required | Description |
|---|---|:---:|---|
| `description` | `string` |  | Describe this step. |
| `condition` | `lua-expression` (`string`) | ✅ | A Lua expression which determines whether to generate a message based on the event. |
| `notification-type` | [`Notification Type`](#notification-type-options) | ✅ | Is this message an alert or an info notification? |
| `message-content` | `multiline-text` (`string`) | ✅ | The content of the message. |
| `log-event` | `boolean` (`bool`) |  | Send this event to the job log? |







### Notification Type Options

| Value | Name | Description |
|---|---|---|
| `alert` | alert | The message indicates that something is wrong |
| `info` | info | This message is informational |




---
Prev: [Key Value](key-value.md)  
Next: [Remove](remove.md)  
