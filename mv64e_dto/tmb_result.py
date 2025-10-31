from typing import Optional
from pydantic import BaseModel, Field

class TmbResult(BaseModel):
    unit: Optional[str] = Field(default=None, alias="unit")
    value: Optional[float] = Field(default=None, alias="value") # double in Java

    model_config = {"populate_by_name": True, "from_attributes": True}