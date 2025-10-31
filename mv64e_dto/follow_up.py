from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel, Field
from mv64e_dto.reference import Reference
from mv64e_dto.follow_up_patient_status_coding import FollowUpPatientStatusCoding

class FollowUp(BaseModel):
    # Java Date mit @JsonFormat(pattern = "yyyy-MM-dd") -> datetime.date
    date: Optional[date] = Field(
        default=None,
        alias="date"
    )
    # Java Date ohne Format -> standardmäßig datetime.datetime (ISO 8601)
    last_contact_date: Optional[datetime] = Field(
        default=None,
        alias="lastContactDate"
    )
    patient: Optional[Reference] = Field(
        default=None,
        alias="patient"
    )
    patient_status: Optional[FollowUpPatientStatusCoding] = Field(
        default=None,
        alias="patientStatus"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }