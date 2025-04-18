---
title: System Requirements
description: System Requirements for Edge IQ
slug: start/system-requirements
sidebar:
  label: System Requirements
  order: 2
---

Edge IQ is deployed as a single binary without external dependencies, making it easy to install and maintain.

## Supported Operating Systems

Edge IQ is available for 64-bit Linux, Windows, and macOS. Server and worker processes are interoperable between different operating systems, allowing for flexible deployment configurations.

## Recommended Hardware

The following specifications are recommended for optimal performance:

| OS           | Architecture | RAM  | CPU Cores | Disk Space |
| ------------ | ------------ | ---- | --------- | ---------- |
| Linux (gnu)  | x86-64       | 4 GB | 4 cores   | 10 GB      |
| Linux (musl) | x86-64       | 4 GB | 4 cores   | 10 GB      |
| Linux (gnu)  | aarch64      | 4 GB | 4 cores   | 10 GB      |
| Linux (musl) | aarch64      | 4 GB | 4 cores   | 10 GB      |
| macOS        | x86-64       | 8 GB | 4 cores   | 10 GB      |
| macOS        | aarch64      | 8 GB | 4 cores   | 10 GB      |
| Windows      | x86-64       | 8 GB | 4 cores   | 10 GB      |

:::note
These are minimum recommended specifications. Actual requirements may vary based on your specific use case, data volume, and processing needs.
:::

## Supported Operating System Versions

Edge IQ supports the following minimum versions for each operating system:

| OS           | Architecture | Minimum Versions          |
| ------------ | ------------ | ------------------------- |
| Linux (gnu)  | x86-64       | kernel 3.2+, glibc 2.17+  |
| Linux (musl) | x86-64       | kernel 3.2+, musl 1.2.3   |
| Linux (gnu)  | aarch64      | kernel 4.1+, glibc 2.17+  |
| Linux (musl) | aarch64      | kernel 4.1+, musl 1.2.3   |
| macOS        | x86-64       | macOS 10.12+, Sierra+     |
| macOS        | aarch64      | macOS 11.0+, Big Sur+     |
| Windows      | x86-64       | Windows 10+, Server 2016+ |

## Sizing and Scaling

:::note
More detailed information about sizing and scaling will be available soon.
:::

For optimal performance, consider the following factors when sizing your Edge IQ deployment:

1. **Data Volume**: The amount of data processed per day
2. **Processing Complexity**: The number and complexity of transformations
3. **Concurrent Jobs**: The number of jobs running simultaneously
4. **Network Requirements**: Bandwidth and latency considerations
5. **Storage Requirements**: Data retention and backup needs
