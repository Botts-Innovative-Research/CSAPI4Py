from pydantic import HttpUrl

from conSys.con_sys_api import ConnectedSystemsRequestBuilder
from conSys.constants import APITerms
from conSys.endpoints.endpoints import Endpoint


def list_all_systems(server_addr: HttpUrl, api_root: str = APITerms.API.value):
    """
    Lists all systems in the server at the default API endpoint
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.SYSTEMS.value)
                   .build_url_from_base()
                   .build())
    return api_request


def create_new_systems(server_addr: HttpUrl, request_body: dict, api_root: str = APITerms.API.value):
    """
    Create a new system as defined by the request body
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.SYSTEMS.value)
                   .with_request_body(request_body)
                   .build_url_from_base()
                   .build())
    return api_request


def list_all_systems_in_collection(server_addr: HttpUrl, collection_id: str, api_root: str = APITerms.API.value):
    """
    Lists all systems in the server at the default API endpoint
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.COLLECTIONS.value)
                   .with_resource_id(collection_id)
                   .for_sub_resource_type(APITerms.ITEMS.value)
                   .build_url_from_base()
                   .build())
    return api_request


def add_systems_to_collection(server_addr: HttpUrl, collection_id: str, uri_list: str,
                              api_root: str = APITerms.API.value):
    """
    Lists all systems in the server at the default API endpoint
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.COLLECTIONS.value)
                   .with_resource_id(collection_id)
                   .for_sub_resource_type(APITerms.ITEMS.value)
                   .with_request_body(uri_list)
                   .build_url_from_base()
                   .build())
    return api_request


def retrieve_system_by_id(server_addr: HttpUrl, system_id: str, api_root: str = APITerms.API.value):
    """
    Retrieves a system by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.SYSTEMS.value)
                   .with_resource_id(system_id)
                   .build_url_from_base()
                   .build())
    return api_request


def update_system_description(server_addr: HttpUrl, system_id: str, request_body: dict,
                              api_root: str = APITerms.API.value):
    """
    Updates a system's description by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.SYSTEMS.value)
                   .with_resource_id(system_id)
                   .with_request_body(request_body)
                   .build_url_from_base()
                   .build())
    return api_request


def delete_system_by_id(server_addr: HttpUrl, system_id: str, api_root: str = APITerms.API.value):
    """
    Deletes a system by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.SYSTEMS.value)
                   .with_resource_id(system_id)
                   .build_url_from_base()
                   .build())
    return api_request


def list_system_components(server_addr: HttpUrl, system_id: str, api_root: str = APITerms.API.value):
    """
    Lists all components of a system by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.SYSTEMS.value)
                   .with_resource_id(system_id)
                   .for_sub_resource_type(APITerms.COMPONENTS.value)
                   .build_url_from_base()
                   .build())
    return api_request


def add_system_components(server_addr: HttpUrl, system_id: str, request_body: dict,
                          api_root: str = APITerms.API.value):
    """
    Adds components to a system by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.SYSTEMS.value)
                   .with_resource_id(system_id)
                   .for_sub_resource_type(APITerms.COMPONENTS.value)
                   .with_request_body(request_body)
                   .build_url_from_base()
                   .build())
    return api_request


def list_deployments_of_system(server_addr: HttpUrl, system_id: str, api_root: str = APITerms.API.value):
    """
    Lists all deployments of a system by its id
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
    return api_request


def list_sampling_features_of_system(server_addr: HttpUrl, system_id: str, api_root: str = APITerms.API.value):
    """
    Lists all sampling features of a system by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.SYSTEMS.value)
                   .with_resource_id(system_id)
                   .for_sub_resource_type(APITerms.SAMPLING_FEATURES.value)
                   .build_url_from_base()
                   .build())
    return api_request
