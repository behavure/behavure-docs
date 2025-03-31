---
title: "Adaptive Sampling in Measure IQ "
description: "Definition & use of Adaptive Sampling in Measure IQ "
---
When you run a query that contains a count unique operation, Measure IQ might use an *adaptive sampling* algorithm, when the cardinality of the column is high. The count unique can be a top-level aggregator in the query, or included in the definition of a named expression used in the query. Adaptive sampling allows Measure IQ to return statistically significant results quickly even when processing queries that reference shard keys with a high number of unique values. 

With adaptive sampling, each shard sends a sample of values to the [merge server](../../../../../measure_iq/glossary/merge-server). The merge server aggregates the truncated set of values, which limits the network, memory, and CPU resources required for the computation.

Although there is the risk that this can introduce a small amount of inaccuracy (no more than 1-2%) when computing a count unique on high cardinality columns (columns with a large number of unique values), in practice many of our users do not reach the default sampling limit (8192 unique values per shard), and consider the performance tradeoff worth the minor discrepancy.

## Adaptive sampling and population sampling

The **Fast/Complete** mode dropdown at the bottom left of the Scuba UI determines whether Measure IQ performs *population* sampling, and is independent of adaptive sampling. Measure IQ might use the adaptive sampling algorithm to count unique queries even when running an unsampled query. See [How Measure IQ Performs Data Sampling](../../../measure_iq/key-concepts-and-terminology/how-does-scuba-perform-data-sampling) for detailed information about how Measure IQ performs population sampling.

If Measure IQ did not use adaptive sampling, each shard in your cluster would have to return the entire list of unique values in the shard. Measure IQ would then compute the union of all unique values and perform the count operation. This is a resource-intensive operation: Measure IQ would need to perform operations on each shard, send the (large) results over the network, and then perform the count operation, requiring a large amount of CPU and memory resources on the merge server.
dfdf
## Why are we using this limit?

The sampling strategy that Measure IQ uses is taken from the paper "[On Adaptive Sampling](http://algo.inria.fr/flajolet/Publications/Flajolet90.pdf)" (Flajolet 1990). We determined that this value provides accurate values, within a 1-2% error rate, and that the error rate occurs only with data sets with more than 8192 unique values in the columns being analyzed. Datasets with columns closer to the limit will see discrepancies closer to 1%, whereas datasets with columns significantly above the limit are more likely to see discrepancies closer to 2%.

## When does adaptive sampling kick in?

Adaptive sampling activates when you run a query that either:

- Uses a count unique aggregation on a non-actor column, or
- Uses a count unique aggregation on an actor and also uses a time offset or split by.

For example, if a shard key (actor) is "user," running **count unique user** unsampled does not activate adaptive sampling. However, **count unique user group by platform** unsampled does activate adaptive sampling.

In Measure IQ, adaptive sampling activates for any count unique on a column with a cardinality higher than the limits set on the system. By default, this limit is 8192 for both shard keys and non-shard keys.

## Increasing adaptive sampling limits

In some cases, you may want to increase the adaptive sampling limit. However, increasing the adaptive sampling limits can significantly affect system performance. You might need to increase the size of your Scuba cluster to preserve query performance. Before requesting to increase the limits, talk to your Measure IQ contact(s) about potential performance/infrastructure impacts.