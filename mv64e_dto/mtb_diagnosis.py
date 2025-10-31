from typing import Optional, List
from datetime import date
from pydantic import BaseModel, Field
from mv64e_dto.coding import Coding
from mv64e_dto.grading import Grading
from mv64e_dto.reference import Reference
from mv64e_dto.mtb_diagnosis_guideline_treatment_status_coding import MtbDiagnosisGuidelineTreatmentStatusCoding
from mv64e_dto.staging import Staging
from mv64e_dto.type import Type



class MtbDiagnosis(BaseModel):
    code: Optional[Coding] = Field(default=None, alias="code")
    germline_codes: Optional[List[Coding]] = Field(default=None, alias="germlineCodes")
    grading: Optional[Grading] = Field(default=None, alias="grading") # SIMULATED/PLACEHOLDER: Grading
    guideline_treatment_status: Optional[MtbDiagnosisGuidelineTreatmentStatusCoding] = Field(default=None, alias="guidelineTreatmentStatus")
    histology: Optional[List[Reference]] = Field(default=None, alias="histology")
    id: Optional[str] = Field(default=None, alias="id")
    notes: Optional[List[str]] = Field(default=None, alias="notes")
    patient: Optional[Reference] = Field(default=None, alias="patient")
    # @JsonFormat(pattern = "yyyy-MM-dd") -> datetime.date
    recorded_on: Optional[date] = Field(default=None, alias="recordedOn")
    staging: Optional[Staging] = Field(default=None, alias="staging") # SIMULATED/PLACEHOLDER: Staging
    topography: Optional[Coding] = Field(default=None, alias="topography")
    type: Optional[Type] = Field(default=None, alias="type") # SIMULATED/PLACEHOLDER: Type

    model_config = {"populate_by_name": True, "from_attributes": True}