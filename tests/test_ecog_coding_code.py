from pydantic import BaseModel, ValidationError
import pytest
from mv64e_dto.ecog_coding_code import EcogCodingCode

class EcogCodingCodeTestModel(BaseModel):
    code: EcogCodingCode

def test_ecog_coding_code_values():
    """Prüft die internen und JSON-Werte des Enums."""
    assert EcogCodingCode.CODE_0.value == "0"
    assert EcogCodingCode.CODE_4.name == "CODE_4"

def test_ecog_coding_code_serialization():
    """Prüft die Serialisierung (Python-Objekt -> JSON)."""
    model = EcogCodingCodeTestModel(code=EcogCodingCode.CODE_2)
    dumped_data = model.model_dump()
    assert dumped_data["code"] == "2"

def test_ecog_coding_code_deserialization_success():
    """Prüft die Deserialisierung (JSON-String -> Python-Enum)."""
    data = {"code": "5"}
    model = EcogCodingCodeTestModel(**data)
    assert model.code == EcogCodingCode.CODE_5

def test_ecog_coding_code_deserialization_failure():
    """Prüft die Fehlerbehandlung bei ungültigem Wert."""
    data = {"code": "6"}
    with pytest.raises(ValidationError):
        EcogCodingCodeTestModel(**data)