from datetime import date
from mv64e_dto.mtb_study_enrollment_recommendation import MtbStudyEnrollmentRecommendation
from mv64e_dto.recommendation_priority_coding import RecommendationPriorityCoding
from mv64e_dto.recommendation_priority_coding_code import RecommendationPriorityCodingCode

# Dummy-Daten
DUMMY_PRIORITY = RecommendationPriorityCoding(code=RecommendationPriorityCodingCode.CODE_1)

def test_study_enrollment_deserialization():
    data = {
        "id": "ser1",
        "issuedOn": "2024-03-15",
        "priority": {"code": "1"},
        "medication": [{"code": "L01XE13"}], # Dummy für AtcUnregisteredMedicationCoding
        "study": [{"identifier": "NCT01234567"}] # Dummy für StudyReference
    }
    ser = MtbStudyEnrollmentRecommendation(**data)

    assert ser.id == "ser1"
    assert ser.issued_on == date(2024, 3, 15)
    assert ser.priority.code == RecommendationPriorityCodingCode.CODE_1
    assert ser.medication[0]["code"] == "L01XE13"
    assert ser.study[0]["identifier"] == "NCT01234567"

def test_study_enrollment_serialization():
    ser = MtbStudyEnrollmentRecommendation(
        id="ser2",
        priority=DUMMY_PRIORITY
    )
    dump = ser.model_dump(by_alias=True, exclude_none=True)
    assert dump["id"] == "ser2"
    assert dump["priority"]["code"] == "1"