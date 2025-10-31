from typing import Optional
from datetime import date
from pydantic import BaseModel, Field
# Angenommen existiert
from mv64e_dto.mtb_diagnosis_coding import MtbDiagnosisCoding

class History(BaseModel):
    # Java Date mit @JsonFormat(pattern = "yyyy-MM-dd") -> datetime.date
    date: Optional[date] = Field(
        default=None,
        alias="date"
    )
    value: Optional[MtbDiagnosisCoding] = Field(
        default=None,
        alias="value"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }