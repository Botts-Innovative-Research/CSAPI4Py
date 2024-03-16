import random
from datetime import datetime

from conSys4Py import Systems, SamplingFeatures, Datastreams, SmlJSONBody, GeoJSONBody, model_utils, \
    DatastreamBodyJSON, ObservationFormat, URI, Procedures, Geometry, Deployments, ControlChannels, Observations, \
    Commands
from conSys4Py.datamodels.control_streams import ControlStreamJSONSchema, SWEControlChannelSchema, JSONControlChannelSchema
from conSys4Py.datamodels.datastreams import SWEDatastreamSchema
from conSys4Py.datamodels.encoding import JSONEncoding
from conSys4Py.datamodels.swe_components import BooleanSchema, TimeSchema, DataRecordSchema, CountSchema
from conSys4Py.datamodels.observations import ObservationOMJSONInline
from conSys4Py.datamodels.commands import CommandJSON

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
test_time_start = datetime.utcnow()

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
    sys_list = Systems.list_all_systems(server_url)
    print(sys_list.json())
    retrieved_systems = sys_list.json()


def test_retrieve_system():
    """
    Tests the retrieval of a system using the Connected Systems API by retrieving a single system and a batch of systems.
    :return:
    """
    system_id = Systems.list_all_systems(server_url).json()['items'][0]['id']
    retrieved_system = Systems.retrieve_system_by_id(server_url, system_id)
    print(retrieved_system)
    assert retrieved_system is not None
    assert retrieved_system['id'] == system_id


def test_update_systems():
    retrieved_systems = Systems.list_all_systems(server_url, headers=json_headers).json()['items']
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
Deployments Section
"""


def test_create_deployments():
    deployment = GeoJSONBody(type='Feature', id=str(random.randint(1000, 9999)), properties={
        "featureType": "http://www.w3.org/ns/ssn/Deployment",
        "uid": "urn:test:client:geo-deployment",
        "name": "Test Deployment - GeoJSON",
        "description": "A Test Deployment inserted from the Python CSAPI Client",
        "validTime": ["2024-01-01T00:00:00Z", "2024-12-31T23:59:59Z"]
    }, geometry=Geometry(type="Point", coordinates=[-80.0, 35.0]))
    resp = Deployments.create_new_deployments(server_url, deployment.model_dump_json(exclude_none=True, by_alias=True),
                                              headers=geo_json_headers)
    print(resp)


def test_list_all_deployments():
    deployments = Deployments.list_all_deployments(server_url)
    print(deployments.json())


def test_retrieve_deployment_by_id():
    deployments = Deployments.list_all_deployments(server_url)

    deployment = Deployments.retrieve_deployment_by_id(server_url, deployments.json()['items'][0]['id'])
    print(deployment.json())
    assert deployment.json()['id'] == deployments.json()['items'][0]['id']


def test_update_deployment_by_id():
    deployments = Deployments.list_all_deployments(server_url)

    deployment = GeoJSONBody(type='Feature', id=str(random.randint(1000, 9999)), properties={
        "featureType": "http://www.w3.org/ns/ssn/Deployment",
        "uid": "urn:test:client:geo-deployment",
        "name": "Test Deployment - GeoJSON (Updated)",
        "description": "A Test Deployment updated from the Python CSAPI Client",
        "validTime": ["2024-01-01T00:00:00Z", "2024-12-31T23:59:59Z"]
    }, geometry=Geometry(type="Point", coordinates=[-80.0, 35.0]))
    resp = Deployments.update_deployment_by_id(server_url, deployments.json()['items'][0]['id'],
                                               deployment.model_dump_json(exclude_none=True, by_alias=True),
                                               headers=geo_json_headers)
    print(resp)


def test_add_systems_to_deployment():
    deployments = Deployments.list_all_deployments(server_url)
    systems = Systems.list_all_systems(server_url, headers=json_headers).json()
    system_link = {'href': f"{server_url}/api/systems/{systems['items'][0]['id']}"}
    resp = Deployments.add_systems_to_deployment(server_url, deployments.json()['items'][0]['id'], str(system_link),
                                                 headers=geo_json_headers)
    print(resp)


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
    retrieved_systems = Systems.list_all_systems(server_url, headers=json_headers).json()['items']
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
    retrieved_systems = Systems.list_all_systems(server_url, headers=json_headers).json()['items']
    sf_list = SamplingFeatures.list_sampling_features_of_system(server_url, retrieved_systems[0]['id'])
    print(sf_list.json())
    sf_id = sf_list.json()['items'][0]['id']


def test_update_sampling_feature():
    retrieved_systems = Systems.list_all_systems(server_url, headers=json_headers).json()['items']
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
Datastreams and Observations Section
"""


def test_create_datastreams():
    retrieved_systems = Systems.list_all_systems(server_url, headers=json_headers).json()['items']
    time_schema = TimeSchema(label="Test Datastream Time", definition="http://test.com/Time", name="timestamp",
                             uom=URI(href="http://test.com/TimeUOM"))
    bool_schema = BooleanSchema(label="Test Datastream Boolean", definition="http://test.com/Boolean",
                                name="testboolean")
    datarecord_schema = SWEDatastreamSchema(encoding=JSONEncoding(), obs_format=ObservationFormat.SWE_JSON.value,
                                            record_schema=DataRecordSchema(label="Test Datastream Record",
                                                                           definition="http://test.com/Record",
                                                                           fields=[time_schema, bool_schema]))

    print(f'Datastream Schema: {datarecord_schema.model_dump_json(exclude_none=True, by_alias=True)}')
    datastream_body = DatastreamBodyJSON(name="Test Datastream", output_name="Test Output #1", datastream_schema=datarecord_schema)
    temp_test_json = datastream_body.model_dump_json(exclude_none=True, by_alias=True)
    print(f'Test Datastream JSON: {temp_test_json}')
    resp = Datastreams.add_datastreams_to_system(server_url, retrieved_systems[1]['id'],
                                                 datastream_body.model_dump_json(exclude_none=True, by_alias=True),
                                                 headers=json_headers)
    print(resp)


def test_list_datastreams():
    ds_list = Datastreams.list_all_datastreams(server_url)
    print(ds_list.json())


def test_list_datastreams_of_system():
    sys_list = Systems.list_all_systems(server_url, headers=json_headers).json()
    print(sys_list)
    ds_list = Datastreams.list_all_datastreams_of_system(server_url, sys_list['items'][0]['id'], headers=json_headers)
    # print(ds_list.json())
    print(ds_list)


def test_retrieve_datastream_by_id():
    ds_list = Datastreams.list_all_datastreams(server_url).json()
    ds = Datastreams.retrieve_datastream_by_id(server_url, ds_list['items'][0]['id'])
    print(ds.json())


def test_update_datastream_by_id():
    ds_list = Datastreams.list_all_datastreams(server_url).json()
    time_schema = TimeSchema(label="Test Datastream Time (Updated)", definition="http://test.com/Time",
                             name="timestamp",
                             uom=URI(href="http://test.com/TimeUOM"))
    count_schema = CountSchema(label="Test Datastream Count (Updated)", definition="http://test.com/Count",
                               name="testcount")
    bool_schema = BooleanSchema(label="Test Datastream Boolean (Updated)", definition="http://test.com/Boolean",
                                name="testboolean")

    datarecord_schema = SWEDatastreamSchema(encoding=JSONEncoding(), obs_format=ObservationFormat.SWE_JSON.value,
                                            record_schema=DataRecordSchema(label="Test Datastream Record (Updated)",
                                                                           definition="http://test.com/Record",
                                                                           fields=[bool_schema]))
    print(f'Datastream Schema: {datarecord_schema.model_dump_json(exclude_none=True, by_alias=True)}')
    datastream_body = DatastreamBodyJSON(name="Test Datastream (Updated)", output_name="Test Output #1",
                                         schema=datarecord_schema)
    temp_test_json = datastream_body.model_dump_json(exclude_none=True, by_alias=True)
    print(f'Test Datastream JSON: {temp_test_json}')
    resp = Datastreams.update_datastream_by_id(server_url, ds_list['items'][0]['id'],
                                               datastream_body.model_dump_json(exclude_none=True, by_alias=True),
                                               headers=json_headers)
    print(resp)


def test_add_observations_to_datastream():
    ds_list = Datastreams.list_all_datastreams(server_url).json()
    the_time = datetime.utcnow().isoformat() + 'Z'  # for now just add the Z because I can't be bothered to validate results without a model
    time_millis = datetime.now().timestamp() * 1000
    time_millis = test_time_start.timestamp() * 1000
    obs = ObservationOMJSONInline(phenomenon_time=the_time,
                                  result_time=the_time,
                                  result={
                                      "timestamp": time_millis,
                                      "testboolean": True
                                  })
    print(f'Observation: {obs.model_dump_json(exclude_none=True, by_alias=True)}')
    resp = Observations.add_observations_to_datastream(server_url, ds_list['items'][0]['id'],
                                                       obs.model_dump_json(exclude_none=True, by_alias=True),
                                                       headers=json_headers)
    print(resp)


def test_list_all_observations():
    obs_list = Observations.list_all_observations(server_url)
    print(obs_list.json())


def test_list_observations_of_datastream():
    ds_list = Datastreams.list_all_datastreams(server_url).json()
    obs_list = Observations.list_observations_from_datastream(server_url, ds_list['items'][0]['id'])
    print(obs_list.json())


def test_update_observation_by_id():
    # Fails because the test server asks for a datastream id, but the model provides one so no idea there for now
    obs_list = Observations.list_all_observations(server_url).json()
    the_time = datetime.utcnow().isoformat() + 'Z'  # for now just add the Z because I can't be bothered to validate results without a model
    time_millis = test_time_start.timestamp() * 1000
    obs = ObservationOMJSONInline(phenomenon_time=the_time, datastream_id=obs_list['items'][0]['datastream@id'],
                                  result_time=the_time,
                                  result={
                                      "timestamp": time_millis,
                                      "testboolean": False
                                  })
    print(f'Observation: {obs.model_dump_json(exclude_none=True, by_alias=True)}')
    resp = Observations.update_observation_by_id(server_url, obs_list['items'][0]['id'],
                                                 obs.model_dump_json(exclude_none=True, by_alias=True),
                                                 headers=json_headers)
    print(resp)


"""
Command and Control Channel Section
"""


def test_create_control_channel():
    systems_list = Systems.list_all_systems(server_url, headers=json_headers).json()
    system_id = systems_list["items"][0]["id"]

    time_schema = TimeSchema(label="Test Control Channel Time", definition="http://test.com/Time", name="timestamp",
                             uom=URI(href="http://test.com/TimeUOM"))
    count_schema = CountSchema(label="Test Control Channel Count", definition="http://test.com/Count", name="testcount")

    control_schema = JSONControlChannelSchema(command_format=ObservationFormat.SWE_JSON.value,
                                              params_schema=DataRecordSchema(label="Test Control Channel Record",
                                                                             definition="http://test.com/Record",
                                                                             fields=[time_schema, count_schema]))
    request_body = ControlStreamJSONSchema(name="Test Control Channel", input_name="TestControlInput1",
                                           schema=control_schema)
    print(f'Request Body for Control Stream: {request_body.model_dump_json(exclude_none=True, by_alias=True)}')
    resp = ControlChannels.add_control_streams_to_system(server_url, system_id,
                                                         request_body.model_dump_json(exclude_none=True,
                                                                                      by_alias=True),
                                                         headers=json_headers)
    print(resp)


def test_list_control_streams():
    control_streams = ControlChannels.list_all_control_streams(server_url)
    print(control_streams)


def test_list_control_streams_of_system():
    systems_list = Systems.list_all_systems(server_url, headers=json_headers).json()
    system_id = systems_list["items"][0]["id"]
    control_streams = ControlChannels.list_control_streams_of_system(server_url, system_id)
    print(control_streams)


def test_retrieve_control_stream_by_id():
    control_streams = ControlChannels.list_all_control_streams(server_url).json()
    control_stream_desc = ControlChannels.retrieve_control_stream_description_by_id(server_url,
                                                                                    control_streams["items"][0]["id"])
    control_stream_schema = ControlChannels.retrieve_control_stream_schema_by_id(server_url,
                                                                                 control_streams["items"][0]["id"])
    print(control_stream_desc.json())
    print(control_stream_schema.json())


def test_update_control_stream_by_id():
    control_streams = ControlChannels.list_all_control_streams(server_url).json()

    time_schema = TimeSchema(label="Test Control Channel Time (Updated)", definition="http://test.com/Time",
                             name="timestamp",
                             uom=URI(href="http://test.com/TimeUOM"))
    count_schema = CountSchema(label="Test Control Channel Count (Updated)", definition="http://test.com/Count",
                               name="testcount")
    bool_schema = BooleanSchema(label="Test Control Channel Boolean (Updated)", definition="http://test.com/Boolean",
                                name="testboolean")

    control_schema = JSONControlChannelSchema(command_format=ObservationFormat.SWE_JSON.value,
                                              params_schema=DataRecordSchema(
                                                  label="Test Control Channel Record (Updated)",
                                                  definition="http://test.com/Record",
                                                  fields=[bool_schema]))
    request_body = ControlStreamJSONSchema(name="Test Control Channel (Updated)", input_name="TestControlInput1",
                                           schema=control_schema)
    print(f'Request Body for Control Stream: {request_body.model_dump_json(exclude_none=True, by_alias=True)}')
    resp = ControlChannels.update_control_stream_schema_by_id(server_url, control_streams["items"][0]["id"],
                                                              request_body.model_dump_json(exclude_none=True,
                                                                                           by_alias=True),
                                                              headers=json_headers)
    print(resp)


def test_add_commands_to_control_stream():
    control_streams = ControlChannels.list_all_control_streams(server_url).json()

    command_json = CommandJSON(control_id=control_streams["items"][0]["id"],
                               issue_time=datetime.now().isoformat() + 'Z',
                               params={"timestamp": datetime.now().timestamp() * 1000, "testcount": 1})

    print(f'Issuing Command: {command_json.model_dump_json(exclude_none=True, by_alias=True)}')
    resp = Commands.send_commands_to_specific_control_stream(server_url, control_streams["items"][0]["id"],
                                                             command_json.model_dump_json(exclude_none=True,
                                                                                          by_alias=True),
                                                             headers=json_headers)
    print(resp)


def test_list_all_commands():
    commands = Commands.list_all_commands(server_url)
    print(commands.json())


def test_list_commands_of_control_stream():
    control_streams = ControlChannels.list_all_control_streams(server_url).json()
    commands = Commands.list_commands_of_control_channel(server_url, control_streams["items"][0]["id"])
    print(commands.json())


def test_retrieve_command_by_id():
    commands = Commands.list_all_commands(server_url).json()
    command = Commands.retrieve_command_by_id(server_url, commands["items"][0]["id"])
    print(command.json())


def test_update_command_description():
    commands = Commands.list_all_commands(server_url).json()
    command_json = CommandJSON(control_id=commands["items"][0]["id"],
                               issue_time=datetime.now().isoformat() + 'Z',
                               params={"timestamp": datetime.now().timestamp() * 1000, "testcount": 2})
    resp = Commands.update_command_description(server_url, commands["items"][0]["id"],
                                               command_json.model_dump_json(exclude_none=True, by_alias=True),
                                               headers=json_headers)
    print(resp)


def test_add_command_status_report():
    commands = Commands.list_all_commands(server_url).json()
    report = CommandJSON(control_id=commands["items"][0]["id"],
                         issue_time=datetime.now().isoformat() + 'Z',
                         params={"timestamp": datetime.now().timestamp() * 1000, "testcount": 2})
    resp = Commands.add_command_status_report(server_url, commands["items"][0]["id"],
                                              report.model_dump_json(exclude_none=True, by_alias=True),
                                              headers=json_headers)
    print(resp)


