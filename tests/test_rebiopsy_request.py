from datetime import date
from mv64e_dto.rebiopsy_request import RebiopsyRequest
from mv64e_dto.reference import Reference

# Dummy-Daten
DUMMY_PATIENT_REF = Reference(reference="Patient/123", display="Max Mustermann")
DUMMY_TUMOR_REF = Reference(reference="Diagnosis/d1", display="Primärtumor Kolon")

def test_rebiopsy_request_deserialization():
    data = {
        "id": "rebiopsy-req1",
        "issuedOn": "2024-11-05",
        "patient": {"reference": "Patient/456"},
        "tumorEntity": {"reference": "Diagnosis/d2"}
    }
    req = RebiopsyRequest(**data)

    assert req.id == "rebiopsy-req1"
    assert req.issued_on == date(2024, 11, 5)
    assert req.patient.reference == "Patient/456"
    assert req.tumor_entity.reference == "Diagnosis/d2"

def test_rebiopsy_request_serialization():
    req = RebiopsyRequest(
        id="rebiopsy-req2",
        issued_on=date(2025, 1, 1),
        patient=DUMMY_PATIENT_REF,
        tumor_entity=DUMMY_TUMOR_REF
    )
    dump = req.model_dump(by_alias=True, exclude_none=True)
    assert dump["issuedOn"] == "2025-01-01"
    assert dump["tumorEntity"]["reference"] == "Diagnosis/d1"