---
title: Method 
description: Definition & use of Method 
---
When you create an actor property, event property, or flow property in Measure IQ, you are presented with some or all of the following **methods**. The definitions of the methods are as follows:

- **Show**: Aggregate across events or flows to calculate some value per actor or per flow. This is only available for actor and flow properties.
- **Filter**: Create a Boolean segment. For example, an "Is Registered" actor property, a "Did Reach Shopping Cart" flow property, or an "Is Product Info Page" event property. When analyzing Boolean properties, you can compare segments that are both in or out of the segment.
- **Label**: Similar to the filter method, but the segment is based on a multi-valued filter. For example:
-   Segment actors into Power Users, Core Users, Light Users;
-   Segment events into "Is Chrome", "Is Safari", and "Is Other" event properties;
-   Or segment flows into "Reached Step 1", "Reached Step 2", and "Reached Step 3".
- **Calculate**: Perform any mathematical operation or function on other existing properties. For example:
-   A ratio like (Number of App Opens) / (Number of Rides) = (App Opens per Ride);
-   Or a function like ROUND(\[App Opens\], -1).
- **Flow time**: Create a time-based flow property based on the time spent in the flow or between steps within the flow. (For example, time between Add to Cart and Purchase.) This is only available in flow properties.

## Related terms

- [Actor Property](../actor-property)
- [Event Property](../event-property)
- [Flow Property](../../../glossary/flow-property)

## For more information

- [Create an Actor Property](https://behavure.ai/docs/wiki/spaces/SGV/pages/2139259462/Create+an+Actor+Property+v5)
- [Create an Event Property](https://behavure.ai/docs/wiki/spaces/SGV/pages/2139259425/Create+an+Event+Property+v5)
- [Create a Flow Property](https://behavure.ai/docs/wiki/spaces/SGV/pages/2139259375/Create+a+Flow+Property+v5)