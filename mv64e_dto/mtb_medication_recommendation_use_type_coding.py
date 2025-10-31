from typing import Optional
from pydantic import BaseModel, Field
from mv64e_dto.mtb_medication_recommendation_use_type_coding_code import MtbMedicationRecommendationUseTypeCodingCode

class MtbMedicationRecommendationUseTypeCoding(BaseModel):
    code: Optional[MtbMedicationRecommendationUseTypeCodingCode] = Field(default=None, alias="code")
    display: Optional[str] = Field(default=None, alias="display")
    system: Optional[str] = Field(default=None, alias="system")
    version: Optional[str] = Field(default=None, alias="version")

    model_config = {"populate_by_name": True, "from_attributes": True}