from typing import Optional, List
from datetime import date
from pydantic import BaseModel, Field

from mv64e_dto.care_plan_no_sequencing_performed_reason_coding import CarePlanNoSequencingPerformedReasonCoding
from mv64e_dto.genetic_counseling_recommendation import GeneticCounselingRecommendation
from mv64e_dto.histology_reevaluation_request import HistologyReevaluationRequest
from mv64e_dto.mtb_study_enrollment_recommendation import MtbStudyEnrollmentRecommendation
from mv64e_dto.procedure_recommendation import ProcedureRecommendation
from mv64e_dto.rebiopsy_request import RebiopsyRequest
from mv64e_dto.reference import Reference
from mv64e_dto.mtb_care_plan_recommendations_missing_reason_coding import MtbCarePlanRecommendationsMissingReasonCoding
from mv64e_dto.mtb_medication_recommendation import MtbMedicationRecommendation

class MtbCarePlan(BaseModel):
    genetic_counseling_recommendation: Optional[GeneticCounselingRecommendation] = Field(default=None, alias="geneticCounselingRecommendation") # SIMULATED/PLACEHOLDER: GeneticCounselingRecommendation
    histology_reevaluation_requests: Optional[List[HistologyReevaluationRequest]] = Field(default=None, alias="histologyReevaluationRequests") # SIMULATED/PLACEHOLDER: List[HistologyReevaluationRequest]
    id: Optional[str] = Field(default=None, alias="id")
    # @JsonFormat(pattern = "yyyy-MM-dd") -> datetime.date
    issued_on: Optional[date] = Field(default=None, alias="issuedOn")
    medication_recommendations: Optional[List[MtbMedicationRecommendation]] = Field(default=None, alias="medicationRecommendations")
    no_sequencing_performed_reason: Optional[CarePlanNoSequencingPerformedReasonCoding] = Field(default=None, alias="noSequencingPerformedReason") # SIMULATED/PLACEHOLDER: CarePlanNoSequencingPerformedReasonCoding
    notes: Optional[List[str]] = Field(default=None, alias="notes")
    patient: Optional[Reference] = Field(default=None, alias="patient")
    procedure_recommendations: Optional[List[ProcedureRecommendation]] = Field(default=None, alias="procedureRecommendations") # SIMULATED/PLACEHOLDER: List[ProcedureRecommendation]
    reason: Optional[Reference] = Field(default=None, alias="reason")
    rebiopsy_requests: Optional[List[RebiopsyRequest]] = Field(default=None, alias="rebiopsyRequests") # SIMULATED/PLACEHOLDER: List[RebiopsyRequest]
    recommendations_missing_reason: Optional[MtbCarePlanRecommendationsMissingReasonCoding] = Field(default=None, alias="recommendationsMissingReason")
    study_enrollment_recommendations: Optional[List[MtbStudyEnrollmentRecommendation]] = Field(default=None, alias="studyEnrollmentRecommendations") # SIMULATED/PLACEHOLDER: List[MtbStudyEnrollmentRecommendation]

    model_config = {"populate_by_name": True, "from_attributes": True}