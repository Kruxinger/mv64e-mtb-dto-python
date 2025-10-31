from mv64e_dto.mtb_medication_recommendation_use_type_coding import MtbMedicationRecommendationUseTypeCoding
from mv64e_dto.mtb_medication_recommendation_use_type_coding_code import MtbMedicationRecommendationUseTypeCodingCode

def test_use_type_coding_deserialization():
    data = {
        "code": "off-label",
        "display": "Off-Label Use",
    }
    coding = MtbMedicationRecommendationUseTypeCoding(**data)
    assert coding.code == MtbMedicationRecommendationUseTypeCodingCode.OFF_LABEL
    assert coding.display == "Off-Label Use"

def test_use_type_coding_serialization():
    coding = MtbMedicationRecommendationUseTypeCoding(
        code=MtbMedicationRecommendationUseTypeCodingCode.COMPASSIONATE
    )
    dump = coding.model_dump(by_alias=True, exclude_none=True)
    assert dump["code"] == "compassionate"