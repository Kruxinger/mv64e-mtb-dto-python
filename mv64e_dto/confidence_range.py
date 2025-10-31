from pydantic import BaseModel, Field

class ConfidenceRange(BaseModel):
    max: float = Field(
        alias="max"
    )
    min: float = Field(
        alias="min"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }