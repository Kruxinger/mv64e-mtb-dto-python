from typing import Optional
from pydantic import BaseModel, Field
from mv64e_dto.reference import Reference
from mv64e_dto.msi_interpretation_coding import MsiInterpretationCoding
from mv64e_dto.msi_method_coding import MsiMethodCoding


class Msi(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    interpretation: Optional[MsiInterpretationCoding] = Field(default=None, alias="interpretation")
    method: Optional[MsiMethodCoding] = Field(default=None, alias="method")
    patient: Optional[Reference] = Field(default=None, alias="patient")
    specimen: Optional[Reference] = Field(default=None, alias="specimen")

    # Java 'double' (primitiv) wird als required float angenommen
    value: float = Field(alias="value")

    model_config = {"populate_by_name": True, "from_attributes": True}