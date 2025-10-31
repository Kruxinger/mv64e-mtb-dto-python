from typing import Optional
from pydantic import BaseModel, Field

class StartRange(BaseModel):
    end: Optional[float] = Field(
        default=None,
        alias="end"
    )
    start: float = Field(
        alias="start"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }