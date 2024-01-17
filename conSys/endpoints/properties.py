from conSys.endpoints import endpoints
from conSys.constants import APITerms


def list_available_properties(node_api_endpoint=None, params=None):
    base_url = f'{node_api_endpoint}/{APITerms.PROPERTIES.value}'
    return endpoints.handle_request(base_url, method='get', params=params)


def create_new_properties(node_api_endpoint=None, properties=None):
    base_url = f'{node_api_endpoint}/{APITerms.PROPERTIES.value}'
    return endpoints.handle_request(base_url, method='post', content_json=properties)


def retrieve_property_definition_by_id(node_api_endpoint=None, params=None, property_id=None):
    base_url = f'{node_api_endpoint}/{APITerms.PROPERTIES.value}/{property_id}'
    return endpoints.handle_request(base_url, method='get', params=params)


def update_property_definition_by_id(node_api_endpoint=None, property_id=None, property=None):
    base_url = f'{node_api_endpoint}/{APITerms.PROPERTIES.value}/{property_id}'
    return endpoints.handle_request(base_url, method='put', content_json=property)


def delete_property_definition_by_id(node_api_endpoint=None, property_id=None):
    base_url = f'{node_api_endpoint}/{APITerms.PROPERTIES.value}/{property_id}'
    return endpoints.handle_request(base_url, method='delete')
