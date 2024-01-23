import requests
from pydantic import HttpUrl

from conSys.con_sys_api import ConnectedSystemsRequestBuilder
from conSys.constants import APITerms


def list_all_constrol_streams(server_addr: HttpUrl, api_root: str = APITerms.API.value):
    """
    Lists all control streams
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.CONTROL_STREAMS.value)
                   .build_url_from_base()
                   .build())
    resp = requests.get(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def list_control_streams_of_system(server_addr: HttpUrl, system_id: str, api_root: str = APITerms.API.value):
    """
    Lists all control streams of a system
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.SYSTEMS.value)
                   .with_resource_id(system_id)
                   .for_resource_type(APITerms.CONTROL_STREAMS.value)
                   .build_url_from_base()
                   .build())
    resp = requests.get(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def add_control_streams_to_system(server_addr: HttpUrl, system_id: str, request_body: dict,
                                  api_root: str = APITerms.API.value):
    """
    Adds a control stream to a system by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.SYSTEMS.value)
                   .with_resource_id(system_id)
                   .for_resource_type(APITerms.CONTROL_STREAMS.value)
                   .with_request_body(request_body)
                   .build_url_from_base()
                   .build())
    resp = requests.post(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def retrieve_control_stream_description_by_id(server_addr: HttpUrl, control_stream_id: str,
                                              api_root: str = APITerms.API.value):
    """
    Retrieves a control stream by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.CONTROL_STREAMS.value)
                   .with_resource_id(control_stream_id)
                   .build_url_from_base()
                   .build())
    resp = requests.get(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def update_control_stream_description_by_id(server_addr: HttpUrl, control_stream_id: str, request_body: dict,
                                            api_root: str = APITerms.API.value):
    """
    Updates a control stream by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.CONTROL_STREAMS.value)
                   .with_resource_id(control_stream_id)
                   .with_request_body(request_body)
                   .build_url_from_base()
                   .build())
    resp = requests.put(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def delete_control_stream_by_id(server_addr: HttpUrl, control_stream_id: str, api_root: str = APITerms.API.value):
    """
    Deletes a control stream by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.CONTROL_STREAMS.value)
                   .with_resource_id(control_stream_id)
                   .build_url_from_base()
                   .build())
    resp = requests.delete(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def retrieve_control_stream_schema_by_id(server_addr: HttpUrl, control_stream_id: str,
                                         api_root: str = APITerms.API.value):
    """
    Retrieves a control stream schema by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.CONTROL_STREAMS.value)
                   .with_resource_id(control_stream_id)
                   .for_resource_type(APITerms.SCHEMA.value)
                   .build_url_from_base()
                   .build())
    resp = requests.get(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def update_control_stream_schema_by_id(server_addr: HttpUrl, control_stream_id: str, request_body: dict,
                                       api_root: str = APITerms.API.value):
    """
    Updates a control stream schema by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.CONTROL_STREAMS.value)
                   .with_resource_id(control_stream_id)
                   .for_resource_type(APITerms.SCHEMA.value)
                   .with_request_body(request_body)
                   .build_url_from_base()
                   .build())
    resp = requests.put(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()
