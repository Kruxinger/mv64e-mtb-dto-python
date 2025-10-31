from typing import Optional
from pydantic import BaseModel, Field
from mv64e_dto.publication_system import PublicationSystem

class PublicationReference(BaseModel):
    display: Optional[str] = Field(
        default=None,
        alias="display"
    )
    id: Optional[str] = Field(
        default=None,
        alias="id"
    )
    system: Optional[PublicationSystem] = Field(
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