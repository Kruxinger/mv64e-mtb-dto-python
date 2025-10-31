from typing import Optional
from pydantic import BaseModel, Field

class Reference(BaseModel):
    display: Optional[str] = Field(
        default=None,
        alias="display"
    )
    id: Optional[str] = Field(
        default=None,
        alias="id"
    )
    system: Optional[str] = Field(
        default=None,
        alias="system"
    )
    type: Optional[str] = Field(
        default=None,
        alias="type"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }