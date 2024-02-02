from pydantic import BaseModel, Field, field_validator

from conSys import ObservationFormat


class DatastreamSchema(BaseModel):
    """
    A class to represent the schema of a datastream
    """
    obs_format: str = Field(..., serialization_alias='obsFormat')


class SWEDatastreamSchema(DatastreamSchema):
    encoding: dict = Field(...)
    record_schema: dict = Field(..., record_schema='recordSchema')

    @field_validator('obsFormat')
    @classmethod
    def check_check_obs_format(cls, v):
        if v in [ObservationFormat.SWE_JSON.value, ObservationFormat.SWE_CSV.value,
                 ObservationFormat.SWE_TEXT.value, ObservationFormat.SWE_BINARY.value]:
            raise ValueError('obsFormat must be on of the SWE formats')
        return v
