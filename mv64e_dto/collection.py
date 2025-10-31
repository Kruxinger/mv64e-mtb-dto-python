from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from mv64e_dto.tumor_specimen_collection_localization_coding import TumorSpecimenCollectionLocalizationCoding
from mv64e_dto.tumor_specimen_collection_method_coding import TumorSpecimenCollectionMethodCoding

class Collection(BaseModel):
    # Java Date ohne explizites Format -> standardmäßig datetime
    date: Optional[datetime] = Field(
        default=None,
        alias="date"
    )
    localization: Optional[TumorSpecimenCollectionLocalizationCoding] = Field(
        default=None,
        alias="localization"
    )
    method: Optional[TumorSpecimenCollectionMethodCoding] = Field(
        default=None,
        alias="method"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }