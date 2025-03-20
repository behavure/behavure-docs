---
title: "Boards (Dashboards) "
description: "Definition & use of Boards (Dashboards) "
---
Dashboards, or **boards**, are a shared workspace to save and follow queries built through features tabs. As you explore your data, you can pin the results to a dashboard and share them with your team.

- **Filtering charts on a dashboard**: You can override the timeframes and filters for all charts on a dashboard. These are not saved when you refresh the dashboard or navigate away.
- **Exploring charts on a dashboard**: You can drill down on individual views directly from the dashboard. Click **Explore** in the upper right corner of a chart to open that view in the Explorer.
- **Copying/sharing a dashboard**: Click on the Open Drawer icon in the upper right corner of the Dashboard view to open the dashboard controls. You can share, clone, delete, favorite, or set up advanced filters here.
- **Toggling to Dark Mode:** As a Board owner or editor, you can also move your board to Dark Mode for all viewers from the Open Drawer icon in the upper right corner of the Dashboard view to open the dashboard controls. Then you can select Options and save your changes.
- **Refreshing dashboards**: All panels and the top navigation bar include the last updated time, displayed in UTC time (IE 03/15/2023, 4:21 PM UTC). Click the **Refresh** button at the top of the Dashboard page to refresh all of the charts on the page.
- **Using Pre-Filters with dashboards**: You can easily apply [Pre-Filters](https://scuba.atlassian.net/wiki/spaces/LEXICON/pages/1302430148/Pre-Filters) to dashboards. You can use them in the same way you use normal filters with Dashboards. Click on the ellipsis at the top of the board and navigate to Advanced Filters to see your options.

## Best practices

- **10 charts per dashboard**: Each Dashboard is a collection of queries being run, so loading a dashboard with many charts will take longer than a dashboard with a few charts. Also, scrolling through many charts can be harder for the user.
- **Chart title**: Use descriptive chart titles that include the query timeframe to provide the best context for dashboard viewers, unless you anticipate that the time override filter will be used frequently.
- **Relative time**: Use relative time for dashboards so that queries refresh as you continue to visit.
- **Today**: Use `today` as your relative time endpoint instead of `now` for more complete data. This is because `today` means 12 AM of the current day (in other words, the closest previous 12 AM), while `now` is the current time, and your data import process might not have caught up to the current minute.
- **Saving your work**: [Pinning queries to a dashboard](../../../scuba-guides/scuba-tutorials/create-a-board-with-queries-panels) are a way to save your work from one Scuba session to the next.