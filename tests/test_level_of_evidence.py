from mv64e_dto.level_of_evidence import LevelOfEvidence
from mv64e_dto.level_of_evidence_grading_coding import LevelOfEvidenceGradingCoding
from mv64e_dto.level_of_evidence_grading_coding_code import LevelOfEvidenceGradingCodingCode
from mv64e_dto.level_of_evidence_addendum_coding import LevelOfEvidenceAddendumCoding
from mv64e_dto.level_of_evidence_addendum_coding_code import LevelOfEvidenceAddendumCodingCode

# Dummy-Daten
DUMMY_GRADING = LevelOfEvidenceGradingCoding(
    code=LevelOfEvidenceGradingCodingCode.M1A,
    display="M1A: Highest Level"
)

DUMMY_ADDENDUM = LevelOfEvidenceAddendumCoding(
    code=LevelOfEvidenceAddendumCodingCode.R
)


def test_loe_initialization_and_access():
    loe = LevelOfEvidence(
        grading=DUMMY_GRADING,
        addendums=[DUMMY_ADDENDUM],
        publications=[{"pubmedId": "12345678"}]  # Dummy für PublicationReference
    )
    assert loe.grading.code == LevelOfEvidenceGradingCodingCode.M1A
    assert len(loe.addendums) == 1
    assert loe.addendums[0].code == LevelOfEvidenceAddendumCodingCode.R
    assert loe.publications[0]["pubmedId"] == "12345678"


def test_loe_serialization_and_deserialization():
    data = {
        "grading": {"code": "m2B"},
        "addendums": [{"code": "is"}, {"code": "Z"}]
    }
    loe = LevelOfEvidence(**data)

    # Überprüfung der Deserialisierung
    assert loe.grading.code == LevelOfEvidenceGradingCodingCode.M2B
    assert len(loe.addendums) == 2

    # Überprüfung der Serialisierung (Alias-Namen)
    dump = loe.model_dump(by_alias=True, exclude_none=True)
    assert dump["grading"]["code"] == "m2B"
    assert dump["addendums"][0]["code"] == "is"