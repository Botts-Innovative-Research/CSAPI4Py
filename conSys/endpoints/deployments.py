from conSys.endpoints import endpoints
from conSys.constants import APITerms


def list_available_deployments(node_api_endpoint=None, params=None):
    base_url = f'{node_api_endpoint}/{APITerms.DEPLOYMENTS.value}'
    return endpoints.handle_request(base_url, method='get', params=params)


def create_new_deployments(node_api_endpoint=None, deployments=None):
    base_url = f'{node_api_endpoint}/{APITerms.DEPLOYMENTS.value}'
    return endpoints.handle_request(base_url, method='post', content_json=deployments)


def retrieve_deployment_by_id(node_api_endpoint=None, params=None, deployment_id=None):
    base_url = f'{node_api_endpoint}/{APITerms.DEPLOYMENTS.value}/{deployment_id}'
    return endpoints.handle_request(base_url, method='get', params=params)


def update_deployment_description_by_id(node_api_endpoint=None, deployment_id=None, deployment=None):
    base_url = f'{node_api_endpoint}/{APITerms.DEPLOYMENTS.value}/{deployment_id}'
    return endpoints.handle_request(base_url, method='put', content_json=deployment)


def delete_deployment_by_id(node_api_endpoint=None, deployment_id=None):
    base_url = f'{node_api_endpoint}/{APITerms.DEPLOYMENTS.value}/{deployment_id}'
    return endpoints.handle_request(base_url, method='delete')


def list_deployed_systems(node_api_endpoint=None, params=None, deployment_id=None):
    base_url = f'{node_api_endpoint}/{APITerms.DEPLOYMENTS.value}/{deployment_id}/{APITerms.SYSTEMS.value}'
    return endpoints.handle_request(base_url, method='get', params=params)


def add_system_to_deployment(node_api_endpoint=None, deployment_id=None, system=None):
    base_url = f'{node_api_endpoint}/{APITerms.DEPLOYMENTS.value}/{deployment_id}/{APITerms.SYSTEMS.value}'
    return endpoints.handle_request(base_url, method='post', content_json=system)


def list_deployments_of_specific_system(node_api_endpoint=None, params=None, system_id=None):
    """

    """
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}/{APITerms.DEPLOYMENTS.value}'
    return endpoints.handle_request(base_url, method='get', params=params)
