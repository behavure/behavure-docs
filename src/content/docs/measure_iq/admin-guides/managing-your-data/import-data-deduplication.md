---
title: "Import Data Deduplication"
description: "Learn how Measure IQ prevents duplicate data during import"
---

You've learned what happens behind the scenes when [Measure IQ ingests your data](/measure_iq/admin-guides/managing-your-data/what-goes-on-behind-the-scenes-when-data-is-imported). This document explains what safeguards are in place to ensure that Measure IQ does not ingest duplicate records.

## Deduplication

Measure IQ has two layers of duplicate protection: file hashing and event checks.

### File Hashing

First, Measure IQ evaluates every file that arrives in your cloud storage solution for its upload time, size, name, and other information. It then assigns it a hash. Measure IQ then begins ingesting this file into your data tier.

For ingest jobs that may revisit the same directory in your cloud storage solution over the course of days, your files are again evaluated and hashed. When a hash matches that of an existing file it is then ignored as a duplicate. If anything has changed about a previously downloaded file (upload time, size, arrangement of fields, column names etc.) a new hash will be generated. The file will be seen as new, and it will then be ingested.

### Event Checks

For the second layer of deduplication, the data tier checks incoming events against stored events and discards events that are already stored. For a duplicate event to be dropped in this stage, the event must be exactly the same. All fields must be named the same, all properties must contain the exact same information, and all fields/properties must be in the same order.

### Example:

**File Hashing:**

Measure IQ has a daily ingest job that has a 3-day look back, meaning it will scan its target directory structure for folders and files once a day for 3 days.

On Day one it encounters a file called muppets_6-23-2023.json that contains the following:

| **Timestamp**         | **ID** | **Muppet Name** | **action**   | **Language** | **location** |
| --------------------- | ------ | --------------- | ------------ | ------------ | ------------ |
| 6/23/2023  1:01:01 AM | 1      | Kermit          | hosts        | English      | main stage   |
| 6/23/2023  1:10:01 AM | 2      | Animal          | plays drums  | Howling      | main stage   |
| 6/23/2023  1:15:01 AM | 3      | Fozzy Bear      | tells a joke | English      | main stage   |
| 6/23/2023  1:20:01 AM | 4      | Rolf            | plays piano  | English      | piano bar    |
| 6/23/2023  1:05:01 AM | 5      | Chef            | throws fish  | Swedish      | kitchen      |

A unique hash is created, logged and the file is ingested.

On Day two, ingest creates a hash for muppets_6-23-2023.json and compares it to the existing hash. The file is the same, the hashes are the same. Muppets_6-23-2023.json is ignored.

On Day three, ingest evaluates muppets6-23-2023.json. This time the file is:

| **Timestamp**         | **ID** | **Muppet Name** | **action**            | **Language** | **location** |
| --------------------- | ------ | --------------- | --------------------- | ------------ | ------------ |
| 6/23/2023  1:01:01 AM | 1      | Kermit          | hosts                 | English      | main stage   |
| 6/23/2023  1:10:01 AM | 2      | Animal          | plays drums           | Howling      | main stage   |
| 6/23/2023  1:15:01 AM | 3      | Fozzy Bear      | tells a joke          | English      | main stage   |
| 6/23/2023  1:20:01 AM | 4      | Rolf            | plays piano           | English      | piano bar    |
| 6/23/2023  1:05:01 AM | 5      | Chef            | throws fish           | Swedish      | kitchen      |
| 6/23/2023  1:25:01 AM | 6      | Gonzo           | soars through the air | English      | trapeze      |
| 6/23/2023  1:30:01 AM | 4      | Rolf            | takes a nap           | English      | back stage   |

As another row has been added, the file size is different, the hash will be different and the file will be ingested.

**Event Checking:**

In this example, on the third day's pass, only the new record will be ingested as event checking will evaluate each row for duplication, ignore the first 5 records, and ingest the last 2.

|                       |        |                 |                       |              |              |
| --------------------- | ------ | --------------- | --------------------- | ------------ | ------------ |
| **Timestamp**         | **ID** | **Muppet Name** | **action**            | **Language** | **location** |
| 6/23/2023  1:25:01 AM | 6      | Gonzo           | soars through the air | English      | trapeze      |
| 6/23/2023  1:30:01 AM | 4      | Rolf            | takes a nap           | English      | back stage   |

## Resources

- [What to Think About Before You Add Data](/measure_iq/admin-guides/managing-your-data/what-to-think-about-before-you-add-data)
- [Data Logging](/measure_iq/key-concepts-and-terminology/data-pipeline/data-logging)
- [Planning Your Measure IQ Deployment](/measure_iq/admin-guides/planning-your-measure-iq-deployment)
