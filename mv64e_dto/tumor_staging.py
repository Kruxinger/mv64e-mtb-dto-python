from typing import Optional, List
from datetime import date
from pydantic import BaseModel, Field
from mv64e_dto.coding import Coding
from mv64e_dto.tnm_classification import TnmClassification
from mv64e_dto.tumor_staging_method_coding import TumorStagingMethodCoding

class TumorStaging(BaseModel):
    # @JsonFormat(pattern = "yyyy-MM-dd") -> datetime.date
    date: Optional[date] = Field(default=None, alias="date")
    method: Optional[TumorStagingMethodCoding] = Field(default=None, alias="method")
    other_classifications: Optional[List[Coding]] = Field(default=None, alias="otherClassifications")
    tnm_classification: Optional[TnmClassification] = Field(default=None, alias="tnmClassification") # PLACEHOLDER: TnmClassification

    model_config = {"populate_by_name": True, "from_attributes": True}