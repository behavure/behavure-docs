---
title: "Analyze User Paths With Flows "
description: "Definition & use of Analyze User Paths With Flows "
---

---

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

- [**Understand flow definition conditions**](./understand-flow-definition-conditions)**:**After identifying the critical steps in your experience, it is important for accuracy that you impose some constraints on your flow. The article linked above summarizes the flow definition conditions.
- [**Understand duration flow properties**](./understand-duration-flow-properties)**:**A flow time property lets you specify which steps you want to measure time duration between, and then apply an aggregation.
- [**Query on stages in a flow**](./query-on-stages-in-a-flow)**:**If you're aggregating over events, you can access information about flows in your aggregation.
- [**Create an optional flow step**](./create-an-optional-flow-step)**:**When you define your flow, you can identify one or more steps as optional. For example, you might want to include users that had to log in before purchasing, in addition to users that were already logged in and went directly to purchasing. Here, login is an optional step.
- [**Find the natural frequency of your experience**](./find-a-natural-frequency-of-your-experience)**:**Many experiences have a natural frequency or cadence of usage. To model your experience meaningfully in a flow, you need a sense of how often your users are in your experience when they are using it.
- [**Define a user session using a flow**](./define-a-user-session-using-a-flow)**:**You can perform session analysis using Measure IQ flows. This article summarizes the definitions that help you model a session as a flow. You can then analyze the flow using Measure IQ analysis tools.
- [**Example: Show actor paths using flows**](./example-show-actor-paths-using-flows)**:**This article demonstrates how to create a flow showing users who completed a set of steps over a specified period of time. It then shows how to use the flow to show actor paths and determine the events leading up to success, the events leading up to failure, and the steps completed by an individual user segment.
- [**Example: Analyze paths to conversion using flows**](./example-analyze-paths-to-conversion-using-flows)**:**To better understand your customers, you can analyze the steps they take leading up to a major conversion, such as signing up for a service, creating a profile, or making a purchase.
- [**Example: Analyze user sessions with flows**](./example-analyze-user-sessions-with-flows)**:**This article explains how you can use a flow to explore the details of user sessions, such as the number of comments each user makes, how often they make a purchase or perform other conversions, or how long they stay engaged on your site.
