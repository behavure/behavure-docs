---
title: "What Goes on Behind the Scenes When Data is Imported "
description: "Definition & use of What Goes on Behind the Scenes When Data is Imported "
---

Measure IQ performs data ingests for customers. This document explains what's involved when your data is imported into Measure IQ, and highlights components to consider to expedite the process.

## Getting data into Measure IQ

Importing data into a Scuba cluster is a multi-step process and is the same for all forms of ingest:

- **One-Time**: A file or batch of files, ingested at a prescribed time (data-at-rest).
- **Continuous**: A pipeline (like a cron job) that pushes content into the cluster at a steady rate (data-in-motion).

The Scuba import process can be broken down into the following phases:

1. Download the data
2. Transform the data
3. Concatenate the data into batches
4. Schematize the batches
5. Distribute the data

### 1\. Download the data

Data is downloaded from your [Amazon Web Services (AWS)](../https://aws.amazon.com/), [Microsoft Azure](../https://azure.microsoft.com/en-us/?v=17.44), or other cloud platform environment. The structure of your data can affect how long it takes to ingest into Measure IQ and be made available for queries. For more information, see [What to think about before you add data](../what-to-think-about-before-you-add-data).

### 2\. Transform the data

JSON is the preferred format for Measure IQ. Other formats are supported, however, all other formats require transformation into JSON before being ingested into Measure IQ. The format and organization of your data can affect how long it takes to process or transform. The more transformations that are required, the longer the ingest process will be. For more information, see [Best practices for formatting data for ingest](../best-practices-for-formatting-data-for-ingest).

### 3\. Concatenate the data into batches

After the data is transformed, the files are concatenated into batches. Concatenating transformed files into batches is necessary prior to importing them into Measure IQ. The size of your data files affects the resulting batches. Consider the following when structuring your data for smoother ingests:

- The default batch size is 1 GB.
- There is a limit to how many batches can be processed at one time.
- If the file size is too small, it takes longer to create batches.
- If the file size is too large, it takes longer to upload the batches.
- For optimum ingest times, it is recommended file sizes be between 100-300 MB compressed.

### 4\. Schematize the batches

The batches are schematized prior to import. This means each row of a batch is reviewed to determine the following:

- Is there a valid time stamp?
- Are there any new columns?
- Where should the data go, to which node and folder?

### 5\. Distribute the data

After the batches are schematized, the data is sent to the appropriate nodes (data, string, etc), and the following occurs:

- The imported batch files are deleted from the import node.
- Records are placed in the Measure IQ SQL database documenting the import of each file. The records contain information on the original file size, the transformed file size, how many lines each file contains, which machine imported the file (if there are multiple import nodes), and if the import was successful or something went wrong.

## Ways to increase import speed

Measure IQ processes thousands of lines of data per second. There are several conditions that can influence Measure IQ's processing speed. If you think your imports are lagging, consider making adjustments in the following areas.

- **The number of import nodes in your cluster.** If you are importing a large volume of data and are not satisfied with the performance, you may need to increase the number of import nodes on your cluster. In general, it is recommended that you have _1_ import node for every _4_ data nodes. However, you can add ingest nodes to accommodate bulk imports, then remove the extra nodes after the bulk import is done. For more information, see [Planning your Measure IQ deployment](../admin-guides/planning-your-scuba-deployment) and consult with your Measure IQ technical customer success manager (TCSM).
- **The number of data and string nodes in your cluster.** The main constraint for a data tier is disk space. However, beware of under-provisioning the CPU and memory resources as it can result in reduced performance. You should also consider your expected data retention, and adjust your data node configuration accordingly. The main constraint for a string tier is disk space, though sufficient memory is important as well. SSDs are strongly recommended for the string tier. Use an odd number of string nodes, 3 or 5 such instances, and keep an eye on the disk usage. For more information, see [Planning your Measure IQ deployment](../admin-guides/planning-your-scuba-deployment) and consult with your TSCM.
- **The number of files and their size.** The number of files you are importing can affect the time it takes for the data to be processed. A large number of files will take longer to transform and ingest.File size is another important consideration for performance. If the files are too small, it will take longer to create batch files. If the files are too large, they take longer to transform and upload. The optimum file size is between 100 MB and 300 MB. For more information, see [What you should know about structuring your data](../what-you-should-know-about-structuring-your-data) and consult with your TCSM.
- **The size of the batch files.** Batch file size can affect import speed. If batch files are too large, they take longer to process. Review the previous sections on concatenating data into batches and the number of files and their size, then consult with your TCSM.
- **The number of batches processed at a time.** The number of batch files that are processed at one time can affect the import speed. Performance can lag if the size of the batch files is large, as well as processing too many at once. Review the previous sections on concatenating data into batches and the size of batch files, then consult with your TCSM.
- **The number of jobs running simultaneously.** The number of overall jobs running at one time can affect import speed. Modifying the configuration of your cluster may be necessary to accommodate your data. For more information, see [Planning your Measure IQ deployment](../admin-guides/planning-your-scuba-deployment) and consult with your TCSM.

## Resources

- [What to Think About Before You Add Data](../what-to-think-about-before-you-add-data)
- [Data Logging](../measure_iq/key-concepts-and-terminology/data-pipeline/data-logging)
- [Data Deduplication](../https://behavure.ai/docs/wiki/spaces/SGV/pages/2207940609/Import+Data+DeDuplication+v5)
- [Planning Your Measure IQ Deployment](../admin-guides/planning-your-scuba-deployment)
