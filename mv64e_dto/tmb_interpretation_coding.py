from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

from mv64e_dto.interpretation_coding_code import InterpretationCodingCode




class TmbInterpretationCoding(BaseModel):
    code: Optional[InterpretationCodingCode] = Field(default=None, alias="code") # PLACEHOLDER: InterpretationCodingCode
    display: Optional[str] = Field(default=None, alias="display")
    system: Optional[str] = Field(default=None, alias="system")
    version: Optional[str] = Field(default=None, alias="version")

    model_config = {"populate_by_name": True, "from_attributes": True}