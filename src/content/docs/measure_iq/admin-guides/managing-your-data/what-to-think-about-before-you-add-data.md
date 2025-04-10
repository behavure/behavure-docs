---
title: "What to Think About Before You Add Data "
description: "Definition & use of What to Think About Before You Add Data "
---

Measure IQ's most powerful query patterns analyze the behavior of many actors in parallel, connecting multiple events to characterize the actor's behavior over time. Unlike a traditional data warehouse system, Measure IQ computes these per-actor metrics on the fly during the query, allowing an extraordinary degree of interactivity when defining and refining them. This is especially important when the log data is "raw" and likely to be contaminated in ways that are not fully understood up front.

## Events can be related only if they're in the same table

Every event is placed in one or more [event tables (datasets)](/measure_iq/glossary/dataset-table/) in your Measure IQ instance. Each property of the event goes in the table column corresponding to the name of the property. Typically, an event has several columns that describe the event itself, and several that allow it to be placed in the context of other events. For example, an event representing a click on a web page might have properties describing the click target and the state of the user's interaction with the page, plus properties that identify the user account and server-side session that went into creating the web page.

A table may contain events of very different kinds:

- Client and server
- Interactions and batch processes
- Logged "live" and delayed/backdated.

What matters is not the uniformity of the columns on the events, but combining properties of multiple events at query time to understand the behavior of the actors they have in common.

:::tip[Pro Tip]
**Pro Tip:** Focus on the layers of your systhttps://github.com/behavure/behavure-docs/edit/main/src/content/docs/measure_iq/admin-guides/managing-your-data/what-to-think-about-before-you-add-data.mdem from which events can be logged with enough context to relate them to one another.
:::

## Every event must have a time stamp

A [timestamp](/measure_iq/glossary/timestamp/) doesn't always correspond to the exact time that the event is logged. It might be backdated to reflect an estimate of when the event "really happened," or filled in based on data extracted from another source.

When thinking about what timestamp to put on an event, it's a good idea to put it in sequence with related events, and to ensure that this sequence is consistent for each actor, even if the related events are logged by different systems. Events can only be related to one another efficiently if they are nearby in time, and some Measure IQ features are much easier and more efficient to use if the events they relate are reliably in a specific order.

:::tip[Pro Tip]
Favor a consistent ordering of timestamps on related events over absolute accuracy, even to the extent of time-shifting some of them and correcting for this later in the analysis.
:::

## Associate events with actors

