---
title: "Event Properties vs. Actor Properties"
description: "Definition & use of Event Properties vs. Actor Properties"
---

One of the most common questions asked by users is **what is the difference between event properties and actor properties**? In this article, we aim to provide further insight into both properties as well as the differences between the two.

## Event Properties

An event property can be a reference to data columns, a reference to values derived from lookups, or a logical expression evaluating multiple data columns.

Event properties are critical in organizing and getting specific with your data set. You can add new roll-up columns, create static filter sets, rename columns or values and have them as persistent saved objects, and more. Event properties are solely concerned with events and event meta-data.

- An event property that uses **filter** is an event property with one specified value.
- An event property that uses **label** is an event property with more than one specified value.
- An event property that uses **calculate** is an event property that performs a mathematical function.

For more information and examples of event properties defined with other methods, see [Building an event property](../measure-user-guides/enrich-your-data-with-properties/build-an-event-property.md) in the User's Guide.

## Actor Properties

Actor properties can be created by users to allow the editing and creation of objects related directly to **actors** and the events they perform. Actor properties can be thought of as **segments of users** who do similar behaviors or are in similar demographics.

- An actor property that uses the **show** method aggregates over the events that belong to each actor and produces a value for each actor.

## What is The Difference?

The big difference is **scope**.

The scope of a query refers to the type of entity an aggregation in Measure IQ iterates over to produce a result. An aggregation can iterate over events, actors, or flows. It follows that Measure IQ's three query scopes are called event scope, actor scope, and flow scope.

In general, every Measure IQ query or measure involves some sort of aggregation. Here are some aggregations (with example context) that you can specify in Measure IQ:

- **count unique** users that viewed the support page
- **average** session durations for Android devices
- **sum** play time per music service

We're going to focus on the first two to dig deeper into the differences between event and actor properties.

### Event Scope

**Event** properties are used to filter or calculate on a **per-event basis** over time, meaning they are centered around the actions themselves: **_what_** was done. When you create a query that iterates directly over the events imported to a Measure IQ table or dataset, the query is in **event scope**.

You can visualize the data aggregated over in an event scope query as a spreadsheet or relational database table, **with one row per event**, and each column corresponding to either a raw event property imported directly from the source data, or a manual event property created in Measure IQ.

### Actor Scope

**Actor** properties are used to filter or calculate on a **per-actor basis** over time, meaning they are centered around the Actor: **_who_** did the action. When you create a query that iterates directly over the actors contained within the Measure IQ table or dataset, the query is in **actor scope**.

Unlike in event scope, the actor-based tables that an actor scope query iterates over are not stored on disk or generated during the Measure IQ import process. Instead, Measure IQ produces an actor-based table from a subquery over the event data, and then produces results from the actor-based table.

To learn more about scope and how to resolve scope mismatches, please read our [Understand Scope](../measure-user-guides/queries/understanding-scope.md) article.

### Related

- [Create an Actor Property](../measure-tutorials/create-an-actor-property)
- [Create an Event Property](../measure-tutorials/create-an-event-property)
