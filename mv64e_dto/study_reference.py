from typing import Optional
from pydantic import BaseModel, Field
from mv64e_dto.study_system import StudySystem

class StudyReference(BaseModel):
    display: Optional[str] = Field(
        default=None,
        alias="display"
    )
    id: Optional[str] = Field(
        default=None,
        alias="id"
    )
    system: Optional[StudySystem] = Field(
        default=None,
        alias="system"
    )
    type: Optional[str] = Field(
        default=None,
        alias="type"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }