---
title: CrowdStrike Falcon
description: Write to Crowdstrike Falcon LogScale
slug: product-integrations/crowdstrike
sidebar:
  label: CrowdStrike Falcon
  order: 3
draft: false
---

Edge IQ integrates with CrowdStrike Falcon LogScale, CrowdStrike's enterprise SIEM (Security Information and Event Management) platform. By leveraging Edge IQ's secure connectors, schema-less enrichment, and real-time streaming, your security team gains comprehensive visibility—sending not just raw logs but full behavioral context into CrowdStrike for faster, more accurate detection and response.

This integration enables organizations to:

- Centralize security event data from Edge IQ devices into CrowdStrike's industry-leading security platform
- Leverage CrowdStrike's advanced threat detection and response capabilities
- Maintain comprehensive security visibility across your entire network infrastructure
- Meet compliance requirements with detailed security logging and monitoring

Choose from multiple integration methods to best suit your security architecture:

### LogScale HEC API

- add Edge IQ output **splunk-hec**
- configure [Crowdstrike ingest endpoint URL](https://library.humio.com/falcon-logscale-cloud/endpoints.html)
- configure HEC token
- configure Splunk fields: index, host, source, sourcetype, timestamp
- see also: [LogScale HEC](https://library.humio.com/logscale-api/log-shippers-hec.html)

### LogScale Ingest APIs

- add Edge IQ output **http-post**
- configure [Crowdstrike ingest endpoint URL](https://library.humio.com/falcon-logscale-cloud/endpoints.html)
- configure required headers (Authorization: Bearer foo)
- see also: [LogScale Ingest APIs](https://library.humio.com/logscale-api/api-ingest.html)

### S3

[Crowdstrike S3 Ingestion](https://www.crowdstrike.com/tech-hub/ng-siem/crowdstrike-falcon-logscale-s3-ingest/)
