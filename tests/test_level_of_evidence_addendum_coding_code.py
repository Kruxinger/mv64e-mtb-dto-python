from pydantic import BaseModel, ValidationError
import pytest
from mv64e_dto.level_of_evidence_addendum_coding_code import LevelOfEvidenceAddendumCodingCode

class AddendumCodeTestModel(BaseModel):
    code: LevelOfEvidenceAddendumCodingCode

def test_addendum_code_values():
    """Prüft die Werte, die sowohl Klein- als auch Großbuchstaben enthalten."""
    assert LevelOfEvidenceAddendumCodingCode.IS.value == "is"
    assert LevelOfEvidenceAddendumCodingCode.R.value == "R"

def test_addendum_code_serialization():
    model = AddendumCodeTestModel(code=LevelOfEvidenceAddendumCodingCode.IV)
    dumped_data = model.model_dump()
    assert dumped_data["code"] == "iv"

def test_addendum_code_deserialization_success():
    data = {"code": "Z"}
    model = AddendumCodeTestModel(**data)
    assert model.code == LevelOfEvidenceAddendumCodingCode.Z