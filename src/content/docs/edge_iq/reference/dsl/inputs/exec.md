# Exec (`exec`)

Obtain data by executing a shell command.


## Contents

- [Fields](#fields)




## Fields


| Field | Type | Required | Description |
|---|---|:---:|---|
| `trigger` | `trigger` |  | When and How to run the command. |
| `retry` | [`Retry`](#retry-fields) |  | Retry policy. |
| `command` | `multiline-text` (`string`) | ✅ | A shell command (Powershell on Windows, system shell otherwise). |
| `batch` | [`Batch`](#batch-fields) |  | Marking each group of input events in a distinct way. |
| `result` | [`Result`](#result-fields) |  | Fields where output, errors and status go (default is just stdout). |
| `json` | `boolean` (`bool`) |  | True if the input is already in JSON format. |
| `no-strip-linefeeds` | `boolean` (`bool`) |  | Do not remove any line endings from the command. |
| `ignore-line-breaks` | `boolean` (`bool`) |  | Treat result as one event. |
| `env` | `exec_input:env` |  | Environment as a YAML file or inline name-value pairs. |
| `timeout` | `string` |  | Maximum time to wait (500ms, 2s, etc). |





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



<h3 id="result-fields">Result Fields</h3>

| Field | Type | Required | Description |
|---|---|:---:|---|
| `status-field` | [`string`](../types/exec-input-result-status-field.md#exec-input-result-status-field) | ❌ | Field where exit status of command will be stored. |
| `stderr-field` | [`string`](../types/exec-input-result-stderr-field.md#exec-input-result-stderr-field) | ❌ | Field where stderr of command will be stored. |
| `stdout-field` | [`string`](../types/exec-input-result-stdout-field.md#exec-input-result-stdout-field) | ❌ | Field where stdout of command will be stored. |






---
Prev: [Echo](echo.md)  
Next: [File Store](file-store.md)  
