---
title: "Find a Natural Frequency of Your Experience "
description: "Definition & use of Find a Natural Frequency of Your Experience "
---
Many experiences have a natural frequency or cadence of usage. To model your experience meaningfully in a [flow](../flow), you need a sense of how often your users are in your experience *when* they are using it. This knowledge helps you choose accurate time-based options for ending your flow.

Common categories of frequencies include:

- Daily: Facebook, Instagram, social, and messaging use cases.
- Weekly: Meetings, work week, or weekend-specific use cases, such as exercise.
- Monthly: Subscription services, like book or wine clubs.

These cases are often regular, so you can guide your users to form habits around your experience. But even if the natural frequency of your experience is long and irregular (like car buying), you can create intermediate experiences so that you can bring users back into your experience when they are ready. For example:

- In an online store, actions like searching and reading reviews precede a purchase. You might decide to tie a marketing message to an event like a session of reading product reviews.
- House listing searches precede house buying or selling. You might want to trigger a marketing message after an event like subscribing to home listing alerts.

## Find the frequency of your experience

To find your flow’s natural frequency:

1. Choose a primary use case in your experience and model it by [creating a flow](../../../measure_iq/measure-tutorials/work-with-flows/create-a-flow). Save the flow.
2. Create a [flow property](../../../measure_iq/measure-tutorials/work-with-flows/create-a-flow-property) that filters to flows that reach the last step.
3. Use your new flow property in [Distribution View](../../measure-user-guides/streamline-analysis-with-additional-explorations/analyze-a-distribution) to construct a frequency histogram of how many times your users complete this flow in a given period of time. If your hypothesis is a daily or weekly frequency, your histogram should be over at least 30 days.
4. Inspect the results. Ideally, you can see the frequency of usage over time. If you don’t see anything definitive or have multiple peaks in your distribution, try adding another [split-by](../../../../../measure_iq/glossary/split-by) to further segment your users.