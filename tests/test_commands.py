import json
import time
from datetime import datetime

from conSys import GeoJSONBody, Systems, ControlChannels, ObservationFormat, Commands
from conSys.datamodels.commands import CommandJSON
from conSys.datamodels.control_streams import ControlStreamJSONSchema, JSONControlChannelSchema
from conSys.datamodels.swe_components import DataRecordSchema, TimeSchema, CountSchema, URI
from conSys.comm.mqtt import MQTTClient

server_url = "http://localhost:8282/sensorhub"
geo_json_headers = {"Content-Type": "application/geo+json"}
sml_json_headers = {"Content-Type": "application/sml+json"}
json_headers = {"Content-Type": "application/json"}
systems_list = []


def test_setup():
    geo_temp = GeoJSONBody(type='Feature', id='12345-commanded',
                           description="Test Insertion of System via GEOJSON",
                           properties={
                               "featureType": "http://www.w3.org/ns/ssn/System",
                               "name": f'Test System - GeoJSON',
                               "uid": f'urn:test:client:geo-single',
                               "description": "A Test System inserted from the Python Connected Systems API Client",
                           })
    resp = Systems.create_new_systems(server_url, geo_temp.model_dump_json(exclude_none=True, by_alias=True),
                                      uname="admin",
                                      pword="admin",
                                      headers=geo_json_headers)
    print(resp)

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
    ctl_resp = ControlChannels.add_control_streams_to_system(server_url, system_id,
                                                             request_body.model_dump_json(exclude_none=True,
                                                                                          by_alias=True),
                                                             headers=json_headers)
    print(ctl_resp)

    control_streams = ControlChannels.list_all_control_streams(server_url).json()
    command_json = CommandJSON(control_id=control_streams["items"][0]["id"],
                               issue_time=datetime.now().isoformat() + 'Z',
                               params={"timestamp": datetime.now().timestamp() * 1000, "testcount": 1})

    print(f'Issuing Command: {command_json.model_dump_json(exclude_none=True, by_alias=True)}')
    cmd_resp = Commands.send_commands_to_specific_control_stream(server_url, control_streams["items"][0]["id"],
                                                                 command_json.model_dump_json(exclude_none=True,
                                                                                              by_alias=True),
                                                                 headers=json_headers)
    print(cmd_resp)


def test_subscribe_and_command():
    mqtt_client = MQTTClient(url='localhost')

    control_streams = ControlChannels.list_all_control_streams(server_url).json()
    control_id = control_streams["items"][0]["id"]

    mqtt_client.connect()

    def on_message_command(client, userdata, msg):
        print("Received Command")
        print(f'{msg.payload.decode("utf-8")}')
        control_stream_id = control_id
        resp = {
            'id': '*******',
            'command@id': control_stream_id,
            'statusCode': 'COMPLETED'
        }
        # client.publish(f'/api/controls/{control_stream_id}/status', payload=json.dumps(resp), qos=1)

    def on_message_all(client, userdata, msg):
        print(f'\nReceived Message:{msg}')
        print(f'{msg.payload.decode("utf-8")}')
        print(f'Topic: {msg.topic}\n')

    mqtt_client.set_on_message_callback(f'/api/controls/{control_id}/commands', on_message_command)
    mqtt_client.set_on_message_callback('#', on_message_all)
    mqtt_client.subscribe('#')
    mqtt_client.subscribe(f'/api/controls/{control_id}/commands')
    mqtt_client.start()

    time.sleep(2)
    command_json = CommandJSON(control_id=control_streams["items"][0]["id"],
                               issue_time=datetime.now().isoformat() + 'Z',
                               params={"timestamp": datetime.now().timestamp() * 1000, "testcount": 1})

    print(f'Issuing Command: {command_json.model_dump_json(exclude_none=True, by_alias=True)}')
    cmd_resp = Commands.send_commands_to_specific_control_stream(server_url, control_streams["items"][0]["id"],
                                                                 command_json.model_dump_json(exclude_none=True,
                                                                                              by_alias=True),
                                                                 headers=json_headers)
    print(f'\n*****Command Response: {cmd_resp}*****')
    status_resp = {
        'id': '*******',
        'command@id': "unknown",
        'statusCode': 'COMPLETED'
    }
    Commands.add_command_status_reports(server_url, "0", json.dumps(status_resp))