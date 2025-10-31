from typing import Optional
from pydantic import BaseModel, Field
from mv64e_dto.components import Components
from mv64e_dto.reference import Reference
from mv64e_dto.hrd_score_interpretation_coding import HrdScoreInterpretationCoding

class HrdScore(BaseModel):
    components: Optional[Components] = Field(
        default=None,
        alias="components"
    )
    id: Optional[str] = Field(
        default=None,
        alias="id"
    )
    interpretation: Optional[HrdScoreInterpretationCoding] = Field(
        default=None,
        alias="interpretation"
    )
    patient: Optional[Reference] = Field(
        default=None,
        alias="patient"
    )
    specimen: Optional[Reference] = Field(
        default=None,
        alias="specimen"
    )
    # Java 'double' (primitiv) wird hier als required float angenommen
    value: float = Field(
        alias="value"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }