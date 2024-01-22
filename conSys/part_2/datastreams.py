import requests
from pydantic import HttpUrl

from conSys.con_sys_api import ConnectedSystemsRequestBuilder
from conSys.constants import APITerms


def list_all_datastreams(server_addr: HttpUrl, api_root: str = APITerms.API.value):
    """
    Lists all datastreams
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.DATASTREAMS.value)
                   .build_url_from_base()
                   .build())
    resp = requests.get(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def list_all_datastreams_of_system(server_addr: HttpUrl, system_id: str, api_root: str = APITerms.API.value):
    """
    Lists all datastreams of a system
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.SYSTEMS.value)
                   .with_resource_id(system_id)
                   .for_resource_type(APITerms.DATASTREAMS.value)
                   .build_url_from_base()
                   .build())
    resp = requests.get(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def add_datastreams_to_system(server_addr: HttpUrl, system_id: str, request_body: dict,
                              api_root: str = APITerms.API.value):
    """
    Adds a datastream to a system by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.SYSTEMS.value)
                   .with_resource_id(system_id)
                   .for_resource_type(APITerms.DATASTREAMS.value)
                   .with_request_body(request_body)
                   .build_url_from_base()
                   .build())
    resp = requests.post(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def retrieve_datastream_by_id(server_addr: HttpUrl, datastream_id: str, api_root: str = APITerms.API.value):
    """
    Retrieves a datastream by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.DATASTREAMS.value)
                   .with_resource_id(datastream_id)
                   .build_url_from_base()
                   .build())
    resp = requests.get(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def update_datastream_by_id(server_addr: HttpUrl, datastream_id: str, request_body: dict,
                            api_root: str = APITerms.API.value):
    """
    Updates a datastream by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.DATASTREAMS.value)
                   .with_resource_id(datastream_id)
                   .with_request_body(request_body)
                   .build_url_from_base()
                   .build())
    resp = requests.put(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def delete_datastream_by_id(server_addr: HttpUrl, datastream_id: str, api_root: str = APITerms.API.value):
    """
    Deletes a datastream by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.DATASTREAMS.value)
                   .with_resource_id(datastream_id)
                   .build_url_from_base()
                   .build())
    resp = requests.delete(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def retrieve_datastream_schema(server_addr: HttpUrl, datastream_id: str, api_root: str = APITerms.API.value):
    """
    Retrieves a datastream schema by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.DATASTREAMS.value)
                   .with_resource_id(datastream_id)
                   .for_resource_type(APITerms.SCHEMA.value)
                   .build_url_from_base()
                   .build())
    resp = requests.get(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def update_datastream_schema(server_addr: HttpUrl, datastream_id: str, request_body: dict,
                             api_root: str = APITerms.API.value):
    """
    Updates a datastream schema by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.DATASTREAMS.value)
                   .with_resource_id(datastream_id)
                   .for_resource_type(APITerms.SCHEMA.value)
                   .with_request_body(request_body)
                   .build_url_from_base()
                   .build())
    resp = requests.put(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()
