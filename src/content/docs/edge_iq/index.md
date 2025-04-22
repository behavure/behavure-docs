---
title: "Edge IQ"
description: "Complete documentation for Edge IQ - Behavure's advanced edge computing platform"
sidebar:
  order: 2
---

## Product Overview

**Edge IQ for Behavure** is a data integration solution for creating and maintaining high‑performance data pipelines. Our platform provides a reliable, repeatable, scalable, and simplified approach for automating data flow between systems, as well as handling all common pipeline transformations. This minimizes the engineering effort required to solve data integration challenges.

Customers leverage Edge IQ to extract value from their data faster, with less complexity and overhead. Simplifying data engineering at both the edge and core is what Edge IQ for Behavure does best.

- Decentralized Processing - Process, enrich and route data at the source, reducing latency and bandwidth costs while improving data quality.
- No-Code Data Pipeline Management - Connect to any data source through intuitive visual interfaces without complex scripting or coding.
- Data Agnostic Universal Integrations - Easily integrate all major data sources from legacy systems to modern APIs and IoT devices.

---

## User Experience (UX)

- **Intuitive Interface**  
  Define, schedule, and monitor pipelines via a visual editor that's accessible to teams without deep data‑engineering expertise.

- **Visual Pipeline Builder**  
  Drag‑and‑drop components simplify development, testing, and troubleshooting.

- **Versioning & Rollback**  
  All pipeline definitions are versioned for auditability and easy rollback.

- **Centralized Secrets**  
  Manage static and dynamic (runtime) credentials securely from a single pane of glass.

---

## Advanced Data Routing

- **Universal Connectivity**  
  Direct any structured, semi‑structured, or unstructured data from any source to any destination.

- **Edge‑to‑Core Consistency**  
  Apply the same routing and transformation logic across distributed edge nodes and centralized clusters.

- **No‑Code Enrichment**  
  Configure real‑time filtering, enrichment, and optimization through the visual editor—no software development skills required.

---

## Centralized Management & Collaboration

- **Holistic Pipeline Dashboard**  
  Gain a unified view of job status, performance metrics, and alerts across all workers and environments.

- **Team Collaboration**  
  Intuitive tools and workflows reduce bottlenecks—data engineers, analysts, and ops teams can work together more efficiently.

- **Audit Trail**  
  Track every change, deployment, and pipeline run for full lifecycle oversight.

---

## Privacy & Security

Security is core to Edge IQ's design, engineered for the most sensitive environments:

- **Tamper‑Proof Pipelines**  
  Cryptographically secure data processing across all nodes.

- **Self‑Hosted Control**  
  Maximize privacy by self‑managing your deployment, with full control over PII cleanup, redaction, and obfuscation—even at the edge.

---

## Real‑Time Monitoring

- **Comprehensive Telemetry**  
  Collect and expose internal metrics, events, and logs for live visibility.

- **External Integration**  
  Forward system telemetry to SIEMs, observability platforms, or custom dashboards via native exporters and webhooks.

---

## Benefits

- **Accelerated Time‑to‑Value**  
  Onboard new users quickly with UI‑driven pipelines and reusable templates.

- **Cost Efficiency**  
  Lower infrastructure spend through optimized, high‑throughput processing.

- **Reduced Complexity**  
  Empower non‑engineers to contribute to data projects, freeing experts to focus on innovation.

- **Consistent Best Practices**  
  Turn repeatable workflows into templates to enforce standards across the organization.

## Architecture

- Secure-by-design, scalable distributed architecture
- Edge‑native data processing
- Centralized configuration management
- Cloud‑native, on‑premise, and hybrid deployment options
- Real‑time monitoring and remote capture on live pipelines
- Usage metrics collection and audit logging

## YAML Configuration

Edge IQ supports comprehensive YAML-based configuration for defining data pipelines, making it easy to version control and automate deployments:

- **Input Definitions**

  - Configure data sources using YAML
  - Define connection parameters, authentication, and polling intervals
  - Specify data format and parsing rules
  - Set up error handling and retry policies

- **Output Definitions**

  - Define destination endpoints and protocols
  - Configure batching and buffering settings
  - Set up data transformation rules
  - Specify error handling and retry mechanisms

- **Action Definitions**
  - Define data transformation steps
  - Configure filtering and enrichment rules
  - Set up conditional routing logic
  - Specify data validation and quality checks

Example YAML structure:

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

## Contact

**Email:** [sales@behavure.ai](mailto:sales@behavure.ai)  
**Website:** [www.behavure.ai](https://www.behavure.ai)

## Support

Need help with Edge IQ? Contact our support team at [support@behavure.ai](mailto:support@behavure.ai).
