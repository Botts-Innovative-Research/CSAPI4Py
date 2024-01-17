import requests
from conSys.endpoints import endpoints
from conSys.constants import APITerms


def get_systems(node_api_endpoint=None, params: dict = None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}'
    return endpoints.handle_request(base_url, method='get', params=params)


def get_system(node_api_endpoint=None, params=None, system_id=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}'
    return endpoints.handle_request(base_url, method='get', params=params)


def get_system_details(node_api_endpoint=None, params=None, system_id=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}/details'
    return endpoints.handle_request(base_url, method='get', params=params)


def get_system_datastreams(node_api_endpoint=None, params=None, system_id=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}/datastreams'
    return endpoints.handle_request(base_url, method='get', params=params)


def get_system_controls(node_api_endpoint=None, params=None, system_id=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}/controls'
    return endpoints.handle_request(base_url, method='get', params=params)


def get_system_fois(node_api_endpoint=None, params=None, system_id=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}/featuresOfInterest'
    return endpoints.handle_request(base_url, method='get', params=params)


def get_system_history(node_api_endpoint=None, params=None, system_id=None, version=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}/history'

    if version is not None:
        base_url = f'{base_url}/{version}'

    return endpoints.handle_request(base_url, method='get', params=params)


def post_system(node_api_endpoint=None, system=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}'
    return endpoints.handle_request(base_url, method='post', content_json=system)


def post_system_contact(node_api_endpoint=None, system_id=None, contact=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}/contacts'
    return endpoints.handle_request(base_url, method='post', content_json=contact)


def post_system_events(node_api_endpoint=None, system_id=None, events=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}/events'
    return endpoints.handle_request(base_url, method='post', content_json=events)


def post_system_member(node_api_endpoint=None, system_id=None, member=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}/members'
    return endpoints.handle_request(base_url, method='post', content_json=member)


def post_system_datastream(node_api_endpoint=None, system_id=None, datastream=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}/datastreams'
    return endpoints.handle_request(base_url, method='post', content_json=datastream)


def post_system_controls(node_api_endpoint=None, system_id=None, controls=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}/controls'
    return endpoints.handle_request(base_url, method='post', content_json=controls)


def post_system_foi(node_api_endpoint=None, system_id=None, foi=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}/featuresOfInterest'
    return endpoints.handle_request(base_url, method='post', content_json=foi)


def post_system_history(node_api_endpoint=None, system_id=None, history=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}/history'
    return endpoints.handle_request(base_url, method='post', content_json=history)


def put_system(node_api_endpoint=None, system_id=None, system=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}'
    return endpoints.handle_request(base_url, method='put', content_json=system)


def put_system_details(node_api_endpoint=None, system_id=None, details=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}/details'
    return endpoints.handle_request(base_url, method='put', content_json=details)


def put_system_history_version(node_api_endpoint=None, system_id=None, version=None,
                               history=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}/history/{version}'
    return endpoints.handle_request(base_url, method='put', content_json=history)
