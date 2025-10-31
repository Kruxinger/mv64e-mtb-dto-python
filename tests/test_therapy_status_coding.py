from pydantic import BaseModel
from mv64e_dto.therapy_status_coding import TherapyStatusCoding
from mv64e_dto.therapy_status_coding_code import TherapyStatusCodingCode


class CodeTestModel(BaseModel):
    code: TherapyStatusCodingCode


def test_code_enum_values():
    assert TherapyStatusCodingCode.COMPLETED.value == "completed"
    assert TherapyStatusCodingCode.ON_GOING.value == "on-going"


def test_code_deserialization():
    model = CodeTestModel(code="stopped")
    assert model.code == TherapyStatusCodingCode.STOPPED


def test_coding_serialization_and_deserialization():
    data = {
        "code": "on-going",
        "display": "Läuft noch",
        "system": "http://mtb-codesystem.de/status"
    }
    coding = TherapyStatusCoding(**data)

    # Überprüfung der Deserialisierung
    assert coding.code == TherapyStatusCodingCode.ON_GOING

    # Überprüfung der Serialisierung (Alias-Namen)
    dump = coding.model_dump(by_alias=True, exclude_none=True)
    assert dump["code"] == "on-going"
    assert dump["display"] == "Läuft noch"