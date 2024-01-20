from pydantic import BaseModel, HttpUrl

from conSys.sensor_ml.sml import TypeOf


class RequestBody(BaseModel):
    type: str
    id: str
    description: str = None
    # properties: dict = None
    # geometry: dict = None
    # bbox: list = None
    links: list = None


class GeoJSONBody(RequestBody):
    type: str
    id: str
    description: str = None
    properties: dict = None
    geometry: dict = None
    bbox: list = None
    links: list = None


class SmlJSONBody(RequestBody):
    # TODO: implement other classes to represent the specifics of certain top-level properties
    type: str
    id: str
    description: str = None
    uniqueId: str = None
    label: str = None
    lang: str = None
    keywords: list = None
    identifiers: list = None
    classifiers: list = None
    valid_time: list = None
    security_constraints: list = None
    legal_constraints: list = None
    characteristics: list = None
    capabilities: list = None
    contacts: list = None
    documents: list = None
    history: list = None
    definition: HttpUrl = None
    type_of: TypeOf = None
    configuration: HttpUrl = None
    features_of_interest: list = None
    inputs: list = None
    outputs: list = None
    parameters: list = None
    modes: list = None
    method: str = None
    position: list = None
    links: list = None
