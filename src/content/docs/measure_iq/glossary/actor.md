---
title: Actor 
description: Definition & use of Actor 
---
An **actor** is any person or thing that generates or participates in an [event](../event). Actors on digital services may be people who access your service directly, and are often thought of as "users" or "people." However, you might have more than one kind of "person," or actor. For example, when a rider (actor) hails a ride with a driver (another actor) in a ridesharing service. Actors can also be real or virtual things. For example, different devices, topics, accounts, or even “bots”, which can also be thought to “behave,” and about whom you may have the same kinds of behavioral questions that you have about people. For these reasons, Scuba does not equate "behavior" with "user behavior."

Actor columns are identified at ingest time by explicitly making them [shard keys](../shard-key-colocated-shard-key). When an event source has multiple actor populations, such as the rider/driver scenario above, we implement them through multiple shard keys in the same [event table (dataset)](../dataset-table).

The series of events associated with a given actor is considered their [journey](../journey-actor-user). The patterns found in and across actors' journeys are what we refer to as [behavior](../behavior), such as progress through [funnels](../funnel). Behavioral knowledge objects like funnels, [sessions](../session), [cohorts](../cohort), and [actor metrics](../per-actor-metric) depend on actors being ingested as shard keys, which is why it is important to identify the actors required to support your critical analyses before ingesting data.

## Related terms

- [Behavior](../behavior)
- [Event](../event)
- [Shard Key](../shard-key-colocated-shard-key)