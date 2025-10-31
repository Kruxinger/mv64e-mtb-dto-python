from typing import Optional, Dict, Any
from datetime import date
from pydantic import BaseModel, Field

from mv64e_dto.ecog_coding import EcogCoding
from mv64e_dto.reference import Reference


class PerformanceStatus(BaseModel):
    # @JsonFormat(pattern = "yyyy-MM-dd") -> datetime.date
    effective_date: Optional[date] = Field(default=None, alias="effectiveDate")
    id: Optional[str] = Field(default=None, alias="id")
    patient: Optional[Reference] = Field(default=None, alias="patient")
    value: Optional[EcogCoding] = Field(default=None, alias="value") # PLACEHOLDER: EcogCoding

    model_config = {"populate_by_name": True, "from_attributes": True}