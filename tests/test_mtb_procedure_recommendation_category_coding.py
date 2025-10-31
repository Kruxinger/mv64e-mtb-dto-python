from mv64e_dto.mtb_procedure_recommendation_category_coding import MtbProcedureRecommendationCategoryCoding
from mv64e_dto.mtb_procedure_recommendation_category_coding_code import MtbProcedureRecommendationCategoryCodingCode

def test_category_coding_deserialization():
    data = {
        "code": "OP",
        "system": "http://mtb-codesystem.de/procedure-category"
    }
    coding = MtbProcedureRecommendationCategoryCoding(**data)
    assert coding.code == MtbProcedureRecommendationCategoryCodingCode.OP
    assert coding.system == "http://mtb-codesystem.de/procedure-category"

def test_category_coding_serialization():
    coding = MtbProcedureRecommendationCategoryCoding(
        code=MtbProcedureRecommendationCategoryCodingCode.WS,
        display="Weitere Sequenzierung"
    )
    dump = coding.model_dump(by_alias=True, exclude_none=True)
    assert dump["code"] == "WS"
    assert dump["display"] == "Weitere Sequenzierung"