---
title: "Intro to Lookup Tables "
description: "Definition & use of Intro to Lookup Tables "
---
There are two types of tables you can create in Scuba: an event table and a lookup table. Generally, Scuba recommends storing all of your event data in a single event table (which is different than a relational database model). However, we support lookup tables, where your primary event table can refer to a separate lookup table to do static lookups of names and details based on a field in the primary event table.

You can create a lookup table that contains information that you’re not collecting with your event data but that you want to associate with the shard key.

Lookup tables are analogous to Left Joins in SQL. Because you’re associating static data in the lookup table with active data (the event data you’re collecting) in your event table, lookup tables are useful for data that does not change frequently. For example, date of birth, product ID, or ISBN. 

For example, let’s say you have a primary event table with a `userId` column. You may have information about your users that isn’t collected as part of the event data. For example, when a user creates an account, you ask them for their name, birthday, and email address. This information isn’t part of the event data, but you want to be able to query on it. 

What happens if the user gets a new email address? You can update the lookup table value to have the user’s latest email address and because lookup tables are joined to event data at read time, all event data queries that reference `userId.email_address` will instantly display the updated email address.

You can join a lookup table containing `userId`, `name`, and `birthday` where there is a one-to-one mapping between the `userId` values in the primary event table and the new lookup table. Then Scuba will show you a list of fields like `userId.name` and `userId.birthday` that you can use in your queries. 

## Accessing lookup table data in the user interface

If you create a lookup table with columns `id` and `email` and attach it to an event data table based on the column `user`, the user interface will show a new set of virtual columns: `user.id` and `user.email`. These virtual columns can be referenced just like regular columns.

You cannot query lookup table directly from the Scuba application. You can only access this data as a read-time join to an event data query.

## Storage options for lookup tables

You can store the lookup data itself as either sharded (spread across data nodes to save space) or unsharded (copied fully onto every data node). The sharded storage mode is more efficient in terms of disk space used, but there are some restrictions about building queries that use sharded lookup tables.

If you store the lookup table as a sharded table, then the data must be joined to one of the shard keys, or actor fields, in your event dataset. Because of this, you need to reference that shard key when running a query that references any columns in the lookup table. 

For example, let’s say you have two shard keys in your dataset: `userId` and `OrganizationId`. If you join your lookup table to `userId`, then all queries that reference columns in that lookup table must use the `userId` shard key. You can’t run any queries that use the `OrganizationId` shard key, since Scuba doesn’t support querying on more than one shard key. 

If you store the lookup table as unsharded data, a copy of the lookup table must be copied to every data node. However, you can join the lookup table to any column in your data (the column doesn’t need to be a shard key) and you can reference any of the lookup table columns in a query without using a specific shard key. 

Use this table as a reference:

| Question | Sharded Lookup table | Unsharded Lookup table |
| --- | --- | --- |
| Can it be joined on a shard key? | Yes | Yes |
| Can it be joined on a non-shard key? | No  | Yes |

If you need to join a lookup table to a column that is not a shard key, then you must create an *unsharded* lookup table. For example, if your dataset uses `userId` as a shard key, but you want to include more information about the products your users are buying (such as manufacturer, unit cost, model numbers) that isn’t logged with event data, but you don’t have a `productId` shard key. In this case, you can create an unsharded lookup table and join it to an non-shard key column in your dataset, and reference those columns (`manufacturer`, `unitCost`, `modelNum`) in your queries. 

We do not support “sharing” a single lookup table with multiple event tables. You must join a lookup table to exactly one event table. 

## Limitations and costs of unsharded lookup tables

Creating an unsharded lookup table offers more options for creating queries, but there are tradeoffs to that flexibility. 

For unsharded lookup tables, you must have a complete copy of the table on each data server. Because lookup tables are stored in memory, we support the unsharded option for lookup tables with up to 10 million rows. Tables larger than that must be sharded due to memory requirements. So unsharded tables give you more flexibility in terms of queries that you can create, but come with greater resource requirements. 

## Ingesting additional data

Once you’ve created lookup tables, you can import data via the standard Scuba pipeline service. There are two main reasons to import new data:

- Update existing data (for example, changing a manufacturer ID or SKU)
- Add new data (adding lookup table data for new actors)

You only need to provide us with the changed (or new) data; you do not need to provide the entire lookup table (although you can). So if you’re adding data to account for new users (and the existing data is remaining the same), just send us the new data to ingest. 

Scuba updates lookup tables on a row-by-row basis. In addition, if a user starts a query during the update process, the update will stop and wait until the query is finished. When querying while a lookup table is being updated, the lookup data may be in an inconsistent state, where only some of rows have been updated.

## Updating and overwriting lookup table information

Lookup tables have no sense of time. Lookup tables can only have one entry per primary key and updating the information will overwrite existing data. The most recently imported value will always take precedence. If you overwrite existing data in a lookup table column, those values will be returned for all queries that reference that column, even if the query is for data prior to when you updated the lookup table. 

For example, userId 104234 updates their mailing address from San Francisco to New York City. 

|     | userId | mailingCity |
| --- | --- | --- |
| Previous row | 104324 | San Francisco |
| Updated row | 104324 | New York City |

The most recently imported value (New York City) will overwrite the previous value (San Francisco). If you query data for `userId.mailingCity`, you will get “New York City,” even if your query includes a time before the row was updated.

### Lookup tables and null values

When updating a row of an existing lookup table, you cannot reset a non-null value back to null. So if your lookup table has a row like:

|     |     |     |     |
| --- | --- | --- | --- |
| Foo | Bar | Zoo | Zoobar |

You cannot update the Zoo value to be an empty null (if Scuba sees a null value, it will not update the entry). Instead, you can use a literal null value like NULL and set the value to:

|     |     |     |     |
| --- | --- | --- | --- |
| Foo | Bar | NULL | Zoobar |

### Lookup tables and decimal values

Decimal (float) values are not currently supported in lookup tables. Upon ingestion, decimal values will not be ingested, resulting in empty values for the corresponding column/rows. Please convert decimal values to integer (whole number) format so that they can be added and used in your lookup table, or reach out to the Scuba team at [help@scuba.io](../mailto:help@scuba.io) so we can update the column’s data type after ingestion.