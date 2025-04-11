---
title: "Building Blocks"
description: "Foundational concepts for understanding and using Measure IQ"
---

This article introduces the conceptual building blocks and basic queries that provide a foundation for creating and analyzing queries in the Measure IQ UI.

Before you jump into using Measure IQ, familiarize yourself with the following:

- [Events](#events)
- [Actors](#actors)
- [Flows](#flows)
- [Time](#time)
- [Basic queries](#basic)

## Events

An event is something that happens at a specific time. In Measure IQ, an event consists of an **actor**, an **action**, and the **time** that the action occurred.

**You can associate properties with events**, depending on the type of action. Properties can act as filters or perform functions, depending on the purpose of the query. Measure IQ has pre-configured event properties you can use, or you can create your own custom properties. Creating a property is similar to creating a formula-based column in Excel. For more information, see [Create an Event Property](/measure_iq/measure-tutorials/create-an-event-property).

**You can create aggregations of events**, choosing the event property you want to aggregate, and then the operator. This is similar to how you'd create a formula-based summary row in Excel. You can create event aggregations directly as a query in the Explorer, in the inspector or as part of a custom actor property or custom flow property.

## Actors

An actor is the person, utility, or bot that generates an event. Measure IQ stores events separately for each actor. This means you can construct queries that perform simple aggregations of event properties for each actor, much like a pivot table in Excel. Such as, a pivot table that calculates a few sums, plus a maximum, over all the events, then groups those results by user. These aggregations are defined as a custom actor property.

In addition to custom actor properties that do _aggregations of events_, you can build custom actor properties that run a _formula_ against other custom actor properties for the same actor. For more information, see [Create an Actor Property](/measure_iq/measure-tutorials/create-an-actor-property).

## Flows

A flow is a visual representation of a path of actions an actor takes, an intuitive graph plotting the actor's journey. You can view the paths of all actors simultaneously, and then take a sequence of events by a particular [actor](/measure_iq/glossary/journey-actor-user) to analyze with finer granularity.

Among their many uses, flows provide the ability to analyze actor engagement, conversion, and path discovery. For more information, see [Create a Flow](/measure_iq/measure-user-guides/analyze-user-paths-with-flows/create-a-flow) and [Create a Flow Property](/measure_iq/measure-user-guides/analyze-user-paths-with-flows/create-a-flow-property).

## Time

When you construct a query, you specify the time over which the query scans for results by choosing from intuitive intervals or entering custom values. You can specify non-uniform intervals, such as month and calendar quarter, as well as uniform intervals such as seconds, minutes, hours, days, and years. You can select either exact dates or relative time. For more information, see [Specify Time in a Query](/measure_iq/measure-user-guides/build-queries-and-visualizations/specify-time-in-a-query).

## Basic queries

The following are examples of queries that provide information important to most businesses. You can create these queries while getting oriented with Measure IQ without having to build custom objects. For step-by-step instructions for creating these queries, see [Build queries and visualizations](/measure_iq/measure-user-guides/build-queries-and-visualizations) in the User's Guide.

- [Show count of events](#count-events)
- [Show count of actors](#count-actors)
- [Show count unique split by action](#count-unique-action)
- [Show count unique split by two categories](#count-unique-split)

##### Show count of events

![](./attachments/count%20of%20events.png)

See [Show a count of events](/measure_iq/measure-user-guides/build-queries-and-visualizations/show-a-count-of-events) for more information.

##### Show count of actors

![](./attachments/count%20of%20actors.png)

See [Show a count of actors](/measure_iq/measure-user-guides/build-queries-and-visualizations/show-a-count-of-actors) for more information.

##### Show count unique split by action

![](./attachments/actors%20by%20action.png)

##### Show count unique split by two categories

![](./attachments/cont%20unique%20split%20by%202.png)

## What's Next

- [Measures](/measure_iq/measure-user-guides/learn-about-measure-iq-concepts/using-measures-in-measure-iq)
- [Manage Objects and Concepts](/measure_iq/measure-tutorials/manage-objects-and-queries)
- [Roadmap for Measure IQ](/measure_iq/measure-user-guides/learn-about-measure-iq-concepts/roadmap-for-using-measure-iq)
- [Tutorials](/measure_iq/measure-tutorials)
