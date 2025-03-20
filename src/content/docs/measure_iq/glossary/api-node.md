---
title: API Node 
description: Definition & use of API Node 
---
The **API node** serves the Scuba application, merges results of queries from data and string nodes, and then presents those results. Nginx is *only* installed on the API node. 

The API node performs a number of tasks, facilitating interactions with users (web server, API endpoint) and planning queries. When query requests arrive, the query planner sequences the work and distributes it among the data and string nodes. It awaits responses, manages multiple scans, and merges results from data and string nodes. Unless the cluster is actively accessed by thousands of users the typical load on the API node is relatively low although, when needed, Scuba can use multiple API nodes. 

## Related terms

- [API](../api)