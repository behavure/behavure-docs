---
title: Aggregation Engine 
description: Definition & use of Aggregation Engine 
---
The **Aggregation Engine** combines streams of data into a single value using the selected aggregation function. Built-in aggregation functions include options like count, sum, mean, median, percentile, first/last values, min/max, etc.

You can also define your own custom metrics using our visual UI and use them as the aggregation function. The engine takes time range, aggregation function, compare groups, and filter conditions as inputs. It figures out which columns to scan based on the stored and virtual columns used in the query.

The aggregation engine is also an important part of other more complex queries. It's usually the engine that runs last and aggregates values from the physical and virtual columns generated earlier to deliver the requested results.

## Related terms

- [Annotation Engine](../annotation-engine)
- [Knowledge Object (knob)](../knowledge-object-knob)
- [Lookup Table](../lookup-table)
- [Scan Engines](../scan-engines)

## More information

- [Admin Guide](https://scuba.atlassian.net/wiki/spaces/SGV/pages/2139261269/Admin+Guides+v5)