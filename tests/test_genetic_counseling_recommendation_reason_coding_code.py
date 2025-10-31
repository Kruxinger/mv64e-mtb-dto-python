from pydantic import BaseModel
from mv64e_dto.genetic_counseling_recommendation_reason_coding_code import GeneticCounselingRecommendationReasonCodingCode

class ReasonCodeTestModel(BaseModel):
    code: GeneticCounselingRecommendationReasonCodingCode

def test_reason_code_values():
    assert GeneticCounselingRecommendationReasonCodingCode.SECONDARY_TUMOR.value == "secondary-tumor"
    assert GeneticCounselingRecommendationReasonCodingCode.SELF_ANAMNESIS.name == "SELF_ANAMNESIS"

def test_reason_code_serialization():
    model = ReasonCodeTestModel(code=GeneticCounselingRecommendationReasonCodingCode.FAMILY_ANAMNESIS)
    dumped_data = model.model_dump()
    assert dumped_data["code"] == "family-anamnesis"