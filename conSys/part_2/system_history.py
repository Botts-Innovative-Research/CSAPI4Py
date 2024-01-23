import requests
from pydantic import HttpUrl

from conSys.con_sys_api import ConnectedSystemsRequestBuilder
from conSys.constants import APITerms


def list_system_history(server_addr: HttpUrl, system_id: str, api_root: str = APITerms.API.value):
    """
    Lists all history versions of a system
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.SYSTEMS.value)
                   .with_resource_id(system_id)
                   .for_resource_type(APITerms.HISTORY.value)
                   .build_url_from_base()
                   .build())
    resp = requests.get(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def retrieve_system_historical_description_by_id(server_addr: HttpUrl, system_id: str, history_id: str,
                                                 api_root: str = APITerms.API.value):
    """
    Retrieves a historical system description by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.SYSTEMS.value)
                   .with_resource_id(system_id)
                   .for_resource_type(APITerms.HISTORY.value)
                   .with_secondary_resource_id(history_id)
                   .build_url_from_base()
                   .build())
    resp = requests.get(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def update_system_historical_description(server_addr: HttpUrl, system_id: str, history_id: str, request_body: dict,
                                         api_root: str = APITerms.API.value):
    """
    Updates a historical system description by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.SYSTEMS.value)
                   .with_resource_id(system_id)
                   .for_resource_type(APITerms.HISTORY.value)
                   .with_secondary_resource_id(history_id)
                   .with_request_body(request_body)
                   .build_url_from_base()
                   .build())
    resp = requests.put(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def delete_system_historical_description_by_id(server_addr: HttpUrl, system_id: str, history_id: str,
                                               api_root: str = APITerms.API.value):
    """
    Deletes a historical system description by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.SYSTEMS.value)
                   .with_resource_id(system_id)
                   .for_resource_type(APITerms.HISTORY.value)
                   .with_secondary_resource_id(history_id)
                   .build_url_from_base()
                   .build())
    resp = requests.delete(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()
