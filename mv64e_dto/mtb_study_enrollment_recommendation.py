from typing import Optional, List
from datetime import date
from pydantic import BaseModel, Field

from mv64e_dto.atc_unregistered_medication_coding import AtcUnregisteredMedicationCoding
from mv64e_dto.gene_alteration_reference import GeneAlterationReference
from mv64e_dto.level_of_evidence import LevelOfEvidence
from mv64e_dto.reference import Reference
from mv64e_dto.recommendation_priority_coding import RecommendationPriorityCoding
from mv64e_dto.study_reference import StudyReference




class MtbStudyEnrollmentRecommendation(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    # @JsonFormat(pattern = "yyyy-MM-dd") -> datetime.date
    issued_on: Optional[date] = Field(default=None, alias="issuedOn")
    level_of_evidence: Optional[LevelOfEvidence] = Field(default=None, alias="levelOfEvidence")
    medication: Optional[List[AtcUnregisteredMedicationCoding]] = Field(default=None, alias="medication") # PLACEHOLDER: List[AtcUnregisteredMedicationCoding]
    patient: Optional[Reference] = Field(default=None, alias="patient")
    priority: Optional[RecommendationPriorityCoding] = Field(default=None, alias="priority")
    reason: Optional[Reference] = Field(default=None, alias="reason")
    study: Optional[List[StudyReference]] = Field(default=None, alias="study") # PLACEHOLDER: List[StudyReference]
    supporting_variants: Optional[List[GeneAlterationReference]] = Field(default=None, alias="supportingVariants") # PLACEHOLDER: List[GeneAlterationReference]

    model_config = {"populate_by_name": True, "from_attributes": True}