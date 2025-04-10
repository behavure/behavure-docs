---
title: Google Cloud Storage (GCS)
description: Read from and write to GCS
slug: product-integrations/gcs
sidebar:
  label: Google Cloud Storage (GCS)
  order: 8
draft: false
---

## GCS

Edge IQ supports reading from and writing to Google Cloud Storage (GCS)

### Configure Edge IQ to read data from GCS

Add Edge IQ input **gcs** to a job and configure:

- **Bucket Name**: The storage service container.
- **Object Name**: The objects names.
- **Application Credentials**:
- **Service Account**:

### Configure Edge IQ to write data to GCS

Add Edge IQ output **gcs** to a job and configure:

- **Bucket Name**: The storage service container.
- **Object Name**: The objects names.
- **Application Credentials**:
- **Service Account**:

### Recommendations for files and folders

- each file should not be larger than 100MB-150MB (compressed gzip or parquet)
- Y/M/ or Y/M/D/ or Y/M/D/H/ folders