Many queries require that an event be associated with an [actor](https://docs.behavure.ai/guides/actor). Depending on the nature of your data and the complexity of your analysis needs, you might have one or more classes of actors whose behavior you are interested in analyzing.

For example, if your data is about user interactions with a website, your actors might be:

- The visitor's browser ID, as stored in a first-party cookie
- The visitor's account ID, for users who log in

## Shard keys - a mechanism to connect events

An actor has a permanent identifier, called a [shard key](https://docs.behavure.ai/guides/shard-key), which is a specific value of a specific shard column. If you want to analyze any relationship between multiple events, those events must have a shard key in common; for example, events resulting from a single user session must all refer to the same shard value.

The data for each shard is processed together on ingestion. Once it's stored in the Measure IQ cluster, it's possible to do actor analysis on the data that is sharded together.

## Permanent properties - augment your data with dimension data

Measure IQ also supports [lookup tables](https://docs.behavure.ai/guides/lookup-table) for permanent properties of an actor, and for mapping values of any column (for example, ZIP code) to properties not logged directly on events (for example, city, state, country).

## Plan your shard keys

An actor has a permanent identifier, called a [shard key](https://docs.behavure.ai/guides/shard-key), which is a specific value of a specific shard column. If you want to analyze any relationship between multiple events, those events must have a shard key in common. A table can have multiple shard columns—at some cost in system resources—but these columns are part of the definition of the table, and changing them is a major administrative operation. Where possible, use multiple shard columns in the same table to associate events with completely different classes of actors, not with different kinds of identifiers for the same actor.

Think carefully about the potential shard keys that occur in your data, especially if an actor may have different identifiers in different layers of your logging architecture (for example, browser session ID vs. user account ID vs. billing account ID). A good rule of thumb is to identify actors by a property that is constant for the duration of one sequence of connected events. For example, if you run an e-commerce site, and you want to analyze a customer acquisition process that starts before the customer has logged into (or even created) a user account, you will need a shard column containing a unique identifier assigned at the beginning of the process. You might also want to analyze sequences of purchases by the same user account, but this analysis will rely on a different shard column, perhaps in a completely different table (which does not need to contain any of the events preceding the login step of each visit to the site).

:::tip
 **Pro Tip:** Remember that the same real-world entity may be known by different IDs in different parts of your system, which are different "actors" for analysis purposes; plan your analysis accordingly.
:::

## Queries look at events within a time window

Every query has a time window, and only looks at the event data for events within (or, in some cases, close to) the time window. An actor might have other permanent properties, but most of the interesting properties of an actor can be extracted from events in or near the query's time window. Event streams that involve long-lived user sessions, or other kinds of event context that isn't always in the immediate time neighborhood, might need to be supplemented with periodic "keep-alive" logging. This can be added to the main log stream or supplied as a separate source of events to be folded into the same table.

Measure IQ also supports [lookup tables](https://docs.behavure.ai/guides/lookup-table) for permanent properties of an actor, and for mapping values of any column (for example, ZIP code) to properties not logged directly on events (for example, country, state, median income). This is analogous to a SQL left outer join. Lookup tables can be useful for anonymizing values of an event column or filling in properties that are not normally accessible from the main logging system; but almost any mutable property of an actor can be more efficiently and accurately captured by applying Measure IQ's "cohort" and "per-actor metric" capabilities to the event table itself.

:::tip[Pro Tip]
**Pro Tip:** Give preference to categorizing actors by their recent behavior—and logging extra events as necessary to provide this context—over static auxiliary lookup tables.
:::

## Identify clusters of related events in as many ways as you can

You may also have smaller clusters of events for which you want to measure a cluster-level property. For example, the delay between delivering a message to a user's inbox and the first time the user opened it for reading, or the number of times that the message was forwarded to other users. This kind of analysis works well when each event cluster is confined to a single shard key and is clearly separated from other clusters with the same shard key, in one of four ways:

- **A gap in time between adjacent clusters of events:** This is one classic definition of a "session" in relatively unstructured log streams, and corresponds to a Measure IQ "session," with new sessions started based on an "idle time" parameter.
- **A specific event that reliably occurs between adjacent clusters of events:** A mobile app might record an event each time the app is started, which implies that the user switched away from the app long enough for it to be stopped by the mobile OS. This is another way of defining a "session," and corresponds to "separator events" in Measure IQ sessions.
- **One or more events within the cluster that occur in a known order**: These begin with a specific "start event" with known properties (for example, an "event_name" column with the value "session_start"). Each occurrence of this event marks the start of a new cluster for the associated shard key. This corresponds to an Measure IQ "funnel," which is one of the more powerful mechanisms in Measure IQ for analyzing relatively structured log streams.
- **A unique identifier for the cluster of events, in a** **_different_** **column from the shard key column:** Each value found in this _colocated column_ should be associated with a single value of the shard key. For example, a "logged-in browser session ID" column could be colocated with a "user account ID" shard key, or an "ad impression ID" column could be colocated with an "app installation ID" shard key. This is particularly useful when several clusters of events for the same shard key may overlap in time—as in the example of a user receiving, opening, and forwarding a specific message, which may be interleaved with activities associated with other messages. Unlike adding a shard column, adding a colocated column is a trivial operation, as long as it's present in your data. Colocated columns can be used together with both sessions and funnels, and a query may compute properties for each value of a colocated column and then summarize them as properties of the actor (shard key) to which they correspond.

Analysis of clustered events can provide great insights into users' and customers' behavior; but it can be a challenge to make this analysis robust against data loss and contamination due to software bugs, data handling errors, and unexpected or even malicious user behavior. Structuring your log data to make effective use of colocated columns may take some effort, but pays off in query speed and confidence in the results.

:::tip[Pro Tip]
**Pro Tip:** Identify clusters of related events in as many ways as possible—grouping in time, separator events, sequences with a known order, and per-cluster identifiers in colocated columns. Then back up your preferred analysis with cross-checks based on alternate clustering criteria.
:::

## Use transformations and derived columns, when necessary

Any column that is defined in an Measure IQ table, but not present on a specific event within the table, is considered to have a null value for that event in that column. Nulls are represented more compactly in Measure IQ than any other value. If a column in your data usually has a particular value (either fixed, or predictable from other properties of the same event), and only occasionally has some other value—for instance, an "affected account ID" that is almost always the same as the event's main account ID, but is occasionally the account of another family member—it might be worthwhile to represent the predictable value with a null, and only record values that differ from the predictable value.

This transformation can be done as data is added to Measure IQ, and undone at query time using a derived column. Derived columns let you compute additional event properties at query time, usually by combining several properties of the raw event. Other common uses for derived columns include arithmetic (for example, divide the total price of a shopping cart's contents by the number of items) and complex filter expressions (for example, exclude events that appear to be fraudulent by at least two out of eight criteria).

:::tip[Pro Tip]
**Pro Tip:** Log events as "raw" as possible. Consider using ingest-time transformations and derived columns to eliminate redundancy, store events more compactly, and postpone complex decisions to query time.
:::

## Build helper columns

There are situations where it may be appropriate to represent one action in the system doing the logging by multiple events in Measure IQ. For instance, if an action is associated with two or more different actors in the same class—perhaps the sender and receiver of a message, both of which are user accounts—and you want to put it in sequence with each, you may need to log several copies of it, each with a different actor ID in the shard column. The copies may also differ in other columns, such as the role of the actor ID in the shard column (for example, "sender" vs. "receiver").

If you do this, then you should have:

- A column containing an "action ID" that is the same for all copies (but different from the IDs of other multiple-event actions), omitted from non-multiple events.
- A column containing the "event multiplicity", the number of events that were logged for this same action, also omitted from non-multiple events.
- Acolumn containing a "duplicate index", which should be null for exactly one event associated with each action (and non-null, possibly an integer, for the others).

These three columns, with the help of derived columns (to synthesize appropriate values for non-multiple events), can be used to build efficient queries that don't over-count actions represented by multiple events.

Depending on the goal of the query, you might count unique action IDs, divide the weight of each event by its multiplicity, or filter out events whose duplicate index is non-null.

The following Pro Tip illustrates a broader principle, worth keeping in mind as you refine your logging strategy:

:::tip[Pro Tip]
**Pro Tip:** It's better to have multiple helper columns, each mostly nulls, than to have one helper column that tries to account for all of the use cases. Columns are cheap as long as they're mostly null, and practically free if they're not used in queries. Think about how each event should contribute to summary statistics, and annotate it in all the ways that might help weight its contribution accurately.
:::
