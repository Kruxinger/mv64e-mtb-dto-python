from datetime import date
from mv64e_dto.histology_reevaluation_request import HistologyReevaluationRequest
from mv64e_dto.reference import Reference

DUMMY_PATIENT_REF = Reference(id="pat_h", type="Patient")
DUMMY_SPECIMEN_REF = Reference(id="spec_h", type="Specimen")


def test_hrr_initialization():
    issue_date = date(2024, 1, 15)
    hrr = HistologyReevaluationRequest(
        id="hrr_1",
        issued_on=issue_date,
        patient=DUMMY_PATIENT_REF,
        specimen=DUMMY_SPECIMEN_REF
    )
    assert hrr.id == "hrr_1"
    assert hrr.issued_on == issue_date
    assert hrr.specimen.id == "spec_h"


def test_hrr_date_serialization_and_deserialization():
    data = {
        "issuedOn": "2024-05-20",
        "patient": {"id": "pat_j"}
    }
    hrr = HistologyReevaluationRequest(**data)
    assert hrr.issued_on == date(2024, 5, 20)

    dump = hrr.model_dump(by_alias=True, mode='json')
    assert dump["issuedOn"] == "2024-05-20"