from typing import Optional
from pydantic import BaseModel, Field
from mv64e_dto.reference import Reference
from mv64e_dto.coding import Coding
from mv64e_dto.protein_expression_ic_score_coding import ProteinExpressionIcScoreCoding
from mv64e_dto.protein_expression_tc_score_coding import ProteinExpressionTcScoreCoding
from mv64e_dto.protein_expression_result_coding import ProteinExpressionResultCoding


class ProteinExpression(BaseModel):
    ic_score: Optional[ProteinExpressionIcScoreCoding] = Field(default=None, alias="icScore")
    id: Optional[str] = Field(default=None, alias="id")
    patient: Optional[Reference] = Field(default=None, alias="patient")
    protein: Optional[Coding] = Field(default=None, alias="protein")
    tc_score: Optional[ProteinExpressionTcScoreCoding] = Field(default=None, alias="tcScore")

    # Java Long -> Optional[int]
    tps_score: Optional[int] = Field(default=None, alias="tpsScore")
    # Java Long -> Optional[int]
    cps_score: Optional[int] = Field(default=None, alias="cpsScore")

    value: Optional[ProteinExpressionResultCoding] = Field(default=None, alias="value")

    model_config = {"populate_by_name": True, "from_attributes": True}