from pydantic import HttpUrl

from conSys.con_sys_api import ConnectedSystemsRequestBuilder
from conSys.constants import APITerms


def list_all_deployments(server_addr: HttpUrl, api_root: str = APITerms.API.value):
    """
    Lists all deployments in the server at the default API endpoint
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.DEPLOYMENTS.value)
                   .build_url_from_base()
                   .build())
    return api_request


def create_new_deployments(server_addr: HttpUrl, request_body: dict, api_root: str = APITerms.API.value):
    """
    Create a new deployment as defined by the request body
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.DEPLOYMENTS.value)
                   .with_request_body(request_body)
                   .build_url_from_base()
                   .build())
    return api_request


def retrieve_deployment_by_id(server_addr: HttpUrl, deployment_id: str, api_root: str = APITerms.API.value):
    """
    Retrieve a deployment by its ID
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.DEPLOYMENTS.value)
                   .with_resource_id(deployment_id)
                   .build_url_from_base()
                   .build())
    return api_request


def update_deployment_by_id(server_addr: HttpUrl, deployment_id: str, request_body: dict,
                            api_root: str = APITerms.API.value):
    """
    Update a deployment by its ID
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.DEPLOYMENTS.value)
                   .with_resource_id(deployment_id)
                   .with_request_body(request_body)
                   .build_url_from_base()
                   .build())
    return api_request


def delete_deployment_by_id(server_addr: HttpUrl, deployment_id: str, api_root: str = APITerms.API.value):
    """
    Delete a deployment by its ID
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.DEPLOYMENTS.value)
                   .with_resource_id(deployment_id)
                   .build_url_from_base()
                   .build())
    return api_request


def list_deployed_systems(server_addr: HttpUrl, deployment_id, api_root: str = APITerms.API.value):
    """
    Lists all deployed systems in the server at the default API endpoint
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.DEPLOYMENTS.value)
                   .with_resource_id(deployment_id)
                   .for_sub_resource_type(APITerms.SYSTEMS.value)
                   .build_url_from_base()
                   .build())
    return api_request


def add_systems_to_deployment(server_addr: HttpUrl, deployment_id: str, uri_list: str,
                              api_root: str = APITerms.API.value):
    """
    Lists all systems in the server at the default API endpoint
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.DEPLOYMENTS.value)
                   .with_resource_id(deployment_id)
                   .for_sub_resource_type(APITerms.SYSTEMS.value)
                   .with_request_body(uri_list)
                   .build_url_from_base()
                   .build())
    return api_request


def retrieve_deployed_system_by_id(server_addr: HttpUrl, deployment_id: str, system_id: str,
                                   api_root: str = APITerms.API.value):
    """
    Retrieves a system by its id
    :return:
    """

    # TODO: Add a way to have a secondary resource ID for certain endpoints
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.DEPLOYMENTS.value)
                   .with_resource_id(deployment_id)
                   .for_sub_resource_type(APITerms.SYSTEMS.value)
                   .with_secondary_resource_id(system_id)
                   .build_url_from_base()
                   .build())
    return api_request


def update_deployed_system_by_id(server_addr: HttpUrl, deployment_id: str, system_id: str, request_body: dict,
                                 api_root: str = APITerms.API.value):
    """
    Update a system by its ID
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.DEPLOYMENTS.value)
                   .with_resource_id(deployment_id)
                   .for_sub_resource_type(APITerms.SYSTEMS.value)
                   .with_secondary_resource_id(system_id)
                   .with_request_body(request_body)
                   .build_url_from_base()
                   .build())

    return api_request


def delete_deployed_system_by_id(server_addr: HttpUrl, deployment_id: str, system_id: str,
                                 api_root: str = APITerms.API.value):
    """
    Delete a system by its ID
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.DEPLOYMENTS.value)
                   .with_resource_id(deployment_id)
                   .for_sub_resource_type(APITerms.SYSTEMS.value)
                   .with_secondary_resource_id(system_id)
                   .build_url_from_base()
                   .build())
    return api_request


def list_deployments_of_specific_system(server_addr: HttpUrl, system_id: str, api_root: str = APITerms.API.value):
    """
    Lists all deployments of a specific system in the server at the default API endpoint
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.SYSTEMS.value)
                   .with_resource_id(system_id)
                   .for_sub_resource_type(APITerms.DEPLOYMENTS.value)
                   .build_url_from_base()
                   .build())
