from typing import Optional
from pydantic import BaseModel, Field
from mv64e_dto.value_code import ValueCode

class MtbDiagnosisCoding(BaseModel):
    # Nimmt an, dass 'code' ein ValueCode-Objekt ist, das den Code enthält
    code: Optional[ValueCode] = Field(
        default=None,
        alias="code"
    )
    display: Optional[str] = Field(
        default=None,
        alias="display"
    )
    system: Optional[str] = Field(
        default=None,
        alias="system"
    )
    version: Optional[str] = Field(
        default=None,
        alias="version"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }