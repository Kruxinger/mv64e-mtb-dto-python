from typing import Optional, List
from pydantic import BaseModel, Field

from mv64e_dto.period_date import PeriodDate
from mv64e_dto.reference import Reference

class MtbEpisodeOfCare(BaseModel):
    diagnoses: Optional[List[Reference]] = Field(default=None, alias="diagnoses")
    id: Optional[str] = Field(default=None, alias="id")
    patient: Optional[Reference] = Field(default=None, alias="patient")
    period: Optional[PeriodDate] = Field(default=None, alias="period") # SIMULATED/PLACEHOLDER: PeriodDate

    model_config = {"populate_by_name": True, "from_attributes": True}