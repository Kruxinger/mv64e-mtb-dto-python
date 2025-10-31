from datetime import date
from mv64e_dto.procedure_recommendation import ProcedureRecommendation
from mv64e_dto.mtb_procedure_recommendation_category_coding import MtbProcedureRecommendationCategoryCoding
from mv64e_dto.mtb_procedure_recommendation_category_coding_code import MtbProcedureRecommendationCategoryCodingCode
from mv64e_dto.recommendation_priority_coding import RecommendationPriorityCoding
from mv64e_dto.recommendation_priority_coding_code import RecommendationPriorityCodingCode

# Dummy-Daten
DUMMY_CODE = MtbProcedureRecommendationCategoryCoding(
    code=MtbProcedureRecommendationCategoryCodingCode.WS,
    display="Weitere Sequenzierung"
)
DUMMY_PRIORITY = RecommendationPriorityCoding(
    code=RecommendationPriorityCodingCode.CODE_2
)

def test_procedure_recommendation_deserialization():
    data = {
        "id": "pr1",
        "issuedOn": "2024-10-25",
        "code": {"code": "WS"},
        "priority": {"code": "2"},
        "supportingVariants": [{"id": "var1"}, {"id": "var2"}] # Dummy für GeneAlterationReference
    }
    pr = ProcedureRecommendation(**data)

    assert pr.id == "pr1"
    assert pr.issued_on == date(2024, 10, 25)
    assert pr.code.code == MtbProcedureRecommendationCategoryCodingCode.WS
    assert pr.priority.code == RecommendationPriorityCodingCode.CODE_2
    assert len(pr.supporting_variants) == 2

def test_procedure_recommendation_serialization():
    pr = ProcedureRecommendation(
        id="pr2",
        issued_on=date(2024, 1, 1),
        code=DUMMY_CODE,
        priority=DUMMY_PRIORITY
    )
    dump = pr.model_dump(by_alias=True, exclude_none=True)
    assert dump["issuedOn"] == "2024-01-01"
    assert dump["code"]["code"] == "WS"
    assert dump["priority"]["code"] == "2"