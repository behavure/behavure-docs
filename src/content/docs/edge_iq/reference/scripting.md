---
title: Scripting
description: Scripting
draft: true
sidebar:
  label: Scripting
  order: 1
  # badge:
  #   text: New
  #   variant: tip
---

## Purpose

`script` action like `add` action is primarily used to add new fields to events ([enrichment](/docs/advanced_usage/enriching_data)). The differentiator from `add` is that `script` can *calculate* and *conditionally* add fields.

These expressions are in [Lua](https://www.lua.org) format, with conditions such as `a > 2` and `b < 1` and expressions such as `2 * a - 1`. All event fields are available in these expressions. We also allow `!=` instead of `~=`, and `&&`.

Nested fields are accessed with a `.` and arrays are indexed with `[]`.

If our event is `{"a":{"b":1},"c":[10,20,30]}`, then the value of `1` can be accessed with `a.b`. Array values are accessed starting at _one_, so `c[1] == 10`.

:::note

For this to work field names must be valid Lua variables. Fields must start with a letter, and contain only letters, digits, and underscores. As this restriction also applies to [`extract`](/docs/dsl/actions/extract), we recommend using this format for all field names.

:::

Regular Lua keywords such as `function` or `end` can be used as field names — with the exception of `true`, `false`, `nil`, `or`, and `and`.

## Extra Functions

Apart from the usual Lua 5.4 functions in the `math`, `table` and `string` tables, we have:

- `round(x)` returns the nearest integer to a floating point number, like `round(tmillis/1000)`, useful for converting bytes to kB and milliseconds since epoch to seconds since epoch
- `count()` is the count since Pipe start
- `random(n)` is a random integer between `1` and `n`
- `pick_random(...)` returns one of multiple arguments randomly
- `sum(acc,val,cond)` and `avg(acc,val,cond)` are the running sum and average of value `val`
- `sec_s()` will return seconds since epoch, `sec_ms()` is milliseconds since epoch
- `cidr(addr, spec)` will match an IPv4 network address against a CIDR specification like '10.0.0.0/24'
- `ip2asn` uses the Team Cymru services to match IP addresses to a domain owner
- `cond(condition, value1, value2)` will return `value1` if a condition is true, and if not true returns `value2`
- `condn(...)` is similar to `cond` but for multiple conditions and values
- `array(...)` transforms its arguments into an array
- `len(v)` is the length of array or number of characters in text
- `map(...)` makes an object
- hashes:
  + `md5(txt)`
  + `sha1(txt)`
  + `sha256(txt)`
  + `sha512(txt)`
- `uuid()` returns a unique identifier each time
- `encrypt(txt,key)` encrypts text using AES-128-CBC with a key and encodes as Base64
- `decrypt(txt,key)` decrypt result of `encrypt` using the same key
- `emit(v)` writes out data directly

:::danger
Any field with one of the above names will _overwrite_ the function.
:::

### Examples

It’s convenient to use `map`to build "deep" objects. For example,
given the input `{"a":1,"b":2}` then setting `res` to `map("one",a+b,"two",a-b,"three",a*b)`
will result in `res` becoming `{"three":2,"two":-1,"one":3}`

Lua objects do not preserve order.

`condn` is useful for more complicated conditions and simple lookups. For example, `condn(a < 2,"small",a == 2, "medium",a > 2, "large)` will classify a field `a` by its size.

## Useful Standard Lua Functions

### Processing Text

- `string.upper(txt)` converts text to upper-case
- `string.lower(txt)` converts text to lower-case
- `string.sub(txt,istart,iend)` is a substring of text
- `string.find(txt,patt)` finds matching patterns
- `table.concat(txt,sep)` joins an array as text with a separator

`string.sub` is useful for trimming long strings. So setting `txt` to `string.sub(txt,1,20)` will ensure that `txt` is never longer than 20 characters.

It is possible to join (concatenate) strings together using the `..` operator. 
E.g. set `full_name` to `first_name .. " " .. second_name`.

### Mathematical Functions

- `math.ceil(x)` is the nearest greater integer e.g., `1.4` -> `2`
- `math.floor(x)` is the nearest smaller integer e.g., `1.4` -> `1`
- `math.min(...)` is the smallest of multiple values
- `math.max(...)` is the largest of multiple values
- `math.log(x,b)` is the log of `x` with base `b`
- `math.exp(x)` exponential
- `math.sin`, `math.cos` etc., are trigonometric functions (in radians)
- `math.pi`

Visit the Lua [manual](https://www.lua.org/manual/5.4/manual.html#6) for the full list of available functions.

:::note

Some functionality has been removed for safe sandboxing. This is why the global functions `require`, `dofile`, and `load` are not present.

:::

