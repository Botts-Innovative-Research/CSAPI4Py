from typing import Union

import requests
from pydantic import HttpUrl

from conSys.con_sys_api import ConnectedSystemsRequestBuilder
from conSys.constants import APITerms


def list_all_datastreams(server_addr: HttpUrl, api_root: str = APITerms.API.value, headers: dict = None):
    """
    Lists all datastreams
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.DATASTREAMS.value)
                   .build_url_from_base()
                   .with_headers(headers)
                   .with_request_method('GET')
                   .build())

    return api_request.make_request()


def list_all_datastreams_of_system(server_addr: HttpUrl, system_id: str, api_root: str = APITerms.API.value,
                                   headers=None):
    """
    Lists all datastreams of a system
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.SYSTEMS.value)
                   .with_resource_id(system_id)
                   .for_sub_resource_type(APITerms.DATASTREAMS.value)
                   .build_url_from_base()
                   .with_headers(headers)
                   .with_request_method('GET')
                   .build())
    return api_request.make_request()


def add_datastreams_to_system(server_addr: HttpUrl, system_id: str, request_body: Union[str, dict],
                              api_root: str = APITerms.API.value, headers=None):
    """
    Adds a datastream to a system by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.SYSTEMS.value)
                   .with_resource_id(system_id)
                   .for_sub_resource_type(APITerms.DATASTREAMS.value)
                   .with_request_body(request_body)
                   .build_url_from_base()
                   .with_headers(headers)
                   .with_request_method('POST')
                   .build())
    return api_request.make_request()


def retrieve_datastream_by_id(server_addr: HttpUrl, datastream_id: str, api_root: str = APITerms.API.value,
                              headers=None):
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
                   .with_headers(headers)
                   .with_request_method('GET')
                   .build())
    return api_request.make_request()


def update_datastream_by_id(server_addr: HttpUrl, datastream_id: str, request_body: Union[str, dict],
                            api_root: str = APITerms.API.value, headers=None):
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
                   .with_headers(headers)
                   .with_request_method('PUT')
                   .build())
    return api_request.make_request()


def delete_datastream_by_id(server_addr: HttpUrl, datastream_id: str, api_root: str = APITerms.API.value, headers=None):
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
                   .with_headers(headers)
                   .with_request_method('DELETE')
                   .build())
    return api_request.make_request()


def retrieve_datastream_schema(server_addr: HttpUrl, datastream_id: str, api_root: str = APITerms.API.value,
                               headers=None):
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
                   .with_headers(headers)
                   .with_request_method('GET')
                   .build())
    return api_request.make_request()


def update_datastream_schema(server_addr: HttpUrl, datastream_id: str, request_body: dict,
                             api_root: str = APITerms.API.value, headers=None):
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
                   .with_headers(headers)
                   .with_request_method('PUT')
                   .build())
    return api_request.make_request()
