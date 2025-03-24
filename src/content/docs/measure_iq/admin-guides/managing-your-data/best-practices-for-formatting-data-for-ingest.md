---
title: "Best Practices for Formatting Data for Ingest "
description: "Definition & use of Best Practices for Formatting Data for Ingest "
---
This document covers best practices for configuring your data logging when preparing to load your data into Scuba.

## JSON format

JSON is Scuba's preferred file format. It does not require a dedicated header row, and easily allows us to auto-detect new columns as logging changes over time. 

Create each row, or event, as a complete JSON object that lives on its own line of the file. Here's a multi-row example:

```
1{"userid":"foo","timestamp":1051565134,"event":"Start"}2{"userid":"foo","timestamp":1051543123,"event":"Stop"}3{"userid":"bar","timestamp":1053400240,"event":"Start"}4{"userid":"zen","timestamp":1063334324,"event":"Start"}
```

Use a JSON validator, such as [JSON Lint](../http://jsonlint.com/), to make sure your JSON lines are valid.

We recommend that each row has at least one of the three following columns:

| Column type | Required? | Description |
| --- | --- | --- |
| timestamp | Yes | The timestamp specifies when the event occurred. See the [**Timestamp format**](../https://interana.atlassian.net/wiki/spaces/SGV/pages/2139261753#Timestamp-format) section for more information. |
| actor | Yes | A unique actor that persists over time (for example, users, companies, hospitals, server machines or airplanes). |
| event\_name | No  | The event specifies the action the actor took. Event names should be human-readable so that everyone on your team can understand what they are. Names like “event\_4” or “TSwrite” are less helpful than “registered\_account” or “played\_song”. |

It is recommended that you minimize nesting JSON objects. When Scuba receives nested JSON objects as in the contents of a field, for example `{"experiment": {"some":"json"; "more" : ["stuff", "in" ,"array"]}`, it generates a column for each field in the object, nested as deeply as the object is nested. In this example, Scuba creates two columns: `experiment.some` and `experiment.more`. This flattening allows you to access information in nested objects more easily. However, deeply nested JSON objects create many columns, which can impair performance and usability.

## Character encoding

Your data must contain only ASCII characters. Scuba does not support data that includes non-ASCII characters.

## Case sensitivity

Column names in Scuba are case-sensitive. If you have two columns where the names are the same other than the case (for example, foo and Foo), Scuba will treat these as separate columns, and are treated as case-sensitive in our stack. If the columns are supposed to be the same, edit the source data to use the same capitalization. 

## Multiple-source file types

If you want to import multiple event sources into a single Scuba table (which we support), you must have alignment between the timestamp, actor, and event\_name fields: use the same column name, including case, and the same data type, including format. If your raw logging has different names/types/formats for any of these three, you must transform the data before loading it into Scuba.

If you're avoiding a separate join/lookup table, include all relevant dimensions/fields in both datasets.

For example: if there are fields in data set A called `language` or `platform` that you want to pull in as queries in the context of dataset B, you must include them in dataset B. Even if there is a common link between the fields, such as `session ID`, you can't pull in fields from one dataset to another. Alternatively, you can create a [lookup table](../https://docs.scuba.io/guides/lookup-table). See [Best practices for formatting lookup table data](../best-practices-for-formatting-lookup-table-data) for more information.

## File storage requirements

Scuba can import data from the following file repositories:

- Amazon S3
- Azure BLOB storage
- Apache Kafka
- A local file system
- A remote file system to which you have scp access
- HTTP ingest ([streaming ingest](../https://docs.scuba.io/guides/streaming-ingest) of live data from a cloud or web source)

### Folder structure

We strongly recommend that you use the following format: `mydata/{year}/{month}/{day}/{hour}/`

### File sizes

Our data file size recommendations depend on how often you will be uploading files. If you are uploading a max of 1 file every minute (1440 files per day), then any file size is acceptable. If you plan to upload multiple files every minute, then we recommend you provide files that are as close to 1GB in size as possible. In other words, it's better to give us one 1GB file every minute than 1000 1MB files every minute.

## Timestamp format

We recommend that you format your timestamp data according to the [ISO-8601 standard](../https://en.wikipedia.org/wiki/ISO_8601). For example, `2015-10-05T14:48:00.000Z`, which has a format string of `%Y-%m-%dT%H:%M:%S.%fZ`. 

If your timestamps do not follow the ISO-8601 standard or you cannot reformat your timestamps to follow the standard, Scuba also supports Unix time plus a variety of common `strptime()` time format strings. Note that for a given column in your data, the time format must remain consistent for every event.

Scuba does not support dates prior to January 1, 1970 (the beginning of [Unix epoch time](../https://en.wikipedia.org/wiki/Unix_time)).

## Null values

Scuba interprets the following as null when ingesting data:

- an empty string: `{"foo": ""}`
- the word "null": `{"foo": null}`

This data does not appear in the record.

## Column data types and formats

When you initially create your table, the only columns defined are the time column and shard key columns. A [*shard key*](../https://scuba.atlassian.net/wiki/spaces/GLOSSARY/pages/2160232255/Shard+Key+Colocated+Shard+Key+v5) is a column in your dataset that represents an important entity that the event is about. This is the data on which you want to perform your analysis.

When you run your import pipeline, Scuba automatically detects the rest of the columns and their types from your raw data.

To create a column of type int\_set or string\_set, use JSON array values in your source data. If it is possible for a column to have more than one value, the value should be an array so that multiple values can be provided.

| Type | Examples | Notes |
| --- | --- | --- |
| time | {"time\_column\_sec" : 1448933490}<br><br>{"time\_column\_milli" : 1448933490000}<br><br>{"time\_column\_micro" : 1448933490000000}<br><br>{"time\_column\_with\_format" : "2015-11-30 08:09:12"} | Dates can either be epoch time (seconds, milliseconds, or microseconds) or `strptime` formatted dates (with custom format).<br><br>For a given column, the date format must be consistent in every event. |
| int | {"int\_column" : 12345} | You can filter an int column for exact match or use the standard compare operators.<br><br>You can aggregate int columns (min, max, avg, median, 50%, 75%, 90%, 95%, 99%).<br><br>You can group by int columns. Configure this in the **Settings** tab.<br><br>We support ints up to 53 bits.<br><br>Make sure that integers are unquoted (12345) and strings are quoted ("12345" or hex values like "ABC42"). Otherwise, this can cause Scuba to incorrectly treat a column as an integer when it would have been more appropriate as a string. Conversely, sometimes an unquoted integer value in JSON should be treated as a string (like a ZIP code) because it is groupable data, rather than a number on which to perform mathematical operations. |
| decimal | {"decimal\_column" : 12345.98} | Decimal values have the same properties as int values.<br><br>We support decimals up to 47 bits. |
| dollars | {"dollar\_column" : "$12,345.98"} | Scuba auto-detects numeric strings with dollar signs ($) as decimal columns. <br><br>For example, `{"purchase_dollars": "$13,424.35"}` would generate an int column that you can use just like any other decimal (with Sum, Avg, etc.). |
| string | {"string\_column" : "hello"} | You can filter a string column for exact match, starts with, ends with, or contains.<br><br>You can group by string columns.<br><br>We autocomplete most string columns when you type them into the UI (in a filter, for example). |
| int\_set | {"int\_set\_column" : \[12345, 245, 99834\]} | Int set columns are loaded from JSON arrays, but they have unordered set semantics (contains, does not contain). |
| string\_set | {"string\_set\_column" : \["hello", "goodbye", "nice", "to", "see", "you"\]} | String set columns are loaded from JSON arrays, but they have unordered set semantics (contains, does not contain).<br><br>Scuba will import a list of strings into a column of type "set." You can ask two questions of this column at query time: does the set contain a particular string, or does it not contain a particular string. Creating this type of column is a best practice when you want to do [A/B testing](../scuba-guides/scuba-user-guides/streamline-analysis-with-additional-explorations/analyze-ab-testing-results) (tagging each row with which test groups it's in). <br><br>This is imported as a set, which means that it’s not ordered (versus a list, which would be ordered).<br><br>For example:<br><br>`"tags":["fun","sports","beach"]` |
| JSON object | {"column": {"a": 1, "b": "xxx"}} | Scuba will "flatten" a nested object using a dot-separated notation. The output would be:<br><br>`{"column.a": 1, "column.b": "xxx"}` |
| Array of JSON objects | {"column": \[{"a": 1,"b": "zzz"}, {"a": 2,"b": "yyy"}\]} | The data import process will "shred" a nested array to produce multiple arrays of simple strings (as opposed to a single array of objects). The intermediate output would be:<br><br>`{"column": {"a": [1,2], "b": ["zzz","yyy"]}}`<br><br>Based on the "flatten" logic above, the final output would be:<br><br>`{"column.a": [1,2], "column.b": ["zzz","yyy"]}` |
| Identifiers | {"hex32\_column" : "A2439GF88EA12315A2487GF88EA12312"}<br><br>{"hex32\_column" : "e41249ed-2398-4c29-a6fa-ee81116dd302"} | While Scuba does support identifiers, we typically apply special handling to them before importing into the system. <br><br>Contact your Scuba representative before sending new identifiers into the system.<br><br>You can filter or group by hex32 columns. |
| URL | {"url\_column" : "[https://www.mywebsite.com/landing/blue/](../https://www.mywebsite.com/landing/blue/)"} | URL columns are split into multiple columns (domain, path, filename, etc.), separated at each "/" character. These columns are easier to manipulate separately. |
| IP address | {"ip\_column" : "127.0.0.1"} | IP address columns are parsed via a geoIP lookup to generate additional geographic information columns such as country and city. |
| User agent | {"user\_agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_10\_0)"} | User agent columns are split into multiple columns.<br><br>For web browser user agent strings, Scuba will add user-friendly columns for browser, platform, etc. |

## Working with large string data

It is possible to send very large chunks of string data into logs, which takes up a lot of string storage space on the system. 

Strings like URLs or GEOIP information tend to be long and have high cardinality (they’re uncommon or even unique). They take up a lot of space and may not be useful for queries. String columns in Scuba are stored in a string server that stores each unique string once. For most string columns, this is an optimized storage approach, but for some string columns the cardinality is very high (meaning there is little duplication) and the storage cost becomes high. We recommend removing these columns before importing to Scuba or splitting the column into more useful sub-columns that are of lower cardinality.

[Contact Scuba](../mailto:help@scuba.io) before sending new large string columns into the system.

## Columns containing a list of mixed data types

Be sure your data is meaningful. Using this example:

`"foo":["300",0,300]`

Scuba imports this snippet where the `foo` key maps to a list of `["300",0,300]`, but Scuba treats the entire list as a single string. While this will not cause an error, it’s not clear what the string `"300",0,300` is supposed to mean. Depending on the questions we want to ask about the data, we recommend that you pre-process this (or use derived columns) to achieve a more meaningful format.

### Auto-generated column names

Data that contains column names that are auto-generated based on data can cause an explosion of columns in the system (and these columns are typically not easy to work with within a dashboard). 

For example, suppose that for each experiment you run on your system, you auto-generate columns called `experiment1.foo` and `experiment1.bar`. This means that if you run 100 experiments, you will generate 200 new columns. A better approach would be to make a stable column name called \`experiment\_id\` and give it values of (1, 2, ...). Then you can make a stable dashboard on the `experiment.foo` and `experiment.bar` columns with a filter or group by `experiment.id`. 

Remove the auto-generated columns before importing them into Scuba. Importing auto-generated columns can result in an explosion of unintended columns within Scuba, which impairs performance and usability.