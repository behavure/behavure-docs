---
title: Core Concepts
description: Edge IQ Core Concepts
slug: start/core-concepts
sidebar:
  label: Core Concepts
  order: 1
---

This page introduces the foundational elements of Edge IQ. Understanding these components will help you design and maintain efficient, reliable data pipelines.

## Server

The Server is the control plane for Edge IQ. It manages configuration details, tracks system health, and orchestrates the execution of Jobs across a distributed set of Workers. The Server also provides a central point for monitoring logs, metrics, and alerts related to pipeline activity.

### Key Responsibilities

- Stores and manages all Job definitions
- Oversees resource allocation by coordinating with Workers
- Collects metrics and status data for operational visibility

## Jobs

A Job defines a specific pipeline. Each Job configuration indicates how data is ingested from a single source, optionally transformed, and then delivered to a single output. While a single Job focuses on one input and one output, you can connect multiple Jobs via Worker channels to support more complex workflows.

### Common Job Elements

- **Input** – A single data source (e.g., file system, API, or queue).
- **Transformations (Actions)** – Optional processing steps such as filtering, parsing, or enrichment.
- **Output** – A single destination where processed data is stored or forwarded.

## Workers

Workers instantiate the runtime for each Job and performs any necessary orchestration and coordination. In a distributed Edge IQ deployment, multiple Workers can run in parallel to handle multiple Jobs or increased data volume.

### How Workers Operate

Workers form the execution layer for Jobs. They communicate with the Server to retrieve information about which Jobs should run, instantiate the Job runtime, and forward operational data for monitoring. The typical workflow proceeds as follows:

1. **Server Coordination** – The Worker connects to the Server, which schedules one or more Jobs to be run on that Worker.
2. **Runtime Instantiation** – Once a Job is assigned, the Worker sets up the necessary runtime environment to handle ingestion, transformations, and output delivery.
3. **Job Payloads** – The Worker receives the Job's configuration and associated parameters (input, transformations, output) from the Server.
4. **Execution and Monitoring** – As the Worker executes the Job, it collects metrics, logs, and traces and forwards them to the Server for centralized monitoring and troubleshooting.

In this model, a Worker handles a single input and output per Job, but you can chain multiple Jobs together with Worker channels to build more complex data flows. Each Worker's isolation also contributes to resilience, as errors typically affect only the Jobs running on that Worker, leaving others uninterrupted.

### Worker Channels

When you need to fan out or compose data flows across multiple Jobs, Worker channels serve as in-memory pathways that allow Jobs to pass events among themselves. This mechanism provides flexibility in building complex pipelines without adding external message brokers. For instance, you can have one Job's output feed directly into another Job's input by linking them through a channel, enabling multi-step processing flows or branching logic.

### Scaling and Resilience

- **Horizontal Scalability** – You can add additional Workers to handle more Jobs or higher data throughput.
- **Isolated Failure Handling** – If one Worker encounters an error, it typically does not affect other Workers. This design limits disruption and ensures that healthy Jobs continue running.

## Pipelines and Data Flow

In Edge IQ, each Job can be viewed as a discrete pipeline from one input to one output, with optional transformations in between. By default, a Job's data flow is self-contained, but you can connect multiple Jobs using Worker channels to fan out or chain together more advanced workflows. Edge IQ manages the orchestration of these pipelines, handling retries, error reporting, and scaling, minimizing the need for custom integration code.

## Configuration and Management

Edge IQ is primarily configured through a combination of the Server UI and environment variables. Each Job is defined with parameters for inputs, actions, outputs, and runtime behavior. Once created, Jobs are monitored and administered via the Server, which aggregates logs and metrics to provide operational insights.

---

By familiarizing yourself with these core concepts—Server, Jobs, Workers, and Worker channels—you will be better equipped to design effective data workflows using Edge IQ. For detailed guidance on creating and running Jobs, refer to the **Guides** section, or consult the **Reference** for information on specific configuration parameters.
