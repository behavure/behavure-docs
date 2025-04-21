---
title: Job actions
description: Job actions
slug: jobs/actions
sidebar:
  label: Actions
  order: 14
---

In jobs, various actions are available to perform simple and advanced data transformation and manipulation. The actions configured in a Job are executed sequentially, after Job input, and before Job output.

## Terminology

Data which enters and flows through Jobs are referred to as **event data**. For example, when reading multiple lines from a log file, each line's text enters the Job as a single **event**. Each input determines how input data is structured into discreet events.

Events are typically represented as JSON within Jobs. Actions typically operate on **fields** within an event's JSON representation. For example, the basic add, remove and rename actions are field-level transformations.

## Concept Mappings

E.g. 'I want to use regular expressions':

- _extract_: extract fields using a regular expression with groups
- _extract_: substitute text using `output-pattern`
- _filter_: pass through events if field values match (`how:patterns`) or not (`how:exclude`)

Some people might be aware of `extract` as **grok** in other systems.

Can arrive at _filter_ from more direct questions like 'Only pass through certain events?', 'Enforce schema?'.

Multiple ways of accessing this information. For instance, a FAQ is a good old-fashioned way, very searchable.

'I want to reshape/manipulate events'

- _add_: new fields - can `overwrite`. The new values may contain _variable expansions_.
- _copy_: new fields copied from other parts of the event, using JSONPath notation.
- _script_: new fields initialized using _Lua expressions_.
- _remove_: existing fields. May choose to complain if not present.
- _flatten_: remove any 'nested' objects in the event, force it to be flat.

So there's a number of words like 'reshape' or 'manipulate' which point to the same need.

'I want to convert text into numbers'

- _convert_: specify fields and the desired type, e.g. 'num'. Can just set `auto` to get a reasonable guess.
- _csv_: can specify 'num' etc. when defining columns. There is `autoconvert`.
- _extract_: can optionally specify this with `convert` parameter.

_Conversion_ is a very broad concept, including time! _convert_ is more UI discoverable than before, since `conversions` presents a drop-down of the conversion options, rather than having to remember the magic words. (There is also `units` similarly for the question 'How do I convert units?' )
