from typing import Optional
from pydantic import BaseModel, Field
from mv64e_dto.reference import Reference
from mv64e_dto.tumor_cell_content_method_coding import TumorCellContentMethodCoding

class TumorCellContent(BaseModel):
    id: Optional[str] = Field(
        default=None,
        alias="id"
    )
    method: Optional[TumorCellContentMethodCoding] = Field(
        default=None,
        alias="method"
    )
    patient: Optional[Reference] = Field(
        default=None,
        alias="patient"
    )
    specimen: Optional[Reference] = Field(
        default=None,
        alias="specimen"
    )
    # Java 'double' (primitiv) wird als required float angenommen
    value: float = Field(
        alias="value"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }