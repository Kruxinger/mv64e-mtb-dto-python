from typing import Optional
from pydantic import BaseModel, Field
from .no_sequencing_performed_reason_code import NoSequencingPerformedReasonCode

class CarePlanNoSequencingPerformedReasonCoding(BaseModel):
    code: Optional[NoSequencingPerformedReasonCode] = Field(default=None, alias="code")
    display: Optional[str] = Field(default=None, alias="display")
    system: Optional[str] = Field(default=None, alias="system")
    version: Optional[str] = Field(default=None, alias="version")

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }
