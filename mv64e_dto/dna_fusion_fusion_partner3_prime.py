from typing import Optional
from pydantic import BaseModel, Field
from mv64e_dto.chromosome import Chromosome
from mv64e_dto.coding import Coding

class DnaFusionFusionPartner3Prime(BaseModel):
    chromosome: Optional[Chromosome] = Field(
        default=None,
        alias="chromosome"
    )
    gene: Optional[Coding] = Field(
        default=None,
        alias="gene"
    )
    # Java 'double' (primitiv) wird hier als required float angenommen
    position: float = Field(
        alias="position"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }