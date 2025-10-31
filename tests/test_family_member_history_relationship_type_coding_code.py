from pydantic import BaseModel, ValidationError
import pytest
from mv64e_dto.family_member_history_relationship_type_coding_code import FamilyMemberHistoryRelationshipTypeCodingCode

class RelationshipCodeTestModel(BaseModel):
    code: FamilyMemberHistoryRelationshipTypeCodingCode

def test_relationship_code_values():
    """Prüft die internen und JSON-Werte des Enums."""
    assert FamilyMemberHistoryRelationshipTypeCodingCode.EXT.value == "EXT"
    assert FamilyMemberHistoryRelationshipTypeCodingCode.FAMMEMB.name == "FAMMEMB"

def test_relationship_code_serialization():
    """Prüft die Serialisierung (Python-Objekt -> JSON)."""
    model = RelationshipCodeTestModel(code=FamilyMemberHistoryRelationshipTypeCodingCode.EXT)
    dumped_data = model.model_dump()
    assert dumped_data["code"] == "EXT"

def test_relationship_code_deserialization_success():
    """Prüft die Deserialisierung (JSON-String -> Python-Enum)."""
    data = {"code": "FAMMEMB"}
    model = RelationshipCodeTestModel(**data)
    assert model.code == FamilyMemberHistoryRelationshipTypeCodingCode.FAMMEMB

def test_relationship_code_deserialization_failure():
    """Prüft die Fehlerbehandlung bei ungültigem Wert."""
    data = {"code": "REL"}
    with pytest.raises(ValidationError):
        RelationshipCodeTestModel(**data)