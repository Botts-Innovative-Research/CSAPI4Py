from __future__ import annotations

from numbers import Real
from typing import Union

from pydantic import BaseModel, Field, field_validator

from conSys import GeometryTypes
from conSys.datamodels.api_utils import UCUMCode, URI

"""
 NOTE: The following classes are used to represent the Record Schemas that are required for use with Datastreams
The names are likely to change to include a "Schema" suffix to differentiate them from the actual data structures.
The current scope of the project likely excludes conversion from received data to actual SWE Common data structures, 
in the event this is added it will most likely be in a separate module as those structures have use cases outside of
the API solely
"""


# TODO: Add field validators that are missing
# TODO: valid string fields that are intended to represent time/date values
# TODO: Validate places where string fields are not allowed to be empty


class AnyComponent(BaseModel):
    id: str = Field(None)
    label: str = Field(None)
    description: str = Field(None)
    type: str = Field(...)
    updatable: bool = Field(False)
    optional: bool = Field(False)
    definition: str = Field(None)


class DataRecord(AnyComponent):
    type: str = "DataRecord"
    fields: list[AnyComponent] = Field(...)


class Vector(AnyComponent):
    label: str = "Vector"
    type: str = Field(...)
    definition: str = Field(...)
    reference_frame: str = Field(...)
    local_frame: str = Field(None)
    # TODO: VERIFY might need to be moved further down when these are defined
    coordinates: Union[list[Count], list[Quantity], list[Time]] = Field(...)


class DataArray(AnyComponent):
    type: str = "DataArray"
    element_count: int = Field(..., serialization_alias='elementCount')  # Should type of Count
    element_type: list[AnyComponent] = Field(..., serialization_alias='elementType')
    encoding: str = Field(...)  # TODO: implement an encodings class
    values: list = Field(None)


class Matrix(AnyComponent):
    type: str = "Matrix"
    element_count: int = Field(..., serialization_alias='elementCount')  # Should be type of Count
    element_type: list[AnyComponent] = Field(..., serialization_alias='elementType')
    encoding: str = Field(...)  # TODO: implement an encodings class
    values: list = Field(None)
    reference_frame: str = Field(None)
    local_frame: str = Field(None)


class DataChoice(AnyComponent):
    type: str = "DataChoice"
    updatable: bool = Field(False)
    optional: bool = Field(False)
    choice_value: Category = Field(..., serialization_alias='choiceValue')  # TODO: Might be called "choiceValues"
    items: list[AnyComponent] = Field(...)


class Geometry(AnyComponent):
    label: str = Field(...)
    type: str = "Geometry"
    updatable: bool = Field(False)
    optional: bool = Field(False)
    definition: str = Field(...)
    constraint: dict = {
        'geomTypes': [GeometryTypes.POINT.value, GeometryTypes.LINESTRING.value, GeometryTypes.POLYGON.value,
                      GeometryTypes.MULTI_POINT.value, GeometryTypes.MULTI_LINESTRING.value,
                      GeometryTypes.MULTI_POLYGON.value]}
    nil_values: list = Field(None, serialization_alias='nilValues')
    srs: str = Field(...)
    value = Field(None)


class AnySimpleComponent(AnyComponent):
    label: str = Field(...)
    description = Field(None)
    type: str = Field(...)
    updatable = Field(False)
    optional = Field(False)
    definition: str = Field(...)
    reference_frame: str = Field(None, serialization_alias='referenceFrame')
    axis_id: str = Field(None, serialization_alias='axisID')
    quality: Union[list[Quantity], list[QuantityRange], list[Category], list[Text]] = Field(
        None)  # TODO: Union[Quantity, QuantityRange, Category, Text]
    nil_values: list = Field(None, serialization_alias='nilValues')
    constraint = Field(None)
    value = Field(None)


class AnyScalarComponent(AnySimpleComponent):
    """
    A base class for all scalar components. The structure is essentially that of AnySimpleComponent
    """
    pass


class Boolean(AnyScalarComponent):
    type: str = "Boolean"
    value: bool = Field(None)


class Count(AnyScalarComponent):
    type: str = "Count"
    value: int = Field(None)


class Quantity(AnyScalarComponent):
    type: str = "Quantity"
    value: Union[Real, str] = Field(None)
    uom: Union[UCUMCode, URI] = Field(...)

    @field_validator('value')
    @classmethod
    def validate_value(cls, v):
        if isinstance(v, Real):
            return v
        elif isinstance(v, str):
            if v in ['NaN', 'INFINITY', '+INFINITY', '-INFINITY']:
                return v
            else:
                raise ValueError(
                    'string representation of value must be one of the following: NaN, INFINITY, +INFINITY, -INFINITY')
        else:
            try:
                return float(v)
            except ValueError:
                raise ValueError('value must be a number or a string representing a special value '
                                 '[NaN, INFINITY, +INFINITY, -INFINITY]')


class Time(AnyScalarComponent):
    type: str = "Time"
    value: str = Field(None)
    reference_time: str = Field(None, serialization_alias='referenceTime')
    local_frame: str = Field(None)
    uom: Union[UCUMCode, URI] = Field(...)


class Category(AnyScalarComponent):
    type: str = "Category"
    value: str = Field(None)
    code_space: str = Field(None, serialization_alias='codeSpace')


class Text(AnyScalarComponent):
    type: str = "Text"
    value: str = Field(None)


class CountRange(AnySimpleComponent):
    type: str = "CountRange"
    value: list[int] = Field(None)
    uom: Union[UCUMCode, URI] = Field(...)


class QuantityRange(AnySimpleComponent):
    type: str = "QuantityRange"
    value: list[Union[Real, str]] = Field(None)
    uom: Union[UCUMCode, URI] = Field(...)


class TimeRange(AnySimpleComponent):
    type: str = "TimeRange"
    value: list[str] = Field(None)
    reference_time: str = Field(None, serialization_alias='referenceTime')
    local_frame: str = Field(None)
    uom: Union[UCUMCode, URI] = Field(...)


class CategoryRange(AnySimpleComponent):
    type: str = "CategoryRange"
    value: list[str] = Field(None)
    code_space: str = Field(None, serialization_alias='codeSpace')
