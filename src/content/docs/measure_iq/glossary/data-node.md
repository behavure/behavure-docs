---
title: Data Node 
description: Definition & use of Data Node 
---
A **data node** in a Measure IQ cluster is where your data is stored. Data nodes do most of the querying work and are scaled out to accommodate the event volume and number of simultaneous query requests.

Each data node needs to have sufficient storage to hold all its events and be able to scan them quickly during queries. A data node also needs to have sufficient CPU cycles to run the scan engines and enough memory to hold aggregated state while the scan engines are working. 

The data and string nodes make up the query and storage tier, which are often referred to as the [data tier](../data-tier) and [string](../string-node) tier respectively.

## Related terms

- [Cluster](../cluster)
- [String Node](../string-node)