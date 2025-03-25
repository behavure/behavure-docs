---
title: "Time Zones in Measure IQ "
description: "Definition & use of Time Zones in Measure IQ "
---

There are two types of time zones in Measure IQ:

- The data time zone: all data is stored using the Universal Time Zone (UTC)
- The query time zone: this is the time zone of your Measure IQ instance. The default query time zone is either UTC or Pacific Standard Time (PST), but this can be configured to any time zone that you want to use.

Changing the query time zone simply shifts the events as they are displayed in Measure IQ, but doesn't change their original timestamps.

## How does the time zone affect relative time queries?

Relative time queries will be relative to the configured time zone. For example, "yesterday until today" will align to 12:00 AM XXX depending on the configured time zone. Queries using "1 day ago exactly until now" will be exactly 24 hours previous. See [Time query syntax](../../measure-user-guides/queries/time-query-syntax-reference) for more information.

## How can I check which time zone I'm querying in?

Your time zone is displayed in the Explore page and preview panes within data model pages, next to the time fields.

## What happens if I'm in San Francisco and I share a query with my coworker in New York?

You will both see the query in the query time zone (think of this as "HQ Time"). Both users see exactly the same data and time zone.

## What do I do about daylight savings time?

Our customer support team handles this for you. But feel free to [contact us](mailto:help@behavure.ai) if you have any questions or concerns.
