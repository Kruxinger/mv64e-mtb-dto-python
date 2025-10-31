from typing import Optional
from pydantic import BaseModel, Field

class Components(BaseModel):
    loh: float = Field(
        alias="loh"
    )
    lst: float = Field(
        alias="lst"
    )
    tai: float = Field(
        alias="tai"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }