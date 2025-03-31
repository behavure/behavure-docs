---
title: Shard
description: Definition & use of Shard
---

A **shard** is a partition in a database table. Small data shards in a database table effectively allow for faster accessibility and management of the information.

Horizontal partitioning is a design principle whereby rows of a database table are held separately, rather than split by columns (as for normalization). Each partition forms part of a shard, which may in turn be located on a separate database server or physical location. The advantage is that the number of rows in each table is reduced, which in turn reduces the index size and improves search performance.

If the sharding is based on data where it's possible to infer the appropriate shard membership, such as European customers vs. American customers, then it is possible to only query the relevant shard. Measure IQ assigns each [actor](../actor) to a shard.

## Related terms

- [Actor](../actor)
- [Denormalized Data](../denormalized-data)
- [Event](../event)
- [Shard Key](../shard-key-colocated-shard-key)

## More information

- [Best Practices for Formatting Data for Ingest](/measure_iq/admin-guides/managing-your-data/best-practices-for-formatting-data-for-ingest)
- [What You Should Know About Structuring Your Data](/measure_iq/admin-guides/managing-your-data/what-you-should-know-about-structuring-your-data)
