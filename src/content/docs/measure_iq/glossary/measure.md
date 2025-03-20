---
title: Measure 
description: Definition & use of Measure 
---
You can **measure** almost any count or aggregation over a data column, properties that you create, or properties that Scuba creates automatically when you create [knowledge objects (knobs)](../knowledge-object-knob),(specifically [flows](../flow)).

Use the [query builder](../query-builder) to specify a top-level aggregation function using the Measure controls. You can create multiple measures and adjust which one(s) you want to see using [chart options](../chart-options).

Selecting a raw column (or raw event property) in the filter clause causes the column to be scanned and aggregated. A virtual column (user-created property) will be interpreted either during the scan (derived and lookup table columns) or during prior scans (custom metrics). The query planner minimizes the number of required scans and collapses the work as much as possible.

## Related terms

- [Flows](../flow)
- [Knowledge objects (knobs)](../knowledge-object-knob)
- [Metric](../metric)
- [Query Builder](../query-builder)

## More information

- [Analyze user paths with flows](https://scuba.atlassian.net/wiki/spaces/SGV/pages/2139260084/Analyze+User+Paths+With+Flows+v5)