from typing import Optional
from datetime import date
from pydantic import BaseModel, Field
from mv64e_dto.model_project_consent_purpose import ModelProjectConsentPurpose
from mv64e_dto.consent_provision import ConsentProvision # Simuliert

class Provision(BaseModel):
    # Java Date mit @JsonFormat(pattern = "yyyy-MM-dd") -> datetime.date
    date: Optional[date] = Field(
        default=None,
        alias="date"
    )
    purpose: Optional[ModelProjectConsentPurpose] = Field(
        default=None,
        alias="purpose"
    )
    type: Optional[ConsentProvision] = Field(
        default=None,
        alias="type"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }