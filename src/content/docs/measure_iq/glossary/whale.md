---
title: Whale
description: Definition & use of Whale
---

A **whale** is an actor that creates a disproportionate number of events in relation to the other actors. A whale actor can be any of the following:

- Real actor: Users who are an order of magnitude more active than most.
- System actor: Services, notifications, and other automated events.
- Bot: A utility that automatically generates events.

The imbalance that a whale creates can cause sampling errors, especially if the whale happens to be picked as a sampling shard. For unsampled queries, the whale shard impedes performance. If the whale continues to expand unchecked, the node runs out of disk space much faster than the other nodes in the cluster.

Measure IQ dissipates the data of actors who are detected to be whales across all the other shards on the node. In effect, this *splashes* the actors across the other shards on the node. The act of *splashing* balances the distribution of data to ensure efficient sampling.

## Related terms

- [Actor](../actor)
- [Query](../query)
- [Sampling](../sampling)

## More information

- [Balance Data for Efficient Sampling](/measure_iq/key-concepts-and-terminology/how-does-measure-iq-perform-data-sampling)
- [How Measure IQ Performs Data Sampling](/measure_iq/key-concepts-and-terminology/how-does-measure-iq-perform-data-sampling)
