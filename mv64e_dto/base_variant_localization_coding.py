from typing import Optional
from pydantic import BaseModel, Field
from .base_variant_localization_coding_code import BaseVariantLocalizationCodingCode

class BaseVariantLocalizationCoding(BaseModel):
    code: Optional[BaseVariantLocalizationCodingCode] = Field(default=None, alias="code")
    display: Optional[str] = Field(default=None, alias="display")
    system: Optional[str] = Field(default=None, alias="system")
    version: Optional[str] = Field(default=None, alias="version")

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }
