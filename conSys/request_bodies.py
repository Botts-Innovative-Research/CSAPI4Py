from typing import Union

from pydantic import BaseModel, HttpUrl, Field, model_serializer, RootModel

from conSys.sensor_ml.sml import TypeOf


class GeoJSONBody(BaseModel):
    type: str
    id: str
    properties: dict = None
    geometry: dict = None
    bbox: list = None
    links: list = None


class SmlJSONBody(BaseModel):
    system_type: str = Field(None, serialization_alias='type')
    id: str = Field(None)
    description: str = Field(None)
    unique_id: str = Field(..., serialization_alias='uniqueId')
    label: str = Field(...)
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
    links: list = Field(None)


class OMJSONBody(BaseModel):
    datastream_id: str = Field(None, alias="datastream@id")
    foi_id: str = Field(None, alias="foi@id")
    phenomenon_time: str = Field(None, alias="phenomenonTime")
    result_time: str = Field(None, alias="resultTime")
    parameters: list = Field(None)
    result: dict = Field(None)
    result_links: list = Field(None, alias="result@links")


class RequestBody(BaseModel):
    """
    Wrapper class to support different request json structures
    """
    json_structure: Union[GeoJSONBody, SmlJSONBody, OMJSONBody] = Field(..., serialization_alias='json')
    test_extra: str = Field("Hello, I am test", serialization_alias='testExtra')

    @model_serializer
    def ser_model(self):
        print("Serializing model...")
        return self.json_structure


class RequestBodyList(RootModel):
    root: list[Union[GeoJSONBody, SmlJSONBody, OMJSONBody]] = Field(...)