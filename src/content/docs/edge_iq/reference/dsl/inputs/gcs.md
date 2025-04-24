---
title: Google Cloud Storage
description: Reference for the Google Cloud Storage component in Edge IQ's DSL
slug: inputs/gcs
---

# Google Cloud Storage (`gcs`)

Read objects from Google Cloud Storage.


## Contents

- [Fields](#fields)
- [Object Properties](#object-properties)




## Fields


| Field | Type | Required | Description |
|---|---|:---:|---|
| `trigger` | `trigger` |  | How often to run the command. |
| `bucket-name` | `string` | ✅ | The storage service container for created objects. |
| `object-names` | `string` | ✅ | Names for objects. If we are listing these are prefixes. |
| `mode` | [`Mode`](#mode-options) |  | List-and-download, List or just download. |
| `ignore-linebreaks` | `boolean` (`bool`) |  | Treat object as one event. |
| `credentials` | `gcs_input:credentials` | ✅ | credentials for accessing the object. |
| `timestamp-mode` | [`Timestamp Mode`](#timestamp-mode-options) |  | Derive a timestamp for this blob for filtering purposes based on the selected strategy. |
| `maximum-age` | `string` |  | Remove any blobs older than this many seconds from the candidate list. |
| `fingerprinting` | `boolean` (`bool`) |  | Enable object fingerprinting, which will cause an object to only be downloaded once. |
| `maximum-fingerprint-age` | `duration` (`string`) |  | Remove any object fingerprints older than this from the tracker. |
| `preprocessors` | [`Preprocessors`](#preprocessors-options) |  | Preprocessors (process downloaded data before making it available to the job) these processors will be run in the order they are specified. |
| `include-regex` | `string` |  | Include objects matching the specified regular expressions. |
| `exclude-regex` | `string` |  | Exclude objects matching the specified regular expressions. |
| `retry` | [`Retry`](#retry-fields) |  | How to retry failed operations. |



## Object Properties

<details>
<summary>Object Properties</summary>


| Field | Type | Required | Description |
|---|---|:---:|---|
| `object-name-field` | `event-field` (`string`) |  | The field that a object name from an operation should be stored in. |
| `creation-time-field` | `event-field` (`string`) |  | The field that the object creation time should be stored in. |
| `last-modified-field` | `event-field` (`string`) |  | The field that the object last modified time should be stored in. |
| `content-length-field` | `event-field` (`string`) |  | The field that the object content length information should be stored in. |
| `content-type-field` | `event-field` (`string`) |  | The field that the object content type information should be stored in. |
| `etag-field` | `event-field` (`string`) |  | The field that the object ETag should be stored in. |
| `data-field` | `event-field` (`string`) |  | A field to take the object data (default is to merge fields if possible). |

</details>





### Retry Fields

| Field | Type | Required | Description |
|---|---|:---:|---|
| `count` | `integer` |  | How to retry? Either forever or for a limited number of times. |
| `pause` | `string` |  | How long to pause before re-trying. |





### Mode Options

| Value | Name | Description |
|---|---|---|
| `list-and-download-objects` | list-and-download-objects | List Objects and Download |
| `list-objects` | list-objects | List Objects |
| `download-objects` | download-objects | Download Given Objects |



### Timestamp Mode Options

| Value | Name | Description |
|---|---|---|
| `none` | none | The default mode, do not filter based on timestamps |
| `last-modified` | last-modified | Filter object on the last-modified timestamp reported by the service |
| `blob-name-pattern` | blob-name-pattern | Filter blobs on the timestamp derived from the object name for example: `relevant-name-pattern: =(?P<Y>[\\d]{4,4})-(?P<m>[\\d]{2,2})-(?P<d>[\\d]{2,2})/` |



### Preprocessors Options

| Value | Name | Description |
|---|---|---|
| `extension` | extension | Preprocess the object or blob based on the extension of the object or blob name (.gz, .parquet) |
| `gzip` | gzip | UnGzip the received data |
| `parquet` | parquet | Extract the received data as JSON rows from a parquet file |
| `base64` | base64 | Encode the binary data as base64 |




---
Prev: [File Store](file-store.md)  
Next: [HTTP Poll](http-poll.md)  
