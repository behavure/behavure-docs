---
title: Variable expansion
description: Variable expansion features in Jobs
draft: true
---

Variable expansion is an advanced feature in Job configuration. This feature allows Jobs to:

- access centralized or external configuration data
- access event data
- access data about internal Job statistics and state
- access dynamic variables
- access data from message payloads (for message-triggered jobs)
- generate and format inline timestamps, without using the time action

## Variable expansion syntax

Within Job configuration, there are two kinds of syntax used for variable expansion.

The `{{IDENTIFIER}}` syntax, or "double curly" syntax, is used for accessing context data.

The `${IDENTIFIER}` syntax, or "dollar curly" syntax, is used for all other variable expansion features.

The dollar curly syntax has some variants, which are used to access different kinds of data in a Job. This list is a summary, and more detailed information is provided in the following sections.

| Syntax                      | Description                                                  |
| --------------------------- | ------------------------------------------------------------ |
| `${FIELD_NAME}`             | Used to access the value of a named field in event data      |
| `${stat\|IDENTIFIER}`       | Used to access Job stats                                     |
| `${dyn\|IDENTIFIER}`        | Used to access values of dynamic variables                   |
| `${msg\|FIELD_NAME}`        | Used to access the value of a field within a message payload |
| `${time\|FORMAT_SPECIFIER}` | Used to generate and/or format timestamps                    |

## Context

Context is user-provided configuration data that can be specified:

- At the Job level
- At the Worker level
- At the Server level

Context data consists of key-value pairs, where each key is unique, and which can be accessed within Jobs using a special syntax.

For example, context is often used to store secrets and API keys. If a context key named `API_KEY` is defined at the server level, it can be accessed within a Job configuration using the following syntax:

```
{{API_KEY}}
```

This syntax is used within job configuration, and is replaced with the actual value of the `API_KEY` context key at runtime.

## Accessing event data

As event data flows through different stages of the Job, it is often useful to directly access this data within the Job configuration.

For example, a Job input produced an event like this:

```json
{
  "server": "pri01.domain.com",
  "disk_usage_pc": 23.4,
  "memory_pc": 52.1,
  "cpu_load_5m_pc": 49.05
}
```

Any field value within event data is accessible within actions and outputs. For example, to create a new field named `server_orignal` that contains the value of the `server` field:

1. Configure an add action in the job
2. Add a new field, named `server_original`
3. Use `${server}` as the field value.

The `${server}` will be replaced with the actual value of the `server` field in the event data.

## Accessing Job stats

Job stats are internal statistics and runtime state within a running Job. In some cases, it is useful to access these stats within the Job configuration. These stats can be used to enrich event data, or to make decisions within the Job.

Job stats can be accessed using the following syntax:

```
${stat|STAT_KEY}
```

In which `STAT_KEY` is one of the following values:

:::note
TODO
:::

## Accessing dynamic variables

Job stats are internal data and/or statistics which can be accessed within a running Job.

### Batch number

Within Job outputs, most of which supports output batching, the current batch number can be accessed using the following syntax:

```
${stat|_BATCH_NUMBER}
```

Accessing the batch number is sometimes useful for generating file names or paths in object stores.

Note that the default batch number is always 1.

## Dynamic variables

Dynamic variables are a job feature that supports realtime and blocking configuration changes. Dynamic variables may be set in other Jobs, via messages, and then be accessed in any job configuration using this syntax:

```
${dyn|IDENTIFIER}
```

Where `IDENTIFIER` is the name of a dynamic variable. Note that when a Job attempts to access a dynamic variable which is not set, or otherwise not available, the Job will block (pause) until that dynamic variable is available.

Behind the scenes, the platform's message system is used to propagate dynamic variable changes across all Jobs that use them. This means that dynamic variables are not only realtime, but also distributed across all Workers in the platform.

## Time and date generation

Timestamps and be generated and formatted using the following syntax:

```
`${time|FORMAT_SPECIFIER}`
```

Where `FORMAT_SPECIFIER` is a string that specifies the format of the timestamp. The following format specifiers are supported:

```
${time|now_time_iso}
${time|now_time_secs}
${time|now_time_msecs}
${time|now_time_fmt %Y %m %d}
${time|now_time_fmt %H - 1h}
${time|now_time_fmt %M + 1m}
```
