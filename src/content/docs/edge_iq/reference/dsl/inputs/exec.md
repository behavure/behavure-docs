---
title: Exec
description: Reference for the Exec component in Edge IQ's DSL
slug: inputs/exec
---



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



### Result Fields

| Field | Type | Required | Description |
|---|---|:---:|---|
| `status-field` | `string` |  | Field where exit status of command will be stored. |
| `stderr-field` | `string` |  | Field where stderr of command will be stored. |
| `stdout-field` | `string` |  | Field where stdout of command will be stored. |






---
Prev: [Echo](echo.md)  
Next: [File Store](file-store.md)  
