from pydantic import BaseModel
from mv64e_dto.level_of_evidence_grading_coding_code import LevelOfEvidenceGradingCodingCode

class GradingCodeTestModel(BaseModel):
    code: LevelOfEvidenceGradingCodingCode

def test_grading_code_values():
    """Prüft die gemischte Schreibweise (Zahl und Großbuchstabe)."""
    assert LevelOfEvidenceGradingCodingCode.M1C.value == "m1C"
    assert LevelOfEvidenceGradingCodingCode.M4.value == "m4"

def test_grading_code_serialization():
    model = GradingCodeTestModel(code=LevelOfEvidenceGradingCodingCode.M2A)
    dumped_data = model.model_dump()
    assert dumped_data["code"] == "m2A"

def test_grading_code_deserialization_success():
    data = {"code": "m3"}
    model = GradingCodeTestModel(**data)
    assert model.code == LevelOfEvidenceGradingCodingCode.M3