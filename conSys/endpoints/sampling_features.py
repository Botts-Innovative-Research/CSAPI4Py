from conSys.endpoints import endpoints
from conSys.constants import APITerms


def list_all_sampling_features(node_api_endpoint=None, params=None):
    base_url = f'{node_api_endpoint}/{APITerms.SAMPLING_FEATURES.value}'
    return endpoints.handle_request(base_url, method='get', params=params)


def list_sampling_features_by_system(node_api_endpoint=None, params=None, system_id=None):
    base_url = f'{node_api_endpoint}/{APITerms.SYSTEMS.value}/{system_id}/{APITerms.SAMPLING_FEATURES.value}'
    return endpoints.handle_request(base_url, method='get', params=params)


def add_new_sampling_feature(node_api_endpoint=None, sampling_feature=None):
    base_url = f'{node_api_endpoint}/{APITerms.SAMPLING_FEATURES.value}'
    return endpoints.handle_request(base_url, method='post', content_json=sampling_feature)


def get_sampling_feature_by_id(node_api_endpoint=None, params=None, sampling_feature_id=None):
    base_url = f'{node_api_endpoint}/{APITerms.SAMPLING_FEATURES.value}/{sampling_feature_id}'
    return endpoints.handle_request(base_url, method='get', params=params)


def update_sampling_feature_by_id(node_api_endpoint=None, sampling_feature_id=None, sampling_feature=None):
    base_url = f'{node_api_endpoint}/{APITerms.SAMPLING_FEATURES.value}/{sampling_feature_id}'
    return endpoints.handle_request(base_url, method='put', content_json=sampling_feature)


def delete_sampling_feature_by_id(node_api_endpoint=None, sampling_feature_id=None):
    base_url = f'{node_api_endpoint}/{APITerms.SAMPLING_FEATURES.value}/{sampling_feature_id}'
    return endpoints.handle_request(base_url, method='delete')
