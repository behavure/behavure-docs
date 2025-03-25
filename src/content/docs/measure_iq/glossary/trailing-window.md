---
title: Trailing Window 
description: Definition & use of Trailing Window 
---
In a Time view chart, a **trailing window** is a rolling window of time prior to each point used to calculate that point.

It is common to set the trailing window equal to the time [resolution](../resolution) between two points (for example, resolution 1 day, trailing 1 day). With this setting, every data point uses data that does not appear in other data points.

Less commonly, you might want to smooth the data by setting a trailing window that is longer than the time resolution between the data points.

You can set a trailing window for an actor property in addition to setting one in the top-level query. If the trailing window for an actor property differs from that specified for the top-level query, the actor property trailing window applies for the calculation of the actor property value.

## Related terms

- [Every X Trailing Y](../every-x-trailing-y)
- [Resolution](../resolution)

## More information

See [Specify Relative Time in a Query](https://behavure.ai/docs/wiki/spaces/CSSD/pages/1302431088/Specify+time+in+a+query) in the User Guide.