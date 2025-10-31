from typing import Optional
from pydantic import BaseModel, Field

class Position(BaseModel):
    # Java 'Double' (nullable) und 'double' (primitive) werden beide zu Optional[float]
    end: Optional[float] = Field(default=None, alias="end")
    start: Optional[float] = Field(default=None, alias="start")

    model_config = {"populate_by_name": True, "from_attributes": True}