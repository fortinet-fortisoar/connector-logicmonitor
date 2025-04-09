## About the connector
LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. This connector enables automated operations such as Get Alert List, Get Device Group List, Get Device List, Get Device Alerts, Get Report List, and Get Report by ID.
<p>This document provides information about the LogicMonitor Connector, which facilitates automated interactions, with a LogicMonitor server using FortiSOAR&trade; playbooks. Add the LogicMonitor Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with LogicMonitor.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-logicmonitor</pre>

## Prerequisites to configuring the connector
- You must have the credentials of LogicMonitor server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the LogicMonitor server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>LogicMonitor</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Account Name</td><td>Specify your LogicMonitor account name.
</td>
</tr><tr><td>Bearer Token</td><td>Specify the bearer token to authenticate LogicMonitor REST API. Refer: https://www.logicmonitor.com/support/adding-a-bearer-token
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Alert List</td><td>Retrieve a list of alerts from LogicMonitor based on the input parameters you have specified.</td><td>get_alert_list <br/>Investigation</td></tr>
<tr><td>Get Device Group List</td><td>Retrieve a list of device groups from LogicMonitor based on the input parameters you have specified.</td><td>get_device_group_list <br/>Investigation</td></tr>
<tr><td>Get Device List</td><td>Retrieve a list of devices from LogicMonitor based on the input parameters you have specified.</td><td>get_device_list <br/>Investigation</td></tr>
<tr><td>Get Device Alerts</td><td>Retrieve alerts for a specific device from LogicMonitor based on the input parameters you have specified.</td><td>get_device_alerts <br/>Investigation</td></tr>
<tr><td>Get Report List</td><td>Retrieve a list of reports from LogicMonitor based on the input parameters you have specified.</td><td>get_report_list <br/>Investigation</td></tr>
<tr><td>Get Report by ID</td><td>Retrieve a specific report from LogicMonitor based on the report ID you have specified.</td><td>get_report_by_id <br/>Investigation</td></tr>
</tbody></table>

