from datetime import date
from mv64e_dto.genetic_counseling_recommendation import GeneticCounselingRecommendation
from mv64e_dto.reference import Reference
from mv64e_dto.genetic_counseling_recommendation_reason_coding import GeneticCounselingRecommendationReasonCoding
from mv64e_dto.genetic_counseling_recommendation_reason_coding_code import \
    GeneticCounselingRecommendationReasonCodingCode

# Dummy-Daten
DUMMY_REF = Reference(id="pat_g", type="Patient")
DUMMY_REASON = GeneticCounselingRecommendationReasonCoding(
    code=GeneticCounselingRecommendationReasonCodingCode.FAMILY_ANAMNESIS)


def test_gcr_initialization():
    issue_date = date(2023, 10, 31)
    gcr = GeneticCounselingRecommendation(
        id="gcr_1",
        issued_on=issue_date,
        patient=DUMMY_REF,
        reason=DUMMY_REASON
    )
    assert gcr.id == "gcr_1"
    assert gcr.issued_on == issue_date
    assert gcr.patient.id == "pat_g"
    assert gcr.reason.code == GeneticCounselingRecommendationReasonCodingCode.FAMILY_ANAMNESIS


def test_gcr_date_serialization_and_deserialization():
    # Deserialisierung von JSON (String-Input)
    data = {
        "issuedOn": "2024-01-20",
        "reason": {"code": "self-anamnesis"}
    }
    gcr = GeneticCounselingRecommendation(**data)

    # Überprüfung der Deserialisierungstypen und -werte
    assert gcr.issued_on == date(2024, 1, 20)
    assert gcr.reason.code == GeneticCounselingRecommendationReasonCodingCode.SELF_ANAMNESIS

    # Überprüfung der Serialisierung (Alias-Namen und korrekte Formate)
    dump = gcr.model_dump(by_alias=True, mode='json')
    assert dump["issuedOn"] == "2024-01-20"