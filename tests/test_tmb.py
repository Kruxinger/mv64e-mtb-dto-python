from mv64e_dto.tmb import Tmb
from mv64e_dto.tmb_result import TmbResult
from mv64e_dto.reference import Reference

# Dummy-Daten
DUMMY_TMB_VALUE = TmbResult(value=12.5, unit="mut/Mb")

def test_tmb_deserialization():
    data = {
        "id": "tmb-1",
        "value": {"value": 8.0, "unit": "mut/Mb"},
        "interpretation": {"code": "high", "display": "Hoch"}, # Dummy Interpretation
        "patient": {"reference": "Patient/p10"},
    }
    tmb = Tmb(**data)

    assert tmb.id == "tmb-1"
    assert tmb.value.value == 8.0
    assert tmb.value.unit == "mut/Mb"
    assert tmb.patient.reference == "Patient/p10"
    assert tmb.interpretation["code"] == "high"

def test_tmb_serialization():
    tmb = Tmb(
        id="tmb-2",
        value=DUMMY_TMB_VALUE,
        specimen=Reference(reference="Specimen/s5")
    )
    dump = tmb.model_dump(by_alias=True, exclude_none=True)
    assert dump["value"]["value"] == 12.5
    assert dump["specimen"]["reference"] == "Specimen/s5"