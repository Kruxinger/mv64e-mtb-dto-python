from typing import Optional, List, Any
from datetime import date
from pydantic import BaseModel, Field
from mv64e_dto.reference import Reference
from mv64e_dto.claim_stage_coding import ClaimStageCoding
from mv64e_dto.atc_unregistered_medication_coding import AtcUnregisteredMedicationCoding # Achtung: Platzhalter

class Claim(BaseModel):
    id: Optional[str] = Field(
        default=None,
        alias="id"
    )
    # Java verwendet java.util.Date mit Format "yyyy-MM-dd".
    # Python verwendet pydantic.date, das dieses Format nativ unterstützt.
    issued_on: Optional[date] = Field(
        default=None,
        alias="issuedOn"
    )
    patient: Optional[Reference] = Field(
        default=None,
        alias="patient"
    )
    recommendation: Optional[Reference] = Field(
        default=None,
        alias="recommendation"
    )
    # Liste des Platzhalter-DTOs
    requested_medication: Optional[List[AtcUnregisteredMedicationCoding]] = Field(
        default=None,
        alias="requestedMedication"
    )
    stage: Optional[ClaimStageCoding] = Field(
        default=None,
        alias="stage"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }