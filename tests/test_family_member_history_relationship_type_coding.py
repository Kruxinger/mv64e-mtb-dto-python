from mv64e_dto.family_member_history_relationship_type_coding import FamilyMemberHistoryRelationshipTypeCoding
from mv64e_dto.family_member_history_relationship_type_coding_code import FamilyMemberHistoryRelationshipTypeCodingCode

def test_relationship_coding_initialization():
    c = FamilyMemberHistoryRelationshipTypeCoding(
        code=FamilyMemberHistoryRelationshipTypeCodingCode.FAMMEMB,
        display="Family member"
    )
    assert c.code == FamilyMemberHistoryRelationshipTypeCodingCode.FAMMEMB
    assert c.display == "Family member"
    assert c.model_dump(by_alias=True)["code"] == "FAMMEMB"

def test_relationship_coding_alias_input():
    data = {
        "code": "EXT",
        "system": "http://system.org"
    }
    c = FamilyMemberHistoryRelationshipTypeCoding(**data)
    assert c.code == FamilyMemberHistoryRelationshipTypeCodingCode.EXT
    assert c.system == "http://system.org"