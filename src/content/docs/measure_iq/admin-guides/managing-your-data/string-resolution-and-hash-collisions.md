---
title: "String Resolution and Hash Collisions "
description: "Definition & use of String Resolution and Hash Collisions "
---

If a user has encountered this error, some string values in the query are being misreported. This error will only come up in queries run across multiple clusters.

The only way to resolve a string hash collision is for the user to go to each individual cluster and run the query in single cluster mode. This will provide the user with the correct data.

### Multi-Cluster and Privacy

Our multi-cluster architecture was designed around privacy. Users are allowed to access the most information possible within the constraints set by their administrator. For string fields, this means we've built our system using **hashes**, a computer science technique that gives individual strings an ID. These IDs can then be passed around freely, since they can't be converted back to the original strings. This allows us to do things like count unique string values across clusters _without sharing the strings directly_.

### Hash Collision

While statistically unlikely, it is possible for two string hashes to resolve to the same ID, which is known as a **hash collision**. If you've come to this page via an error message in the system, that's what happened.

There are a few ways these strings could be affected, but the two most likely scenarios are as follows:

- Two different string values hashed to the same ID would cause the count of their results to be _combined_
- The same string value on different clusters hashed to different IDs would mean the results were _not combined as they should be_. They would either show up as different entries or one cluster's results would be left out.

If the information isn't restricted due to column protection, the error message will tell you what string values were affected.

### Summary

With the shift toward better and stronger data privacy protections, our multi-cluster environment provides Measure IQ users the ability to query on data without violating any rules and regulations.
