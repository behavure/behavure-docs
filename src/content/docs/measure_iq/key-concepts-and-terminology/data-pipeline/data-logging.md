---
title: "Data Logging"
description: "Definition & use of Data Logging"
---
In this guide, you will find the most effective methods for configuring your logging to load your data into Measure IQ.

## JSON format

JSON is Measure IQ's preferred file format. It does not require a dedicated header row, and easily allows us to auto-detect new columns as logging changes over time.

Create each row, or event, as a complete JSON object that lives on its own line of the file. Here's a multi-row example:

```
1 {"userid":"foo","timestamp":1051565134,"event":"Start"}
2 {"userid":"foo","timestamp":1051543123,"event":"Stop"}
3 {"userid":"bar","timestamp":1053400240,"event":"Start"}
4 {"userid":"zen","timestamp":1063334324,"event":"Start"}
```

Use a JSON validator, such as [JSON Lint](http://jsonlint.com/), to make sure your JSON lines are valid.

We recommend that each row has at least the following columns:

| Column type | Required? | Description |
| --- | --- | --- |
| timestamp | Yes | The timestamp specifies when the event occurred. |
| actor | Yes | A unique actor that persists over time (for example, users, companies, hospitals, server machines or airplanes). |
| event\_name | No  | The event specifies the action the actor took. Event names should be human-readable so that everyone on your team can understand what they are. Names like “event\_4” or “TSwrite” are less helpful than “registered\_account” or “played\_song”. |

## Character encoding

Your data must contain only ASCII characters. Measure IQ does not support data that includes non-ASCII characters.

## Case sensitivity

Column names in Measure IQ are case sensitive. If you have two columns where the names are the same other than the case (for example, foo and Foo), Measure IQ will treat these as separate columns, and we treat them as case-sensitive in our stack. If the columns are supposed to be the same, edit the source data to use the same capitalization.

## Multiple-source file types

If you want to import multiple event sources into a single Measure IQ table (and we recommend doing this), you must have alignment between the timestamp, actor, and event\_name fields: use the same column name, including case, and the same data type, including format. If your raw logging has different names/types/formats for any of these three, you must transform the data before loading into Measure IQ.

If you're avoiding a separate join/lookup table, include all relevant dimensions/fields in both datasets.

For example, if there are fields in data set A called `language` or `platform` that you want to pull in as queries that are in the context of dataset B, you must include them in dataset B. Even if there is a common link between the fields, such as `session ID`, you can't pull in fields from one dataset to another. Alternatively, you can create a join table.

## File storage requirements

Measure IQ can import data from the following file repositories:

- Amazon S3
- Azure BLOB storage
- A remote file system to which you have scp access

## Folder structure

We strongly recommend that you use the following format: `mydata/{year}/{month}/{day}/{hour}/`

## File sizes

Our data file size recommendations depend on how often you will be uploading files. If you are uploading a max of 1 file every minute (1440 files per day), then any file size is okay. If you plan to upload multiple files every minute, then we recommend you provide files that are as close to 1GB in size as possible. In other words, it's better to give us one 1GB file every minute than 1000 1MB files every minute.

## Timestamp format

We recommend that you format your timestamp data according to the [ISO-8601 standard](https://en.wikipedia.org/wiki/ISO_8601). For example, `2015-10-05T14:48:00.000Z`, which has a format string of `%Y-%m-%dT%H:%M:%S.%fZ`.

If your timestamps do not follow the ISO-8601 standard or you cannot reformat your timestamps to follow the standard, Measure IQ also supports Unix time plus a variety of common `strptime()` time format strings. Note that for a given column in your data, the time format must remain consistent for every event.

Measure IQ does not support dates prior to January 1, 1970 (the beginning of [Unix epoch time](https://en.wikipedia.org/wiki/Unix_time)

## Null values

Measure IQ interprets the following as null when ingesting data:

- an empty string: `{"foo": ""}`
- the word "null": `{"foo": null}`
- the data does not appear in the record

## Column data types and formats

When you initially create your table, the only columns defined are the time column and shard key columns. A *shard key* is a column in your dataset that represents an important entity that the event is about. This is the data on which you want to perform your analysis.

When you run your import pipeline, Measure IQ will automatically detect the rest of the columns and their types from your raw data.

| **Type** | **Examples** | **Notes** |
| --- | --- | --- |
| time | {"time\_column\_sec" : 1448933490}{"time\_column\_milli" : 1448933490000}{"time\_column\_micro" : 1448933490000000}{"time\_column\_with\_format" : "2015-11-30 08:09:12"} | Dates can either be epoch time (seconds, milliseconds, or microseconds) or strptime formatted dates (with custom format).For a given column, the date format must be consistent in every event. |
| int |     |     |
| decimal |     |     |
| dollars |     |     |
| string |     |     |
| int\_set |     |     |
| string\_set |     |     |
| JSON object |     |     |
| array of JSON objects |     |     |
| identifier |     |     |
| URL |     |     |
| user agent |     |     |
| IP address |     |     |

## Working with large string data

It is possible to send very large chunks of string data into logs, which takes up a lot of string storage space on the system.

Strings like URLs or GEOIP information tend to be long and have high-cardinality (they’re uncommon or even unique). They take up a lot of space and may not be useful for queries. String columns in MeasureIQ are stored in a string server that stores each unique string once. For most string columns, this is an optimized storage approach, but for some string columns the cardinality is very high (meaning there is little duplication) and the storage cost becomes high. We recommend removing these columns before importing to MeasureIQ or splitting the column into more useful sub-columns that are lower cardinality.

Contact [help@behavure.ai](mailto:help@behavure.ai) before sending new large string columns into the system.

## Columns containing a list of mixed data types

Be sure your data is meaningful. Using this example: `"foo":["300",0,300]`  
MeasureIQ imports this snippet where the `foo` key maps to a list of `["300",0,300]`, but MeasureIQ treats the entire list as a single string. While this will not cause an error, it’s not clear what the string `"300",0,300` is supposed to mean. Depending on the questions we want to ask about the data, we recommend that you pre-process this (or use derived columns) to achieve a more meaningful format.

## Auto-generated column names

Data that contains column names that are auto-generated based on data can cause an explosion of columns in the system (and these columns are typically not easy to work with in a dashboard).

For example, suppose that for each experiment you run on your system, you auto-generate columns called `experiment1.foo` and `experiment1.bar`. This means that if you run 100 experiments, you will generate 200 new columns. A better approach would be to make a stable column name called `experiment_id` and give it values of (1, 2, ...). Then you can make a stable dashboard on the `experiment.foo` and `experiment.bar` columns with a filter or group by `experiment.id`.

Remove the auto-generated columns before importing into MeasureIQ. Importing auto-generated columns can result in an explosion of unintended columns within MeasureIQ, which impairs performance and usability.