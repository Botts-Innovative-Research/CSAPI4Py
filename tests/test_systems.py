from pydantic import HttpUrl

from src.consys4py.part_1 import list_all_systems, retrieve_system_by_id, list_all_systems_in_collection, \
    list_system_components, list_sampling_features_of_system


def test_list_systems_default():
    url: HttpUrl = 'https://api.georobotix.io/ogc/t18'
    respjson = list_all_systems(url)
    print(respjson)


def test_create_system():
    pass


def test_retrieve_systems_in_collection():
    url: HttpUrl = 'https://api.georobotix.io/ogc/t18'
    collection_id = 'all_systems'
    respjson = list_all_systems_in_collection(url, collection_id)
    print(respjson)


def test_retrieve_system_by_id():
    url: HttpUrl = 'https://api.georobotix.io/ogc/t18'
    sys_id = 'b2rju765gua3c'
    respjson = retrieve_system_by_id(url, sys_id)
    print(respjson)


def test_list_system_components():
    url: HttpUrl = 'https://api.georobotix.io/ogc/t18'
    system_id = 'b2rju765gua3c'
    respjson = list_system_components(url, system_id)
    print(respjson)

def test_list_system_sampling_features():
    url: HttpUrl = 'https://api.georobotix.io/ogc/t18'
    system_id = 'b2rju765gua3c'
    respjson = list_sampling_features_of_system(url, system_id)
    print(respjson)
