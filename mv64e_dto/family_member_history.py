from typing import Optional
from pydantic import BaseModel, Field
from mv64e_dto.reference import Reference
from mv64e_dto.family_member_history_relationship_type_coding import FamilyMemberHistoryRelationshipTypeCoding

class FamilyMemberHistory(BaseModel):
    id: Optional[str] = Field(
        default=None,
        alias="id"
    )
    patient: Optional[Reference] = Field(
        default=None,
        alias="patient"
    )
    relationship: Optional[FamilyMemberHistoryRelationshipTypeCoding] = Field(
        default=None,
        alias="relationship"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }