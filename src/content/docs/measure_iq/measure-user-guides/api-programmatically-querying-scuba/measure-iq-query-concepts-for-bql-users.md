---
title: "Measure IQ Query Concepts for BQL Users "
description: "Definition & use of Measure IQ Query Concepts for BQL Users "
---

This article describes how a Measure IQ query is interpreted and executed, the behavioral database query model.

For more information about the Measure IQ query language, see:

- [BQL syntax and usage](../bql-syntax-and-usage) for a description of BQL building blocks and examples of common Measure IQ queries in BQL.
- [BQL vs. SQL comparison](../compare-bql-and-sql-commands) for similarities and differences between BQL and SQL concepts.

For information about querying with the API, see [Use the Measure IQ external query API](../use-the-scuba-external-query-api).

## Basic concepts

### Query

A query is an instruction to retrieve a result set from a Scuba table. It has a list of measures, each of which aggregates and/or calculates data, optionally along with group by and order by, similar to SQL. Unlike SQL, a Measure IQ query has a timespec, which specifies the time aspects of the query.

### Measure

A measure is a unit of aggregation and/or calculation of a query. A measure can be an aggregation or calculation between aggregations and/or constants.

### Aggregation

An aggregation aggregates data in a scope and returns a value as a result. COUNT, COUNT UNIQUE, and AVG are examples of aggregations. These aggregations work the same way as their SQL counterparts. One notable difference in Measure IQ is that an aggregation can have its own filtering (WHERE) clause, whereas SQL allows only a single query-wide WHERE clause.

