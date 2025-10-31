from typing import Optional, List
from pydantic import BaseModel, Field

from mv64e_dto.claim import Claim
from mv64e_dto.claim_response import ClaimResponse
from mv64e_dto.family_member_history import FamilyMemberHistory
#from mv64e_dto.follow_up import FollowUp
from mv64e_dto.histology_report import HistologyReport
from mv64e_dto.mtb_care_plan import MtbCarePlan
from mv64e_dto.mtb_diagnosis import MtbDiagnosis
from mv64e_dto.mtb_episode_of_care import MtbEpisodeOfCare
from mv64e_dto.ihc_report import IhcReport # Bereits erstellt
from mv64e_dto.msi import Msi # Bereits erstellt
from mv64e_dto.mtb_systemic_therapy import MtbSystemicTherapy
from mv64e_dto.mvh_metadata import MvhMetadata
from mv64e_dto.onco_procedure import OncoProcedure
from mv64e_dto.patient import Patient
from mv64e_dto.performance_status import PerformanceStatus
from mv64e_dto.prior_diagnostic_report import PriorDiagnosticReport
from mv64e_dto.response import Response
from mv64e_dto.somatic_ngs_report import SomaticNgsReport
from mv64e_dto.systemic_therapy import SystemicTherapy
from mv64e_dto.tumor_specimen import TumorSpecimen

# Fehlt: SystemicTherapy

class Mtb(BaseModel):
    care_plans: Optional[List[MtbCarePlan]] = Field(default=None, alias="carePlans")
    claim_responses: Optional[List[ClaimResponse]] = Field(default=None, alias="claimResponses") # PLACEHOLDER: List[ClaimResponse]
    claims: Optional[List[Claim]] = Field(default=None, alias="claims") # PLACEHOLDER: List[Claim]
    diagnoses: Optional[List[MtbDiagnosis]] = Field(default=None, alias="diagnoses")
    episodes_of_care: Optional[List[MtbEpisodeOfCare]] = Field(default=None, alias="episodesOfCare")
    family_member_histories: Optional[List[FamilyMemberHistory]] = Field(default=None, alias="familyMemberHistories") # PLACEHOLDER: List[FamilyMemberHistory]
    #follow_ups: Optional[List[FollowUp]] = Field(default=None, alias="followUps") # PLACEHOLDER: List[FollowUp]
    guideline_procedures: Optional[List[OncoProcedure]] = Field(default=None, alias="guidelineProcedures") # PLACEHOLDER: List[OncoProcedure]
    guideline_therapies: Optional[List[MtbSystemicTherapy]] = Field(default=None, alias="guidelineTherapies") # PLACEHOLDER: List[MtbSystemicTherapy]
    histology_reports: Optional[List[HistologyReport]] = Field(default=None, alias="histologyReports") # PLACEHOLDER: List[HistologyReport]
    ihc_reports: Optional[List[IhcReport]] = Field(default=None, alias="ihcReports")
    metadata: Optional[MvhMetadata] = Field(default=None, alias="metadata") # PLACEHOLDER: MvhMetadata
    ngs_reports: Optional[List[SomaticNgsReport]] = Field(default=None, alias="ngsReports") # PLACEHOLDER: List[SomaticNgsReport]
    msi_findings: Optional[List[Msi]] = Field(default=None, alias="msiFindings")
    patient: Optional[Patient] = Field(default=None, alias="patient") # PLACEHOLDER: Patient
    performance_status: Optional[List[PerformanceStatus]] = Field(default=None, alias="performanceStatus") # PLACEHOLDER: List[PerformanceStatus]
    prior_diagnostic_reports: Optional[List[PriorDiagnosticReport]] = Field(default=None, alias="priorDiagnosticReports") # PLACEHOLDER: List[PriorDiagnosticReport]
    responses: Optional[List[Response]] = Field(default=None, alias="responses") # PLACEHOLDER: List[Response]
    specimens: Optional[List[TumorSpecimen]] = Field(default=None, alias="specimens") # PLACEHOLDER: List[TumorSpecimen]
    systemic_therapies: Optional[List[SystemicTherapy]] = Field(default=None, alias="systemicTherapies") # PLACEHOLDER: List[SystemicTherapy]

    model_config = {"populate_by_name": True, "from_attributes": True}