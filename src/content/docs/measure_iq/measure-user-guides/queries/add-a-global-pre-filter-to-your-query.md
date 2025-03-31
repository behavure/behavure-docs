---
title: "Add a global pre-filter to your query"
description: "Definition & use of Add a global pre-filter to your query"
---

When building queries in Measure IQ, you may find that some data is less useful to you. To simplify query building, you can "pre-filter" this data out, or pre-filter _only_ to the events you care about, before any other calculations are performed. For example, you might have backend events with names that mirror frontend events, or device heartbeat data that you don't care about.

A pre-filter differs from a measure filter in that a pre-filter completely discards events that don't match the filter, while a measure filter considers events that match the filter but still performs calculations on all events.

From the query exploration pane, click the arrow next to **For** to expand the section. Select a property and its value(s).

![](<attachments/2023-05-24_12-15-43%20(1).webp>)

#### What's the difference between a pre-filter and a measure filter?

Let's say you want to create a table that shows the number of confirmed purchases with at least one item, split by the number of confirmed purchases per user.

To achieve this, you can use the filter `IS_NOT_EMPTY(item)` and the actor property `purchase_confirmed` (which represents the count of purchase events per user).

Now, you have the option to either put the `IS_NOT_EMPTY(item)` filter into the "count events" measure or use it as a pre-filter.

Both approaches would show a count of events, use the `IS_NOT_EMPTY(item)` filter, and split the data by `purchase_confirmed`. However, the results would differ.

#### **Why?**

When using a pre-filter, events that don't match `IS_NOT_EMPTY(item)` are completely discarded. As a result, when you count `purchase_confirmed` events per user, there are no events left because they don't have a value for item and are not queryable.

On the other hand, when you add a filter in the measure, events that have a value for item are considered. The query engine looks at the associated user, counts how many events that user has that match `purchase_confirmed`, and splits the data accordingly. Even though some `purchase_confirmed` events may not pass the item filter, they are still available for aggregation.

Here's how the query engine proceeds with each filtering method:

_Using a pre-filter in the query exploration pane_

1. Remove all events without a value for item.
2. Count how many `purchase_confirmed` events each user has in the filtered dataset. Since no `purchase_confirmed` events have a value for item (as they were removed), the count is 0.
3. Split the data by the unique values produced in step 2. Since the count is 0 for each purchase event, there is only one row (with a count of 0) in the returned table chart.

_Using a measure filter_

1. Look at every event that has a value for `item`.
2. Count how many `purchase_confirmed` events each associated user has.
3. Since the dataset itself isn't filtered, all of the `purchase_confirmed` events are still countable, and returns results.
4. Split the data by unique values produced in step 2. Since each user with `purchase_confirmed` events also has `item` events, we would see multiple rows in our returned table chart.

The crucial difference is that with the filter in the measure, all events are still available for aggregation and querying. However, with a pre-filter in the query exploration pane, it's as if those events don't exist at all.

#### Default pre-filters and board filters are important aspects to consider when working with Measure IQ

If you notice a pre-filter already applied to your query, it means that your admin has set a default pre-filter. This default pre-filter is automatically applied to all queries, excluding boards and the flow builder.

To remove a default pre-filter, simply click on the adjacent trash icon. If you want to reapply a default pre-filter, click "Clear all" in the query builder.

Additionally, a board can provide a pre-filter to queries that are pinned to it. If you want to remove a board filter from your query, you can open the query in Explore. See [Save variants of a board with board filters](/wiki/pages/createpage.action?spaceKey=SGV&title=v5%20Measure IQ%20Save%20variant%20of%20a%20board%20with%20board%20filters&linkCreation=true&fromPageId=2139260782) for more information.

> [!INFO]
> Keep in mind: Even when a pre-filter is applied, Measure IQ still scans all events initially. This means that the performance improvement from using a pre-filter might not be significant, depending on your query definition.

Use caution when applying pre-filters, as using them incorrectly can impact your query results. Since a pre-filter causes the query engine to completely ignore events that don't match your filter(s), there may be certain circumstances where this leads to different results than intended.
