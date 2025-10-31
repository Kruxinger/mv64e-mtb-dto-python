from typing import Optional, List, Dict, Any
from datetime import date
from pydantic import BaseModel, Field

from mv64e_dto.coding import Coding




class TumorGrading(BaseModel):
    codes: Optional[List[Coding]] = Field(default=None, alias="codes") # PLACEHOLDER: List[Coding]
    # @JsonFormat(pattern = "yyyy-MM-dd") -> datetime.date
    date: Optional[date] = Field(default=None, alias="date")

    model_config = {"populate_by_name": True, "from_attributes": True}