---
title: Lookup Table
description: Definition & use of Lookup Table
---

**Lookup table** columns join a stored column with an optional table of additional attributes.

Use lookup tables to store information that you’re not collecting with your event data but that you want to associate with the shard key or other event column. If the recorded event data lacks dimensions available in other operational data stores such as customer or transaction databases, lookup tables help bring in additional columns.

There are two types of tables you can create in Measure IQ: an event table and a lookup table. Generally, Measure IQ recommends storing all of your event data in a single event table (which is different than a relational database model). However, we support lookup tables, where your primary event table can refer to a separate lookup table to do static lookups of names and details based on a field in the primary event table.

Lookup tables are analogous to Left Joins in SQL. Because you’re associating static data in the lookup table with active data (the event data you’re collecting) in your event table, lookup tables are useful for data that does not change frequently. For example: date of birth, product ID, or ISBN.

## Related terms

- [Dataset (table)](./dataset-table)
- [Shard Key](./shard-key-colocated-shard-key)

## More information

- [Best Practices for Formatting Lookup Table Data](http://localhost:4321/measure_iq/admin-guides/managing-your-data/best-practices-for-formatting-lookup-table-data)
