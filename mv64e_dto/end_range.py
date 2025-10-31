from typing import Optional
from pydantic import BaseModel, Field

class EndRange(BaseModel):
    end: Optional[float] = Field(
        default=None,
        alias="end"
    )
    # Java 'double' (primitiv) wird in Python zu 'float' (optional, da es im DTO enthalten ist und Pydantic Primitiven in Java standardmäßig als optional behandelt, wenn sie in Lombok-DTOs mit @NoArgsConstructor sind)
    start: float = Field(
        alias="start"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }