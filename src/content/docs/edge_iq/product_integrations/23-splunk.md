---
title: Splunk Cloud, Splunk Enterprise
description: Write to Splunk HEC
slug: product-integrations/splunk
sidebar:
  label: Splunk
  order: 23
draft: false
---

Edge IQ supports seamless integration with Splunk Cloud and Splunk Enterprise through the Splunk HTTP Event Collector (HEC). By leveraging Edge IQ's secure connectors, real-time streaming, and flexible data transformation capabilities, your team can efficiently route and process data into Splunk for comprehensive log analysis, security monitoring, and operational intelligence while maintaining optimal performance and scalability.

## Splunk HEC output

Edge IQ supports Splunk Http Event Collector (HEC) to send data to Splunk.

### Configure Edge IQ to send data to Splunk HEC

Add Edge IQ output **splunk-hec** to a job and configure:

- **URL**: Splunk HEC endpoint, example: https://127.0.0.1:8088/services/collector/event
- **HEC token**: authentication token
- **Splunk fields**: (index, host, source, sourcetype). Edit the value or the fieldname in the data, where the value can be found.
- **Batch**: Batching input events together
- **Retry**: Retry behaviour
- **Insecure**: Ignore TLS certificate validation errors (This is unsafe to use)
- **Metrics**: Send a metrics formatted payload to the HEC endpoint
- **Remove**: Consume (remove) fields from the event payload before submitting to the endpoint. Applicable to time-field, host-field, source-field, sourcetype-field, index-field and hec-token-field
- **Event Field**: If specified the field's contents will be submitted as the event payload to the endpoint
- **Time Field**: Use the specified field for the timestamp of the endpoint, should be in Unix epoch format

We're currently working on expanding our Edge IQ documentation. Check back soon for detailed guides, tutorials, and reference materials.
