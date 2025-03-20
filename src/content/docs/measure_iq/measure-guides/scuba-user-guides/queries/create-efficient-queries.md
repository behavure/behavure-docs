---
title: "Create Efficient Queries "
description: "Definition & use of Create Efficient Queries "
---
You can use various components to build a Scuba query, such as [knowledge objects](https://scuba.atlassian.net/wiki/spaces/GLOSSARY/pages/2160231434/Knowledge+Object+knob+v5). The types and number of components you use to structure a query can affect how quickly you receive the results. This topic provides general guidelines for creating efficient queries that optimize performance. 

## General guidelines for efficient queries 

Follow these basic guidelines for optimum query performance: 

- Run sampled queries whenever possible (that is, unless you are querying over a small number of actors or an otherwise abnormal distribution of data). Unsampled queries always take longer than sampled queries due to the amount of data that must be scanned. 
- Use the minimum number of measures.
- Use the minimum number of filters possible. The more filters there are in a query, the longer it takes, due to the number of computations that must be performed.
- Minimize the number of referenced columns. The more columns that are referenced, the slower the query is, due to the amount of data that must be scanned.
- Minimize query date ranges. The longer the query date ranges are, the slower the query is, due to the amount of data that must be scanned.
- If you use a **Split By**, in general, you can expect slower results. If you use multiple **Split By**, query performance will be even slower due to the added results that must be returned. 
- Minimize the number of properties, measures, and segments in queries. Each of these objects requires individual computations, so the more you use in a query the slower the response time is.
- A "starts with", "contains", or regular expression operator takes up more resources—resulting in a slower response time—than a "matches" or "is empty" filter.
- Table View queries are more efficient than Time View queries, because a Time View query requires computations for every point on the graph and a Table View query only requires one computation.
- Queries involving sets contain more data and therefore have a slower response time than queries that don't contain sets.
- The more data you have, the slower your query response is, due to the amount of data that must be scanned.

## Cluster maintenance tips 

Use the following basic guidelines for optimum query performance:

- Delete dashboards that are not being used.
- Moderate the number of external API queries that are running while UI queries are running. The more external API queries that are running, the slower the UI queries will be.
- Delete unused columns in your data.
- If you run queries during a high import volume, your query response will be slower due to the resources being consumed on the data and string tiers.

## Simpler is usually faster 

In most cases when building queries, the simpler the construction, the more efficient the query, due to fewer necessary computations. This is especially true when query segments and measures contain filters. The computations required for segments and measures slow query response time, and are often used when a simple filter would suffice.