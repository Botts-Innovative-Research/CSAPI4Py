from pydantic import BaseModel, HttpUrl, Field


class TypeOf(BaseModel):
    href: HttpUrl
    rel: str = None
    media_type: str = Field(None, serialization_alias='type')
    href_lang: str = Field(None, serialization_alias='hreflang')
    title: str = None
    uid: str = None
    target_resource: str = Field(None, serialization_alias='rt')
    interface: str = Field(None, serialization_alias='if')


class SensorML(BaseModel):
    description: str = None
    uniqueId: str = None
    name: str = None
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
