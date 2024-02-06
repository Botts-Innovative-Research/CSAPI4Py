import random

from conSys import Systems, SamplingFeatures, Datastreams, SmlJSONBody, GeoJSONBody, model_utils, \
    DatastreamBodyJSON, ObservationFormat, URI
from conSys.datamodels.datastreams import SWEDatastreamSchema
from conSys.datamodels.encoding import JSONEncoding
from conSys.datamodels.swe_components import BooleanSchema, TimeSchema, DataRecordSchema

server_url = "http://localhost:8282/sensorhub"
geo_json_headers = {"Content-Type": "application/geo+json"}
sml_json_headers = {"Content-Type": "application/sml+json"}
json_headers = {"Content-Type": "application/json"}

system_json = []
retrieved_systems = []
procedure_json = []
deployment_json = []
component_json = []
command_json = []
control_channel_json = []

"""
Setup Section
"""


def test_add_systems():
    """
    Tests the creation of systems using the Connected Systems API by adding a single system and a batch of systems.
    :return:
    """
    arg_keys = ['type', 'id', 'description', 'properties']
    property_keys = ['featureType', 'name', 'uid', 'description']

    sml_temp = SmlJSONBody(object_type='SimpleProcess', id=str(random.randint(1000, 9999)),
                           description="A Test System inserted from the Python Connected Systems API Client",
                           unique_id=f'urn:test:client:sml-single', label=f'Test System - SML Single',
                           definition="http://test.com")

    geo_temp = GeoJSONBody(type='Feature', id=str(random.randint(1000, 9999)),
                           description="Test Insertion of System via GEOJSON",
                           properties={
                               "featureType": "http://www.w3.org/ns/ssn/System",
                               "name": f'Test System - GeoJSON',
                               "uid": f'urn:test:client:geo-single',
                               "description": "A Test System inserted from the Python Connected Systems API Client",
                           })
    system_json.append(sml_temp)
    system_json.append(geo_temp)
    Systems.create_new_systems(server_url, sml_temp.model_dump_json(exclude_none=True, by_alias=True), uname="admin",
                               pword="admin",
                               headers=sml_json_headers)
    Systems.create_new_systems(server_url, geo_temp.model_dump_json(exclude_none=True, by_alias=True), uname="admin",
                               pword="admin",
                               headers=geo_json_headers)

    batch_systems = []
    for i in range(2, 6):
        temp = SmlJSONBody(object_type='SimpleProcess', id=str(random.randint(1000, 9999)),
                           description="Batch inserted system from a test of the Python API Client",
                           unique_id=f'urn:test:client:{i}', label=f'Test System - {i}',
                           definition="http://test.com")
        new_json = temp.model_dump(exclude_none=True, by_alias=True)
        batch_systems.append(temp)
        system_json.append(temp.model_dump_json(exclude_none=True, by_alias=True))

    batch_json_str = model_utils.serialize_model_list(batch_systems)
    Systems.create_new_systems(server_url, batch_json_str, uname="admin", pword="admin",
                               headers=sml_json_headers)


def test_list_systems():
    """
    Tests the listing of systems using the Connected Systems API by listing all systems and all systems in a collection.
    :return:
    """
    sys_list = Systems.list_all_systems(server_url)["items"]
    retrieved_systems.extend(sys_list)

    for system in retrieved_systems:
        print(system)


def test_retrieve_system():
    """
    Tests the retrieval of a system using the Connected Systems API by retrieving a single system and a batch of systems.
    :return:
    """
    system_id = retrieved_systems[0]['id']
    retrieved_system = Systems.retrieve_system_by_id(server_url, system_id)
    print(retrieved_system)
    assert retrieved_system is not None
    assert retrieved_system['id'] == system_id


def test_update_systems():
    if retrieved_systems is None or len(retrieved_systems) == 0:
        raise ValueError("No systems to update")
    for system in retrieved_systems:
        print(system)
        sml_temp = SmlJSONBody(object_type='SimpleProcess', id=str(random.randint(1000, 9999)),
                               description="Modified by an update via CSAPI4Py",
                               unique_id=system['properties']['uid'], label=system['properties']['name'],
                               definition="http://test.com")
        Systems.update_system_description(server_url, system['id'],
                                          sml_temp.model_dump_json(exclude_none=True, by_alias=True),
                                          headers=sml_json_headers)


"""
Procedure Tests
"""
# def test_create_procedures():
#     sml_procedure = SmlJSONBody(object_type='SimpleProcess', id=str(random.randint(1000, 9999)),
#                                 description="A Test Procedure inserted from the Python CSAPI Client",
#                                 unique_id=f'urn:test:client:sml-procedure',
#                                 label=f'Test Procedure - SML',
#                                 definition="http://www.w3.org/ns/sosa/Procedure")
#     geo_procedure = GeoJSONBody(type='Feature', id=str(random.randint(1000, 9999)),
#                                 description="Test Insertion of Procedure via GEOJSON",
#                                 properties={
#                                     "featureType": "http://www.w3.org/ns/ssn/Procedure",
#                                     "name": f'Test Procedure - GeoJSON',
#                                     "uid": f'urn:test:client:geo-procedure',
#                                     "description": "A Test Procedure inserted from the Python CSAPI Client",
#                                 })
#
#     resp = Procedures.create_new_procedures(server_url, geo_procedure.model_dump_json(exclude_none=True, by_alias=True),
#                                             headers=geo_json_headers)
#     print(resp)

