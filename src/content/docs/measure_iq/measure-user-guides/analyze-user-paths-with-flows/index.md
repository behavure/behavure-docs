---
title: "Analyze User Paths With Flows"
description: "Learn how to analyze and visualize user paths and flows in Measure IQ"
---

Learn how to analyze and visualize user paths and flows in Measure IQ to understand user behavior and journey patterns.

- [Understand Flow Definition Conditions](./understand-flow-definition-conditions)
- [Understand Duration Flow Properties](./understand-duration-flow-properties)
- [Query on Stages in a Flow](./query-on-stages-in-a-flow)
- [Create an Optional Flow Step](./create-an-optional-flow-step)
- [Find Natural Frequency of Your Experience](./find-a-natural-frequency-of-your-experience)
- [Define a User Session Using a Flow](./define-a-user-session-using-a-flow)
- [Example: Show Actor Paths Using Flows](./example-show-actor-paths-using-flows)
- [Example: Analyze Paths to Conversion](./example-analyze-paths-to-conversion-using-flows)
- [Example: Analyze User Sessions with Flows](./example-analyze-user-sessions-with-flows)

A flow is an object in Measure IQ that a user defines to study their user experience. A flow defines a sequence of conditions or milestones, that identifies users that performed actions matching the defined sequence. The flow definition includes one or more start conditions, one or more steps, and transition rules between the steps.

In Measure IQ, the default visualization for a flow is a [Sankey diagram](/measure_iq/glossary/sankey-view-diagram). This visualizes the flow instances (that is, the actors' individual passes through the flow) as they transition between flow steps.

Once you have defined a flow, you can use it in the following ways:

- Examine events between any of the flow's milestones using the built-in event path capability.
- Use the flow definition in a [query](/measure_iq/glossary/query) to aggregate, filter, or group by properties of the flow.
- Segment a flow using a [flow property](/measure_iq/glossary/flow-property).
- Use a flow to segment the actors associated with the flow, for example, users that did not reach the "checkout" step.
- Filter events using a flow.

[Sessions](/measure_iq/glossary/session) and [funnels](/measure_iq/glossary/funnel) are part of Measure IQ [Flows](/measure_iq/glossary/flow), with additional functionality.

Common reasons for using flows:

- **Path discovery**: Show actors in the flow performing various steps, as demonstrated in the article on how to create a flow. You can then analyze the steps in an actor's path and filter flows that reach a specified step to track trends.
- **Conversion**: Show what actors did on the path to conversion, or when they dropped off. A conversion involves a known target event with a strict set of steps to reach the end state, such as a purchase, creating a profile, or signing up for a service. You can analyze how long it took actors to move from one step to the next, the process for actors who reached the end state, as well as what happened with the actors who didn't reach the end state.
- **Engagement**: Show how actors are engaging with your product. Measure session times, as well as metrics that occurred within a session.

See the articles below for conceptual information about flows as well as some examples.
