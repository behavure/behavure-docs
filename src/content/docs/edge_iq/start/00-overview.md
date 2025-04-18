---
title: Overview
description: Edge IQ overview
slug: start/overview
sidebar:
  label: Overview
  order: 0
---

Edge IQ is a flexible, distributed data integration platform designed to reliably move and transform data between various sources and destinations. By abstracting away the operational complexity of pipelines, Edge IQ lets you focus on extracting insights and value, rather than managing connectivity and scale.

### What is ETL?

ETL (Extract, Transform, Load) is a data integration process that:

- **Extract**: Collects data from various sources
- **Transform**: Processes and converts data into the desired format
- **Load**: Delivers the processed data to its destination

Edge IQ streamlines this process by providing a configuration-driven approach to ETL, eliminating the need for complex custom scripting.

### Core Components

- **Server** – Serves as the control plane for all data flows. It tracks configuration details, orchestrates job execution, and consolidates monitoring data.
- **Jobs** – Define the individual pipelines, specifying how data is ingested, processed, and delivered. Jobs can be tailored for simple one-off tasks or for high-throughput, multi-step workflows.
- **Workers** – Run Jobs in the background. This distributed pool of processes handles data ingestion, transformation, and output, scaling automatically as volume and complexity grow.

### Why Use Edge IQ

Managing data at scale often involves juggling multiple data formats, sources, and failure modes. Edge IQ addresses these challenges by providing:

- **A Configuration-Driven Approach** – Use a straightforward configuration file or UI-based method to define each pipeline, reducing the need for custom scripting or ad hoc integrations.
- **Reliable and Scalable Execution** – Built-in worker management allows users to distribute tasks efficiently and recover from common failures, ensuring pipelines continue running smoothly.
- **Clear Operational Visibility** – The Server centralizes logs, metrics, and alerts so you can quickly identify and address potential bottlenecks or errors.

### How to Get Started

If you are new to Edge IQ, begin by installing and running the Server to establish the core environment. From there, you can set up your first Job to read from a simple source (such as a local file) and deliver it to a target of your choice. This initial exercise provides a hands-on introduction before you move on to more advanced capabilities like scheduling, partitioning, or complex transformations.

### Next Steps

- Review the [Installation](/install/overview/) guide to set up your environment.
- Explore our **Guides** for step-by-step instructions on common scenarios, such as ingesting from S3 or forwarding data to analytics platforms.
- For more detailed configuration options and troubleshooting information, refer to the **Reference** section.

By following these resources, you can quickly configure reliable data pipelines and tailor them to your organization's needs.
