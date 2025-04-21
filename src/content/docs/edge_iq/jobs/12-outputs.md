---
title: Job outputs
description: Job outputs
slug: jobs/outputs
sidebar:
  label: Outputs
  order: 12
---

## Output Batching

Events flow through jobs as individual JSON documents and it is useful to _batch them together_ for outputs.

For instance, it is much more efficient to send a batch of a 1000 events than 1000 requests with one event each in HTTP. For this you configure the `Batch` option with `Mode` as Fixed, and `Fixed Size` set to 1000.

With an intermittent, 'bursty' event stream this can lead to batches held up until enough events arrive to fill the batch. So set `Timeout` to the duration after which the batch will be sent, full or not.

## Documents

The other option is when `Mode` is set to Document. Many inputs naturally create groups of events, for instance each file read by _input-files_ will consist of many events.

Document mode is a way for the output to respect the input grouping of events.

## Headers and Footers

If set `Header` will be written before the the events in the batch, and if set `Footer` will be written at the end.

These may contain _variable expansions_.

## Wrap as JSON

The `Wrap as JSON` option does two things to the JSON events

- adds a comma
- wraps them in `[` and `]`

Which makes the batch a valid JSON array.

This is essential if submitting multiple events to API endpoints. With a creative use of headers & footers a full payload can be created. For instance can set `Header` to '{ "events":' and `Footer` to '}'.
