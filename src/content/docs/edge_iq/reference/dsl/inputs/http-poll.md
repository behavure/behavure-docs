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





<h3 id="retry-fields">Retry Fields</h3>

| Field | Type | Required | Description |
|---|---|:---:|---|
| `count` | [`integer`](../types/retry-count.md#retry-count) | ❌ | How to retry? Either forever or for a limited number of times. |
| `pause` | [`string`](../types/retry-pause.md#retry-pause) | ❌ | How long to pause before re-trying. |



<h3 id="batch-fields">Batch Fields</h3>

| Field | Type | Required | Description |
|---|---|:---:|---|
| `uuid-field` | [`string`](../types/batch-uuid-field.md#batch-uuid-field) | ❌ | Field where generated uuid, the unique marker for the group, will be stored. |
| `invocation-time-field` | [`string`](../types/batch-invocation-time-field.md#batch-invocation-time-field) | ❌ | Field where invocation time will be stored. |
| `completion-time-field` | [`string`](../types/batch-completion-time-field.md#batch-completion-time-field) | ❌ | Field where completion (end of execution) time will be stored. |
| `begin-marker-field` | [`string`](../types/batch-begin-marker-field.md#batch-begin-marker-field) | ❌ | Field used to mark first event in the group. |
| `end-marker-field` | [`string`](../types/batch-end-marker-field.md#batch-end-marker-field) | ❌ | Field used to mark last event in the group. |
| `line-count-field` | [`string`](../types/batch-line-count-field.md#batch-line-count-field) | ❌ | Field used to store the line count of the batch. |
| `line-num-field` | [`string`](../types/batch-line-num-field.md#batch-line-num-field) | ❌ | Field used to store the line number of the batch. |



<h3 id="auth-fields">Auth Fields</h3>

| Field | Type | Required | Description |
|---|---|:---:|---|
| `username` | [`string`](../types/string.md#string) | ✅ | Name of User. |
| `password` | [`string`](../types/string.md#string) | ✅ | Password. |



<h3 id="response-fields">Response Fields</h3>

| Field | Type | Required | Description |
|---|---|:---:|---|
| `json` | [`bool`](../types/http-poll-input-response-json.md#http-poll-input-response-json) | ❌ | Return response in JSON format as single line-delimited event. |
| `status-field` | [`string`](../types/http-poll-input-response-status-field.md#http-poll-input-response-status-field) | ❌ | Field to store HTTP status code. |
| `headers-field` | [`string`](../types/http-poll-input-response-headers-field.md#http-poll-input-response-headers-field) | ❌ | Field to store response headers. |
| `response-field` | [`string`](../types/http-poll-input-response-response-field.md#http-poll-input-response-response-field) | ❌ | Field to store the body of the response. |





<h3 id="method-options">Method Options</h3>

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
