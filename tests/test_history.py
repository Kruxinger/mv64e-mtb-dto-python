from datetime import date
from mv64e_dto.history import History
from pydantic import BaseModel
from typing import Optional


# Simuliere MtbDiagnosisCoding DTO
class MtbDiagnosisCoding(BaseModel):
    code: Optional[str] = None
    system: Optional[str] = None


DUMMY_VALUE = MtbDiagnosisCoding(code="C34.9", system="ICD-10")


def test_history_initialization():
    hist_date = date(2020, 7, 1)
    h = History(
        date=hist_date,
        value=DUMMY_VALUE
    )
    assert h.date == hist_date
    assert h.value.code == "C34.9"


def test_history_date_serialization_and_deserialization():
    data = {
        "date": "2021-03-03",
        "value": {"code": "C77.0"}
    }
    h = History(**data)
    assert h.date == date(2021, 3, 3)

    dump = h.model_dump(by_alias=True, mode='json')
    assert dump["date"] == "2021-03-03"
    assert dump["value"]["code"] == "C77.0"