from datetime import date
from mv64e_dto.mtb_systemic_therapy import MtbSystemicTherapy
from mv64e_dto.mtb_systemic_therapy_category_coding_code import MtbSystemicTherapyCategoryCodingCode
from mv64e_dto.mtb_systemic_therapy_dosage_density_coding_code import MtbSystemicTherapyDosageDensityCodingCode
from mv64e_dto.mtb_systemic_therapy_recommendation_fulfillment_status_coding_code import MtbSystemicTherapyRecommendationFulfillmentStatusCodingCode
from mv64e_dto.mtb_therapy_intent_coding_code import MtbTherapyIntentCodingCode
from mv64e_dto.therapy_status_coding_code import TherapyStatusCodingCode

def test_mtb_systemic_therapy_deserialization():
    data = {
        "id": "st1",
        "category": {"code": "S"},
        "dosage": {"code": "over-50%"},
        "intent": {"code": "P"},
        "status": {"code": "stopped"},
        "statusReason": {"code": "toxicity"},
        "recordedOn": "2024-10-31",
        "recommendationFulfillmentStatus": {"code": "partial"},
        "therapyLine": 3,
        "medication": [{"atc": "L01XE13"}] # Dummy für AtcUnregisteredMedicationCoding
    }
    st = MtbSystemicTherapy(**data)

    assert st.id == "st1"
    assert st.category.code == MtbSystemicTherapyCategoryCodingCode.S
    assert st.dosage.code == MtbSystemicTherapyDosageDensityCodingCode.OVER_50
    assert st.intent.code == MtbTherapyIntentCodingCode.P
    assert st.status.code == TherapyStatusCodingCode.STOPPED
    assert st.status_reason.code.value == "toxicity"
    assert st.recorded_on == date(2024, 10, 31)
    assert st.recommendation_fulfillment_status.code == MtbSystemicTherapyRecommendationFulfillmentStatusCodingCode.PARTIAL
    assert st.therapy_line == 3
    assert st.medication[0]["atc"] == "L01XE13"

def test_mtb_systemic_therapy_serialization():
    st = MtbSystemicTherapy(
        id="st2",
        category={"code": "I"},
        intent={"code": "K"}
    )
    dump = st.model_dump(by_alias=True, exclude_none=True)
    assert dump["category"]["code"] == "I"
    assert dump["intent"]["code"] == "K"