from typing import Optional, List
from datetime import date
from pydantic import BaseModel, Field

from mv64e_dto.gene_alteration_reference import GeneAlterationReference
from mv64e_dto.mtb_procedure_recommendation_category_coding import MtbProcedureRecommendationCategoryCoding
from mv64e_dto.level_of_evidence import LevelOfEvidence
from mv64e_dto.reference import Reference
from mv64e_dto.recommendation_priority_coding import RecommendationPriorityCoding

class ProcedureRecommendation(BaseModel):
    code: Optional[MtbProcedureRecommendationCategoryCoding] = Field(
        default=None,
        alias="code"
    )
    id: Optional[str] = Field(
        default=None,
        alias="id"
    )
    # @JsonFormat(pattern = "yyyy-MM-dd") -> datetime.date
    issued_on: Optional[date] = Field(
        default=None,
        alias="issuedOn"
    )
    level_of_evidence: Optional[LevelOfEvidence] = Field(
        default=None,
        alias="levelOfEvidence"
    )
    patient: Optional[Reference] = Field(
        default=None,
        alias="patient"
    )
    priority: Optional[RecommendationPriorityCoding] = Field(
        default=None,
        alias="priority"
    )
    reason: Optional[Reference] = Field(
        default=None,
        alias="reason"
    )
    supporting_variants: Optional[List[GeneAlterationReference]] = Field(
        default=None,
        alias="supportingVariants"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }