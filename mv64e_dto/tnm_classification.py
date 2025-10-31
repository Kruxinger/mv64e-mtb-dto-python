from typing import Optional
from pydantic import BaseModel, Field
from mv64e_dto.coding import Coding

class TnmClassification(BaseModel):
    metastasis: Optional[Coding] = Field(
        default=None,
        alias="metastasis"
    )
    nodes: Optional[Coding] = Field(
        default=None,
        alias="nodes"
    )
    tumor: Optional[Coding] = Field(
        default=None,
        alias="tumor"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }