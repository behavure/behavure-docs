---
title: "Compare BQL and SQL Commands "
description: "Definition & use of Compare BQL and SQL Commands "
---
Although BQL is similar to existing database query languages like SQL, its custom design for Measure IQ queries means that it differs in a few key points.

The following table compares and identifies differences between BQL and SQL clauses.

|     |     |     |     |
| --- | --- | --- | --- |
| **Concept** | **SQL** | **BQL** | **Notes** |
| **select \*** | select \* from my\_table | Not supported |     |
| **select count(\*)** | select count(\*) from my\_table | select count(\*) from my\_table |     |
| **select distinct** | select count(distinct user) from my\_table | select count\_unique(user) from my\_table | Use “select count\_unique” instead of “select count distinct”. |
| **where** | select count(\*) from my\_table where user = “jack” | select count(\* where user=”jack”) from my\_table | In BQL, “where” used as a filter is contained within an aggregation. This is because you can have multiple aggregations, each with its own set of filters. |
| **and, or, not** | select count(\*) from my\_table where not(user = “jack” or user = “jill”) | select count(\* where not(user=”jack” or user=”jill”)) from my\_table |     |
| **order by** | select count(distinct purchase) from my\_table order by user asc | select count\_unique(purchase) as purchases, user from my\_table order by purchases asc |     |
| **min, max, avg, count, sum** | select min(time\_in\_app) from my\_table | select min(time\_in\_app) from my\_table |     |
| **in** | select count(\*) from my\_table where user in (“jack”,”jill”) | select count(\* where user in (“jack”,”jill”)) from my\_table |     |
| **between** | select count(\*) from my\_table where user\_id between 1 and 100 | select count(\*) from my\_table between 2019-2-19 and now | BQL `between` is specifically a Measure IQ timespec syntax. BQL does not support “between” as a regular operator, and SQL lacks the notion of timespec. |
| **group by** | select count(\*),country from my\_table group by country | select count(\*) from my\_table group by user between 2014-2-19 4pm and now | "group by" corresponds to "split by" in the Measure IQ UI. |
| **limit** | select count(\*) from my\_table limit 5 | select count(\*) from my\_table group by user limit 5 between 2014-2-19 4pm and now<br><br>select count(\*) from my\_table group by user, country limit 5 and by platform limit 3 | BQL can use hierarchical "group by", as shown in the second example here. The syntax, though, is the same from SQL to BQL. |
| **joins** | select my\_table.user, lookup\_table.age from inner join my\_table.user = lookup\_table.user | Not supported | BQL does not support "joins" because they are implied depending on the property combinations. |
| **having** | select count(user), country from my\_table group by country having count(user) > 5 | Not supported |     |
| **on scope** | Not supported | select count(\* on event) from my\_table group by Actor<user>(max(age))<br><br>select count(\* on Actor<user>) from my\_table group by Actor<user>(max(age)) | Explicitly specify the scope of an aggregation.<br><br>  <br>The first query counts the number of events grouped by the user’s age.<br><br>The second query counts the number of users grouped by the user’s age. This is the same as:<br><br>select count(\*) from my\_table group by Actor<user>(max(age)) |
| **math (round, sqrt, etc.)** | select count(user) from my\_table where sqrt(age)>5 | select count\_unique(user where sqrt(age) > 5) from my\_table |     |
| **percentile** | select distinct month, P90 = percentile\_disc(0.9) within group (order by score) over (partition by \[month\]) from my\_table | select percentile(user\_high\_score, 90) from my\_table | Percentile is similar to percentile\_desc in relational databases, but the two functions are not exactly the same, hence the different name. |
| **beginning\_of\_time,**  <br>**for every** | Not supported | select count(\*) from my\_table for every week over 7 days between beginning\_of\_time and now | Some powerful time operators are present in BQL but not in SQL. This example counts the number of events that happened in a 7 day period, and performs this calculation every week from the beginning of time to now. |
| **like** | select count(\*) from my\_table where name like ‘%jack%’ | select count(\* where name like ‘.\*jack.\*’) from my\_table | BQL "like" searches for text contained within a column. It is similar to mysql "rlike". It accepts regular expressions, unlike SQL "like", which accepts %foo% syntax. |