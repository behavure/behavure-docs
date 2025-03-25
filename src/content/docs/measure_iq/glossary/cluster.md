---
title: Cluster
description: Definition & use of Cluster
---

A **cluster** consists of a set of connected systems (nodes) that work together, and in many ways can be viewed as a single system. The nodes of a cluster are usually connected through local area networks, with each node running its own instance of the same operating system.

A Measure IQ cluster consists of the following nodes that can be deployed on a single machine (as a single-node cluster) or multiple machines (as a multi-node cluster):

- [Config Node](../config-node): Maintains the cluster configuration in a MySQL database. Loads on this node are typically low. This node is configured first. The config and API nodes make up the application tier.
- [API Node](../api-node): Serves the Measure IQ application, receives query requests from the user, distributes queries to the data and string nodes, then merges the results and presents those results to the user. Nginx is installed only on the API node.
- [Data Node](../data-node): Data nodes do most of the work in a Measure IQ cluster. These nodes must have enough storage, CPU, and memory to store all events, scan the events quickly, hold state while scanning, and stream simultaneous query results, in addition to receiving data from the ingest tier. The data and string nodes make up the query and storage tier, which is sometimes referred to as the data tier.
- [String Node](../string-node): String storage for the active strings in the dataset, stored in compressed format. Requires sufficient memory to hold the working set of strings accessed during queries.
- [Import Node](../import-node): Connects to data repositories (S3, Azure, local file system), downloads new files, processes the data, and then sends it to the data and string tiers, as appropriate. The ingest tier is made up of one or more import nodes.
- Push Node: Used as an access point to a multi-node cluster for maintenance activities.
- Listener Node: Streams live data from the web or cloud. Also known as streaming ingest. This node is optional during installation.

## Related terms

- [Node](../node)

## More information

- [Measure IQ Admin Guide](https://behavure.ai/docs/wiki/spaces/SGV/pages/2139261269/Admin+Guides+v5)
