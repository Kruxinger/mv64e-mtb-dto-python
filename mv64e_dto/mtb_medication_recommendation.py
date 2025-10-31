from typing import Optional, List
from datetime import date
from pydantic import BaseModel, Field

from mv64e_dto.gene_alteration_reference import GeneAlterationReference
from mv64e_dto.level_of_evidence import LevelOfEvidence
from mv64e_dto.mtb_medication_recommendation_use_type_coding import MtbMedicationRecommendationUseTypeCoding
from mv64e_dto.recommendation_priority_coding import RecommendationPriorityCoding
from mv64e_dto.reference import Reference
from mv64e_dto.mtb_medication_recommendation_category_coding import MtbMedicationRecommendationCategoryCoding
from mv64e_dto.atc_unregistered_medication_coding import AtcUnregisteredMedicationCoding

class MtbMedicationRecommendation(BaseModel):
    category: Optional[List[MtbMedicationRecommendationCategoryCoding]] = Field(default=None, alias="category")
    id: Optional[str] = Field(default=None, alias="id")
    # @JsonFormat(pattern = "yyyy-MM-dd") -> datetime.date
    issued_on: Optional[date] = Field(default=None, alias="issuedOn")
    level_of_evidence: Optional[LevelOfEvidence] = Field(default=None, alias="levelOfEvidence") # SIMULATED/PLACEHOLDER: LevelOfEvidence
    medication: Optional[List[AtcUnregisteredMedicationCoding]] = Field(default=None, alias="medication") # SIMULATED/PLACEHOLDER: List[AtcUnregisteredMedicationCoding]
    patient: Optional[Reference] = Field(default=None, alias="patient")
    priority: Optional[RecommendationPriorityCoding] = Field(default=None, alias="priority") # SIMULATED/PLACEHOLDER: RecommendationPriorityCoding
    reason: Optional[Reference] = Field(default=None, alias="reason")
    supporting_variants: Optional[List[GeneAlterationReference]] = Field(default=None, alias="supportingVariants") # SIMULATED/PLACEHOLDER: List[GeneAlterationReference]
    use_type: Optional[MtbMedicationRecommendationUseTypeCoding] = Field(default=None, alias="useType") # SIMULATED/PLACEHOLDER: MtbMedicationRecommendationUseTypeCoding

    model_config = {"populate_by_name": True, "from_attributes": True}