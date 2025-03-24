---
title: "Use the Scuba External Query API "
description: "Definition & use of Use the Scuba External Query API "
---
The Scuba external API lets you extract summarized and aggregated data for use in downstream processes, dashboards, or reports.

To use the API, you need the following:

- An API token
- A query response identifier or BQL query

Once you have these two pieces of information, you can submit POST requests through the API.

API queries use cluster resources on a scale similar to ad hoc queries initiated in the Scuba UI. To maintain performance across your Scuba cluster when using the query API, use the same best practices for query efficiency that you use with queries that originate in the UI.

## Generate an API token

You can generate an API token using your browser:

1. In your browser, log into Scuba.
2. In the URL bar, append `/api/create_token` to the host name of your Scuba cluster and hit Enter. For example, if your Scuba host name is [https://my\_cluster.scuba.io](https://my_cluster.scuba.io), enter [**https://my\_cluster.scuba.io/api/create\_token**](https://my_cluster.scuba.io/api/create_token).
3. The browser immediately returns either a failure message or a success message with an API token. A success message looks like this:
```
{"token": "san+aslnasw50293sjlfhgnoOvWW/sQH09y0", "success": true}
```
The quoted string after "token" is your API token (without the quotes). Copy/save this token to use later. Be sure to store it somewhere secure! Anyone with this token will be able to programmatically query the API using your account.

## Obtain a query

You have two ways to create a query:

- You can use the Scuba UI to create a query, then use the query response identifier to run the exact query programmatically.
- You can use the Scuba behavioral query language (BQL) to define a query using SQL-like syntax, and run the BQL query programmatically.

### Define a query in the UI

1. Use the UI to define the query you wish to make programmatic. Press RUN to run the query.
2. When you press RUN, the URL in your browser appends a query response identifier, like `r9372` or something similar. Copy the query response identifier to use in the API later.

*Note: All measures must be made visible in the UI query to be returned in JSON.*

### Define a query using BQL

1. Define a [BQL query](#).
2. Use the existing endpoint to send BQL instead of the query response identifier.

Once you've defined your query, either in the UI or using BQL, proceed to the next step of using the API.

### Use the API

#### Request

The API accepts HTTP POST requests from any HTTP client (for example, curl or a UI-based HTTP client).

|     |     |     |
| --- | --- | --- |
|     | **Query response ID** | **BQL query** |
| Endpoint | `https://{your_domain_name}/v1/query` | `https://{your_domain_name}/v1/query` |
| Request parameter format | JSON in the body of the request in the `query_response_id` field | JSON in the body of the request in the `bql` field |
| Example request location | `{"query_response_id": "r9372"}` | `{"bql": "select count(*) from foreverMusic"}` |

Your domain name is the URL at which you access the Scuba UI. Pass the API token in the Authorization header prefixed with "Token" and separated by a single space.

You can also include additional elements in the body of your request to dictate the output type, format, and chart options. See below table for specifics.

| **JSON Element** | **Description** | **Valid Values** |
| --- | --- | --- |
| bql | Your BQL query | See BQL syntax |
| query\_response\_id | The query\_response\_id of a previous explore request or BQL execution | `r` followed by numbers |
| return\_type | If we want a json containing the data in return or a link to an explore URL view | `data` *(default)*  <br>`explore_url` |
| result\_format | Mandatory if return\_data is `data`<br><br>Defines the format of the data in response | `JSON_POWER_BI`: flat array of dictionaries. 1 dict per group per time bucket.  <br>`DEFAULT`: format that the UI expects<br><br>`CSV` |
| chart\_options.name | The name of your new chart to be created (only valid with `return_type` = “explore\_url”) | any string |
| chart\_options.type | The type of visualization to be used in your new chart (only valid with `return_type` = “explore\_url”) | `TIME` *(default)* : Time view  <br>`TABLE` : Table view  <br>`SANKEY` : Sankey view  <br>`NUMBER`: Number view  <br>`BAR` : Bar view  <br>`SUNBURST`: Pie view  <br>`SCATTER` : Line view |

#### Sample requests

If you are using curl to make your requests, you can optionally use the--verbose flag and receive some output below the request, before the curl response. Then the request and the confirmation output is as follows:

```
$ curl 'https://11.2.34.141/v1/query' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Token san+aslnasw50293sjlfhgnoOvWW/sQH09y0' \
    -d '{"query_response_id": "r9372"}' --verbose
> POST /v1/query HTTP/2
> Host: 11.2.34.141
> User-Agent: curl/7.54.0
> Accept: */*
> Content-type: application/json
> Authorization: Token san+aslnasw50293sjlfhgnoOvWW/sQH09y0
> Content-Length: 32

```

Pass the API token in the Authorization header prefixed with "Token" and separated by a single space.

If instead of curl, you are using an HTTP client, the POST request might look like the following:

```
POST /v1/query
HTTP/1.1
Host: 11.2.34.141
Authorization: Token san+aslnasw50293sjlfhgnoOvWW/sQH09y0
Content-Type: application/json {"query_response_id": "r9372"}

```

A sample curl request with BQL looks like this:

```
curl 'https://11.2.34.141/v1/query' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Token san+aslnasw50293sjlfhgnoOvWW/sQH09y0' \
    -d '{'bql': 'select count(*) from foreverMusic}' --verbose
> POST /v1/query HTTP/2
> Host: 11.2.34.141
> User-Agent: curl/7.54.0
> Accept: */*
> Content-type: application/json
> Authorization: Token san+aslnasw50293sjlfhgnoOvWW/sQH09y0
> Content-Length: 32

```

#### Response

The response includes:

- Start and end times for every measurement
- A measurement value for each measurement
- A value for any split by columns or properties

Here is a sample response for a simple **show count of events** query splitting by artist:

```
[
{
"measure 1":473,
"end_time_0":1540846400000,
"start_time_0":1540760000000
"artist": "All Others"
},
{
"measure 1": 130,
"end_time_0": 1540364400000,
"start_time_0": 1509260400000,
"artist": "Gorillaz"
},
{ "measure 1": 11,
"end_time_0": 154103400000,
"start_time_0": 15124300000,
"artist": "Beethoven"
},
...
]
```