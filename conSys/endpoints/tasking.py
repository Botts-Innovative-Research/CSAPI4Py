import requests

from conSys.constants import APITerms
from conSys.endpoints import endpoints


def get_tasking_interface(node_api_endpoint=None, params=None, system_id=None, tasking_id=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}/{APITerms.TASKING.value}'

    if tasking_id is not None:
        base_url += f'/{tasking_id}'

    return endpoints.handle_request(base_url, method='get', params=params)


def get_tasking_interface_schema(node_api_endpoint=None, params=None, system_id=None, tasking_id=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}/{APITerms.TASKING.value}' \
               f'/{tasking_id}/schema'

    return endpoints.handle_request(base_url, method='get', params=params)


def get_tasking_interface_commands(node_api_endpoint=None, params=None, system_id=None, tasking_id=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}/{APITerms.TASKING.value}/{tasking_id}/commands'

    return endpoints.handle_request(base_url, method='get', params=params)


def get_tasking_interface_status(node_api_endpoint=None, params=None, system_id=None, tasking_id=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}/{APITerms.TASKING.value}/{tasking_id}/status'

    return endpoints.handle_request(base_url, method='get', params=params)


def get_command_status(node_api_endpoint=None, params=None, system_id=None, tasking_id=None, command_id=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}/{APITerms.TASKING.value}' \
               f'/{tasking_id}/commands/{command_id}/status'

    return endpoints.handle_request(base_url, method='get', params=params)


def post_command(node_api_endpoint=None, system_id=None, tasking_id=None, command=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}/{APITerms.TASKING.value}' \
               f'/{tasking_id}/commands'

    return endpoints.handle_request(base_url, method='post', content_json=command)


def post_command_status(node_api_endpoint=None, system_id=None, tasking_id=None, command_id=None,
                        status=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}/{APITerms.TASKING.value}' \
               f'/{tasking_id}/commands/{command_id}/status'

    return endpoints.handle_request(base_url, method='post', content_json=status)
