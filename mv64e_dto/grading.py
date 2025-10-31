from typing import Optional, List
from pydantic import BaseModel, Field
# Angenommen existiert, aber simulieren den Import für dieses DTO
from mv64e_dto.tumor_grading import TumorGrading

class Grading(BaseModel):
    history: Optional[List[TumorGrading]] = Field(
        default=None,
        alias="history"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }