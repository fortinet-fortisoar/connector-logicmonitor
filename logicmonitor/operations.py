# License details
"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""


# Imports
from connectors.core.connector import ConnectorError, get_logger
import requests

# Initialize logger
logger = get_logger('logicmonitor')


# Common function to make external API calls.
def make_api_call(method="GET", endpoint="", config=None, params=None, headers=None, data=None, json_data=None):
    try:
        default_headers = {
            "Authorization": f"Bearer {config.get('token')}",
            "X-Version": 3
        }
        url = f"https://{config.get('account_name')}.logicmonitor.com/santaba/rest{endpoint}"
        if headers:
            default_headers.update(headers)
        logger.debug("url: "+str(url))
        logger.debug("method: "+str(method))
        logger.debug("headers: "+str(default_headers))
        logger.debug("data: "+str(data))
        logger.debug("json_data: "+str(json_data))

        response = requests.request(method=method, url=endpoint, headers=headers, data=data, json=json_data, params=params, verify=config.get('verify_ssl'))
        if response.ok:
            if response.content:
                response = response.json()
            else:
                response = {"result": "No Data Returned", "status": "success"}
            return response
        else:
            try:
                error_resp = response.json()
                error_message = error_resp.get('errorMessage', 'No error message provided')
            except ValueError:
                raw_text = response.text  # fallback if response isn't JSON
                error_message = raw_text
                error_resp = {'raw_response': raw_text}
            logger.error("{0} Error: {1}".format(response.status_code, error_resp))
            raise ConnectorError('{0}:{1}'.format(response.status_code, error_message))
    except requests.exceptions.SSLError as e:
        logger.exception('{0}'.format(e))
        raise ConnectorError('{0}'.format(e))
    except requests.exceptions.ConnectionError as e:
        logger.exception('{0}'.format(e))
        raise ConnectorError('{0}'.format(e))
    except Exception as e:
        logger.error('{0}'.format(e))
        raise ConnectorError('{0}'.format(e))


def build_params(params):
    return {k: v for k, v in params.items() if v is not None and v != ''}


# Operation definitions
def get_alert_list(config, params):
    params = build_params(params)
    endpoint = "/alert/alerts"
    return make_api_call(config=config, params=params, endpoint=endpoint)


def get_device_group_list(config, params):
    params = build_params(params)
    endpoint = "/device/groups"
    return make_api_call(config=config, params=params, endpoint=endpoint)


def get_device_list(config, params):
    params = build_params(params)
    endpoint = "/device/devices"
    return make_api_call(config=config, params=params, endpoint=endpoint)


def get_device_alerts(config, params):
    params = build_params(params)
    endpoint = f"/device/devices/{params.pop('id')}/alerts"
    return make_api_call(config=config, params=params, endpoint=endpoint)


def get_report_list(config, params):
    params = build_params(params)
    endpoint = "/report/reports"
    return make_api_call(config=config, params=params, endpoint=endpoint)


def get_report_by_id(config, params):
    params = build_params(params)
    endpoint = f"/report/reports/{params.pop('id')}"
    return make_api_call(config=config, params=params, endpoint=endpoint)


operations_map = {
    'get_alert_list': get_alert_list,
    'get_device_group_list': get_device_group_list,
    'get_device_list': get_device_list,
    'get_device_alerts': get_device_alerts,
    'get_report_list': get_report_list,
    'get_report_by_id': get_report_by_id
}