import requests
from pydantic import HttpUrl

from conSys.con_sys_api import ConnectedSystemsRequestBuilder
from conSys.constants import APITerms


def list_all_observations(server_addr: HttpUrl, api_root: str = APITerms.API.value):
    """
    Lists all observations
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.OBSERVATIONS.value)
                   .build_url_from_base()
                   .build())
    resp = requests.get(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def list_observations_from_datastream(server_addr: HttpUrl, datastream_id: str, api_root: str = APITerms.API.value):
    """
    Lists all observations of a datastream
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.DATASTREAMS.value)
                   .with_resource_id(datastream_id)
                   .for_resource_type(APITerms.OBSERVATIONS.value)
                   .build_url_from_base()
                   .build())
    resp = requests.get(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def add_observations_to_datastream(server_addr: HttpUrl, datastream_id: str, request_body: dict,
                                   api_root: str = APITerms.API.value):
    """
    Adds an observation to a datastream by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.DATASTREAMS.value)
                   .with_resource_id(datastream_id)
                   .for_resource_type(APITerms.OBSERVATIONS.value)
                   .with_request_body(request_body)
                   .build_url_from_base()
                   .build())
    resp = requests.post(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def retrieve_observation_by_id(server_addr: HttpUrl, observation_id: str, api_root: str = APITerms.API.value):
    """
    Retrieves an observation by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.OBSERVATIONS.value)
                   .with_resource_id(observation_id)
                   .build_url_from_base()
                   .build())
    resp = requests.get(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def update_observation_by_id(server_addr: HttpUrl, observation_id: str, request_body: dict,
                             api_root: str = APITerms.API.value):
    """
    Updates an observation by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.OBSERVATIONS.value)
                   .with_resource_id(observation_id)
                   .with_request_body(request_body)
                   .build_url_from_base()
                   .build())
    resp = requests.put(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()


def delete_observation_by_id(server_addr: HttpUrl, observation_id: str, api_root: str = APITerms.API.value):
    """
    Deletes an observation by its id
    :return:
    """
    builder = ConnectedSystemsRequestBuilder()
    api_request = (builder.with_server_url(server_addr)
                   .with_api_root(api_root)
                   .for_resource_type(APITerms.OBSERVATIONS.value)
                   .with_resource_id(observation_id)
                   .build_url_from_base()
                   .build())
    resp = requests.delete(api_request.url, params=api_request.body, headers=api_request.headers)
    return resp.json()
