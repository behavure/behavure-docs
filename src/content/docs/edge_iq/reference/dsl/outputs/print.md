---
title: Print
description: Reference for the Print component in Edge IQ's DSL
slug: outputs/print
---

# Print (`print`)

Print event payloads to the terminal.


## Contents

- [Fields](#fields)




## Fields


| Field | Type | Required | Description |
|---|---|:---:|---|
| `output` | [`Output`](#output-options) | ✅ | the kind of output: standard output, standard error, pretty output. |







### Output Options

| Value | Name | Description |
|---|---|---|
| `stdout` | stdout | Standard output of job |
| `stderr` | stderr | Standard error of job |
| `pretty-stdout` | pretty-stdout | Nice JSON to standard output |
| `pretty-stderr` | pretty-stderr | Nice JSON to standard error |




---
Prev: [Message](message.md)  
Next: [S3](s3.md)  
