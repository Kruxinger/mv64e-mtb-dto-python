from typing import Optional
from pydantic import BaseModel, Field
from mv64e_dto.mtb_therapy_intent_coding_code import MtbTherapyIntentCodingCode

class MtbTherapyIntentCoding(BaseModel):
    code: Optional[MtbTherapyIntentCodingCode] = Field(default=None, alias="code")
    display: Optional[str] = Field(default=None, alias="display")
    system: Optional[str] = Field(default=None, alias="system")
    version: Optional[str] = Field(default=None, alias="version")

    model_config = {"populate_by_name": True, "from_attributes": True}