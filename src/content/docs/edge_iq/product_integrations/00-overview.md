---
title: Overview
description: All product integrations
slug: product-integrations/overview
sidebar:
  label: Overview
  order: 0
draft: false
---

| Product Integration              | Source Input                   | Destination Output             |
| -------------------------------- | ------------------------------ | ------------------------------ |
| AWS S3                           | s3                             | s3                             |
| AWS Cloudtrail                   | s3                             | s3                             |
| AWS Cloudwatch                   | s3                             | s3                             |
| CrowdStrike Falcon LogScale      |                                | http-post, splunk-hec, s3      |
| CrowdStrike Detection Monitoring | http-poll                      |                                |
| Elastic                          |                                | http-post                      |
| Google Analytics (GA4)           | s3, gcs                        |                                |
| Google Ad Manager (GAM)          | s3, gcs                        |                                |
| Google Cloud Storage (GCS)       | gcs                            | gcs                            |
| Logsign                          |                                | files                          |
| Edge IQ Worker                   | worker-channel                 | worker-channel                 |
| Microsoft Azure                  | azure-blob                     | azure-blob                     |
| Microsoft Graph API              |                                | http-post                      |
| Microsoft Sentinel               | s3, azure-blob                 | s3, azure-blob, gcs, http-post |
| Microsoft Windows                | windows-event-log              |                                |
| Scuba Analytics                  | s3, azure-blob, gcs, http-poll | s3, azure-blob, gcs, http-post |
| Linux shell                      | exec                           |                                |
| Splunk                           | http-poll                      | splunk-hec                     |
| Twilio Segment                   | s3, azure-blob, gcs, http-poll |                                |
