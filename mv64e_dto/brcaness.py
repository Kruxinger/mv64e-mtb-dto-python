from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

from mv64e_dto.confidence_range import ConfidenceRange
from mv64e_dto.reference import Reference

class Brcaness(BaseModel):
    confidence_range: Optional[ConfidenceRange] = Field(
        default=None,
        alias="confidenceRange"
    )
    id: Optional[str] = Field(
        default=None,
        alias="id"
    )
    patient: Optional[Reference] = Field(
        default=None,
        alias="patient"
    )
    specimen: Optional[Reference] = Field(
        default=None,
        alias="specimen"
    )
    value: Optional[float] = Field(
        default=None,
        alias="value"
    ) # double in Java wird zu float in Python

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }