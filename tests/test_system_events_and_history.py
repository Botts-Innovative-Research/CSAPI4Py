import pytest

from datetime import datetime

from consys4py import Systems, SamplingFeatures, Datastreams, SmlJSONBody, GeoJSONBody, model_utils, \
    DatastreamBodyJSON, ObservationFormat, URI, Procedures, Geometry, Deployments, ControlChannels, Observations, \
    Commands
from consys4py.datamodels.control_streams import ControlStreamJSONSchema, SWEControlChannelSchema, JSONControlChannelSchema
from consys4py.datamodels.datastreams import SWEDatastreamSchema
from consys4py.datamodels.encoding import JSONEncoding
from consys4py.datamodels.swe_components import BooleanSchema, TimeSchema, DataRecordSchema, CountSchema
from consys4py.datamodels.observations import ObservationOMJSONInline
from consys4py.datamodels.commands import CommandJSON
from consys4py.datamodels.system_events_and_history import SystemEventOMJSON

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
