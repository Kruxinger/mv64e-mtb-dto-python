from typing import Optional, List
from datetime import datetime, date
from pydantic import BaseModel, Field
from mv64e_dto.provision import Provision

class ModelProjectConsent(BaseModel):
    # Java Date ohne Format-Annotation wird zu datetime.datetime
    date: Optional[datetime] = Field(
        default=None,
        alias="date"
    )
    provisions: Optional[List[Provision]] = Field(
        default=None,
        alias="provisions"
    )
    version: Optional[str] = Field(
        default=None,
        alias="version"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }