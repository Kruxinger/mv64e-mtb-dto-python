from pydantic import BaseModel
from mv64e_dto.mtb_therapy_status_reason_coding import MtbTherapyStatusReasonCoding
from mv64e_dto.mtb_therapy_status_reason_coding_code import MtbTherapyStatusReasonCodingCode


class CodeTestModel(BaseModel):
    code: MtbTherapyStatusReasonCodingCode


def test_code_enum_values():
    assert MtbTherapyStatusReasonCodingCode.PROGRESSION.value == "progression"
    assert MtbTherapyStatusReasonCodingCode.PATIENT_REFUSAL.value == "patient-refusal"


def test_code_deserialization():
    model = CodeTestModel(code="toxicity")
    assert model.code == MtbTherapyStatusReasonCodingCode.TOXICITY


def test_coding_serialization_and_deserialization():
    data = {
        "code": "patient-death",
        "display": "Tod des Patienten",
        "system": "http://mtb-codesystem.de/therapy-stop-reason"
    }
    coding = MtbTherapyStatusReasonCoding(**data)

    # Überprüfung der Deserialisierung
    assert coding.code == MtbTherapyStatusReasonCodingCode.PATIENT_DEATH

    # Überprüfung der Serialisierung (Alias-Namen)
    dump = coding.model_dump(by_alias=True, exclude_none=True)
    assert dump["code"] == "patient-death"