from typing import Optional
from pydantic import BaseModel, Field

class Address(BaseModel):
    municipality_code: Optional[str] = Field(
        default=None,
        alias="municipalityCode"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }
