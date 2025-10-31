from typing import Optional
from datetime import date
from pydantic import BaseModel, Field

class PeriodDate(BaseModel):
    # @JsonFormat(pattern = "yyyy-MM-dd") -> datetime.date
    end: Optional[date] = Field(
        default=None,
        alias="end"
    )
    # @JsonFormat(pattern = "yyyy-MM-dd") -> datetime.date
    start: Optional[date] = Field(
        default=None,
        alias="start"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }