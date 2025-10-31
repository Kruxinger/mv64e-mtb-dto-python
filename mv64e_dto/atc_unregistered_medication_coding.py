from typing import Optional
from pydantic import BaseModel, Field
from .requested_medication_system import RequestedMedicationSystem

class AtcUnregisteredMedicationCoding(BaseModel):
    code: Optional[str] = Field(default=None, alias="code")
    display: Optional[str] = Field(default=None, alias="display")
    system: Optional[RequestedMedicationSystem] = Field(default=None, alias="system")
    version: Optional[str] = Field(default=None, alias="version")

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }
