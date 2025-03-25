---
title: Shard Key, Colocated Shard Key
description: Definition & use of Shard Key, Colocated Shard Key
---

A **shard key** is a column in your dataset that represents the [actors](../actor) that performed the actions in your event data. This is the technical implementation that allows Measure IQ to determine your actors. An actor can be a user, device, or other action-performing entity that you'll use to construct queries.

**Colocated shard keys** are an alternative to creating new dataset copies when adding shard keys. When you want to establish a new shard key, you usually need to create a new dataset copy. Because each new dataset copy creates a complete copy of the underlying dataset, this linearly increases the storage required in your cluster. Colocated *columns* allow you to avoid creating new dataset copies when adding shard keys, if the shard key fulfills certain criteria.

If the shard key you want to add has a one-to-one or many-to-one relationship with an existing shard key, you can create a colocated column instead of creating a new copy of your dataset. The important point is that each instance of the new shard key must map to exactly one instance of an existing shard key.

## Related terms

- [Actor](../actor)
- [Event Data](../event-data)
- [Knowledge Object (knob)](../knowledge-object-knob)

## More information

- [What You Should Know About Structuring Your Data](https://behavure.ai/docs/wiki/spaces/CSSD/pages/1302431464/What+you+should+know+about+structuring+your+data)
- [What to Think About Before You Add Data](https://behavure.ai/docs/wiki/spaces/CSSD/pages/1561821201/What+to+think+about+before+you+add+data)
