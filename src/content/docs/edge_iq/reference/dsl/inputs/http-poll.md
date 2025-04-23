# HTTP Poll (`http-poll`)

Run HTTP queries.


## Contents

- [Fields](#fields)




## Fields


| Field | Type | Required | Description |
|---|---|:---:|---|
| `trigger` | `trigger` |  | When and How to run this input. |
| `retry` | [`Retry`](#retry-fields) |  | How to retry operation if it fails. |
| `batch` | [`Batch`](#batch-fields) |  | Marking each group of input events in a distinct way. |
| `url` | `url` (`string`) | ✅ | The URL for this request. |
| `json` | `boolean` (`bool`) |  | Use for when data is text or already JSON. |
| `ignore-line-breaks` | `boolean` (`bool`) |  | Do not treat separate lines as distinct events. |
| `events-field` | `event-field` (`string`) |  | extract events from this field of the response, assumed to be an array. Body is assumed to be JSON and we ignore line breaks. |
| `document-mode` | `boolean` (`bool`) |  | collect all the output together as a single document (will affect batching on the output). |
| `headers` | `string` |  | Headers to send with the query. |
| `query` | `string` |  | Query parameters to send with the query. |
| `auth` | [`Auth`](#auth-fields) |  | Basic HTTP authentication (user:pass). |
| `body` | `multiline-text` (`string`) |  | The payload to send. |
| `form-urlencoded-body` | `string` |  | Payload as key-value pairs posted as form-urlencoded. |
| `method` | [`Method`](#method-options) |  | HTTP method to use for the query - default is GET. |
| `timeout` | `time-interval` (`string`) |  | Timeout for the request (e.g. 500ms, 2s, etc. - the default is 30 seconds). |
| `response` | [`Response`](#response-fields) |  | Fields to include in returned event. |
| `insecure` | `boolean` (`bool`) |  | Ignore TLS certificate validation errors (This is unsafe to use). |





### Retry Fields

| Field | Type | Required | Description |
|---|---|:---:|---|
| `count` | `integer` |  | How to retry? Either forever or for a limited number of times. |
| `pause` | `string` |  | How long to pause before re-trying. |



### Batch Fields

| Field | Type | Required | Description |
|---|---|:---:|---|
| `uuid-field` | `string` |  | Field where generated uuid, the unique marker for the group, will be stored. |
| `invocation-time-field` | `string` |  | Field where invocation time will be stored. |
| `completion-time-field` | `string` |  | Field where completion (end of execution) time will be stored. |
| `begin-marker-field` | `string` |  | Field used to mark first event in the group. |
| `end-marker-field` | `string` |  | Field used to mark last event in the group. |
| `line-count-field` | `string` |  | Field used to store the line count of the batch. |
| `line-num-field` | `string` |  | Field used to store the line number of the batch. |



### Auth Fields

| Field | Type | Required | Description |
|---|---|:---:|---|
| `username` | `string` | ✅ | Name of User. |
| `password` | `string` | ✅ | Password. |



### Response Fields

| Field | Type | Required | Description |
|---|---|:---:|---|
| `json` | `bool` |  | Return response in JSON format as single line-delimited event. |
| `status-field` | `string` |  | Field to store HTTP status code. |
| `headers-field` | `string` |  | Field to store response headers. |
| `response-field` | `string` |  | Field to store the body of the response. |





### Method Options

| Value | Name | Description |
|---|---|---|
| `get` | get | Get |
| `post` | post | Post |
| `put` | put | Put |
| `patch` | patch | Patch |
| `delete` | delete | Delete |
| `options` | options | Options |
| `head` | head | Head |




---
Prev: [Google Cloud Storage](gcs.md)  
Next: [HTTP Server](http-server.md)  
