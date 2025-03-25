---
title: Flow Property 
description: Definition & use of Flow Property 
---
A **flow property** is a user-created *object* associated with a *flow*.

For example, you could define a flow property that counts the number of errors users encounter during a sequence of actions. Then you can use this property to compute the number of errors.

When you create a flow property, you select a *method*. We can think about two types of methods:

- A flow property that uses the *show* method aggregates over the events that belong to each flow instance and produces a single value for each flow instance. When you create a flow property using the show method, you can choose objects that are tied to the events (that is, event properties, actor properties, and flow properties).
- A flow property that uses label, filter, calculate, or flow time performs comparisons or arithmetic with other flow properties, actor properties, and/or literal values. These also produce a single value for each flow instance. You can create a label, filter, calculate, or flow time flow property using objects related to your flow, and you can access actor properties, but you can't access event properties.

### Related terms

- [Actor Property](../actor-property)
- [Flow](../flow)
- [Flow Instance](../flow-instance)
- [Knowledge Object (knob)](../knowledge-object-knob)
- [Method](../method)
- [Show](../show-actor-flow-property)

### More information

- [Create a Flow Property](https://behavure.ai/docs/wiki/spaces/SGV/pages/2139259375/Create+a+Flow+Property+v5)