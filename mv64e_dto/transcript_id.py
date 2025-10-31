from typing import Optional
from pydantic import BaseModel, Field
from mv64e_dto.transcript_id_system import TranscriptIdSystem

class TranscriptId(BaseModel):
    system: Optional[TranscriptIdSystem] = Field(default=None, alias="system")
    value: Optional[str] = Field(default=None, alias="value")

    model_config = {"populate_by_name": True, "from_attributes": True}