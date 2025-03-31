---
title: String Node
description: Definition & use of String Node
---

A **string node** is used to store active strings and requires sufficient memory to hold the working set of strings accessed during queries. Strings are stored in a [deduplicated](../deduplication-dedupe) and compressed format, taking up relatively little space on disk. The steady-state computational load on the string nodes is relatively low, but they must have sufficient memory to hold the working set of strings accessed during queries.

String nodes replicate their strings to a partner node for resiliency. In production, it is recommended that you deploy a prime number of string nodes (1, 3, or 5), each with sufficient memory for the number of active strings it will manage.

## Related terms

- [Cluster](../cluster)
- [Data Node](../data-node)
- [Node](../node)

## More information

- [Planning Your Measure IQ Deployment](/measure_iq/admin-guides/planning-your-measure-iq-deployment)
