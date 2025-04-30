from pydantic import BaseModel, Field

from src.consys4py.constants import GeometryTypes


# TODO: Add specific validations for each type
class Geometry(BaseModel):
    """
    A class to represent the geometry of a feature
    """
    type: GeometryTypes = Field(...)
    coordinates: list
    bbox: list = None
