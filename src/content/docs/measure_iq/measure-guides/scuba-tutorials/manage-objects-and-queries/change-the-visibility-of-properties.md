---
title: "Change the Visibility of Properties "
description: "Definition & use of Change the Visibility of Properties "
---

This article explains how to change the display of properties that you've created or that have been shared with you:

- [Hiding and Unhiding Properties](#hiding)
- [Favoriting Properties](#favoriting)

## Hiding and Unhiding Properties 

There are two global visibility settings for properties: *hidden* or *visible*.

- **Visible properties**—can be viewed and searched for in the expression builder by all users. Properties can be selected to define other properties, as well as used in queries. Objects are visible by default.
- **Hidden properties**—can help keep drop-down lists manageable, and discourage other users from using specific properties. Hidden properties are not shown in drop-down menus in the expression builder. Hidden properties are still visible in object lists.

All Scuba users can toggle a property to be visible or hidden, provided they can view the property (that is, provided they have created the property or someone [shared it with them](../../../scuba-guides/scuba-user-guides/manage-your-created-objects/share-an-object-with-other-users)).

You might want to hide properties that other users don't rely on, or that they shouldn’t use in a query or object definition. The following are examples of when you would want to hide a property.

- If you have a raw event property that has important data but needs to be cleaned up, you can create another event property for the clean version (with a user friendly name), then hide the original raw event property. That way, other users can use only the clean version of the event property.
- If you've created an Event Property A that is defined by a second object, Event Property B, which is in turn defined by a third object, Event Property C. In this case, you might want only Event Property A to be visible.

To use an object in a query or to define an object but otherwise hide it from lists, first make the object visible. Then after you've used it, toggle it back to *hidden*.

###### To hide a property and make it visible again, do the following:

1. Click **Data** in the left menu.
2. In the right pane, click the tab for the type of property you want to hide (event property, actor property, and so on).
3. In the list of properties, select the property you want to hide.
4. At the top of the page, click the eye icon and select **Hidden** from the drop-down list. The property will be hidden from every user's expression builder.
5. To make the property visible again, repeat steps 1 and 2, click the eye icon, and select **Visible** from the drop-down list.

## Favoriting Properties

Users want to be able to easily identify objects for use in their queries and reference the correct data. This is especially true if knowledge objects have similar names. There are two categories of favorites:

- **Personal favorite**—can be applied by any user and is visible only to that user. Personal favorites are identified by a gold star. An object's popularity rating is based on the number of times it has been marked as a favorite by users.
- **Admin favorite**—can be applied only by admin users, and is visible to all users. Admin favorites are identified by a gray star. Admin favorited properties can help guide users in their selection for queries.

Favorited items appear at the top of lists, in alphabetical order. Personal favorites are shown before admin favorites.

###### To favorite a property, do the following:

1. In the left menu bar, click **Data**.
2. At the top of the page, click the tab of object you want to favorite (event property, actor property, flow, flow property, or measure).
3. Click the star for the property you want to favorite. The star to the left of the property name appears gold, and will appear at the top of your lists, in alphabetical order. Your personal favorites (gold stars) appear before admin favorites (gray stars).

## What's Next 

You've successfully created properties and changed the visibility. Now learn how to:

- [Manage properties](../manage-properties)
