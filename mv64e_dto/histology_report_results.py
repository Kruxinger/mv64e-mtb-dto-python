from typing import Optional
from pydantic import BaseModel, Field
# Angenommen existieren
from mv64e_dto.tumor_cell_content import TumorCellContent
from mv64e_dto.tumor_morphology import TumorMorphology

class HistologyReportResults(BaseModel):
    tumor_cell_content: Optional[TumorCellContent] = Field(
        default=None,
        alias="tumorCellContent"
    )
    tumor_morphology: Optional[TumorMorphology] = Field(
        default=None,
        alias="tumorMorphology"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }