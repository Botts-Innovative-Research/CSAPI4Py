from conSys.endpoints import endpoints
from conSys.constants import APITerms


def list_available_procedures(node_api_endpoint=None, params=None):
    base_url = f'{node_api_endpoint}/{APITerms.PROCEDURES.value}'
    return endpoints.handle_request(base_url, method='get', params=params)


def create_new_procedures(node_api_endpoint=None, procedures=None):
    base_url = f'{node_api_endpoint}/{APITerms.PROCEDURES.value}'
    return endpoints.handle_request(base_url, method='post', content_json=procedures)


def retrieve_procedure_by_id(node_api_endpoint=None, params=None, procedure_id=None):
    base_url = f'{node_api_endpoint}/{APITerms.PROCEDURES.value}/{procedure_id}'
    return endpoints.handle_request(base_url, method='get', params=params)


def update_procedure_by_id(node_api_endpoint=None, procedure_id=None, procedure=None):
    base_url = f'{node_api_endpoint}/{APITerms.PROCEDURES.value}/{procedure_id}'
    return endpoints.handle_request(base_url, method='put', content_json=procedure)


def delete_procedure_by_id(node_api_endpoint=None, procedure_id=None):
    base_url = f'{node_api_endpoint}/{APITerms.PROCEDURES.value}/{procedure_id}'
    return endpoints.handle_request(base_url, method='delete')
