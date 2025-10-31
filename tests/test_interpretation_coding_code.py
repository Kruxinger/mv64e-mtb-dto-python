from pydantic import BaseModel, ValidationError
import pytest
from mv64e_dto.interpretation_coding_code import InterpretationCodingCode

class InterpretationCodeTestModel(BaseModel):
    code: InterpretationCodingCode

def test_interpretation_code_values():
    """Prüft die internen und JSON-Werte des Enums."""
    assert InterpretationCodingCode.HIGH.value == "high"
    assert InterpretationCodingCode.INTERMEDIATE.name == "INTERMEDIATE"

def test_interpretation_code_serialization():
    """Prüft die Serialisierung (Python-Objekt -> JSON)."""
    model = InterpretationCodeTestModel(code=InterpretationCodingCode.LOW)
    dumped_data = model.model_dump()
    assert dumped_data["code"] == "low"

def test_interpretation_code_deserialization_success():
    """Prüft die Deserialisierung (JSON-String -> Python-Enum)."""
    data = {"code": "intermediate"}
    model = InterpretationCodeTestModel(**data)
    assert model.code == InterpretationCodingCode.INTERMEDIATE

def test_interpretation_code_deserialization_failure():
    """Prüft die Fehlerbehandlung bei ungültigem Wert."""
    data = {"code": "negative"}
    with pytest.raises(ValidationError):
        InterpretationCodeTestModel(**data)