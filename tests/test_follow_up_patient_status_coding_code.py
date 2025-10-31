from pydantic import BaseModel, ValidationError
import pytest
from mv64e_dto.follow_up_patient_status_coding_code import FollowUpPatientStatusCodingCode

class StatusCodeTestModel(BaseModel):
    code: FollowUpPatientStatusCodingCode

def test_status_code_values():
    """Prüft die internen und JSON-Werte des Enums."""
    assert FollowUpPatientStatusCodingCode.LOST_TO_FU.value == "lost-to-fu"

def test_status_code_serialization():
    """Prüft die Serialisierung (Python-Objekt -> JSON)."""
    model = StatusCodeTestModel(code=FollowUpPatientStatusCodingCode.LOST_TO_FU)
    dumped_data = model.model_dump()
    assert dumped_data["code"] == "lost-to-fu"

def test_status_code_deserialization_success():
    """Prüft die Deserialisierung (JSON-String -> Python-Enum)."""
    data = {"code": "lost-to-fu"}
    model = StatusCodeTestModel(**data)
    assert model.code == FollowUpPatientStatusCodingCode.LOST_TO_FU