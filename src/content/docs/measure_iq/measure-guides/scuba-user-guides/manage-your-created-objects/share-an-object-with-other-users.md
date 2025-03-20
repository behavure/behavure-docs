---
title: "Share an Object With Other Users "
description: "Definition & use of Share an Object With Other Users "
---
After you've created a few properties and boards, you can share them with other users. You can share an object with another user or an entire role, according to your [role definition](https://scuba.atlassian.net/wiki/spaces/LEXICON/pages/1302266661/User+roles).

## How sharing works

When you first create a board, property, flow, or measure, only you and your admin can see it. Other users cannot view your object until you share it with them or with your role.

For example, User A and User B are on the product marketing team. Users A and B are both members of the same Scuba role, called "product marketing". User A creates an object. User B does not see User A's object until User A shares it either with User B or with the product marketing role.

Note that admins can see all objects, even ones that you haven't shared with anyone.

## Share a board or user-created object

You can share a board, property, flow, or measure that you have created. You can also share an object that another user has created, up to the limit of your permission on that object. That is, if you have write access to an object, you can grant read or write access. But if you only have read access, you can only grant read access.

You can also remove access that's been granted to an object, up to the limit of your permission on that object. This way, you can correct a mistake you made in sharing the object.

You can share with an individual user or with every user in a role. The roles you can share with are determined by your Scuba role definition. 

> [!INFO]
> Copying a property or board's URL and sending it to your recipient, instead of using the share button as described here, might not allow your recipient to view your results.

### **To share a board**:

1. In the Scuba UI, navigate to the board you want to share.
2. Click the **Open Drawer** icon.
3. Click the **Permissions** option to open up this section of the inspector.
4. Select the username or role that you want to share with.
5. Use the slider to grant  **Query**, **Read,** or **Edit** access.
-   To share the board but not have it populate the other user's board lists, grant **query** access. 
-   To allow the other user to share the board with additional users, grant **read** or **write** access.
6. Click **Save**. Your board is now visible to the user or users you shared it with.  
![](./attachments/share%20a%20board.mov)

### **To share a property, flow, or measure**:

1. Using the left menu, navigate to the object you want to share. For example, to share an actor property, click **Data**, then **Actor properties**, and then in the list click the name of the property.
2. Click the name of the property you wish to share and this will open the drawer on the right side of the screen.
3. Click the plus sign to select a role or individual user to share with.
4. Select the username or role that you want to share with.
5. Use the slider to grant  **Query**, **Read,** or **Edit** access.
-   To share the property but not have it populate the other user's property lists, grant **query** access. 
-   To allow the other user to share the property with additional users, grant **read** or **write** access.
6. Click **Save**. Your object is now visible to the user or users you shared it with.

![](./attachments/edit%20perms%20from%20DD.mov)

### How access to an object is inherited

If a user is granted permission for a board, property, flow, or measure, they get *explicit* permission for that object, and they automatically get *implicit* query permission for all dependents of that object, within the limits of their dataset access.

For example, say you are granted read access to a board made up of several charts. You are granted *explicit* permission to view the board, and the board appears in your boards list. You are also granted *implicit* permission to the charts, queries, and other objects that are used in the board, but these objects do not appear in your object lists and type-aheads.

To the consumer of a board or property, implicit and explicit permissions look the same—you can view any object that you have either implicit or explicit permission to view. But when you inspect an object in the Scuba UI, you see only the users and roles with *explicit* permissions to view the object. The UI does not tell you who has *implicit* permissions on an object.

For security reasons, when you share a query from Explore or an app using the URL (in contrast to the **Share** button that you can use for a property or board), the user does not automatically get permissions to the query, unless the recipient has permissions on each of the top-level objects referenced in the query. This can be accomplished by any of the following:

- The cluster admin configuring all users to have query permission on all new objects.
- When you share a query, you would have to grant permission for every top-level object in the query before sharing the query. See [Share a board or user-created object](https://scuba.atlassian.net/wiki/pages/resumedraft.action?draftId=2139260690) above.

Without one of these, the recipient sees an error message.

### About adding and removing objects on boards

Query permission is also inherited on objects that are created privately and then pinned to shared boards. For example, say you create a query but don't explicitly grant User B access to the query. Then you [pin](https://scuba.atlassian.net/wiki/spaces/LEXICON/pages/1302266337/Pin) your query to a board that has already been shared with User B. Once you pin the query to the board, User B can view the query and its dependent objects. Whether the recipient is granted read or write access on the board, they are granted query permission on the dependent objects.

If you remove a query from a board, the implicit permissions on its dependent objects are removed. Users with implicit permission to view that dependent object can no longer view it, unless they have also been explicitly granted permission to that object.

### Understand inherited permissions on an object

When you're working with an object such as a board, measure actor, action, flow, or property, you can see who has read access to it.

To inspect the permissions on an object:

1. On the left-hand menu, click **Data**, then click the tab for the type of property you wish to inspect.
2. In the list of properties, find your property and click its row.
3. In the right panel, click the **Permissions** tab.
4. A list displays the users and roles with read, write, or query permission on this object. You can view or modify permissions here.

![](./attachments/Screen%20Recording%202023-03-30%20at%203.51.15%20PM.mov)

### About naming objects

One user cannot create two objects with the same name, but two users can give their objects the same name.

For example, User A can create an actor property called "AP - young or old" and so can User B. If User A shares her Weekly Report with User B, User B will have access to two actor properties called "AP - young or old".

User B can distinguish between the two properties by navigating to the object and inspecting the **Owner** column.

![](./attachments/same%20name.mov)

### Share a query from Explore or an app

You can copy a query URL that allows another user to re-run that specific query. You can share the URL using email or another communication service, or bookmark the query to save your query definition and re-run the query later.

The user with which you want to share a query must have an account on your Scuba instance, access to your dataset, and permission to view all of the objects used in your query. In addition, your admin can hide the query share button. To ensure that sharing is successful, pin your query to a board and follow the steps in [Share a board or user-created object](https://scuba.atlassian.net/wiki/pages/resumedraft.action?draftId=2139260690) above.

To share a query without pinning it to a board, do the following: 

1. From Explore or an app, click **Share** in the top right corner of the window.
2. From the URL dialog, click **Copy**. The URL is copied to the clipboard.
3. Share this URL with your recipient by pasting it into an email or other communication channel. 

> [!INFO]
> The query from a shared URL reflects data from when query was originally run. To view updated data, your recipient can click **Run** to re-run the query.

### Troubleshoot sharing issues

The following table helps you troubleshoot sharing issues.

| Problem | Diagnosis |
| --- | --- |
| I can't see someone else's object. I get an error that the property does not exist, or a similar message. | Ask them to share the object with you or with your role. |
| I can't see someone else's query. | Ask them to share the top-level dependent objects with your or your role, or ask them to pin the query to a board and share the board. |
| I see a blank panel on a shared board. | The panel might contain data from a dataset that you do not have access to. |
| My object doesn't look right. | Check the owner column in the explorer table. Is it yours, or is it someone else's with the same name? |
| I can't share an object. | Verify that your role can share with the role you want to share to. Your Scuba admin can check this in the definition for your role. |

## What's Next

After you create and share properties, you might want to tidy up your Scuba workspace. Learn how in the following topics:

- [Change the Visibility of Properties](../../../scuba-guides/scuba-tutorials/manage-objects-and-queries/change-the-visibility-of-properties)
- [Manage Properties](../../../scuba-guides/scuba-tutorials/manage-objects-and-queries/manage-properties)