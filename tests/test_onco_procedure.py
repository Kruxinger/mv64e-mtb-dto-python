from datetime import date
from mv64e_dto.onco_procedure import OncoProcedure
from mv64e_dto.onco_procedure_coding import OncoProcedureCoding
from mv64e_dto.onco_procedure_coding_code import OncoProcedureCodingCode
from mv64e_dto.period_date import PeriodDate
from mv64e_dto.reference import Reference

# Dummy-Daten
DUMMY_CODE = OncoProcedureCoding(code=OncoProcedureCodingCode.SURGERY, display="Tumorresektion")
DUMMY_PERIOD = PeriodDate(start=date(2023, 5, 15), end=date(2023, 5, 15))

def test_onco_procedure_deserialization():
    data = {
        "id": "proc-1",
        "code": {"code": "radio-therapy"},
        "period": {"start": "2024-02-01"},
        "recordedOn": "2024-03-01",
        "therapyLine": 2,
        "notes": ["Gute Verträglichkeit"],
        "intent": {"code": "P"}, # Dummy MtbTherapyIntentCoding
        "status": {"code": "completed"} # Dummy TherapyStatusCoding
    }
    op = OncoProcedure(**data)

    assert op.id == "proc-1"
    assert op.code.code == OncoProcedureCodingCode.RADIO_THERAPY
    assert op.period.start == date(2024, 2, 1)
    assert op.recorded_on == date(2024, 3, 1)
    assert op.therapy_line == 2
    assert op.notes[0] == "Gute Verträglichkeit"

def test_onco_procedure_serialization():
    op = OncoProcedure(
        id="proc-2",
        code=DUMMY_CODE,
        period=DUMMY_PERIOD,
        intent={"code": "C"}
    )
    dump = op.model_dump(by_alias=True, exclude_none=True)
    assert dump["code"]["code"] == "surgery"
    assert dump["period"]["start"] == "2023-05-15"
    assert dump["intent"]["code"] == "C"