def test_list_command_status_reports():
    commands = Commands.list_all_commands(server_url).json()
    reports = Commands.list_command_status_reports(server_url, commands["items"][0]["id"])
    print(reports.json())


def test_retrieve_command_status_report_by_id():
    commands = Commands.list_all_commands(server_url).json()
    reports = Commands.list_command_status_reports(server_url, commands["items"][0]["id"]).json()
    report = Commands.retrieve_command_status_report_by_id(server_url, reports["items"][0]["id"])
    print(report.json())


def test_update_command_status_report():
    commands = Commands.list_all_commands(server_url).json()
    reports = Commands.list_command_status_reports(server_url, commands["items"][0]["id"]).json()
    report = CommandJSON(control_id=commands["items"][0]["id"],
                         issue_time=datetime.now().isoformat() + 'Z',
                         params={"timestamp": datetime.now().timestamp() * 1000, "testcount": 3})
    resp = Commands.update_command_status_report_by_id(server_url, reports["items"][0]["id"],
                                                       report.model_dump_json(exclude_none=True, by_alias=True),
                                                       headers=json_headers)
    print(resp)


"""
Teardown Section
"""

# def test_delete_all_command_status_reports():
#     commands = Commands.list_all_commands(server_url).json()
#     for command in commands["items"]:
#         reports = Commands.list_command_status_reports(server_url, command["id"]).json()
#         for report in reports["items"]:
#             Commands.delete_command_status_report_by_id(server_url, report["id"])
#             print(f"Deleted command status report {report['id']}")
#
# def test_delete_all_commands():
#     commands = Commands.list_all_commands(server_url).json()
#     for command in commands["items"]:
#         Commands.delete_command_by_id(server_url, command["id"])
#         print(f"Deleted command {command['id']}")

# def test_delete_all_observations():
#     obs_list = Observations.list_all_observations(server_url).json()
#     print(obs_list)
#     for obs in obs_list["items"]:
#         print(obs)
#         Observations.delete_observation_by_id(server_url, obs["id"])
#         print(f"Deleted observation {obs['id']}")
#
#
# def test_delete_all_collections():
#     pass
#
#
# def test_delete_all_sampling_features():
#     sf_list = SamplingFeatures.list_all_sampling_features(server_url).json()
#     print(sf_list)
#
#     for sf in sf_list["items"]:
#         print(sf)
#
#         SamplingFeatures.delete_sampling_feature_by_id(server_url, sf["id"])
#         print(f"Deleted sampling feature {sf['id']}")
#
#
# def test_delete_all_control_streams():
#     control_streams = ControlChannels.list_all_control_streams(server_url).json()
#     print(control_streams)
#
#     for cs in control_streams["items"]:
#         print(cs)
#
#         ControlChannels.delete_control_stream_by_id(server_url, cs["id"])
#         print(f"Deleted control stream {cs['id']}")
#
#
# def test_delete_all_datastreams():
#     ds_list = Datastreams.list_all_datastreams(server_url).json()
#     print(ds_list)
#
#     for ds in ds_list["items"]:
#         print(ds)
#
#         Datastreams.delete_datastream_by_id(server_url, ds["id"])
#         print(f"Deleted datastream {ds['id']}")
#
#
# def test_delete_all_procedures():
#     proc_list = Procedures.list_all_procedures(server_url).json()
#     print(proc_list)
#
#     for proc in proc_list["items"]:
#         print(proc)
#
#         Procedures.delete_procedure_by_id(server_url, proc["id"])
#         print(f"Deleted procedure {proc['id']}")
#
#
# def test_delete_all_systems():
#     sys_list = Systems.list_all_systems(server_url).json()["items"]
#     print(sys_list)
#
#     for system in sys_list:
#         print(system)
#
#         Systems.delete_system_by_id(server_url, system["id"])
#         print(f"Deleted system {system['id']}")
