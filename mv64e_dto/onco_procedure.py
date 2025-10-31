from typing import Optional, List
from datetime import date
from pydantic import BaseModel, Field

from mv64e_dto.mtb_therapy_intent_coding import MtbTherapyIntentCoding
from mv64e_dto.mtb_therapy_status_reason_coding import MtbTherapyStatusReasonCoding
from mv64e_dto.reference import Reference
from mv64e_dto.period_date import PeriodDate
from mv64e_dto.onco_procedure_coding import OncoProcedureCoding
from mv64e_dto.therapy_status_coding import TherapyStatusCoding



class OncoProcedure(BaseModel):
    based_on: Optional[Reference] = Field(default=None, alias="basedOn")
    code: Optional[OncoProcedureCoding] = Field(default=None, alias="code")
    id: Optional[str] = Field(default=None, alias="id")
    intent: Optional[MtbTherapyIntentCoding] = Field(default=None, alias="intent") # PLACEHOLDER: MtbTherapyIntentCoding
    notes: Optional[List[str]] = Field(default=None, alias="notes")
    patient: Optional[Reference] = Field(default=None, alias="patient")
    period: Optional[PeriodDate] = Field(default=None, alias="period")
    reason: Optional[Reference] = Field(default=None, alias="reason")
    # @JsonFormat(pattern = "yyyy-MM-dd") -> datetime.date
    recorded_on: Optional[date] = Field(default=None, alias="recordedOn")
    status: Optional[TherapyStatusCoding] = Field(default=None, alias="status") # PLACEHOLDER: TherapyStatusCoding
    status_reason: Optional[MtbTherapyStatusReasonCoding] = Field(default=None, alias="statusReason") # PLACEHOLDER: MtbTherapyStatusReasonCoding
    therapy_line: Optional[int] = Field(default=None, alias="therapyLine")

    model_config = {"populate_by_name": True, "from_attributes": True}