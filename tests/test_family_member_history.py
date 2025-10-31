from mv64e_dto.family_member_history import FamilyMemberHistory
from mv64e_dto.reference import Reference
from mv64e_dto.family_member_history_relationship_type_coding import FamilyMemberHistoryRelationshipTypeCoding
from mv64e_dto.family_member_history_relationship_type_coding_code import FamilyMemberHistoryRelationshipTypeCodingCode

# Dummy-Daten
DUMMY_REF = Reference(id="pat_x", type="Patient")
DUMMY_REL = FamilyMemberHistoryRelationshipTypeCoding(code=FamilyMemberHistoryRelationshipTypeCodingCode.FAMMEMB)


def test_family_member_history_initialization():
    f = FamilyMemberHistory(
        id="fam_h_1",
        patient=DUMMY_REF,
        relationship=DUMMY_REL
    )
    assert f.id == "fam_h_1"
    assert f.patient.id == "pat_x"
    assert f.relationship.code == FamilyMemberHistoryRelationshipTypeCodingCode.FAMMEMB


def test_family_member_history_alias_input_and_serialization():
    data = {
        "id": "fam_h_2",
        "relationship": {"code": "EXT"}
    }
    f = FamilyMemberHistory(**data)

    # Überprüfung der Deserialisierung
    assert f.id == "fam_h_2"
    assert f.relationship.code == FamilyMemberHistoryRelationshipTypeCodingCode.EXT

    # Überprüfung der Serialisierung (Alias-Namen)
    dump = f.model_dump(by_alias=True)
    assert dump["id"] == "fam_h_2"
    assert dump["relationship"]["code"] == "EXT"