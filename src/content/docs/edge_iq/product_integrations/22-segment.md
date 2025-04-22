---
title: Segment
description: Write to Segment
slug: product-integrations/segment
sidebar:
  label: Segment
  order: 22
draft: false
---

Edge IQ supports seamless integration with Segment, enabling you to collect, clean, and control your customer data. By leveraging Edge IQ's secure connectors, real-time streaming, and flexible data transformation capabilities, your team can efficiently route and process data into Segment for comprehensive customer analytics, behavioral tracking, and marketing automation while maintaining optimal performance and scalability.

## Segment output

Edge IQ supports writing data to Segment's HTTP API.

### Configure Edge IQ to send data to Segment

Add Edge IQ output **segment** to a job and configure:

- **URL**: Segment HTTP API endpoint, example: https://api.segment.io/v1/track
- **Write Key**: Your Segment write key for authentication
- **Batch**: Batching input events together
- **Retry**: Retry behaviour
- **Insecure**: Ignore TLS certificate validation errors (This is unsafe to use)
- **Remove**: Consume (remove) fields from the event payload before submitting to the endpoint
- **Event Field**: If specified the field's contents will be submitted as the event payload to the endpoint
- **Time Field**: Use the specified field for the timestamp of the endpoint, should be in Unix epoch format

We're currently working on expanding our Edge IQ documentation. Check back soon for detailed guides, tutorials, and reference materials.
