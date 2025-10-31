from typing import Optional
from pydantic import BaseModel, Field
from mv64e_dto.reference import Reference
from mv64e_dto.tmb_interpretation_coding import TmbInterpretationCoding
from mv64e_dto.tmb_result import TmbResult

class Tmb(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    interpretation: Optional[TmbInterpretationCoding] = Field(default=None, alias="interpretation")
    patient: Optional[Reference] = Field(default=None, alias="patient")
    specimen: Optional[Reference] = Field(default=None, alias="specimen")
    value: Optional[TmbResult] = Field(default=None, alias="value")

    model_config = {"populate_by_name": True, "from_attributes": True}