from typing import Optional, List
from datetime import date
from pydantic import BaseModel, Field

from mv64e_dto.atc_unregistered_medication_coding import AtcUnregisteredMedicationCoding
from mv64e_dto.reference import Reference
from mv64e_dto.period_date import PeriodDate
from mv64e_dto.mtb_therapy_intent_coding import MtbTherapyIntentCoding
from mv64e_dto.therapy_status_coding import TherapyStatusCoding
from mv64e_dto.mtb_therapy_status_reason_coding import MtbTherapyStatusReasonCoding
from mv64e_dto.mtb_systemic_therapy_category_coding import MtbSystemicTherapyCategoryCoding
from mv64e_dto.mtb_systemic_therapy_dosage_density_coding import MtbSystemicTherapyDosageDensityCoding
from mv64e_dto.mtb_systemic_therapy_recommendation_fulfillment_status_coding import MtbSystemicTherapyRecommendationFulfillmentStatusCoding


class MtbSystemicTherapy(BaseModel):
    based_on: Optional[Reference] = Field(default=None, alias="basedOn")
    category: Optional[MtbSystemicTherapyCategoryCoding] = Field(default=None, alias="category")
    dosage: Optional[MtbSystemicTherapyDosageDensityCoding] = Field(default=None, alias="dosage")
    id: Optional[str] = Field(default=None, alias="id")
    intent: Optional[MtbTherapyIntentCoding] = Field(default=None, alias="intent")
    medication: Optional[List[AtcUnregisteredMedicationCoding]] = Field(default=None, alias="medication") # PLACEHOLDER: List[AtcUnregisteredMedicationCoding]
    notes: Optional[List[str]] = Field(default=None, alias="notes")
    patient: Optional[Reference] = Field(default=None, alias="patient")
    period: Optional[PeriodDate] = Field(default=None, alias="period")
    reason: Optional[Reference] = Field(default=None, alias="reason")
    recommendation_fulfillment_status: Optional[MtbSystemicTherapyRecommendationFulfillmentStatusCoding] = Field(default=None, alias="recommendationFulfillmentStatus")
    # @JsonFormat(pattern = "yyyy-MM-dd") -> datetime.date
    recorded_on: Optional[date] = Field(default=None, alias="recordedOn")
    status: Optional[TherapyStatusCoding] = Field(default=None, alias="status")
    status_reason: Optional[MtbTherapyStatusReasonCoding] = Field(default=None, alias="statusReason")
    therapy_line: Optional[int] = Field(default=None, alias="therapyLine")

    model_config = {"populate_by_name": True, "from_attributes": True}