---
title: Log Files
description: Reference for the Log Files component in Edge IQ's DSL
slug: inputs/files
---

# Log Files (`files`)

Monitor one or more log files for new lines.


## Contents

- [Fields](#fields)




## Fields


| Field | Type | Required | Description |
|---|---|:---:|---|
| `path` | `path` (`string`) | ✅ | a path with wildcards identifying files to be read. |
| `encoding` | `encoding` (`string`) |  | the text encoding for the monitored files. |
| `include` | `path` (`string`) |  | any other paths to be included. |
| `exclude` | `path` (`string`) |  | paths to be excluded. |
| `ignore-older-than` | `number` (`integer`) |  | ignore files older than this (epoch time in seconds). |
| `glob-minimum-cooldown` | `number` (`integer`) |  | pause after scanning for new files (in milliseconds). |
| `stop-reading-after` | `boolean` (`bool`) |  | do not wait for new files. |
| `ignore-line-breaks` | `boolean` (`bool`) |  | consume each file as one event. |
| `remove-after` | `number` (`integer`) |  | remove files that are done reading  after this period (seconds). |
| `fingerprinting` | `files_input:fingerprinting` |  | File fingerprinting strategy. |
| `oldest-first` | `boolean` (`bool`) |  | default is youngest first. |
| `file-path-field` | `event-field` (`string`) |  | fill this field with the file we are currently reading from. |
| `file-basename` | `boolean` (`bool`) |  | the `file-path-field` path will be the basename (e.g. '/path/frodo.txt' becomes just 'frodo'). |
| `start-at-beginning` | `boolean` (`bool`) |  | ignore stored checkpoints and re-read all specified files. |
| `json` | `boolean` (`bool`) |  | assume lines are already JSON. |
| `max-read-size` | `number` (`integer`) |  | will not attempt to read files larger than this. |
| `max-line-size` | `number` (`integer`) |  | will not attempt to read lines longer than this. |








---
Prev: [Internal Messages](internal-messages.md)  
Next: [S3](s3.md)  
