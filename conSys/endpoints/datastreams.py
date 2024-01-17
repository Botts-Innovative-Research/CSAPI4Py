import requests
from conSys.endpoints import system_ep, endpoints
from conSys.constants import APITerms


def get_datastreams(node_api_endpoint=None, params=None, datastream_id=None):
    base_url = f'{node_api_endpoint}/{APITerms.DATASTREAMS.value}'

    if datastream_id is not None:
        base_url += f'/{datastream_id}'

    return endpoints.handle_request(base_url, method='get', params=params)


def get_datastream_from_system(node_api_endpoint=None, params=None, system_id=None):
    return system_ep.get_system_datastreams(node_api_endpoint=node_api_endpoint, params=params, system_id=system_id)


def get_datastream_schema(node_api_endpoint=None, params=None, datastream_id=None):
    base_url = f'{node_api_endpoint}/{APITerms.DATASTREAMS.value}/{datastream_id}/schema'

    return endpoints.handle_request(base_url, method='get', params=params)


def post_datastream(node_api_endpoint=None, system_id=None, datastream=None):
    return system_ep.post_system_datastream(node_api_endpoint=node_api_endpoint, system_id=system_id,
                                            datastream=datastream)
