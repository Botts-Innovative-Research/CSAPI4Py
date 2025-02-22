import consys4py.core.default_api_helpers as helpers
from consys4py import APIResourceTypes, GeoJSONBody

server_url = 'http://localhost:8282/sensorhub'
api_endpoint = 'api'
geojson_headers = {"Content-Type": "application/geo+json"}


def test_determine_parent_type():
    assert helpers.determine_parent_type(APIResourceTypes.SYSTEM) == APIResourceTypes.SYSTEM
    assert helpers.determine_parent_type(APIResourceTypes.COLLECTION) is None
    assert helpers.determine_parent_type(APIResourceTypes.CONTROL_CHANNEL) == APIResourceTypes.SYSTEM
    assert helpers.determine_parent_type(APIResourceTypes.COMMAND) == APIResourceTypes.CONTROL_CHANNEL
    assert helpers.determine_parent_type(APIResourceTypes.DATASTREAM) == APIResourceTypes.SYSTEM
    assert helpers.determine_parent_type(APIResourceTypes.OBSERVATION) == APIResourceTypes.DATASTREAM
    assert helpers.determine_parent_type(APIResourceTypes.SYSTEM_EVENT) == APIResourceTypes.SYSTEM
    assert helpers.determine_parent_type(APIResourceTypes.SAMPLING_FEATURE) == APIResourceTypes.SYSTEM
    assert helpers.determine_parent_type(APIResourceTypes.PROCEDURE) is None
    assert helpers.determine_parent_type(APIResourceTypes.PROPERTY) is None
    assert helpers.determine_parent_type(APIResourceTypes.SYSTEM_HISTORY) is None
    assert helpers.determine_parent_type(APIResourceTypes.DEPLOYMENT) is None


def test_resource_type_to_ep():
    assert helpers.resource_type_to_endpoint(APIResourceTypes.SYSTEM) == 'systems'
    assert helpers.resource_type_to_endpoint(APIResourceTypes.COLLECTION) == 'collections'
    assert helpers.resource_type_to_endpoint(APIResourceTypes.CONTROL_CHANNEL) == 'controls'
    assert helpers.resource_type_to_endpoint(APIResourceTypes.COMMAND) == 'commands'
    assert helpers.resource_type_to_endpoint(APIResourceTypes.DATASTREAM) == 'datastreams'
    assert helpers.resource_type_to_endpoint(APIResourceTypes.OBSERVATION) == 'observations'
    assert helpers.resource_type_to_endpoint(APIResourceTypes.SYSTEM_EVENT) == 'systemEvents'
    assert helpers.resource_type_to_endpoint(APIResourceTypes.SAMPLING_FEATURE) == 'samplingFeatures'
    assert helpers.resource_type_to_endpoint(APIResourceTypes.PROCEDURE) == 'procedures'
    assert helpers.resource_type_to_endpoint(APIResourceTypes.PROPERTY) == 'properties'
    assert helpers.resource_type_to_endpoint(APIResourceTypes.SYSTEM_HISTORY) == 'history'
    assert helpers.resource_type_to_endpoint(APIResourceTypes.DEPLOYMENT) == 'deployments'
    assert helpers.resource_type_to_endpoint(APIResourceTypes.SYSTEM, APIResourceTypes.COLLECTION) == 'items'


def test_resolve_resource_ep():
    # server_url = 'http://localhost:8181'
    # api_endpoint = 'api'
    api_helper = helpers.APIHelper(server_url, api_endpoint)
    assert api_helper.server_url == server_url
    assert api_helper.api_root == api_endpoint
    assert api_helper.resource_url_resolver(APIResourceTypes.SYSTEM) == f'{server_url}/{api_endpoint}/systems'
    assert api_helper.resource_url_resolver(APIResourceTypes.SYSTEM,
                                            '1234') == f'{server_url}/{api_endpoint}/systems/1234'
    assert api_helper.resource_url_resolver(APIResourceTypes.COLLECTION, '1234',
                                            from_collection=False) == f'{server_url}/{api_endpoint}/collections/1234'
    assert api_helper.resource_url_resolver(APIResourceTypes.SYSTEM, '1234', '5678',
                                            True) == f'{server_url}/{api_endpoint}/collections/5678/items/1234'


def test_user_auth():
    # server_url = 'http://localhost:8181'
    # api_endpoint = 'api'
    uname = 'user'
    pword = 'pass'
    api_helper = helpers.APIHelper(server_url, api_endpoint, uname, pword, True)
    assert api_helper.get_helper_auth() == ('user', 'pass')
    api_helper.user_auth = False
    assert api_helper.get_helper_auth() is None


def test_create_resource_system():
    system_obj = GeoJSONBody(type='Feature', id='',
                             properties={
                                 "featureType": "http://www.w3.org/ns/ssn/System",
                                 "name": f'Test System - APIHelper',
                                 "uid": f'urn:test:client:apihelper',
                                 "description": "A Test System inserted using the APIHelper class"
                             })
    api_helper = helpers.APIHelper(server_url, api_endpoint)
    result = api_helper.create_resource(res_type=APIResourceTypes.SYSTEM,
                                        json_data=system_obj.model_dump_json(exclude_none=True, by_alias=True),
                                        req_headers=geojson_headers)
    print(result)
