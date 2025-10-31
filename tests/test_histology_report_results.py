from mv64e_dto.histology_report_results import HistologyReportResults
from pydantic import BaseModel
from typing import Optional

# Simuliere abhängige DTOs
class TumorCellContent(BaseModel):
    percent: Optional[float] = None

class TumorMorphology(BaseModel):
    code: Optional[str] = None

DUMMY_TCC = TumorCellContent(percent=0.75)
DUMMY_TM = TumorMorphology(code="8000/3")

def test_hrr_results_initialization():
    res = HistologyReportResults(
        tumor_cell_content=DUMMY_TCC,
        tumor_morphology=DUMMY_TM
    )
    assert res.tumor_cell_content.percent == 0.75
    assert res.tumor_morphology.code == "8000/3"

def test_hrr_results_alias_input():
    data = {
        "tumorCellContent": {"percent": 0.5},
        "tumorMorphology": {"code": "8140/3"}
    }
    res = HistologyReportResults(**data)
    assert res.tumor_cell_content.percent == 0.5