---
title: CrowdStrike Falcon
description: Write to Crowdstrike Falcon LogScale
slug: product-integrations/crowdstrike
sidebar:
  label: CrowdStrike Falcon
  order: 3
draft: false
---

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
