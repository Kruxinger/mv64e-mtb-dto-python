from typing import Optional
from pydantic import BaseModel, Field
from mv64e_dto.mtb_care_plan_recommendations_missing_reason_coding_code import MtbCarePlanRecommendationsMissingReasonCodingCode

class MtbCarePlanRecommendationsMissingReasonCoding(BaseModel):
    code: Optional[MtbCarePlanRecommendationsMissingReasonCodingCode] = Field(default=None, alias="code")
    display: Optional[str] = Field(default=None, alias="display")
    system: Optional[str] = Field(default=None, alias="system")
    version: Optional[str] = Field(default=None, alias="version")

    model_config = {"populate_by_name": True, "from_attributes": True}