### operation: Get Alert List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Filter Criteria</td><td>Specify a filter for the results.
</td></tr><tr><td>Fields to Retrieve</td><td>Specify the comma-separated list of fields to include in the response.
</td></tr><tr><td>Limit</td><td>Specify the number of results to return. A maximum of 1000 records can be retrieved per request.
</td></tr><tr><td>Offset</td><td>Specify the count of the first few records to skip while retrieving the result. The maximum offset allowed is 10,000 alerts.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "total": "",
    "searchId": "",
    "items": [
        {
            "resourceId": "",
            "endEpoch": "",
            "threshold": "",
            "type": "",
            "startEpoch": "",
            "enableAnomalyAlertGeneration": "",
            "internalId": "",
            "monitorObjectName": "",
            "dataPointName": "",
            "dataPointId": "",
            "suppressor": "",
            "id": "",
            "ruleId": "",
            "alertExternalTicketUrl": {
                "empty": ""
            },
            "tenant": "",
            "alertValue": "",
            "sdted": "",
            "SDT": {},
            "enableAnomalyAlertSuppression": "",
            "receivedList": "",
            "monitorObjectGroups": {},
            "chainId": "",
            "resourceTemplateId": "",
            "cleared": "",
            "adAlertDesc": "",
            "resourceTemplateName": "",
            "anomaly": "",
            "instanceName": "",
            "monitorObjectId": "",
            "rule": "",
            "ackComment": "",
            "alertGroupEntityValue": "",
            "instanceId": "",
            "suppressDesc": "",
            "logPartition": "",
            "nextRecipient": "",
            "clearExpr": "",
            "adAlert": "",
            "ackedBy": "",
            "severity": "",
            "ackedEpoch": "",
            "chain": "",
            "alertQuery": "",
            "subChainId": "",
            "logMetaData": "",
            "monitorObjectType": "",
            "acked": "",
            "resourceTemplateType": "",
            "clearValue": "",
            "instanceDescription": "",
            "dependencyRoutingState": "",
            "dependencyRole": ""
        }
    ]
}</pre>
### operation: Get Device Group List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Filter Criteria</td><td>Specify a filter for the results.
</td></tr><tr><td>Fields to Retrieve</td><td>Specify the comma-separated list of fields to include in the response.
</td></tr><tr><td>Limit</td><td>Specify the number of results to return. A maximum of 1000 records can be retrieved per request.
</td></tr><tr><td>Offset</td><td>Specify the count of the first few records to skip while retrieving the result.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "total": "",
    "searchId": "",
    "items": [
        {
            "fullPath": "",
            "groupType": "",
            "numOfAWSDevices": "",
            "description": "",
            "appliesTo": "",
            "gcpTestResultCode": "",
            "disableAlerting": "",
            "numOfKubernetesDevices": "",
            "awsRegionsInfo": "",
            "createdOn": "",
            "rolePrivileges": [],
            "hasNetflowEnabledDevices": "",
            "numOfAzureDevices": "",
            "propertyChangeWarningMessage": "",
            "defaultCollectorDescription": "",
            "defaultCollectorId": "",
            "awsTestResult": {
                "warnings": [],
                "noPermissionServices": [],
                "detailLink": "",
                "nonPermissionErrors": []
            },
            "extra": {},
            "numOfDirectSubGroups": "",
            "subGroups": [
                {
                    "fullPath": "",
                    "groupType": "",
                    "userPermission": "",
                    "gcpRegionsInfo": "",
                    "description": "",
                    "appliesTo": "",
                    "rolePrivileges": [],
                    "awsRegionsInfo": "",
                    "numOfHosts": "",
                    "name": "",
                    "numOfDirectSubGroups": "",
                    "numOfDirectDevices": "",
                    "id": "",
                    "azureRegionsInfo": ""
                }
            ],
            "numOfDirectDevices": "",
            "id": "",
            "enableNetflow": "",
            "azureTestResultCode": "",
            "effectiveAlertEnabled": "",
            "defaultCollectorGroupDescription": "",
            "userPermission": "",
            "gcpRegionsInfo": "",
            "saasTestResultCode": "",
            "defaultCollectorGroupId": "",
            "groupStatus": "",
            "numOfGcpDevices": "",
            "azureTestResult": {
                "noPermissionServices": {},
                "detailLink": {}
            },
            "parentId": "",
            "awsTestResultCode": "",
            "customProperties": [
                {
                    "name": "",
                    "value": ""
                }
            ],
            "numOfHosts": "",
            "defaultAutoBalancedCollectorGroupId": "",
            "saasTestResult": {
                "nonPermissionApisErrors": [],
                "invalidStatusUrls": "",
                "noPermissionService": "",
                "resultCode": "",
                "detailLink": "",
                "noPermissionApis": []
            },
            "name": "",
            "gcpTestResult": {
                "noPermissionServices": [],
                "detailLink": "",
                "nonPermissionErrors": []
            },
            "azureRegionsInfo": ""
        }
    ]
}</pre>
### operation: Get Device List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Start Time</td><td>Specify the start time for the query.
</td></tr><tr><td>End Time</td><td>Specify the end time for the query.
</td></tr><tr><td>Netflow Filter</td><td>Specify a filter for netflow data.
</td></tr><tr><td>Filter Criteria</td><td>Specify a filter for the results.
</td></tr><tr><td>Include Deleted Resources</td><td>Specify whether to include deleted resources.
</td></tr><tr><td>Fields to Retrieve</td><td>Specify the comma-separated list of fields to include in the response.
</td></tr><tr><td>Limit</td><td>Specify the number of results to return. A maximum of 1000 records can be retrieved per request.
</td></tr><tr><td>Offset</td><td>Specify the count of the first few records to skip while retrieving the result.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "total": "",
    "searchId": "",
    "items": [
        {
            "logCollectorGroupId": "",
            "disableAlerting": "",
            "netflowCollectorGroupId": "",
            "rolePrivileges": [],
            "systemProperties": [
                {
                    "name": "",
                    "value": ""
                }
            ],
            "isPreferredLogCollectorConfigured": "",
            "hostStatus": "",
            "autoBalancedCollectorGroupId": "",
            "inheritedProperties": [
                {
                    "name": "",
                    "value": ""
                }
            ],
            "id": "",
            "syntheticsCollectorIds": "",
            "upTimeInSeconds": "",
            "deviceType": "",
            "currentCollectorId": "",
            "netflowCollectorId": "",
            "autoPropsAssignedOn": "",
            "updatedOn": "",
            "preferredCollectorGroupId": "",
            "customProperties": [
                {
                    "name": "",
                    "value": ""
                }
            ],
            "collectorDescription": "",
            "preferredCollectorId": "",
            "lastRawdataTime": "",
            "name": "",
            "deletedTimeInMs": "",
            "netflowCollectorGroupName": "",
            "azureState": "",
            "relatedDeviceId": "",
            "logCollectorGroupName": "",
            "displayName": "",
            "logCollectorDescription": "",
            "link": "",
            "awsState": "",
            "description": "",
            "createdOn": "",
            "gcpState": "",
            "autoPropsUpdatedOn": "",
            "scanConfigId": "",
            "enableNetflow": "",
            "lastDataTime": "",
            "hostGroupIds": "",
            "resourceIds": [
                {
                    "name": "",
                    "value": ""
                }
            ],
            "op": "",
            "currentLogCollectorId": "",
            "logCollectorId": "",
            "netflowCollectorDescription": "",
            "userPermission": "",
            "preferredCollectorGroupName": "",
            "autoProperties": [
                {
                    "name": "",
                    "value": ""
                }
            ],
            "toDeleteTimeInMs": "",
            "containsMultiValue": ""
        }
    ]
}</pre>
### operation: Get Device Alerts
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Device ID</td><td>Specify the ID of the device to retrieve alerts.
</td></tr><tr><td>Start Time</td><td>Specify the start time for the query.
</td></tr><tr><td>End Time</td><td>Specify the end time for the query.
</td></tr><tr><td>Netflow Filter</td><td>Specify a filter for netflow data.
</td></tr><tr><td>Need Message</td><td>Specify whether to include message details.
</td></tr><tr><td>Custom Columns</td><td>Specify custom columns to include in the response.
</td></tr><tr><td>Bound</td><td>Specify the bound for the alerts.
</td></tr><tr><td>Filter Criteria</td><td>Specify a filter for the results.
</td></tr><tr><td>Fields to Retrieve</td><td>Specify the comma-separated list of fields to include in the response.
</td></tr><tr><td>Limit</td><td>Specify the number of results to return. A maximum of 1000 records can be retrieved per request.
</td></tr><tr><td>Offset</td><td>Specify the count of the first few records to skip while retrieving the result. The maximum offset allowed is 10,000 alerts.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "total": "",
    "searchId": "",
    "items": [
        {
            "resourceId": "",
            "endEpoch": "",
            "threshold": "",
            "type": "",
            "startEpoch": "",
            "enableAnomalyAlertGeneration": "",
            "internalId": "",
            "monitorObjectName": "",
            "dataPointName": "",
            "dataPointId": "",
            "suppressor": "",
            "id": "",
            "detailMessage": {},
            "ruleId": "",
            "alertExternalTicketUrl": {
                "empty": ""
            },
            "tenant": "",
            "alertValue": "",
            "sdted": "",
            "SDT": {},
            "enableAnomalyAlertSuppression": "",
            "receivedList": "",
            "monitorObjectGroups": {},
            "chainId": "",
            "resourceTemplateId": "",
            "cleared": "",
            "adAlertDesc": "",
            "resourceTemplateName": "",
            "anomaly": "",
            "instanceName": "",
            "monitorObjectId": "",
            "rule": "",
            "ackComment": "",
            "alertGroupEntityValue": "",
            "instanceId": "",
            "suppressDesc": "",
            "logPartition": "",
            "nextRecipient": "",
            "clearExpr": "",
            "adAlert": "",
            "ackedBy": "",
            "severity": "",
            "ackedEpoch": "",
            "chain": "",
            "alertQuery": "",
            "subChainId": "",
            "logMetaData": "",
            "monitorObjectType": "",
            "acked": "",
            "resourceTemplateType": "",
            "clearValue": "",
            "instanceDescription": "",
            "dependencyRoutingState": "",
            "dependencyRole": ""
        }
    ]
}</pre>
### operation: Get Report List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Filter Criteria</td><td>Specify a filter for the results.
</td></tr><tr><td>Fields to Retrieve</td><td>Specify the comma-separated list of fields to include in the response.
</td></tr><tr><td>Limit</td><td>Specify the number of results to return. A maximum of 1000 records can be retrieved per request.
</td></tr><tr><td>Offset</td><td>Specify the count of the first few records to skip while retrieving the result.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "total": "",
    "searchId": "",
    "items": [
        {
            "lastmodifyUserId": "",
            "delivery": "",
            "userPermission": "",
            "lastGenerateOn": "",
            "reportLinkNum": "",
            "groupId": "",
            "format": "",
            "description": "",
            "lastGenerateSize": "",
            "customReportTypeId": "",
            "type": "",
            "lastGeneratePages": "",
            "reportLinkExpire": "",
            "schedule": "",
            "recipients": [
                {
                    "additionInfo": "",
                    "method": "",
                    "type": "",
                    "addr": ""
                }
            ],
            "customReportTypeName": "",
            "name": "",
            "enableViewAsOtherUser": "",
            "lastmodifyUserName": "",
            "id": "",
            "scheduleTimezone": ""
        }
    ]
}</pre>
### operation: Get Report by ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Report ID</td><td>Specify the ID of the report.
</td></tr><tr><td>Fields to Retrieve</td><td>Specify the comma-separated list of fields to include in the response.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "lastmodifyUserId": "",
    "delivery": "",
    "userPermission": "",
    "lastGenerateOn": "",
    "reportLinkNum": "",
    "groupId": "",
    "format": "",
    "description": "",
    "lastGenerateSize": "",
    "customReportTypeId": "",
    "type": "",
    "lastGeneratePages": "",
    "reportLinkExpire": "",
    "schedule": "",
    "recipients": [
        {
            "additionInfo": "",
            "method": "",
            "type": "",
            "addr": ""
        }
    ],
    "customReportTypeName": "",
    "name": "",
    "enableViewAsOtherUser": "",
    "lastmodifyUserName": "",
    "id": "",
    "scheduleTimezone": ""
}</pre>
## Included playbooks
The `Sample - logicmonitor - 1.0.0` playbook collection comes bundled with the LogicMonitor connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the LogicMonitor connector.

- Get Alert List
- Get Device Alerts
- Get Device Group List
- Get Device List
- Get Report List
- Get Report by ID

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
