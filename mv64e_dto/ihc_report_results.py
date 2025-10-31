from typing import Optional, List
from pydantic import BaseModel, Field
from mv64e_dto.protein_expression import ProteinExpression

class IhcReportResults(BaseModel):
    # Liste von ProteinExpressionen für MSI/MMR
    msi_mmr: Optional[List[ProteinExpression]] = Field(default=None, alias="msiMmr")
    # Liste allgemeiner ProteinExpressionen (z.B. PD-L1)
    protein_expression: Optional[List[ProteinExpression]] = Field(default=None, alias="proteinExpression")

    model_config = {"populate_by_name": True, "from_attributes": True}