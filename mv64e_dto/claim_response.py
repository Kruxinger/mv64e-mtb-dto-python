from typing import Optional, List
from datetime import date
from pydantic import BaseModel, Field
from mv64e_dto.reference import Reference
from mv64e_dto.claim_response_status_coding import ClaimResponseStatusCoding
from mv64e_dto.claim_response_status_reason_coding import ClaimResponseStatusReasonCoding

class ClaimResponse(BaseModel):
    claim: Optional[Reference] = Field(
        default=None,
        alias="claim"
    )
    id: Optional[str] = Field(
        default=None,
        alias="id"
    )
    # Datumsformatierung analog zu Claim
    issued_on: Optional[date] = Field(
        default=None,
        alias="issuedOn"
    )
    patient: Optional[Reference] = Field(
        default=None,
        alias="patient"
    )
    status: Optional[ClaimResponseStatusCoding] = Field(
        default=None,
        alias="status"
    )
    status_reason: Optional[List[ClaimResponseStatusReasonCoding]] = Field(
        default=None,
        alias="statusReason"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }