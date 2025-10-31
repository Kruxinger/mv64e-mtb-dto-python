from typing import Optional
from pydantic import BaseModel, Field
from mv64e_dto.reference import Reference
from mv64e_dto.coding import Coding

class TumorMorphology(BaseModel):
    id: Optional[str] = Field(
        default=None,
        alias="id"
    )
    note: Optional[str] = Field(
        default=None,
        alias="note"
    )
    patient: Optional[Reference] = Field(
        default=None,
        alias="patient"
    )
    specimen: Optional[Reference] = Field(
        default=None,
        alias="specimen"
    )
    value: Optional[Coding] = Field(
        default=None,
        alias="value"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }