---
title: Actor Property 
description: Definition & use of Actor Property 
---
An **Actor Property** is a user-created object that produces a single value or set for each actor. For example, you can create an actor property that counts the number of times a user performed a specific action. You can then use this actor property in another query to aggregate, group, or filter. For example, the top-level query can compute the 90th percentile of users based on the number of searches.

When you create an actor property, you must select a method. An actor property that uses the show method aggregates over the events that belong to each actor and produces a value for each actor. Use the show method to create attributes for actors based on their behavior.

An actor property that uses label, calculate, or filter performs comparisons or arithmetic with other actor properties and literal values.

- Use filter or label to segment actors based on attributes. (Use filter if you have no more than two segments to define; use label to define more segments.) 
- To create KPIs for segments, use calculate.

For example, to count the number of times a user searched, create an actor property using the show method. On the other hand, to create a segment of users that have ever searched, create an actor property using the filter method.

## Related terms

- [Actor](../actor)
- [Event Property](../event-property)
- [Method](../method)
- [Segment](../segment)

## More information

- [Create an Actor Property](https://behavure.ai/docs/wiki/spaces/SGV/pages/2139259462/Create+an+Actor+Property+v5)
- [Calculate DAU and MAU](https://behavure.ai/docs/wiki/spaces/SGV/pages/2139260423/Calculate+DAU+and+MAU+v5)