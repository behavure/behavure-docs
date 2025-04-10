---
title: "Configuring Azure for Measure IQ Clusters"
description: "Learn how to configure Azure for a Measure IQ deployment"
---

This document shows you how to install the Azure NPM module, and then use an Azure Subscription to configure an Azure instance for a Measure IQ cluster. Make sure to perform the tasks in order.

## [Prerequisites](#prerequisites)

To successfully complete this process, you must have the following:

- A thorough understanding of Azure. For information see the [Azure documentation](https://docs.microsoft.com/en-us/azure/). If you are unfamiliar with Azure, the [Azure Resource Manager Overview](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-overview) provides a good introduction.
- Co-admin or owner privileges in the Azure Subscription.
- Estimated size requirements for your Measure IQ cluster. For more information, see [Planning your Measure IQ Deployment](/measure_iq/admin-guides/planning-your-measure-iq-deployment) or check with your Measure IQ implementation team.

**Prerequisites must be satisfied before you begin the following tasks:**

1. [Request core and storage quota from Azure](#1-request-core-and-storage-quota-from-azure)
2. [Install the Azure CLI](#2-install-the-azure-cli)
3. [Log in to the Azure Subscription and configure ARM](#3-log-in-to-azure-and-optionally-set-your-subscription)
4. [Create an application and a service principle](#4-create-an-application-and-service-principle)
5. [Create a role and show the account](#5-create-a-role-and-show-the-account)
6. [Submit information to provision a cluster](#6-submit-information-to-provision-a-measure-iq-cluster)

## [1. Request core and storage quota from Azure](#1-request-core-and-storage-quota-from-azure)

Request a core and storage quota for your cluster from Azure in advance. These quotas should match the requirements for your cluster layout, including some additional storage for buffer. Make note of this information as you will need it for step 6 to provision the Measure IQ cluster.

For information on requesting core and storage quotas, see the [Azure solutions documentation](https://azure.microsoft.com/en-us/solutions/), or contact [Azure Support](https://azure.microsoft.com/en-us/support/options/).

## [2. Install the Azure CLI](#2-install-the-azure-cli)

After completing step 1, you will need to install the CLI module for Azure using command line instructions with a tool such as Terminal. For more details, see [Install the Azure CLI on Linux](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt).

### To download and install the Azure CLI, do the following:

1. On your Ubuntu system, open a Terminal window and use the following command. For Mac and Windows systems, follow the instructions found here: [How to install the Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest).

```
$  curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

## [3. Log in to Azure and (optionally) set your subscription](#3-log-in-to-azure-and-optionally-set-your-subscription)

After installing the Azure CLI, log into your Azure subscription to complete the remaining steps.

### To log in to Azure, do the following:

1. In the Terminal window, use the following command to initiate logging into your Azure subscription.

```
$  az login
```

2. Use a web browser to open the page `https://microsoft.com/devicelogin`.

3. Enter the displayed code to authenticate. In the following example, the subscription code is hidden.

```
To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code ######### to authenticate.
```

#### OPTIONAL: If your account manages multiple Azure subscriptions, do the following:

4. After you have logged in, list all Azure subscriptions you have access to. Make a note of the "SubscriptionId" for the subscription you will be using to set up Measure IQ.

```
$  az account list
```

5. With the SubscriptionId from above, use the following command to set which subscription you will be using for the remainder of this guide.

```
$  az account set -s <SubscriptionId>
```

## [4. Create an application and service principle](#4-create-an-application-and-service-principle)

Next, you will create an application for Measure IQ with a client secret (password), and then use the AppID to create a service principle.

### To create an application and a service principle, do the following:

1. To create an application (for Measure IQ), use the following command. Make a note of the password you input, and the AppID `("id"`) that is displayed, for use in the next step.

```
$  az ad app create --display-name "Measure IQ" --password "<replace_with_random_password>"
```

2. Create a Service Principle using the AppId from the previous step. Make a note of the "ObjectId" that is displayed, for when you create a role in the next section.

```
$  az ad sp create --id <AppId>
```

## [5. Create a role and show the account](#5-create-a-role-and-show-the-account)

Finally, you will create a role using the ObjectId generated in the previous section, then show the account information.

### To create a role and show the account, do the following:

1. To create a role, enter the following command using the ObjectId generated when you created a Service Principle in the previous section.

```
$  az role assignment create --role "Owner" --assignee-object-id <ObjectId> --scope /subscriptions/<SubscriptionId>
```

2. To show the details of your Azure account, enter the following command. Make a note of the TenantId in the output.

```
$  az account show
```

## [6. Submit information to provision a Measure IQ cluster](#6-submit-information-to-provision-a-measure-iq-cluster)

Now that you have set up and configured your Azure subscription, you have all of the information you need to submit to Measure IQ to provision a new cluster in Azure.

### Submit the following information to Measure IQ for your cluster:

1. The App Id that you generated when you created an application (in step 4).
2. The Secret that you specified when you created an application (in step 4).
3. The Tenant Id that you generated when showing the account (in step 5).
4. The Region in which the cluster is to be deployed.
5. The Subscription Id, from your Azure Portal.
6. Cluster sizing defined with your Measure IQ implementation team, while [Planning your Measure IQ deployment](/measure_iq/admin-guides/planning-your-measure-iq-deployment).
7. Core and Storage quota you requested from Azure, such as:
8. Quantity of VM Types with respective region:  
   \[Example: 500 cores, D3s, East US 2\]  
   \[Example: 100 cores, A7s, Central US\]

Also include the following information:

- Date of core fulfillment:
- Request is temporary (Yes/No)? **If yes, include the details.**
- Bursting usage pattern (Yes/No)? **If yes, include the details.**
- Amount of Premium Storage in GB or TB:

## [What's next](#whats-next)

The Measure IQ team will deploy and configure your new cluster once we have the above information. After Azure is properly configured and Measure IQ is deployed, you are ready to [add data](/measure_iq/admin-guides/managing-your-data/what-to-think-about-before-you-add-data).
