from typing import Optional
from pydantic import BaseModel, Field
from mv64e_dto.protein_expression_result_coding_code import ProteinExpressionResultCodingCode

class ProteinExpressionResultCoding(BaseModel):
    code: Optional[ProteinExpressionResultCodingCode] = Field(default=None, alias="code")
    display: Optional[str] = Field(default=None, alias="display")
    system: Optional[str] = Field(default=None, alias="system")
    version: Optional[str] = Field(default=None, alias="version")

    model_config = {"populate_by_name": True, "from_attributes": True}