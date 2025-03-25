---
title: "What You Should Know About Structuring Your Data "
description: "Definition & use of What You Should Know About Structuring Your Data "
---
Data structure is the format, organization, and way in which you store data so it can be accessed and modified efficiently. The structure of your data is important, as it can affect how long it takes to ingest into Measure IQ and be made available for queries. Data structure can also affect performance; the time it takes to view the results of your queries. 

This document outlines the topics your Measure IQ onboarding team will discuss with you prior to uploading your data into your Measure IQ cluster. Become familiar with these topics as they apply to your data so you can optimize performance with Measure IQ.

## Data format and organization 

The format and organization of your data can affect how long it takes to process (transform), ingest (into Measure IQ), and be available to query. 

### Data formats 

- JSON is Measure IQ's preferred file formats, for ease of transformation and ingest. Other formats are supported, as well. Be sure to discuss the format of your data with your Measure IQ onboarding team.
- ASCII format is preferred, and table names and column names must be in ASCII.
- Unicode is encoded as UTF-8 strings on import.
- File size is also a consideration for performance. The smaller the file size, the faster the data will be available to you in Measure IQ. Large files take longer to load and transform, and therefore it takes longer for the data to be available to you in Measure IQ.
- The number of files can affect the time it takes for the data to be available in Measure IQ, as well. A large number of files will take longer to transform and ingest. 
- Measure IQ recommends that you format your timestamp data according to the [ISO-8601 standard](../https://en.wikipedia.org/wiki/ISO_8601). For example, `2015-10-05T14:48:00.000Z`, which has a format string of `%Y-%m-%dT%H:%M:%S.%fZ`. If your timestamps do not follow the ISO-8601 standard or you cannot reformat your timestamps to follow the standard, Measure IQ also supports Unix time plus a variety of common `strptime()` time format strings.

### Data organization 

- A logical organizational hierarchy improves the ingest time for your data.
- Proof read your data for accuracy. Typos and other inherent errors can cause problems and impede performance.
- When you have new data you want uploaded into Measure IQ, where will it be stored? Will you use Amazon S3 or Microsoft Azure?
- Your data should be auditable. It should be easy to tell which file an event came from.
- Measure IQ strongly recommends that you use the following directory structure format: `mydata/{year}/{month}/{day}/{hour}/`

## Tables, shard keys, and columns 

The number and types of tables in which you store your data on Measure IQ, the number of shard keys you use, and the number of columns and column names are important to performance and necessary storage capacity.

- You should consider starting with one table. If you realize the data is too disorganized, then create another table.
- Each shard key requires a copy of *all* of your data. Think carefully about how many shard keys are necessary for your data, as it directly affects the storage you'll need.
- Think about the number of columns you need. If a column isn't necessary, then it should be omitted. The more columns there are, the slower performance will be.
- Auto-generated column names that are based on data can cause an explosion of columns in the system (and these columns are typically not easy to work with in a dashboard). 
- Think about what data should be stored in event tables and what data should be stored in lookup tables.
- The less string columns in your data, the faster the performance will be.
- In certain cases, string columns can be hexed and stored in the data tier. For example, a string column can only contain digits 0-9a-f and any spaces or punctuation will be stripped out. Storing strings as hex also eliminates the ability to do text matching queries on them. 

## Your expectations 

At Scuba Analytics, we want all of our customers to be happy with our product. An important factor in ensuring your happiness is managing your expectations. Please discuss the following topics with your Measure IQ onboarding team:

- How much latency do you expect? Do you want new data uploaded every minute, three minutes, ten minutes, or longer?
- How much data retention does your company require? Is 3-6 months sufficient, or do you require 13 months for year-over-year analytics?
- Do you expect to use Measure IQ as a primary data storage tool, or a primary data visualization tool?

## More information 

- [Best Practices for Formatting Data for Ingest](../best-practices-for-formatting-data-for-ingest)
- [Best Practices for Formatting Lookup Table Data](../best-practices-for-formatting-lookup-table-data)
- [Data Types Reference](../data-types-reference)
- [Intro to Lookup Tables](../intro-to-lookup-tables)
- [What to Think About Before You Add Data](../what-to-think-about-before-you-add-data)