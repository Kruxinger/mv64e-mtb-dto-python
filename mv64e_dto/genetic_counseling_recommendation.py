from typing import Optional
from datetime import date
from pydantic import BaseModel, Field
from mv64e_dto.reference import Reference
from mv64e_dto.genetic_counseling_recommendation_reason_coding import GeneticCounselingRecommendationReasonCoding

class GeneticCounselingRecommendation(BaseModel):
    id: Optional[str] = Field(
        default=None,
        alias="id"
    )
    # Java Date mit @JsonFormat(pattern = "yyyy-MM-dd") -> datetime.date
    issued_on: Optional[date] = Field(
        default=None,
        alias="issuedOn"
    )
    patient: Optional[Reference] = Field(
        default=None,
        alias="patient"
    )
    reason: Optional[GeneticCounselingRecommendationReasonCoding] = Field(
        default=None,
        alias="reason"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }