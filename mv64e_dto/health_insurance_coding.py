from typing import Optional
from pydantic import BaseModel, Field
from mv64e_dto.health_insurance_coding_code import HealthInsuranceCodingCode

class HealthInsuranceCoding(BaseModel):
    code: Optional[HealthInsuranceCodingCode] = Field(
        default=None,
        alias="code"
    )
    display: Optional[str] = Field(
        default=None,
        alias="display"
    )
    system: Optional[str] = Field(
        default=None,
        alias="system"
    )
    version: Optional[str] = Field(
        default=None,
        alias="version"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }