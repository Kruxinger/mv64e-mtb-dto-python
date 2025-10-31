from typing import Optional, Dict, Any
from datetime import date
from pydantic import BaseModel, Field

from mv64e_dto.recist_coding import RecistCoding
from mv64e_dto.reference import Reference
from mv64e_dto.response_method_coding import ResponseMethodCoding

class Response(BaseModel):
    # @JsonFormat(pattern = "yyyy-MM-dd") -> datetime.date
    effective_date: Optional[date] = Field(default=None, alias="effectiveDate")
    id: Optional[str] = Field(default=None, alias="id")
    method: Optional[ResponseMethodCoding] = Field(default=None, alias="method")
    patient: Optional[Reference] = Field(default=None, alias="patient")
    therapy: Optional[Reference] = Field(default=None, alias="therapy")
    value: Optional[RecistCoding] = Field(default=None, alias="value") # PLACEHOLDER: RecistCoding

    model_config = {"populate_by_name": True, "from_attributes": True}