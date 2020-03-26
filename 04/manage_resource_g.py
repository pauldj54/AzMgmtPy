import string,random,time,json,subprocess

import os
from msrestazure.azure_exceptions import CloudError

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage.models import (
    StorageAccountCreateParameters,
    StorageAccountUpdateParameters,
    Sku,
    SkuName,
    Kind
)

subscription_id = os.environ.get(
    'AZURE_SUBSCRIPTION_ID',
    'da05ac29-8f4c-4a13-8c3e-43b5a925aba3') # your Azure Subscription Id
credentials = ServicePrincipalCredentials(
    client_id='b0867de5-6c60-4b77-9b9d-4e3c29c39386',
    secret='[8DwQYbAq@030MpdeYs.y?zs?IJWayTq',
    tenant='6005dfb1-84f6-4005-8ae1-77f26eb7aac7'
)

resource_client  = ResourceManagementClient(credentials, subscription_id)

resource_group_params = {'location':'westeurope'}

###
# Create the a resource group for our demo
# We need a resource group and a storage account. A random name is generated, as each storage account name must be globally unique.
###
rg = resource_client.resource_groups

for item in rg.list():
    groupDict = item.__dict__
    gName =  groupDict['name']
    if gName.find('azuremol') == 0:
        try:
            rg.delete(resource_group_name = gName, raw=False)
            print(gName + " was sucessfully deleted")
        except CloudError as err:
            print("Error by deleting the resource group " + gName + " " + format(err))


 