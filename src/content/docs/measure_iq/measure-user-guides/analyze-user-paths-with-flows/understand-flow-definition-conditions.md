---
title: "Understand Flow Definition Conditions "
description: "Definition & use of Understand Flow Definition Conditions "
---

After identifying the critical steps in your experience, it is important for accuracy that you impose some constraints on your [flow](/measure_iq/glossary/flow), including transitions between steps and ending the flow. The following table summarizes the flow definition conditions.

| **Termination condition**    | **Description**                                                                                                                                                                                                                                                                                    | **Available in**             |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| Start flow                   | Define as a filter. If the actor is not already in a flow, and they have an event that matches this filter, start the flow.                                                                                                                                                                        | Flow step definition         |
| Transition from step         | Define as a filter. If an actor has an event that matches this filter while in the target step, transition to this step.                                                                                                                                                                           | Flow step definition         |
| End flow before              | Define as a filter. If an actor is in a flow and has an event that matches this filter, end the flow on the previous event, excluding the event that matches this filter.                                                                                                                          | Flow step definition, global |
| End flow after               | Define as a filter. If an actor is in a flow and has an event that matches this filter, end the flow on this event, including this event.                                                                                                                                                          | Flow step definition, global |
| End flow from inactivity     | Define as a time interval. If an actor is in a flow and does not produce events for the defined time duration, end the flow on the most recent event. If you define an inactivity timeout both globally and on a flow step definition, the flow step definition takes precedence on the flow step. | Flow step definition, global |
| End flow from max total time | Define as a time interval. If an actor is in a flow for longer than this interval, end the flow on the most recent event. If you define both an inactivity condition and a max total time condition, the max total time condition takes precedence.                                                | Global                       |

**End flow before**, **End flow after**, and **End flow from inactivity** are available as a global rule for convenience. Adding one of these conditions as a global rule is equivalent to defining that rule in every step in the flow.

## About global rules

Most experiences have a natural frequency, but that frequency can vary widely. For example, many people use social media apps daily, go shopping weekly, and lease cars every 3 years.

Unless you define conditions for ending each actor's pass through your experience (called a [flow instance](/measure_iq/glossary/flow-instance) in Measure IQ), an actor might start a new session without you realizing it. For accurate results, be sure to define at least one condition to end your flow.

While you can define conditions within your flow steps for exiting the flow instance, Measure IQ also lets you end a flow with the following global rules:

- End flow due to inactivity of X time
- End flow due to timeout of X time
- End flow after/on event Y (or any event)
- End flow before event Y (or any event)

Whether applied as a global rule or to define an individual flow step, the definition conditions fall into two general categories: time-based and event-based.

## Time-based options for ending flows

You can end a flow with two time-based rules: **inactivity** and **timeout**. These options are available only as global rules, which end a flow.

- When your user isn’t using your product or service (that is, generating events) for a period of time, it is a good indicator that they’ve ended their session. While your flow can have local conditions for ending, such as logging out, the absence of activity can be a useful condition to ensure that you start a new flow instance at a user’s next session. To accomplish this, use **End flow due to inactivity of X time**.
- The other time-based option for ending a Measure IQ flow is **End flow due to timeout of X time**. Your experience might have many loops, or your data collection might capture events that aren’t relevant to your flow (for example a periodic machine status, or heartbeat). Specifying a timeout condition for a flow can help you match it to the natural frequency of your experience. This is useful when you know that your users generally use your experience in their everyday work (that is, a daily timeout), or make their decisions over a longer period of time such as online shopping. We strongly recommend that you specify a timeout in your flow definition. If you are unsure of the natural frequency of your experience, see [Find the natural frequency of your experience](../find-a-natural-frequency-of-your-experience).

## Event-based options for ending flows or transitioning between steps

The event-based conditions include ending a flow or step *on* a particular event, or ending the flow or step *before* a particular event.

If you know that a particular event is the end of your user session (for example a logout), you can end your flow on that event using a global rule. Or to end your flow on the last step, you can add a rule to end the flow on any event that reaches that step.

If you know that a particular event indicates the start of a user session (for example a login), then you can define a global rule that ends your flow before that event.

To model different parts of your user experience, event-based conditions can help. For example:

- An acquisition flow can track how anonymous users eventually create an account.
- An activation flow might start on account creation and track user behaviors in a freemium experience before they upgrade to a paid subscription.
- A retention flow might start on an upgrade event and track changes in their behaviors until they churn.

## For more information

1. [Example: Show actor paths using flows](./example-show-actor-paths-using-flows)
2. [Example: Analyze paths to conversion using flows](./example-analyze-paths-to-conversion-using-flows)
3. [Example: Analyze user sessions with flows](./example-analyze-user-sessions-with-flows)
4. [Query on stages in a flow](./query-on-stages-in-a-flow)