Each aggregation runs on a scope. You can specify the scope explicitly with an ON clause, but in most cases, an aggregation scope is determined by the scopes of properties used in the aggregation. This is called [scope inference](#scope-inference).

### Property

A property is a set of data values, one value for each row of the scope. Like a column in a relational database represents a set of values in a table, a property represents a set of values in a scope. Whereas a column in a relational database can have only values of simple types, a property in a scope can be a formula or an aggregation on an underlying scope if the scope is either Actor or Flow.

#### Example

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

### Time series query

A query can be time series or non-time series. A non-time series query is similar to SQL. It returns a single set of results for the specified time range. In contrast, a time series query returns a set of results for each time range (that is, a time bucket).

#### Examples

The following query is a non-time series query that returns a single row of results:

```
> select count(*) from my_table between 2019-01-01 and 2019-01-15
count(*)
--------
35
>

```

The following query is a time series query that returns a row for each time bucket:

```
> select count(*) from my_table for every 1 week between 2019-01-01 and 2019-01-15

Start      End count(*)
------------------------------
2019-01-01 2019-01-08 19
2019-01-08 2019-01-15 16
>
```

### Timespec

A timespec is a set of time-related attributes that define the time range or ranges of a query or a property. These attributes are:

- Start time
- End time
- Resolution
- Trailing window
- Offset

### Start time/end time

The start and end times specified in a query determine the time span in which the query is run.

#### Example

```
select count(*) from my_table between 2019-01-01 and 2019-01-15
```

Note that data outside of the time span can be used in a query when a query or properties used in the query have an offset or trailing window that goes beyond the time span.

A property can have its own start time and end time, or a trailing window with or without offset. Such a property is calculated in its own time span.

### Resolution

In a time series query, an aggregation in a query measure is calculated multiple times over a time span. The resolution determines the interval at which aggregation calculations is done.

#### Example

The following is a time series query with a resolution of 2 weeks. This query counts the number of events for every 2-week bucket.

```
select count(*) from my_table for every 2 weeks between 2019-01-01 and 2019-04-01
```

A property does not have its own resolution. Only a query can have a resolution and the resolution is shared by all properties appearing in the query.

### Trailing window and time bucket

In a time series query, the trailing window determines the time span over which aggregation calculations are run. In a time series query, query measure calculation is done for each resolution point over the time span specified by the trailing window. A time span is also called a time bucket.

A trailing window can be larger than the resolution of the query. For example, a query can have a 2-day trailing window with 1-day resolution. In this case, the trailing windows of two resolution points overlap each other.

#### Example

The following query counts the number of events for each 2-day window every day between 2019-01-01 and 2019-01-15.

```
select count(*) from my_table for every day over 2 days between 2019-01-01 and 2019-01-15
```

In the current version of Measure IQ, a trailing window must be a multiple of the resolution. For example, a trailing window cannot be 7 days if the resolution is 3 days. This also means that a trailing window cannot be smaller than the resolution.

A property can also have a time window. It determines the time span on which the property’s calculation is run.

### Time offset

A property can have a time offset. Without a time offset, a trailing window’s end time is at a resolution point. You can “offset” the trailing window from a resolution point by specifying a time offset. When specified, the trailing window of the property shifts from the resolution point for the specified time offset amount.

#### Example

The following query returns the number of users who had an event between 2019-01-08 and 2019-01-15 but not in the previous week (2019-01-01 to 2019-01-18):

```
with prev_week_activity as Actor<user>(
  count(*) over 1 week offset -1 week
)
select count_unique(user where prev_week_activity = 0) from my_table between 2019-01-08 and 2019-01-15
with last_year_activity as Actor<user>(
  count(*) over 1 week offset -1 year
)
select count_unique(user where last_year_activity > 0) from my_table between 2019-01-08 and 2019-01-15
```

### Scope

A scope corresponds to a table in a relational database. Like a relational database table, a Measure IQ scope has rows of data. A column in a relational database corresponds to a property in a Scuba database.

There are three types of scope in Measure IQ: Event, Actor, and Flow.

### Event scope

Event scope is a type of scope. Event scope allows direct access to data imported to a Scuba table. Only one Event scope exists in a Scuba table.

### Raw event property vs. custom event property

There are two types of event property, raw and custom (or manual). Raw properties are created by the system when data gets imported into a Scuba table. They correspond to columns in the imported data. Custom properties are created by a user.  
For information about custom event property syntax in BQL, see [BQL syntax and usage](../bql-syntax-and-usage).

### Actor scope

Measure IQ creates an actor scope for each shard key (a.k.a. actor column). Since more than one shard key is allowed in a Scuba table, more than one Actor scope can exist in a Scuba table.

An Actor scope has rows whose unique key is its shard key. Actor properties of the scope hold values in a row as a column does in a row of a table in the relational database.

For example, if a raw event property “user” is a shard key. An Actor scope “user” has a row for each unique user. An actor property can be considered as an attribute of a user.

For instance, an actor property

```
  Actor<user>(last(country) between beginning_of_time and now)
```

could be called current_country of the Actor<user> scope.

### Flow scope

Each flow defined in a Scuba table has its own scope.

A flow scope has rows of flow instances whose primary key is the flow instance id. Like a column in a relational database table, a flow property holds a value in a row of a flow scope.

### Flow

A Measure IQ user can define a set of rules and group a series of events performed by an actor. This is called a flow. A flow can also have states in it.

For example, the user can define a flow that starts with a “login” event, then moves to “listening” state with a following “play” event, then moves to “idle” state with a “stop” event. A flow is a kind of finite-state machine that takes a time series of events of an actor as input.

A flow is a powerful mechanism to organize users’ otherwise scattered traces of activities into meaningful user behaviors. The “play session” flow above is one such example. A user subscription or purchase funnel is another great example of a flow.

### Flow instance

Events of actors are grouped together per flow definition. The group of events is a flow instance. A flow instance is a row in a Flow scope.  A flow instance has attributes as defined as flow properties.

## Scope inference rules

Each aggregation in a query has its own scope.  An aggregation scope may be specified explicitly with “on” clause. But in most cases, it can be omitted so that the system can infer the scope. This section describes the scope inference rules.

### Simple inference

If an aggregation has a target property, the scope of the property is the scope of the aggregation.  For example,

```
with last_24hr_activity as Actor<user>(
  count(*) over 24 hours
),
num_flow_events as Flow<user_session>(
  count(*)
)
select avg(price), avg(last_24hr_activity), avg(num_flow_events) from my_table
```

In this query, scopes of the aggregations are event, actor and flow, respectively, assuming that price is an event property.

### Advanced inference

The simple scope inference does not work if an aggregation has no target (e.g. count(\*)). It also does not work if the aggregation target is an actor column because an actor column may appear in any scope, Event, Actor or Flow.  
Advanced scope inference rules kick in in this case.  Advanced scope inference rules look at the scope of properties used in the where clause and group by clause of the aggregation.

1. If an Event scope or a Flow scope exists, it is the scope of the aggregation.  Event scope and Flow scope may not coexist.
2. If an Actor scope exists but no Event or Flow scope exists, the Actor scope is the aggregation scope.
3. If no property exists, Event scope is the aggregation scope.

## Scope alignment rules

A query has its own scope, Event, Actor of a kind, or Flow of a kind.  A query can also have properties of different scopes, with certain limitations. When different scopes appear in a query, they are “joined” together to perform the query. This join is similar in concept to the relational database join. Unlike the relational database join, however, Measure IQ scopes are joined only through an actor property.

### Actor property on event scope

An actor property is joined on the event scope through its actor column.

### Actor property on flow scope

An actor property is joined on the flow scope through its actor column.  The flow scope and the actor property must have the same actor id. Otherwise, the query throws an error.

### Raw event property on actor scope

When a raw event property is used in an actor scope, it is not joined but behaves differently.

#### Subgrouping behavior

The raw event property is used for subdividing actor raw properties for each unique value of the raw event property.  For example, the following query returns the average play time per user per music service:

```
with user_play_time as Actor<user>(
  sum(play_time)
)
select avg(user_play_time) group by music_service
```

If a user used two different music services, A and B, for 10 hours and 50 hours, respectively, the user’s total play time `(sum(play_time))` is divided into two (10 and 50) and accounts for the averages of respective groups.

#### Other scope combinations

Other scope combinations such as flow property on an event scope are not supported.  This is because those combinations do not result in a unique row via an actor id.

## Time alignment rules

### Time buckets

A query has a timespec. A timespec determines time bucket(s) of the query. A time bucket consists of a pair of timestamps, start time, and end time. The rows that fall within the time range are used for calculations for the time bucket.

For the Event scope, those rows whose timestamp value falls into a time bucket belong to the time bucket.

For the Actor and the Flow scope, those rows that have at least one event in the time bucket belong to the time bucket.  For example, user “John” appears in a time bucket 2019-01-01 - 2019-01-08 if he has an event in the time range.  
Time buckets may overlap each other.  For example, the following query has eight overlapping 7 day time buckets one day apart from each other:

```
select count(*) from my_table for every day over 7 days between 2019-01-01 and 2019-01-08
```

### Time alignment

A property is calculated according to its own timespec.  Its time buckets are independent of the time buckets of the query except for the resolution, which is shared across the query. A time bucket of a property might include its corresponding query time bucket entirely (for example, a property time bucket Jan 1 - Jan 8 and a query time bucket Jan 2 - Jan 4), or vice versa (property time bucket Jan 1 - Jan 8, query time bucket Jan 1 - Jan 31), or partially overlapped (property time bucket Jan 1 - Jan 8, query time bucket Jan 5 - Jan 12), or detached completely (property time bucket Jan 1 - Jan 8, query time bucket Feb 1 - Feb 8).

### Properties of a different scope

If the property’s scope is different from the scope of the query and if those scopes are “join-able,” the result value of the property is left joined on rows of the query scope using the actor property as the join key.  If a property value exists for an actor id but the actor id does not exist in the query rows, the property value is ignored. Time buckets play no role in this process.

### Properties of the same scope

For each query time bucket, rows in the time bucket are used for query aggregation.  If a property’s scope matches the scope of the query, the property values will be a part of the rows.

If a property time bucket range is out of the corresponding query time bucket, it’s possible that a property value does not have its row in the query time bucket.  In this case, the row will also be a part of the query aggregation.

#### Example

The following query returns the number of users who had an event last week:

```
with previous_week_activity as Actor<user>(
  count(*) over 1 week offset -1 week
)
select count_unique(user where previous_week_activity > 0)
from my_table between 1 week ago and now
```

The user “John” had some events last week but not this week.  A row for John is not in the query’s time bucket because he had no events this week.  But he has a row in the actor property `previous_week_activity` because he had events last week. His row is a part of the `count_unique` aggregation and therefore he is counted as one of the values in `count_unique`.
