from typing import Optional
from pydantic import BaseModel, Field
from mv64e_dto.coding import Coding
from mv64e_dto.reference import Reference

class GeneAlterationReference(BaseModel):
    display: Optional[str] = Field(
        default=None,
        alias="display"
    )
    gene: Optional[Coding] = Field(
        default=None,
        alias="gene"
    )
    variant: Optional[Reference] = Field(
        default=None,
        alias="variant"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }