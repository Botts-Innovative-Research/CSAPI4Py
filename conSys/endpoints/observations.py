import requests

from conSys.constants import APITerms
from conSys.endpoints import endpoints


def get_observations(node_api_endpoint=None, params=None, observation_id=None):
    """
    List all observations or get a specific observation if an observation_id is provided
    :param self:
    :param node_api_endpoint:
    :param params:
    :param observation_id:
    :return:
    """

    base_url = f'{node_api_endpoint}/{APITerms.OBSERVATIONS.value}'

    if observation_id is not None:
        base_url += f'/{observation_id}'

    return endpoints.handle_request(base_url, method='get', params=params)


def get_datastream_observations(node_api_endpoint=None, params=None, datastream_id=None):
    """
    List all observations for a specific datastream
    :param node_api_endpoint:
    :param params:
    :param datastream_id:
    :return:
    """
    base_url = f'{node_api_endpoint}/{APITerms.OBSERVATIONS.value}/{APITerms.DATASTREAMS.value}/{datastream_id}'

    return endpoints.handle_request(base_url, method='get', params=params)


def post_datastream_observations(node_api_endpoint=None, datastream_id=None, observations=None):
    """
    Post observations for a specific datastream. Can be either a single observation or an array of observations
    :param node_api_endpoint:
    :param datastream_id:
    :param observations:
    :return:
    """
    base_url = f'{node_api_endpoint}/{APITerms.DATASTREAMS.value}/{datastream_id}/{APITerms.OBSERVATIONS.value}'

    return endpoints.handle_request(base_url, method='post', content_json=observations)
