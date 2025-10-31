from typing import Optional
from pydantic import BaseModel, Field
# Angenommen existiert
from mv64e_dto.interpretation_coding_code import InterpretationCodingCode

class HrdScoreInterpretationCoding(BaseModel):
    code: Optional[InterpretationCodingCode] = Field(
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