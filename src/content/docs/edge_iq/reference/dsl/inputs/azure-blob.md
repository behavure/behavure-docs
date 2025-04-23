# Azure Blob (`azure-blob`)

Retrieve (or list) Microsoft Azure Storage Blobs (Block Storage).


## Contents

- [Fields](#fields)
- [Authentication](#authentication)
- [Object Properties](#object-properties)




## Fields


| Field | Type | Required | Description |
|---|---|:---:|---|
| `trigger` | `trigger` |  | How often to run the command. |
| `mode` | [`Mode`](#mode-options) |  | The operating mode for this input. |
| `container-name` | `string` | ✅ | The storage service container for created blobs. |
| `blob-names` | `string` | ✅ | The name for the blobs. |
| `timestamp-mode` | [`Timestamp Mode`](#timestamp-mode-options) |  | Derive a timestamp for this blob for filtering purposes based on the selected strategy. |
| `maximum-age` | `string` |  | Remove any blobs older than this many seconds from the candidate list. |
| `fingerprinting` | `boolean` (`bool`) |  | Enable object fingerprinting, so an object will  only be downloaded once. |
| `maximum-fingerprint-age` | `duration` (`string`) |  | Remove any object fingerprints older than this from the tracker. |
| `preprocessors` | [`Preprocessors`](#preprocessors-options) |  | Preprocessors (process downloaded data before making it available to the job) these processors will be run in the order they are specified. |
| `ignore-linebreaks` | `boolean` (`bool`) |  | Treat object as one event. |
| `include-regex` | `regex` (`string`) |  | Include blobs matching the specified regular expressions. |
| `exclude-regex` | `regex` (`string`) |  | Exclude blobs matching the specified regular expressions. |
| `retry` | [`Retry`](#retry-fields) |  | How to retry after failure. |



## Authentication

<details>
<summary>Authentication</summary>


| Field | Type | Required | Description |
|---|---|:---:|---|
| `storage-account` | `string` | ✅ | The Storage Account Name to be used (credential). |
| `storage-master-key` | `string` | ✅ | The Storage Master Key to be used (credential). |

</details>



## Object Properties

<details>
<summary>Object Properties</summary>


| Field | Type | Required | Description |
|---|---|:---:|---|
| `blob-name-field` | `event-field` (`string`) |  | The field that a blob name from an operation should be stored in. |
| `creation-time-field` | `event-field` (`string`) |  | The field that the blob creation time should be stored in. |
| `last-modified-field` | `event-field` (`string`) |  | The field that the blob last modified time should be stored in. |
| `content-length-field` | `event-field` (`string`) |  | The field that the blob content length information should be stored in. |
| `content-type-field` | `event-field` (`string`) |  | The field that the blob content type information should be stored in. |
| `content-md5-field` | `event-field` (`string`) |  | The field that the blob content md5 should be stored in. |
| `etag-field` | `event-field` (`string`) |  | The field that the object ETag should be stored in. |
| `data-field` | `event-field` (`string`) |  | A field that the blob data should be nested in. |

</details>





<h3 id="retry-fields">Retry Fields</h3>

| Field | Type | Required | Description |
|---|---|:---:|---|
| `count` | [`integer`](../types/retry-count.md#retry-count) | ❌ | How to retry? Either forever or for a limited number of times. |
| `pause` | [`string`](../types/retry-pause.md#retry-pause) | ❌ | How long to pause before re-trying. |





<h3 id="mode-options">Mode Options</h3>

| Value | Name | Description |
|---|---|---|
| `list-and-download-objects` | list-and-download-objects | List Objects and Download |
| `list-objects` | list-objects | List Objects |
| `download-objects` | download-objects | Download Given Objects |



<h3 id="timestamp-mode-options">Timestamp Mode Options</h3>

| Value | Name | Description |
|---|---|---|
| `none` | none | The default mode, do not filter based on timestamps |
| `last-modified` | last-modified | Filter object on the last-modified timestamp reported by the service |
| `blob-name-pattern` | blob-name-pattern | Filter blobs on the timestamp derived from the object name for example: `relevant-name-pattern: =(?P<Y>[\\d]{4,4})-(?P<m>[\\d]{2,2})-(?P<d>[\\d]{2,2})/` |



<h3 id="preprocessors-options">Preprocessors Options</h3>

| Value | Name | Description |
|---|---|---|
| `extension` | extension | Preprocess the object or blob based on the extension of the object or blob name (.gz, .parquet) |
| `gzip` | gzip | UnGzip the received data |
| `parquet` | parquet | Extract the received data as JSON rows from a parquet file |
| `base64` | base64 | Encode the binary data as base64 |




---

Next: [Echo](echo.md)  
