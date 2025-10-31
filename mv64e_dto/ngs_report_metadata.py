from typing import Optional
from pydantic import BaseModel, Field

class NgsReportMetadata(BaseModel):
    kit_manufacturer: Optional[str] = Field(default=None, alias="kitManufacturer")
    kit_type: Optional[str] = Field(default=None, alias="kitType")
    pipeline: Optional[str] = Field(default=None, alias="pipeline")
    reference_genome: Optional[str] = Field(default=None, alias="referenceGenome")
    sequencer: Optional[str] = Field(default=None, alias="sequencer")

    model_config = {"populate_by_name": True, "from_attributes": True}