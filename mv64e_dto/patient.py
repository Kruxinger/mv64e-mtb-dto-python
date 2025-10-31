from typing import Optional, Dict, Any
from datetime import date
from pydantic import BaseModel, Field

from mv64e_dto.address import Address
from mv64e_dto.age import Age
from mv64e_dto.coding import Coding
from mv64e_dto.gender_coding import GenderCoding
from mv64e_dto.health_insurance import HealthInsurance
from mv64e_dto.vital_status_coding import VitalStatusCoding


class Patient(BaseModel):
    address: Optional[Address] = Field(default=None, alias="address") # PLACEHOLDER: Address
    age: Optional[Age] = Field(default=None, alias="age") # PLACEHOLDER: Age
    # @JsonFormat(pattern = "yyyy-MM-dd") -> datetime.date
    birth_date: Optional[date] = Field(default=None, alias="birthDate")
    # @JsonFormat(pattern = "yyyy-MM-dd") -> datetime.date
    date_of_death: Optional[date] = Field(default=None, alias="dateOfDeath")
    gender: Optional[GenderCoding] = Field(default=None, alias="gender") # PLACEHOLDER: GenderCoding
    health_insurance: Optional[HealthInsurance] = Field(default=None, alias="healthInsurance") # PLACEHOLDER: HealthInsurance
    id: Optional[str] = Field(default=None, alias="id")
    managing_site: Optional[Coding] = Field(default=None, alias="managingSite") # PLACEHOLDER: Coding
    vital_status: Optional[VitalStatusCoding] = Field(default=None, alias="vitalStatus") # PLACEHOLDER: VitalStatusCoding

    model_config = {"populate_by_name": True, "from_attributes": True}