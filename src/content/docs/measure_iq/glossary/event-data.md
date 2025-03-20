---
title: Event Data 
description: Definition & use of Event Data 
---
**Event data** describes actions performed by entities, also known as actors. Event data has three key pieces of information: actor, timestamp, and state. 

- Actor is the person or thing generating the event.
- The timestamp is the point in time at which the event happened.
- The state is the other relevant information about the event, including information about actors related to the event.

Example:

`{"userid":"foo","timestamp":1051565134,"event":"Start","region":"united states","age":"49"}`

In the above example, userid is the Actor, timestamp is the time the event happened and event, region & age are the state that further define the event.

## Related terms

- [Actor](../actor)
- [Event](../event)
- [Timestamp](../timestamp)