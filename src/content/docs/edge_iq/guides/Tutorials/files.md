---
title: Reading Files
description: Reading Files
slug: guides/tutorials/files
sidebar:
  label: Reading Files
  order: 3
---


This is not scheduled like other inputs; you provide a `Path` with wildcards and it will keep checking for new files. These will be read, with each line becoming a new event.

## Once-Off Scanning of Directory

I have an example folder `scratch` which contains two files

```json
# test1.json
{"msg":"hello"}
{"msg":"goodbye"}
```
```json
# test2.json
{"msg":"hi"}
{"msg":"ciao"}
```

I set `Path` to `/path-to/scratch/*` and set `JSON` (since the data is already JSON)

By default, it will wait for changes in the file system. We want the job to immediately stop after processing all files matching the wildcards, so set `Stop Reading After` to `true`.

If you then click on the 'Run & Trace' button, you will see four events generated, corresponding to the four lines of JSON documents in the two files.

If you specify an output field name in `File Path Field` (like "file_name") the path will be
added to the data.  By default, that would give the complete path; if you just want the base, then set `File Basename`.

The events will now look like this:

```json
{"msg":"hello","file_name":"test1"}
{"msg":"goodbye","file_name":"test1"}
{"msg":"hi","file_name":"test2"}
{"msg":"ciao","file_name":"test2"}
```

## Watching File Changes

Disable `Stop Reading After`, and click on `Run Output`.  `Run time limit` can be pushed up to 60 seconds. 

After clicking on `Rerun`, then drop a new file into the `scratch` folder

You can always click on `Cancel Run` to terminate the job, if you get impatient for it to finish.

`Files` input remembers what files have been read, and saves this information. If you were now to stage this job and attach it to the built-in worker, it would process all of the files in `scratch`. 

But if you remove it from the worker, and add it again - which restarts it - it will not read from the beginning unless `Start At Beginning` is set.





