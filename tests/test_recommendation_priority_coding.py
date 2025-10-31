from pydantic import BaseModel
from mv64e_dto.recommendation_priority_coding_code import RecommendationPriorityCodingCode
from mv64e_dto.recommendation_priority_coding import RecommendationPriorityCoding


class CodeTestModel(BaseModel):
    code: RecommendationPriorityCodingCode


def test_code_enum_values():
    assert RecommendationPriorityCodingCode.CODE_1.value == "1"
    assert RecommendationPriorityCodingCode.CODE_4.value == "4"


def test_code_deserialization():
    model = CodeTestModel(code="3")
    assert model.code == RecommendationPriorityCodingCode.CODE_3


def test_coding_serialization_and_deserialization():
    data = {
        "code": "2",
        "display": "Zweitrangig",
        "system": "http://mtb-codesystem.de/priority"
    }
    coding = RecommendationPriorityCoding(**data)

    # Überprüfung der Deserialisierung
    assert coding.code == RecommendationPriorityCodingCode.CODE_2

    # Überprüfung der Serialisierung (Alias-Namen)
    dump = coding.model_dump(by_alias=True, exclude_none=True)
    assert dump["code"] == "2"
    assert dump["display"] == "Zweitrangig"