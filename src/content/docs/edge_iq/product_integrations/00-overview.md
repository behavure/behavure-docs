---
title: Overview
description: All product integrations
slug: product-integrations/overview
sidebar:
  label: Overview
  order: 0
draft: false
---

## How Product Integrations Work

Product integrations in Edge IQ are implemented through Jobs, which define how data flows between different systems. Each integration typically consists of:

1. **Input Sources** - Where data is read from (e.g., S3 buckets, HTTP endpoints, file systems)
2. **Output Destinations** - Where processed data is sent (e.g., cloud storage, APIs, SIEM systems)
3. **Actions** - Optional transformations applied to the data as it flows through the pipeline

Jobs are configured using Edge IQ's visual editor or YAML configuration, making it easy to set up and manage these integrations. Each Job can have exactly one input and one output, but you can chain multiple Jobs together using worker channels for more complex workflows.

For detailed information about creating and managing Jobs, see the [Jobs Overview](../jobs/overview).

## YAML Configuration

Edge IQ supports comprehensive YAML-based configuration for defining data pipelines. This makes it easy to version control and automate deployments. A typical Job configuration includes:

```yaml
pipeline:
  name: "example-pipeline"
  inputs:
    - type: "s3"
      config:
        bucket: "source-bucket"
        region: "us-east-1"
  actions:
    - type: "transform"
      config:
        rules:
          - field: "timestamp"
            operation: "format"
            format: "ISO8601"
  outputs:
    - type: "http-post"
      config:
        endpoint: "https://api.example.com/data"
        headers:
          Authorization: "Bearer ${API_KEY}"
```

You can edit Jobs in YAML format by clicking the `Raw Job` button in the visual editor. This is particularly useful for:

- Making quick edits to large Jobs
- Version controlling Job configurations
- Automating deployments
- Reusing configurations across different environments

## HTTP Endpoints

Edge IQ supports various HTTP-based integrations through two main input types:

1. **http-poll** - Makes HTTP requests to fetch data from APIs

   - Configure headers, query parameters, and request body
   - Supports scheduling via triggers
   - Handles JSON and plain text responses
   - Includes retry logic for reliability

2. **http-server** - Listens for incoming HTTP requests
   - Accepts data from external systems
   - Processes requests in real-time
   - Supports various authentication methods

For HTTP outputs, Edge IQ provides:

- **http-post** - Sends data to HTTP endpoints
- **splunk-hec** - Specialized output for Splunk HEC
- Customizable headers and authentication
- Batching support for better performance

## Available Integrations

Below is a comprehensive list of supported product integrations, showing their available input sources and output destinations:

| Product Integration                                           | Source Input                   | Destination Output             |
| ------------------------------------------------------------- | ------------------------------ | ------------------------------ |
| [AWS S3](../s3)                                               | s3                             | s3                             |
| AWS Cloudtrail                                                | s3                             | s3                             |
| AWS Cloudwatch                                                | s3                             | s3                             |
| [CrowdStrike Falcon LogScale](../crowdstrike-falcon-logscale) |                                | http-post, splunk-hec, s3      |
| [CrowdStrike Detection Monitoring](../cdm)                    | http-poll                      |                                |
| [Elastic](../elastic)                                         |                                | http-post                      |
| [Google Analytics (GA4)](../ga4)                              | s3, gcs                        |                                |
| [Google Ad Manager (GAM)](../gam)                             | s3, gcs                        |                                |
| [Google Cloud Storage (GCS)](../gcs)                          | gcs                            | gcs                            |
| [Logsign](../logsign)                                         |                                | files                          |
| Edge IQ Worker                                                | worker-channel                 | worker-channel                 |
| [Measure IQ](../measure-iq)                                   | s3, azure-blob, gcs, http-poll | s3, azure-blob, gcs, http-post |
| [Microsoft Azure](../azure)                                   | azure-blob                     | azure-blob                     |
| Microsoft Graph API                                           |                                | http-post                      |
| [Microsoft Sentinel](../sentinel)                             | s3, azure-blob                 | s3, azure-blob, gcs, http-post |
| [Microsoft Windows](../windows)                               | windows-event-log              |                                |
| Linux shell                                                   | exec                           |                                |
| [Splunk](../splunk)                                           | http-poll                      | splunk-hec                     |
| [Twilio Segment](../segment)                                  | s3, azure-blob, gcs, http-poll |                                |

## Getting Started with Integrations

To set up a new integration:

1. Create a new Job in the Edge IQ UI
2. Select the appropriate input type for your source system
3. Configure any necessary transformations using Actions
4. Set up the output destination
5. Test and deploy the Job

For more detailed instructions, see the [Getting Started Guide](../start/starting).
