from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

from mv64e_dto.mtb_systemic_therapy import MtbSystemicTherapy


class SystemicTherapy(BaseModel):
    history: Optional[List[MtbSystemicTherapy]] = Field(default=None, alias="history") # PLACEHOLDER: List[MtbSystemicTherapy]

    model_config = {"populate_by_name": True, "from_attributes": True}