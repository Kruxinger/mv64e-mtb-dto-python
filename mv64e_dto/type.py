from typing import Optional, List
from pydantic import BaseModel, Field

from mv64e_dto.history import History



class Type(BaseModel):
    history: Optional[List[History]] = Field(default=None, alias="history") # PLACEHOLDER: List[History]

    model_config = {"populate_by_name": True, "from_attributes": True}