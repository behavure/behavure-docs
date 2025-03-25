---
title: "Data Types Reference "
description: "Definition & use of Data Types Reference "
---
This reference guide enumerates each of the data types supported by Measure IQ, and explains how Measure IQ determines which data type to assign at ingest time.

## Data types

These are the core data types you will see in the Measure IQ query UI.

| Data Type | Aggregations | Grouping (Split By) | Filter Operators | Value Typeahead |
| --- | --- | --- | --- | --- |
| Identifier | Count Unique, First, Last | Yes | matches/does not match  <br>is empty/is not empty | No  |
| Integer\* / Decimal | Count Unique, First, Last, Min, Max, Sum, Average, Median, Percentile | Defaults to No, can be configured to Yes by admin | is one of/is not one of  <br>is less than (<)  <br>is greater than (>)  <br>is less than or equal to (<=)  <br>is greater than or equal to (>=) | No  |
| Integer Set / Decimal Set |     | Defaults to No, can be configured to Yes by admin | matches/does not match \[column/value\]  <br>is empty/is not empty | No  |
| String | Count Unique, First, Last | Yes | matches/does not match  <br>text contains/does not contain  <br>starts with/does not start with  <br>ends with/does not end with  <br>is empty/is not empty  <br>text matches regular expression | Yes |
| String Set | Count Unique | Yes | string value matches/does not match  <br>set contains/does not contain text  <br>starts with/does not start with  <br>ends with/does not end with  <br>is empty/is not empty  <br>text matches regular expression | Yes |
| Time | Count Unique, First, Last, Min, Max, Sum, Average, Median, Percentile | No  | is one of, is not one of, is less than (<), is greater than (>), is less than or equal to (<=), is greater than or equal to (>=) | No  |

\*Integers in Measure IQ are stored as 64-bit signed ints and so can only be a value from -(2^63) to 2^63 - 1.

## Expansion types

You won't see these as being first-class data types in the Measure IQ query UI, but at ingest time we apply expansion rules based on these data types. 

| Expansion Type | Data Type of Main Column | Generated Subcolumns |
| --- | --- | --- |
| IP Address | String | city, region, country, continent |
| URL | N/A (not loaded into Measure IQ by default) | scheme, hostname, path, filename, query, params, fragment |
| User Agent | N/A (not loaded into Measure IQ) | browser, device, platform, browser\_majorver, browser\_minorver, browser\_patchver |

## Ingest time auto-transformations

At ingest time, we automatically perform the following transformations on the raw JSON data **before** applying any data type recognition rules or expansions.

| Transformation Rule | Original JSON | Resulting JSON |
| --- | --- | --- |
| Flatten Nested JSON Objects | {"column": {"a": 1, "b": "xxx"}} | {"column.a": 1, "column.b": "xxx"} |
| Shred Arrays of JSON Objects | {"column": \[{"a": 1,"b": "zzz"}, {"a": 2,"b": "yyy"}\]} | {"column.a": \[1,2\], "column.b": \["zzz","yyy"\]} |

### String column transformations

If you have a regular string column that includes only the letters a through h, Measure IQ will auto-detect it as an integer and convert it to base 10. For example, "funding\_series" which has values like (a, b, c, d, e) might fall into this scenario.

| Original data | Transformed into... |
| --- | --- |
| "1234" | Integer values |
| "abc123" | Integer (converted to base 10), for values up to 16 hex digits |
| "abcdef-124" | Identifier, for values of 17 digits or more. The value can include hyphens. |

### Ingest Time Data Type Recognition Rules For JSON Number Columns

At ingest time, when we see a *new* column for the first time (and it is a JSON Number) we detect the data type of the new column using the following matching rules, in the **precedence order** listed below:

| Parsing Rule | Raw Data | Data Type | Rule Details |
| --- | --- | --- | --- |
| Detect Time | {"abc" : 1448933490} | Time | Measure IQ will attempt to interpret JSON ints as epoch timestamps in one of (microseconds, milliseconds, seconds). |
| Detect Integer | {"abc" : 12345} | Integer | Simple JSON ints are interpreted as Integers by Measure IQ. |
| Detect Decimal | {"abc" : 12345.98} | Decimal |     |
| Detect Integer Set | {"abc" : \[12345, 245, 99834\]} | Integer Set |     |
| Detect Decimal Set | {"abc" : \[12345.98, 245.2, 99834\]} | Decimal Set |     |

> [!INFO]
> Based on the order of precedence, if there is ambiguity about whether a column value can be interpreted as an epoch timestamp or an int, Measure IQ will interpret it as an epoch time value.

## Ingest time data type recognition rules for JSON string columns

At ingest time, when we see a *new* column for the first time (and it is a JSON String) we detect the data type of the new column using the following matching rules, in the **precedence order** listed below:

| Parsing Rule | Raw Data | Data Type | Rule Details |
| --- | --- | --- | --- |
| Detect Time From JSON String | {"abc" : "2015-11-30 08:09:12"} | Time | Measure IQ will attempt to interpret JSON strings as timestamps using approximately 40 different format strings (including [ISO-8601](../https://en.wikipedia.org/wiki/ISO_8601)). |
| Detect Identifier from JSON String | {"abc" : "e41249ed-2398-4c29-a6fa-ee81116dd302"} | Identifier | Measure IQ will attempt to interpret JSON strings containing 16 or more characters as hexadecimal identifiers, including some common [uuid](../https://en.wikipedia.org/wiki/Universally_unique_identifier) formats. Note that non-hex characters (like hyphens or dots) are stripped out of the resulting data. |
| Detect Integer From JSON String | {"abc" : "12345"} | Integer |     |
| Detect Decimal From JSON String | {"abc" : "12345.98"} | Decimal |     |
| Detect Decimal From JSON String With Dollar Sign | {"abc" : "$12,345.98"} | Decimal | Note that dollar signs and commas are stripped out of the resulting data. |
| Detect String Set | {"abc" : \["hello", "goodbye", "nice", "to", "see", "you"\]} | String Set |     |
| Detect URL | {"abc" : "[http://www.site.com/landing/](../https://www.mywebsite.com/landing/blue/)"} | URL |     |
| Detect IP Address | {"abc" : "127.0.0.1"} | IP Address |     |
| Detect User Agent | {"abc" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_10\_0)"} | User Agent | Measure IQ will attempt to interpret JSON strings as User Agents using a regex matching scheme. |

If you have any questions, please reach out to [help@behavure.ai](../mailto:help@behavure.ai) or your technical customer success manager (TCSM).

## More Information

- [Best practices for formatting data for ingest](../best-practices-for-formatting-data-for-ingest)
- [Best practices for formatting lookup table data](../best-practices-for-formatting-lookup-table-data)
- [What goes on behind the scenes when data is imported](../what-goes-on-behind-the-scenes-when-data-is-imported)