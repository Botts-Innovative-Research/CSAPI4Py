from datetime import datetime
from typing import Union

from pydantic import BaseModel, StrictStr


class Query(BaseModel):
    id: list = None
    bbox: list = None
    date_time: Union[StrictStr, datetime] = None
    geom = None
    q: list = None
    parent: list = None
    procedure: list = None
    foi: list = None
    observed_property: list = None
    controlled_property: list = None
    recursive: bool = None
    limit: int = 10
