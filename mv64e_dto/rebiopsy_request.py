from typing import Optional
from datetime import date
from pydantic import BaseModel, Field
from mv64e_dto.reference import Reference

class RebiopsyRequest(BaseModel):
    id: Optional[str] = Field(
        default=None,
        alias="id"
    )
    # @JsonFormat(pattern = "yyyy-MM-dd") -> datetime.date
    issued_on: Optional[date] = Field(
        default=None,
        alias="issuedOn"
    )
    patient: Optional[Reference] = Field(
        default=None,
        alias="patient"
    )
    tumor_entity: Optional[Reference] = Field(
        default=None,
        alias="tumorEntity"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }