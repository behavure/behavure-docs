---
title: Flow 
description: Definition & use of Flow 
---
A **flow** is an object that a user can define to explore patterns of behavior or sequences of events.

A flow expresses a sequence of statements or conditions that Scuba uses to identify users that engaged in actions that match the defined sequence. The flow definition includes one or more start conditions, one or more steps, transition rules between the steps, and an end.

In Scuba, the default visualization for a flow is a Sankey Diagram. This visualizes the flow instances transitioning between steps in the flow.

Use a flow to define a sequence of milestones over a window of time for a particular actor. Then you can examine events between any of those milestones using the built-in event path capability. You can use the flow definition in a query to aggregate, filter, or group by properties of the flow.

You can segment a flow using a *flow property*. You can also use a flow to segment the actors associated with the flow. For example, users that did not reach the "checkout" step. You can filter events using a flow.

Sessions and funnels, from earlier versions of Scuba, were folded into Flows with additional functionality. 

## Related terms

- [Actor](../actor)
- [Flow Instance](../flow-instance)
- [Flow Property](../flow-property)
- [Journey](../journey-actor-user)
- [Sankey Diagram](../sankey-view-diagram)

## More information

- [Create a Flow](https://scuba.atlassian.net/wiki/spaces/SGV/pages/2139259296/Create+a+Flow+v5) 
- [Analyze User Paths with Flows](https://scuba.atlassian.net/wiki/spaces/SGV/pages/2139260084/Analyze+User+Paths+With+Flows+v5)
- [Understand Flow Definition Conditions](https://scuba.atlassian.net/wiki/spaces/SGV/pages/2139260124/Understand+Flow+Definition+Conditions+v5)