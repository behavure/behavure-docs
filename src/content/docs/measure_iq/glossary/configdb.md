---
title: ConfigDB 
description: Definition & use of ConfigDB 
---
The **ConfigDB** is a MySQL database (DB) that lives on the [config node](../config-node). This database stores metadata used by the Measure IQ application. For example, it stores information about users, user-created objects, datasets, dashboard queries, and application settings. The ConfigDB *only* stores metadata, so it stays very small, even when the cluster stores a lot of data. 

## Related terms

- [Columnar database](../columnar-database)
- [Data store](../data-store)