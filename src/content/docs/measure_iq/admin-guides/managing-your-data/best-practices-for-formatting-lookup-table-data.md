---
title: "Best Practices for Formatting Lookup Table Data "
description: "Definition & use of Best Practices for Formatting Lookup Table Data "
---
## What are lookup tables?

Lookup tables are similar to what you might call "join tables". They allow us to link a certain field (e.g. user\_id) to other fields where there is an n:1 relationship without having to import every field with every event.

For example, say my user\_id is 555, my name is Diane, and my favorite TV dog is Comet from Full House. Without a lookup table, you could reference this information across all events by importing it as a column on every event:

`{"user_id": "555", "username": "Diane", "fave_dog": "Comet", "event_name": "login"},`

`{"user_id": "555", "username": "Diane", "fave_dog": "Comet", "event_name": "page_view"},`

`{"user_id": "555", "username": "Diane", "fave_dog": "Comet", "event_name": "logout"}`

Now imagine we have a lookup table joined on user\_id and containing the columns "username" and "fave\_dog." We can do this as long as one user\_id always maps to one username and one fave\_dog. Then we can import these events into the event table:

`{"user_id": "555", "event_name": "login"},`

`{"user_id": "555", "event_name": "page_view"},`

`{"user_id": "555", "event_name": "logout"}`

Our lookup table looks like this:

`...`

`{"user_id": "555", "username": "Diane", "fave_dog": "Comet"}`

`...`

or like this, if you prefer to picture it as an actual table:

|     |     |     |
| --- | --- | --- |
| **user\_id** | **username** | **fave\_dog** |
| ... |     |     |
| 555 | Diane | Comet |
| ... |     |     |

Now we can *reference* my username and fave\_dog on all of my events without having to *import* this redundant information with every event.

### Lookup table import

Lookup tables are static. In other words, they are not stateful. Imagine you're a lookup table. If I tell you on Feb 1 that my name is Pryan, and then I tell you on March 1 that my name is Snowflake, and then Max asks you on March 2 what my name is, you say Snowflake. You have no record of me ever having a name other than Snowflake. I only get one row in the lookup table, so when my info changes, the old info gets overwritten. 

This is part of why lookup tables are helpful--they save a lot of space and keep us from having to resolve conflicting/outdated information. On the other hand, this also means that lookup table import is slightly different from event table import. 

At a high level, when we import a row to an event table, we just append the row to the existing dataset. When we import a row to a lookup table, we append and/or overwrite information, according to the following rules:

- If there is no lookup table entry for the join column value, we create a new one from the current row. 
- If there is a lookup table entry for the join column value, we need to update that entry. Now we need to work on a column-by-column basis. For each column in the new row:
- If this column is not in the current entry, add it to the current entry.
- If this column is in the current entry, overwrite the existing value with the new value.

So, depending on what is in the lookup table currently, we might add information, update information, or both. 

**Example:**

I create a new lookup table with user\_id as the join column. Then I import the following rows:

`{"user_id": "1", "name": "Max", "team": "support"},`

`{"user_id": "2", "name": "Emily", "team": "success"}`

Here's what my lookup table looks like initially:

| **user\_id** | **name** | **team** |
| --- | --- | --- |
| 1   | Max | support |
| 2   | Emily | success |

Next, I import this row:

`{"user_id": "4", "name": "Pryan", "team": "success"}`

So now my lookup table looks like this:

| **user\_id** | **name** | **team** |
| --- | --- | --- |
| 1   | Max | support |
| 2   | Emily | success |
| 4   | Pryan | success |

Then I import this row:

`{"user_id": "4", "team": "support", "location": "carpet"}`

There is already a row for `user_id=4`, so we append/update column values. Now the table looks like:

| **user\_id** | **name** | **team** | **location** |
| --- | --- | --- | --- |
| 1   | Max | support |     |
| 2   | Emily | success |     |
| 4   | Pryan | support | carpet |

What just happened?

- There was already a "team" value for `user_id=4`, so we updated it.
- There was no "location" value for `user_id=4,` so we added it.
- The new row didn't say anything about "name", so we left it alone.

## What's the point?

:::note
Because lookup table import involves appending or overwriting information based on the current status of the table, the order in which rows are imported matters.
:::

Consider this lookup table:

|     |     |     |     |
| --- | --- | --- | --- |
| **user\_id** | **name** | **team** | **location** |
| 1   | Christina | success |     |
| 2   | Khalid | success |     |
| 4   | Pryan | support | carpet |

If I import `{"user_id": "2", "location": "Bellevue"}` and then `{"user_id": "2", "location": "RWC"}`, I get this:

|     |     |     |     |
| --- | --- | --- | --- |
| **user\_id** | **name** | **team** | **location** |
| 1   | Christina | success |     |
| 2   | Khalid | success | RWC |
| 4   | Pryan | support | carpet |

But if I import `{"user_id": "2", "location": "RWC"}` and then `{"user_id": "2", "location": "Bellevue"}`, I get this:

|     |     |     |     |
| --- | --- | --- | --- |
| **user\_id** | **name** | **team** | **location** |
| 1   | Christina | success |     |
| 2   | Khalid | success | Bellevue |
| 4   | Pryan | support | carpet |

We need to import the rows in the right order, or else the final table might get Khalid's location wrong!

In order to get blazing-fast import speeds, rows are often imported into Measure IQ in an order that differs from the order they appear in the data store.  Don't worry, though - you can have both speedy import and consistent lookup tables as long as you follow some best practices!

## What should I do?

Congrats on reading this far in! Now you know all about how lookup tables work and how they're imported. Armed with this knowledge, you can prepare files for import that take advantage of lookup tables' efficiency and give you the results you expect. 

### Send the minimum necessary information

Because lookup tables persist any information that is not explicitly changed, you do not need to re-send unchanged information. For example, if you only want to change two of the five fields associated with a particular user\_id, you just have to import a row that contains the user\_id and the two fields that you want to change; the other 3 fields will persist unchanged. Choosing not to re-send old information reduces the chance of accidentally overwriting a new value with an old value. 

### Consolidate your updates

If you need to update multiple fields associated with a particular lookup value, consolidate all of your updates into a single row. For example, instead of sending both 

`{"user_id": 555, "location": "Palm Springs"}` and `{"user_id": 555, "status": "on vacation"}` as separate rows, you should instead just send one row like

#### `{"user_id": 555, "location": "Palm Springs", "status": "on vacation"}.`  

### Update only as often as you need to

You are most likely to see unexpected results when you update one lookup table row many times within a short period of time (where a "short period of time" is ~ 1 day or so). If at all possible, consider sending fewer updates spaced farther apart. 

### Use a literal "null" value

If you're a habitual edge case checker, you might be thinking about null values right now. As you know, if you import a row that does not contain a particular field, the existing value of the field will persist. This certainly has its advantages, but what if you want to change an existing value to a null value? You will need to import a literal null value that will overwrite the existing value. For example, let's say you have a lookup table row that looks like this:

`{"name" : "Beyonce", "hometown": "Houston, TX", "flaws": ["this diamond", "my diamond", "this rock", "my rock"]}`

and you want the "flaws" field to be null. You should import a row that looks like this:

`{"name" : "Beyonce", "flaws": "NULL"}`

Which will give you this row in the lookup table:

`{"name" : "Beyonce", "hometown": "Houston, TX", "flaws": "NULL"}`

You could also use "null", "None", or some other string instead of "NULL", but it's best to be consistent. 

You should follow all of the best practices above as much as is *feasible*. You should never have to sacrifice your analytical flexibility to follow the guidelines. The most important thing is for you to understand what's going on behind the scenes. As always, your technical customer success manager and the Measure IQ support team are here to help.
