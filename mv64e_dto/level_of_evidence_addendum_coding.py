from typing import Optional
from pydantic import BaseModel, Field
from mv64e_dto.level_of_evidence_addendum_coding_code import LevelOfEvidenceAddendumCodingCode

class LevelOfEvidenceAddendumCoding(BaseModel):
    code: Optional[LevelOfEvidenceAddendumCodingCode] = Field(
        default=None,
        alias="code"
    )
    display: Optional[str] = Field(
        default=None,
        alias="display"
    )
    system: Optional[str] = Field(
        default=None,
        alias="system"
    )
    version: Optional[str] = Field(
        default=None,
        alias="version"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }