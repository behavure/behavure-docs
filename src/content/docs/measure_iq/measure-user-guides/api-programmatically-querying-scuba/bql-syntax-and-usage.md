---
title: "BQL Syntax and Usage "
description: "Definition & use of BQL Syntax and Usage "
---

Measure IQ provides a flexible query language to use within an external query API call. This article describes how to format BQL syntax. It includes a table comparing and contrasting some types of queries with analogies in SQL, as well as some example BQL queries.

### BQL syntax

Use BQL inside a call to the Measure IQ external query API.

An example API call containing BQL, with the output returning a Scuba UI explore URL, is formatted as follows:

```
{
	"bql": "select count (*) from foreverMusic group by gender between 7 days ago and now",
	"return_type": "explore_url",
}
```

##### _See_ [_Additional Query Options_](#add-query-opt) _for more information on return_type and other API elements._

A sample curl request with BQL looks like this:

```
curl 'https://11.2.34.141/v1/query' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Token san+aslnasw50293sjlfhgnoOvWW/sQH09y0' \
    -d '{"bql": "select count(*) from foreverMusic"}' --verbose
> POST /v1/query HTTP/2
> Host: 11.2.34.141
> User-Agent: curl/7.54.0
> Accept: */*
> Content-type: application/json
> Authorization: Token san+aslnasw50293sjlfhgnoOvWW/sQH09y0
> Content-Length: 32
```

> [!INFO]
> For more information on using the external query API, see [Use the Measure IQ external query API](./api-programmatically-querying-scuba).

### BQL building blocks

Like other database query languages, BQL statements consist of a sequence of clauses, which can in turn consist of expressions. BQL clauses must be assembled in a specific order to form a valid statement.

To build a BQL query, start by choosing aggregations and the target of the aggregations (that is, the things you want to aggregate over).

Every BQL query must contain the required clauses, as follows:

- aggregation
- table
- time range (if none is supplied, the query defaults to the time range "beginning of time to now")

Other clauses are optional, for example:

- Filter on aggregation
- Group by clause

For example, consider the following statement:

```
select count (* where page = "Error") from my_table group by ROUND(length,10) between 6 months ago and now
```

This BQL statement consists of several clauses and an expression. The clauses in the example are the following:

- select count (\* where page="Error")
- from my_table
- group by artist
- between 6 months ago and now

The expressions in the example are the following:

- ROUND(length,10)
- page = "Error"

More examples of valid expressions include the following:

- ROUND(length,10) + 1
- page like ".\*error.\*"
- length - another_length
- length / 100 \* 100

BQL is case-sensitive.

### BQL equivalents of Scuba UI queries

The following table shows common Measure IQ queries and their equivalents in BQL.

|                                                                                                                                                                  |                                                                                                               |                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| **Measure IQ sentence-model UI**                                                                                                                                      | **BQL statement**                                                                                             | **Concept**                             |
| Show count of events                                                                                                                                             | select count (\*) from my_table                                                                               | Aggregate                               |
| Show count of events <br>Filtered to events with `page` that matches “Error”                                                                                     | select count (\* where page=”Error”) from my_table                                                            | Filter                                  |
| Show count of events <br>Filtered to events with `page` that matches “Error” <br>Split by artist                                                                 | select count (\* where page=”Error”) from my_table group by artist                                            | Split by (group by)                     |
| Show count of events <br>Filtered to events with `page` that matches “Error” <br>Split by `artist` <br>Starting 6 months ago <br>Ending now                      | select count (\* where page=”Error”) from my_table group by artist between 6 months ago and now               | Relative time                           |
| Show count of events <br>Filtered to events with `page` that matches "Error" <br>Split by `ROUND(length,10)` <br>Starting 6 months ago <br>Ending now            | select count (\* where page="Error") from my_table group by ROUND(length,10) between 6 months ago and now     | Calculations                            |
| Show count of events as `cnt` <br>Filtered to all events <br>Split by username <br>Limit 5 <br>Ordered by `cnt` ascending <br>Starting 7 days ago <br>Ending now | select count(\*) as cnt from nightly1_usage group by username limit 5 order by cnt between 7 days ago and now | Order by, refer to measure name (`cnt`) |

> [!INFO]
> Some queries allowed in BQL do not work in the Scuba UI, and vice versa. In particular, many of the restrictions imposed by the UI around query start and end times are enforced because the UI wants to be able to guarantee that the end time is later than the start time no matter when the query is run, in case you pin the query to a board, for example. In that context, the UI does not allow queries whose validity depends on the time of day. The BQL API doesn't concern itself with that; it accepts or rejects the query based on whether the time range is valid at the moment you run the query.

### Time

#### Relative time

The following query defines a relative time window:

```
select count(* where action="hate") from fashion between beginning_of_time and now
```

#### Trailing time windows

The following query counts the number of events for each 2 day window every day between 2021-01-01 and 2021-01-15 UTC:

```
select count(*) from my_table for every day over 2 days between 2021-01-01 and 2021-01-15
```

In the current version of Measure IQ, a trailing window must be a multiple of the resolution. For example, a trailing window cannot be 7 days if the resolution is 3 days. This also means that a trailing window cannot be smaller than the resolution.

#### Specify timezone

By default, BQL uses UTC rather than the timezone that your Scuba cluster uses in UI-based queries. To specify a timezone, append `timezone <timezone>` to the end of your query. For example:

```
select count(*) from my_table between 7 days ago and now timezone US/Pacific
```

To correctly format your timezone, see the timezone database and the related [Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) article. Note that Measure IQ supports only time zones with one-hour alignments. For example, it does not support America/St. Johns (+3:30) or Asia/Calcutta (+5:30).

### Custom event properties

An event property can be raw or custom (also called manual). A custom event property can be created using one of three [methods](/measure_iq/glossary/method): label, filter, or calculate. The syntax for filtering your query on a custom event property varies depending on the method used to create the property, as follows:

|                           |                                                                  |
| ------------------------- | ---------------------------------------------------------------- |
| **Event property method** | **Filter syntax**                                                |
| Calculate                 | where <clc_event_prop_name> = "<value>"                          |
| Label                     | where <lbl_event_prop_name> = "<value>"                          |
| Filter                    | where <flt_event_prop_name>  <br>where not <flt_event_prop_name> |

For example, to filter on a label or calculate event property, use the following:

```
select count(* where action="hate") from fashion
```

But to use a filter event property called `authenticated` (where each value is either "true" or "false"), use the following syntax:

```
select count(* where authenticated) from fashion
```

### Actor property examples

The following query returns the number of users who had an event between 2021-01-08 and 2021-01-15 but not in the previous week (2021-01-01 to 2021-01-18):

```
with prev_week_activity as Actor<user>(
  count(*) over 1 week offset -1 week
)
select count_unique(user where prev_week_activity = 0) from my_table between 2021-01-08 and 2021-01-15
```

The following query defines two actor properties, `user_age` and `years_voting`, the former as an aggregation and the latter as a formula:

```
with user_age as Actor<user>(
  max(age) between beginning_of_time and now
),
years_voting as Actor<user>(
  user_age - 18
)
select ...
```

### Escaping special characters

Access fields with spaces, periods, hyphens, or other special characters by using backquotes. For example:

```
select count(*) from my_table group by `hello.world` between 7 days ago and now
```

Quoted strings are currently not supported in `as` statements.

> [!INFO]
> Be careful to double check the quotes being used.

### Additional Query Options

BQL supports custom options such as return type, chart name, and chart type. See below for more details and some examples.

| **JSON element**   | **Description**                                                                           | **Valid values**                                                                                                                                                                    |
| ------------------ | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bql                | Query definition                                                                          | See [BQL syntax](#bql-syntax), above                                                                                                                                                |
| query_response_id  | The `query_response_id` of a previous UI request or BQL execution                         | `r` followed by numbers; i.e. `r95376`                                                                                                                                              |
| return_type        | Specify if the output should be JSON data or a link to the UI (explore URL)               | `data` _(default)_ <br>`explore_url`                                                                                                                                                |
| result_format      | Mandatory only if `return_type` is “data”; defines the format of the data in response     | `JSON_POWER_BI` _(default)_ : flat array of dictionaries. 1 dict per group per time bucket. <br>`DEFAULT`: format that the UI expects <br>`CSV`                                     |
| chart_options.name | The name of the returned Explore chart; only available when `return_type` = “explore_url” | It should be a string                                                                                                                                                               |
| chart_options.type | The chart type of the graph in Explore                                                    | `TIME` _(default)_: Time view <br>`TABLE` : Table view <br>`SANKEY` : Sankey view <br>`NUMBER`: Number view <br>`BAR` : Bar view <br>`SUNBURST`: Pie view <br>`SCATTER` : Line view |

#### Example calls:

Request 1:

```
{
	"bql": "select count (*) from music group by gender between 7 days ago and now",
	"result_format":"JSON_POWER_BI",
	"return_type": "data"
}
```

Return 1:

```
[
  {
    "count of events": 31128.0,
    "end_time_0": 1616080024320,
    "start_time_0": 1184025600000,
    "gender": null
  },
  {
    "count of events": 391722.0,
    "end_time_0": 1616080024320,
    "start_time_0": 1184025600000,
    "gender": "F"
  },
  {
    "count of events": 431791.0,
    "end_time_0": 1616080024320,
    "start_time_0": 1184025600000,
    "gender": "M"
  }
]
```

Request 2:

```
{
	"bql": "select count (*) as `event count` from music group by gender between 7 days ago and now",
	"return_type": "explore_url",
	"chart_options": {
		"name": "This is a time chart",
		"type": "time"
	}
}
```

Return 2:

```
{
  "url": "https://my_cluster.scuba.io/explorer/r12345"
}
```

Request 3:

```
{
	"query_response_id": "r12345",
	"return_type": "explore_url",
	"chart_options": {
		"name": "This is now a table chart",
		"type": "table"
	}
}
```

Return 3:

```
{
  "url": "https://my_cluster.scuba.io/explorer/r12346"
}
```
