from pydantic import BaseModel, ValidationError
import pytest
from mv64e_dto.gender_coding_code import GenderCodingCode

class GenderCodingCodeTestModel(BaseModel):
    code: GenderCodingCode

def test_gender_coding_code_values():
    """Prüft die internen und JSON-Werte des Enums."""
    assert GenderCodingCode.FEMALE.value == "female"
    assert GenderCodingCode.OTHER.name == "OTHER"

def test_gender_coding_code_serialization():
    """Prüft die Serialisierung (Python-Objekt -> JSON)."""
    model = GenderCodingCodeTestModel(code=GenderCodingCode.MALE)
    dumped_data = model.model_dump()
    assert dumped_data["code"] == "male"

def test_gender_coding_code_deserialization_success():
    """Prüft die Deserialisierung (JSON-String -> Python-Enum)."""
    data = {"code": "unknown"}
    model = GenderCodingCodeTestModel(**data)
    assert model.code == GenderCodingCode.UNKNOWN

def test_gender_coding_code_deserialization_failure():
    """Prüft die Fehlerbehandlung bei ungültigem Wert."""
    data = {"code": "nonbinary"}
    with pytest.raises(ValidationError):
        GenderCodingCodeTestModel(**data)