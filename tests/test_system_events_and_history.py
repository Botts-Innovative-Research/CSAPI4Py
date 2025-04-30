import pytest

from datetime import datetime

from consys4py import Systems, SamplingFeatures, Datastreams, SmlJSONBody, GeoJSONBody, model_utils, \
    DatastreamBodyJSON, ObservationFormat, URI, Procedures, Geometry, Deployments, ControlChannels, Observations, \
    Commands
from src.consys4py.datamodels import SystemEventOMJSON

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


def test_add_system_events():
    sys_event_schema = SystemEventOMJSON(label="Test System Event", definition="http://test.com/SystemEvent",
                                         time=test_time_start.isoformat() + 'Z')

    resp = Systems.add_system_events_to_system(server_url, sys_event_schema.model_dump_json(exclude_none=True,
                                                                                           by_alias=True),
                                               headers=json_headers)
