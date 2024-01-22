from pydantic import BaseModel, HttpUrl, Field

from conSys.sensor_ml.sml import TypeOf


class RequestBody(BaseModel):
    type: str = Field(None)
    id: str = Field(None)
    description: str = Field(None)
    links: list = Field(None)


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
    unique_id: str = Field(None, serialization_alias='uniqueID')
    label: str = None
    lang: str = None
    keywords: list = None
    identifiers: list = None
    classifiers: list = None
    valid_time: list = Field(None, serialization_alias='validTime')
    security_constraints: list = Field(None, serialization_alias='securityConstraints')
    legal_constraints: list = Field(None, serialization_alias='legalConstraints')
    characteristics: list = None
    capabilities: list = None
    contacts: list = None
    documents: list = None
    history: list = None
    definition: HttpUrl = None
    type_of: TypeOf = Field(None, serialization_alias='typeOf')
    configuration: HttpUrl = None
    features_of_interest: list = Field(None, serialization_alias='featuresOfInterest')
    inputs: list = None
    outputs: list = None
    parameters: list = None
    modes: list = None
    method: str = None
    position: list = None
    links: list = None
