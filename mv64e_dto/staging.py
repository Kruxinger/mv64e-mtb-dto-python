from typing import Optional, List
from pydantic import BaseModel, Field
from mv64e_dto.tumor_staging import TumorStaging

class Staging(BaseModel):
    history: Optional[List[TumorStaging]] = Field(default=None, alias="history")

    model_config = {"populate_by_name": True, "from_attributes": True}