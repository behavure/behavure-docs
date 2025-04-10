---
title: "Time Query Syntax Reference "
description: "Definition & use of Time Query Syntax Reference "
---

When working in the Measure IQ Explorer and dashboard view, you can select a time range for your query. Measure IQ supports both literal time values and relative time values. This document provides context about time ranges, timezones, and natural language we support for relative times.

The examples below are provided for a user whose timezone is PST.

![](/measure_iq/measure-user-guides/queries/attachments/relative%20date.png)

Times are displayed in 24-hour format to be unambiguous.

> [!INFO]
> Measure IQ does not support dates prior to January 1, 1970 (the beginning of [Unix epoch time](https://en.wikipedia.org/wiki/Unix_time)).

## Specific dates and times

You can specify query time boundaries using exact dates, exact times, or combinations of date and time.

You have two options for entering dates into the query builder or board filters: The date picker or manually.

### Using the date picker:

![](/measure_iq/measure-user-guides/queries/attachments/date%20picker.png)

Click the calendar next to 'Starting' and 'Ending' to fill in the time range of your query. The date picker allows you to set year, month, day, hour, minute, and second specifics to your dates.

### Manually entering dates/times:

### Dates

You can type in a date using the YYYY-MM-DD. If you do not specify a time component, Measure IQ uses midnight, or the zeroth millisecond of the specified calendar date.

![](/measure_iq/measure-user-guides/queries/attachments/date-type%20in.png)

### Times

You can specify times up to second precision using the format HH:MM. However, the hour and minute components are optional. Measure IQ currently supports 24-hour formats for uniformity.

## Relative time syntax

![](/measure_iq/measure-user-guides/queries/attachments/relative%20date_time_article.png)

Measure IQ also supports relative time syntax. These terms are "sticky," meaning that a query using them will roll forward in real time (versus a query based on literal time values whose results will not change with the passage of time).

The general format for this type of input is "<number> <unit> ago"

For example: `7 days ago`

### Supported numbers

Numbers can be integers or decimals. Measure IQ ignores the sign of numbers used this way.

Use the numeric form and not the spelled-out form of the number. For example, you can use `7 days ago` but not `seven days ago`.

### Supported units

Measure IQ supports the following units of time:

- second(s)
- minute(s)
- hour(s)
- day(s)

The following units align to calendar days, meaning that the time component is set to midnight in the user's timezone:

- week(s)
- year(s)

We support both precise and calendar-aligned relative time:

| **Precise** | **Start-of-Day Aligned (12:00:00 AM**) |
| ----------- | -------------------------------------- |
| now         | today                                  |
| 1 day ago   | yesterday                              |
| 1 week ago  | last week                              |
| 10 days ago | last 10 days                           |
| 1 month ago | last month                             |
| 1 year ago  | last year                              |

> [!INFO]
> A "month" is defined as 30 days. Months are not calendar-aligned.
> Avoid cross-referencing across these columns (for example, don't use "yesterday" to "now"). This will produce time ranges that are +/- hours on either side which is unexpected behavior for most users.

| Input                                                                          | Result for a user in PST (GMT-0800) on 01/01/2015 at 1:15 PM | Notes                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 hour ago                                                                     | Jan 1 2015 **12:15:00** GMT-0800 (PST)                       | Exactly 1 hour ago in the user's timezone                                                                                                                                                                                                                    |
| 1 day ago<br><br>24 hours ago<br><br>1440 minutes ago<br><br>86400 seconds ago | Dec 31 2014 **13:15:00** GMT-0800 (PST)                      | 1 day ago aligned to the current time in the user's timezone                                                                                                                                                                                                 |
| last week                                                                      | Dec 25 2014 **00:00:00** GMT-0800 (PST)                      | Exactly one week before the current time, aligned to the calendar day in the user's timezone.                                                                                                                                                                |
| 7 days ago                                                                     | Dec 25 2014 **13:15:00** GMT-0800 (PST)                      | Exactly 7 days ago aligned to the current time in the user's timezone.                                                                                                                                                                                       |
| last 7 days                                                                    | Dec 25 2014 **00:00:00** GMT-0800 (PST)                      | One week ago, aligned to the start of the calendar day in the user's timezone.                                                                                                                                                                               |
| 1 week ago                                                                     | Dec 25 2014 **13:15:00** GMT-0800 (PST)                      | This works for the time **Start** value and when comparing time periods. This is the default value for time comparisons.<br><br>If you set the Time Window and Resolution of a query to 1 week, `1 week ago` will end at the next Sunday in the time period. |
| one week ago                                                                   | _error_                                                      | Not supported.                                                                                                                                                                                                                                               |
| 1 week ago 5pm                                                                 | _error_                                                      | Not supported.                                                                                                                                                                                                                                               |

**For time ranges of one day or greater**:

- `Ago` will reference the exact time. For example, if the current time is 3:15 PM on July 10, `1 day ago` will result in 3:15 PM July 9.

### Today, yesterday, and now

Measure IQ also supports the `today`, `yesterday`, and `now` keywords. Note that `today` and `yesterday` align to calendar days, and `now` uses the current time in the user's timezone.

| Input     | Result for a user in PST (GMT-0800) on 01/01/2015 at 1:15 PM | Notes                                             |
| --------- | ------------------------------------------------------------ | ------------------------------------------------- |
| now       | Jan 01 2015 **13:15:00** GMT-0800 (PST)                      | The current date and time in the user's timezone. |
| today     | Jan 01 2015 **00:00:00** GMT-0800 (PST)                      | The start of today in the user's timezone.        |
| yesterday | Dec 31 2014 **00:00:00** GMT-0800 (PST)                      | The start of yesterday in the user's timezone.    |
| today 3pm | _error_                                                      | Not supported.                                    |

## Automatic calendar alignment for queries

As of version 2.19, when a query's resolution is greater than one day, the last day of a 1-week, 2-week, 4-week, 13-week, or 52-week time bucket will now end on the day that contains the end time of the query. For example, if the query end time is January 20, 2016 at 2 pm, the weekly time bucket will end on January 21, 2016 at 12 am for this query, including all of its subqueries.

If your Measure IQ instance is configured to use a specific day as the first day of the week, Measure IQ will not perform this automatic calendar alignment. The instance configuration setting takes precedence over the automatic alignment. For example, if your instance is configured to use Monday as the beginning of the week, weeks will always be aligned to run from Monday to Monday.
If your Measure IQ instance is configured to use a specific day as the first day of the week, Measure IQ will not perform this automatic calendar alignment. The instance configuration setting takes precedence over the automatic alignment. For example, if your instance is configured to use Monday as the beginning of the week, weeks will always be aligned to run from Monday to Monday.
