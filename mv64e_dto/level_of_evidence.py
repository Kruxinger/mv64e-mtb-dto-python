from typing import Optional, List
from pydantic import BaseModel, Field
from mv64e_dto.level_of_evidence_addendum_coding import LevelOfEvidenceAddendumCoding # Bereits erstellt
from mv64e_dto.level_of_evidence_grading_coding import LevelOfEvidenceGradingCoding # Bereits erstellt
from mv64e_dto.publication_reference import PublicationReference




class LevelOfEvidence(BaseModel):
    addendums: Optional[List[LevelOfEvidenceAddendumCoding]] = Field(
        default=None,
        alias="addendums"
    )
    grading: Optional[LevelOfEvidenceGradingCoding] = Field(
        default=None,
        alias="grading"
    )
    publications: Optional[List[PublicationReference]] = Field(
        default=None,
        alias="publications"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }