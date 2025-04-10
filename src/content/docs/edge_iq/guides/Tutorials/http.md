---
title: Making an HTTP Request
description: Making an HTTP Request
slug: guides/tutorials/http
sidebar:
  label: Making an HTTP Request
  order: 2
---

## Making a Request

This input will make a HTTP request - by default 'GET'. 

A useful testing URL is `https://httpbin.org/anything`, because it will return exactly what it received in the request.

First, set `Url` to this.

It will return a single JSON document, formatted over multiple lines, so the first thing we need to do is set `JSON` and `Ignore Line Breaks`  to both being true, since the default is false.

To quickly see the result, click on the `Run & Trace` button on the the top left.

The result will appear on the right hand size next to the editor items:

```json
{
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip",
    "Content-Type": "application/json",
    "Host": "httpbin.org",
    "X-Amzn-Trace-Id": "Root=1-6757ea61-75eabe7826c84e78192f3070"
  },
  "json": null,
  "method": "GET",
  "origin": "197.91.187.145",
  "url": "https://httpbin.org/anything"
}
```

We can now add various items to the request:
- set new `Headers`
- set `Query`
- set `Body`

```json
{
  "args": {
    "ITEM": "1"
  },
  "data": "{\"greeting\": \"hello\"}",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip",
    "Content-Length": "21",
    "Content-Type": "application/json",
    "Host": "httpbin.org",
    "X-Amzn-Trace-Id": "Root=1-6757ef19-565679cf4b1943387934ef77",
    "X-My-Header": "HELLO"
  },
  "json": {
    "greeting": "hello"
  },
  "method": "POST",
  "origin": "197.91.187.145",
  "url": "https://httpbin.org/anything?ITEM=1"
}

```

## Streaming Data

It is common for inputs to return multiple lines, each representing a single event

For instance, if the `Url` is `https://httpbin.org/stream/5` then we get 5 JSON objects.

So `JSON` must be enabled, but not `Ignore Line Breaks`.

Each one of these events will pass through all the steps; if you click `Run` and go to `Run Output` then you will see each event has an added time field from the `Time` action.

## Repeating the Request

The next step is scheduling it to happen more than once - select `Trigger` and then `Interval`.

There are two time-based ways to schedule jobs - this is a simple duration expressed in human units (for instance "5h" etc.)  If you need to run a job at precise times like on the hour, then `Cron`
is preferred.

You can safely hit `Run` because these _transient_ jobs will always end:

- the _event limit_ was reached
- the _time limit_ was reached
- there was an error
- the job was cancelled

Click the `Run Output` button, and click `Run`:

Notice the `Run time limit` and the `Output event limit`. 

If left alone, our scheduled job will end when 10 seconds is up - the default run time limit. We will get 5 events, as expected.

While running, the `Cancel Job` button is active and can be used to bail out at any time. 

