---
title: Job overview
description: Job overview
slug: jobs/overview
sidebar:
  label: Overview
  order: 0
---

Jobs in Edge IQ define how data is read, processed, and written. Jobs are usually created via the UI's visual editor and executed by workers.

## Job Definition

A **Job Definition** is the saved configuration describing how a Job should run. Internally, it's stored as YAML, though you can view and edit it as JSON or YAML in the Edge IQ UI if needed. A Job Definition includes:

- **Name** – A user-defined label for the Job.
- **Input** – Exactly one data source (file, S3, HTTP, etc.), with optional scheduling or triggers.
- **Actions** – Zero or more transformations, enrichments, or filters applied to data as it flows.
- **Output** – Exactly one destination to write data (file, API endpoint, cloud storage, etc.).

This definition resides on the Edge IQ Server, where it's versioned and can be managed or deployed across different workers.

**Important:** A single Job has exactly one input and one output. If you need multiple inputs or outputs in a larger pipeline, use **worker channels** to compose multiple Jobs together.

Edge IQ enforces one input and one output per Job. If you need:

- **Multiple outputs** (e.g., archiving to S3, plus sending to a SIEM), or
- **Multiple inputs** (fan-in from various sources),

you can chain Jobs using **worker channels**.

## Job Types

Edge IQ supports several types of Jobs:

- **Once-off Jobs**: Run once, complete their task, then stop (no trigger configured).
- **Streaming Jobs**: Remain active and continuously process new data as it arrives.
- **Scheduled Jobs**: Trigger at a regular interval or according to a user-defined schedule.

### Scheduling and Triggers

Scheduling in Edge IQ is configured within the **input**'s **Trigger** section if relevant. Some inputs don't require a schedule or trigger—those inputs are "always on," continuously reading data as it appears.

## Job Components

Each Job in Edge IQ consists of:

1. **Input**

   - The single source that reads events (plaintext, compressed, or otherwise) from files, object storage, APIs, or any other supported data location.
   - If scheduling is applicable for this input type, configure it under the **Trigger** section (e.g., a cron-like schedule or a specific time interval).

2. **Actions** (Zero or more)

   - Actions process the input data—called "event data"—to filter, enrich, transform, or extract fields.
   - A variety of actions is available, from simple field renaming to advanced data manipulation or enrichment with external lookups.

3. **Output**
   - The single destination that writes event data (for example, to files, APIs, or cloud storage).
   - If you need to send data to multiple destinations, the next section addresses **Worker Channels** which can help you compose multiple Jobs together.

## Worker Channels for Multi-Job Pipelines

Because each Job can only have one input and one output, you may occasionally need to **fan in** from multiple data sources or **fan out** to multiple destinations. Edge IQ provides **in-memory worker channels** to stitch these scenarios together:

**worker channels**.

- **Standard channels** pass data between Jobs in a pipeline in a first-in, first-out manner.
- **Clone Channels**: Duplicate events to multiple downstream Jobs (useful if you want to archive data and simultaneously forward it to a SIEM).
- **Round-Robin Channels**: Distribute events across several downstream Jobs (helpful for load balancing or parallel processing).

In practice, you can create:

1. A Job with your real data **input** and an **output** pointing to an in-memory channel.
2. Additional Job(s) that read from that channel as their **input** and write to their respective final destinations.

This modular design gives you flexibility while keeping each individual Job simple.

## Creating and Editing Jobs

1. **Open the Visual Editor**  
   Navigate to **Jobs** in the Edge IQ UI and click **New Job** (or edit an existing one).

2. **Job Quick Setup Wizard**

   - Choose an Input type, where the data is coming from.
   - Choose an Output type, where the data is going.
   - Optionally, add timestamps to all events.
   - Or, skip the wizard and start with the default canvas.

3. **Configure the Job Name**

   - Click on the Job name at the top of the canvas to rename it, the default name is "new-job".

4. **Configure the Input**

   - Select a single input type (e.g., file, S3, HTTP) and fill in any required connection details by selecting "Change Input" and then "Configure".
   - If scheduling is relevant (for example, you want the input to run once daily), set it up under the **Trigger** field of the input.
   - When you are done press the "Close Input" button.

5. **Add Actions**

   - Add, remove, or reorder actions as needed to transform or enrich your data.

6. **Specify the Output**

   - Choose your single output destination.
   - Fill in connection details (e.g., credentials, endpoint URLs).

7. **(Optional)** Test the Job

   - Use the **Run** or **Run & Trace** buttons to run the Job with a small sample of data to verify that it's working as expected.
   - The number of samples and other parameters can be configured under "Run Output".

8. **Save and Deploy**
   - Review the configuration, and then save it.
   - When you're ready, stage and deploy your Job to one or more workers.

## Once Deployed

You can monitor Jobs' status in the UI, where you'll see logs, any error messages, and performance metrics.

## Job Execution

While Jobs internally **represent event data as JSON** for transformation, they can process any plain-text data—and certain inputs handle compressed or binary formats if configured to do so.

When you **run** or **deploy** a Job, Edge IQ's worker(s) read the Job Definition (YAML on the server, presented as a digitally signed JSON configuration to the runtime) and instantiate a **Job runtime**. The worker then sets up the actual process according to your configuration.

- **Multithreaded Scaling**  
   The runtime is multithreaded and will leverage as many CPU cores as available, making Edge IQ highly scalable even under heavy loads.

- **Single Config, Single Runtime**  
   Each Job execution uses one version of the config at a time. If you modify a Job Definition, and stage the new version, future runs will pick up the changes, but ongoing executions continue with the existing config until they complete or are restarted.

- **Event Representation**  
   Within the runtime, events are converted to JSON objects in memory. These objects store key-value pairs and any extracted fields, making it easier for actions to filter, enrich, and transform data.

- **Monitoring and Logs**  
   You can monitor each Job's execution in the UI. Logs, error messages, and performance metrics help you diagnose issues or tune performance.

## Summary

- **One Input, One Output** per Job keeps configurations straightforward.
- **Actions** let you shape and transform data en route.
- **Worker Channels** allow you to chain multiple Jobs together for more complex pipelines.
- **Scheduling** is set in the **input** configuration for inputs that support triggered runs.

For more details on available inputs, actions, and outputs, explore the related reference pages or check the examples in our [Getting Started Guide](/start/starting/).
