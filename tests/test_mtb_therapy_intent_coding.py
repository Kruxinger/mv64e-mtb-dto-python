from pydantic import BaseModel
from mv64e_dto.mtb_therapy_intent_coding import MtbTherapyIntentCoding
from mv64e_dto.mtb_therapy_intent_coding_code import MtbTherapyIntentCodingCode


class CodeTestModel(BaseModel):
    code: MtbTherapyIntentCodingCode


def test_code_enum_values():
    assert MtbTherapyIntentCodingCode.K.value == "K"
    assert MtbTherapyIntentCodingCode.P.value == "P"


def test_code_deserialization():
    model = CodeTestModel(code="S")
    assert model.code == MtbTherapyIntentCodingCode.S


def test_coding_serialization_and_deserialization():
    data = {
        "code": "P",
        "display": "Palliativ",
        "system": "http://mtb-codesystem.de/intent"
    }
    coding = MtbTherapyIntentCoding(**data)

    # Überprüfung der Deserialisierung
    assert coding.code == MtbTherapyIntentCodingCode.P

    # Überprüfung der Serialisierung (Alias-Namen)
    dump = coding.model_dump(by_alias=True, exclude_none=True)
    assert dump["code"] == "P"
    assert dump["display"] == "Palliativ"