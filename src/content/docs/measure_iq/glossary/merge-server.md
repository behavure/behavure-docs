---
title: Merge Server 
description: Definition & use of Merge Server 
---
**Merge server** is the process that combines results from individual data nodes.

Each data node is responsible for a subset of actors. The query planner determines what information needs to get collected and in which order. It then executes the plan by asking the data nodes to do the scanning and analysis. Data nodes all run the required scan engine in parallel to scan and analyze data for the actors they hold. They then forward the results back to the merge server, which combines all the results from the individual nodes.

## Related terms

- [Adaptive Sampling](https://scuba.atlassian.net/wiki/spaces/SGV/pages/2139260766/Adaptive+Sampling+in+Scuba+v5)
- [Shard Key](../shard-key-colocated-shard-key)