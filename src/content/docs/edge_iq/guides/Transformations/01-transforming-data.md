---
title: Transforming Data
description: Transforming Data in Jobs
draft: true
---

## Overview

The _transform_ part of ETL involves transforming data into more convenient forms for storage and later processing. Event data is manipulated in JSON format - if it's not initially then it is _quoted_ using a special field `_raw` (e.g. `{"_raw":"10,2.4,Data is not Always JSON"}`).

We first convert data into JSON if necessary and reshaping the resulting events.

## Converting Text into JSON

Once data is in this canonical form of 'single-line' JSON events, then it can be further reshaped; converting values, removing fields, adding or copying fields.

If it is not already JSON then it first needs to be converted from existing formats like CSV or XML - this is called _expansion_. Or data needs to be _extracted_ from text using regular expressions (similar to the common 'grok' operation)

Another example of expansion is taking a JSON document containing an array, and expanding that into multiple events for each value in that array.

All of these operations allow specifying the `Input Field`, which defaults to `_raw`. Can choose to `Remove` this field after processing. By default, warnings are raised, but they can be suppressed.

### CSV

There are a number of options for the _CSV action_, because there are multiple ways that the data is presented.

If reading a document that starts with a CSV header, then enable the `Header` option. If you already know the columns, then `Fields` can be used to specify the name and the _type_ of each column (e.g. 'str' or 'num'). Or simply `Gen Headers` to get `_1`, `_2` etc. But you must specify one of these to proceed. Unless specified exactly with `Fields` the columns are auto-converted where possible.

The default delimiter is a comma, but this can be overriden with `Delim`. Can use `\t` to specify the common case of tab-separated columns.

### Key Value

This is a common in some log formats, e.g. `age=52,name=bilbo,score=5.2`. The `Delim` defaults to comma, but there is also a `Key Value Delim` which defaults to `=`. There is no need for headers since the field names are explicit. Use `Autocorrect` to convert into numbers if possible.

There might be multiple key-value pairs with the same keys - use `Multiple` to specify how to resolve this case.

### Extract

This uses the full power of regular expressions, so this is the most general JSON conversion.

You provide `Pattern` which is a regular expression, optionally with named groups. If there are no named groups, there are two options: just provide them with `Output Fields` or specify the fields and their types (like with `CSV` above) with `Convert`.

By default, if the pattern does not match, the event just passes through unaffected. So you can have multiple `extract` actions working on different kinds of data. 

If `Drop` is specified, we don't pass through if we fail, which is useful for filtering out bad data.

## Converting Individual Data Fields

### Convert

Once the data is in JSON format, you may wish to have more control over conversions. The `convert` action goes way beyond simple conversions to numbers, etc.

For instance, text fields containing JSON can be converted to JSON; fields containing comma-separated lists can be converted to JSON arrays.

Common unit conversions like expressing file sizes in megabytes are available with `Conversions`.

### Time

The `time` action can be used to convert between times in different formats, if you provide an `Input Field` and an `Input Format`. For instance, if we have a timestamp which is seconds since the UNIX epoch, then a format of `%s` will parse it. You always have to provide `Output Field`; the `Output Format` has a reasonable ISO default.

## Adding, Copying and Removing Fields

### Add

The `add` action can create a new field from either text (`Add as Text`) or inline JSON (`Add as JSON`). (If you toggle `Overwrite` then the field need not be new)

These text can contain [variable expansions](../../reference/variable_expansion.md). This is like the reverse of extraction: combining various field values into text, like "`${name}-${age}`". Note that the expansions can use JSONPath expressions like `${context.age}`.

There is a difference here between how text and JSON is interpreted. If I define the new field `extras` as `{"stuff":"always at ${age}","comments":"never"}` then I would usually want this to be understood at as a nested JSON object:

```json
{
  "age": "52",
  "extras": {
    "comments": "never",
    "stuff": "always at 52"
  }
}
```
Note that any text values of the fields can also contain variable expansions.

### Script

This is the version of `Add` where the values of new fields are _computed_ using Lua expressions.

There are the usual Lua functions like `string.upper`,`string.lower` and `string.sub` for [string manipulation](../../reference/scripting.md#useful-standard-lua-functions)

Some specialized conversions can only be done using `Script`; e.g. `tonumber(field,16)` will convert hexadecimal numbers into decimal.

Some [useful functions](../../reference/scripting.md#extra-functions) EW defined; converting to and from base64, calculating hashes and encryping secrets.

### Copy

With `Copy` action both the destination and the source of the copy are specified with JSONPath.
Together with the `Remove` action this is a very powerful way to restructure events.

It can copy _nested objects_ from one part of the document to another. For instance, given `{"a": {"b": [10,20]}}` then copying from `$.a.b` to `arr` will give `{"a":{"b":[10,20]},"arr":[10,20]}`. And then `a.b` can be removed.

### Remove

To remove fields, provide a list of fields - they can end with a `*` wildcard.

## Expanding and Filtering Events

Sometimes data arrives as a large JSON document, containing arrays of data. It is best to work with many individual events instead. Bear in mind that `Http Poll` has `Events Field`, which is an array-valued field containing the actual events; this is common with API bulk data requests.

The other side of the coin is where we receive a large number of events and wish to process & store only those events which are needed for our application. Events of low salience can be *filtered* out. 

:::Note
The `Condition` field does not filter events; if present, it decides whether this action will _process_ a event. So, an action can be disabled by setting `Condition` to "false", and the events will be passed to the next action or output (this is how the UI `Disable Ation` feature works)
:::

### Expand Events

This tries to expand any arrays in a large document. For example, we come in with `{"a":"ay","b":[{"msg":"hello"},{"msg":"goodbye"}]}` and end up with two events:

```json
{"a":"ay","b":{"msg":"hello"}}
{"a":"ay","b":{"msg":"goodbye"}}
```

If we had nested arrays:

```json
{
  "a": "ay",
  "b": [
    {
      "msg": [
        10,
        20
      ]
    },
    {
      "msg": [
        100,
        200
      ]
    }
  ]
}
```

then _four_ events are generated, `{"a":"ay","b":{"msg":10}}` etc.

### Filter

These are the ways an event can be filtered, that is, not passed to the next action.

 - `Empty` the event has no fields `{}` or no data `{"_raw":""}`
 - `Patterns` field names and regular expressions that must match their values
 - `Exclude` like `Patterns` except must _not_ match
 - `Schema` provide a list of field names that _must_ be present in the event
 - `Expression` a Lua expression that must be true for the event to be passed on.

For example, with the above events, setting `Expression` to `b.msg > 10` will exclude `{"a":"ay","b":{"msg":10}}`.








