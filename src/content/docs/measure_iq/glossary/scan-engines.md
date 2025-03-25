---
title: Scan Engines 
description: Definition & use of Scan Engines 
---
**Scan engines** are the Measure IQ processes that analyze streams of data during scans. Scan engines come in two flavors: *aggregation* and *annotation*.

- Aggregation engines apply a function that results in a single value.
- Annotating engines result in an array of values where every array row is associated with a row of data in the analyzed time interval.

These annotations can be treated as virtual columns that enrich the recorded **event data** and either contain the desired query results or are used as input for further passes over the data.

## Related terms

- [Event Data](../event-data)