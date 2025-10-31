from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

from mv64e_dto.collection import Collection
from mv64e_dto.reference import Reference
from mv64e_dto.tumor_specimen_coding import TumorSpecimenCoding

class TumorSpecimen(BaseModel):
    collection: Optional[Collection] = Field(default=None, alias="collection") # PLACEHOLDER: Collection
    diagnosis: Optional[Reference] = Field(default=None, alias="diagnosis")
    id: Optional[str] = Field(default=None, alias="id")
    patient: Optional[Reference] = Field(default=None, alias="patient")
    type: Optional[TumorSpecimenCoding] = Field(default=None, alias="type")

    model_config = {"populate_by_name": True, "from_attributes": True}