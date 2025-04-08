# License details
"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""


# Imports
from connectors.core.connector import Connector, ConnectorError, get_logger
from .operations import operations_map, make_api_call

# Initialise logger
logger = get_logger('logicmonitor')


# Class Definition
class LogicMonitor(Connector):
    def execute(self, config, operation, params, **kwargs):
        action = operations_map.get(operation)
        return action(config, params)

    def check_health(self, config):
        try:
            # Example health check operation
            response = make_api_call(config=config, endpoint="/device/devices")
            return response.get('status', '').lower() == 'success'
        except Exception as err:
            logger.error("Check Health Failed. Error: {0}".format(str(err)))
            raise ConnectorError(str(err))
