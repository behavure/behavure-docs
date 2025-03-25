---
title: Config Node 
description: Definition & use of Config Node 
---
The **config node** is in a Measure IQ cluster from which you administer the cluster. MySQL database (DB) is *only* installed on this node for storage of Measure IQ metadata.

The config node is part of the API tier, along with the API node. The config node maintains the cluster configuration in a MySQL database. The largest parts of the database track stored columns, created query building blocks, and dashboard queries. Typical loads on the config node are low, even in large clusters. 

## Related terms

- [API Node](../api-node)