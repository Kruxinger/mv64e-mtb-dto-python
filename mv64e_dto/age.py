from typing import Optional
from pydantic import BaseModel, Field
from .unit import Unit

class Age(BaseModel):
    unit: Optional[Unit] = Field(default=None, alias="unit")
    value: Optional[float] = Field(default=None, alias="value")

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }
