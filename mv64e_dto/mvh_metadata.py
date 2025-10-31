from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from mv64e_dto.mvh_submission_type import MvhSubmissionType
# Fehlt: ModelProjectConsent
# Fehlt: ResearchConsentReasonMissing

class MvhMetadata(BaseModel):
    model_project_consent: Optional[Dict[str, Any]] = Field(
        default=None,
        alias="modelProjectConsent"
    ) # PLACEHOLDER: ModelProjectConsent
    research_consents: Optional[List[Dict[str, Any]]] = Field(
        default=None,
        alias="researchConsents"
    ) # List<Map<String, Object>> wird zu List[Dict]
    reason_research_consent_missing: Optional[Dict[str, Any]] = Field(
        default=None,
        alias="reasonResearchConsentMissing"
    ) # PLACEHOLDER: ResearchConsentReasonMissing
    transfer_tan: Optional[str] = Field(
        default=None,
        alias="transferTAN"
    )
    type: Optional[MvhSubmissionType] = Field(
        default=None,
        alias="type"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }