---
title: Event Property 
description: Definition & use of Event Property 
---
An **event property** produces a single value for each *event*.

An event property can exist in your source data, in which case the UI identifies it as a **raw event property**. Or a user can define a custom event property, in which case the UI identifies it as a **manual event property**. When you define an event property, you must choose a method.

For example, if your log data includes a start and end time, you could define a new event property using the calculate method, named "duration", as \[end time\] minus \[start time\]. You can use "duration" in a more complicated query (in an aggregation, split by, or filter) or to construct another event property. Then the top-level query can compute the duration for any event in your data that has both a start and end time.

#### Related terms

- [Event](../event)
- [Knowledge Object (knob)](../knowledge-object-knob)
- [Method](../method)

#### More information

- [Building an Event Property](https://scuba.atlassian.net/wiki/spaces/SGV/pages/2139260404/Build+an+Event+Property+v5)
- [Create an Event Property](https://scuba.atlassian.net/wiki/spaces/SGV/pages/2139259425/Create+an+Event+Property+v5)