"""
Sampling Feature Tests
"""
sf_id = None


def test_create_sampling_feature():
    geo_sf = GeoJSONBody(type='Feature', id=str(random.randint(1000, 9999)),
                         description="Test Insertion of Sampling Feature via GEOJSON",
                         properties={
                             "featureType": "http://www.w3.org/ns/ssn/SamplingFeature",
                             "name": f'Test Sampling Feature - GeoJSON',
                             "uid": f'urn:test:client:geo-sf',
                             "description": "A Test Sampling Feature inserted from the Python CSAPI Client",
                         })

    resp = SamplingFeatures.create_new_sampling_features(server_url, retrieved_systems[0]['id'],
                                                         geo_sf.model_dump_json(exclude_none=True, by_alias=True),
                                                         headers=geo_json_headers)

    geo_sf = GeoJSONBody(type='Feature', id=str(random.randint(1000, 9999)),
                         description="Test Insertion of Sampling Feature via GEOJSON",
                         properties={
                             "featureType": "http://www.w3.org/ns/ssn/SamplingFeature",
                             "name": f'Test Sampling Feature - GeoJSON',
                             "uid": f'urn:test:client:geo-sf2',
                             "description": "A Test Sampling Feature inserted from the Python CSAPI Client",
                         })

    resp = SamplingFeatures.create_new_sampling_features(server_url, retrieved_systems[1]['id'],
                                                         geo_sf.model_dump_json(exclude_none=True, by_alias=True),
                                                         headers=geo_json_headers)
    print(resp)


def test_list_sampling_features():
    sf_list = SamplingFeatures.list_all_sampling_features(server_url)
    print(sf_list.json())


def test_list_sampling_feature_by_system():
    sf_list = SamplingFeatures.list_sampling_features_of_system(server_url, retrieved_systems[0]['id'])
    print(sf_list.json())
    sf_id = sf_list.json()['items'][0]['id']


def test_update_sampling_feature():
    sf_list = SamplingFeatures.list_sampling_features_of_system(server_url, retrieved_systems[0]['id'])
    print(sf_list.json())
    sf_id = sf_list.json()['items'][0]['id']
    geo_sf = GeoJSONBody(type='Feature', id=str(random.randint(1000, 9999)),
                         description="Test Insertion of Sampling Feature via GEOJSON",
                         properties={
                             "featureType": "http://www.w3.org/ns/ssn/SamplingFeature",
                             "name": f'Test Sampling Feature - GeoJSON (Updated)',
                             "uid": f'urn:test:client:geo-sf',
                             "description": "A Test Sampling Feature updated from the Python CSAPI Client",
                         })

    resp = SamplingFeatures.update_sampling_feature_by_id(server_url,
                                                          sf_id,
                                                          geo_sf.model_dump_json(exclude_none=True,
                                                                                 by_alias=True),
                                                          headers=geo_json_headers)
    print(resp)


def test_retrieve_sampling_feature_by_id():
    sf = SamplingFeatures.retrieve_sampling_feature_by_id(server_url, sf_id)
    print(f'Retrieved by ID: {sf.json()}')


"""
Datastream Section
"""


def test_create_datastreams():
    time_schema = TimeSchema(label="Test Datastream Time", definition="http://test.com/Time",
                             uom=URI(href="http://test.com/TimeUOM"))
    bool_schema = BooleanSchema(label="Test Datastream Boolean", definition="http://test.com/Boolean")
    datarecord_schema = SWEDatastreamSchema(encoding=JSONEncoding(), obs_format=ObservationFormat.SWE_JSON.value,
                                            record_schema=DataRecordSchema(label="Test Datastream Record",
                                                                           definition="http://test.com/Record",
                                                                           fields=[time_schema, bool_schema]))

    print(f'Datastream Schema: {datarecord_schema.model_dump_json(exclude_none=True, by_alias=True)}')
    datastream_body = DatastreamBodyJSON(name="Test Datastream", output_name="Test Output #1", schema=datarecord_schema)
    temp_test_json = datastream_body.model_dump_json(exclude_none=True, by_alias=True)
    print(f'Test Datastream JSON: {temp_test_json}')
    resp = Datastreams.add_datastreams_to_system(server_url, retrieved_systems[0]['id'],
                                                 datastream_body.model_dump_json(exclude_none=True, by_alias=True),
                                                 headers=json_headers)
    print(resp)


"""
Teardown Section
"""

# def test_delete_all_systems():
#     sys_list = Systems.list_all_systems("http://localhost:8181/sensorhub")["items"]
#     print(sys_list)
#
#     for system in sys_list:
#         print(system)
#
#         Systems.delete_system_by_id("http://localhost:8181/sensorhub", system["id"])
#         print(f"Deleted system {system['id']}")
