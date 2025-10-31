from typing import Optional
from pydantic import BaseModel, Field
from mv64e_dto.reference import Reference # Angenommen existiert
from mv64e_dto.health_insurance_coding import HealthInsuranceCoding

class HealthInsurance(BaseModel):
    reference: Optional[Reference] = Field(
        default=None,
        alias="reference"
    )
    type: Optional[HealthInsuranceCoding] = Field(
        default=None,
        alias="type"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }