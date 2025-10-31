from pydantic import BaseModel, ValidationError
import pytest
from mv64e_dto.value_code import ValueCode

class ValueCodeTestModel(BaseModel):
    code: ValueCode

def test_value_code_values():
    """Prüft die internen und JSON-Werte des Enums."""
    assert ValueCode.MAIN.value == "main"
    assert ValueCode.METACHRONOUS.name == "METACHRONOUS"

def test_value_code_serialization():
    """Prüft die Serialisierung (Python-Objekt -> JSON)."""
    model = ValueCodeTestModel(code=ValueCode.SECONDARY)
    dumped_data = model.model_dump()
    assert dumped_data["code"] == "secondary"

def test_value_code_deserialization_success():
    """Prüft die Deserialisierung (JSON-String -> Python-Enum)."""
    data = {"code": "metachronous"}
    model = ValueCodeTestModel(**data)
    assert model.code == ValueCode.METACHRONOUS

def test_value_code_deserialization_failure():
    """Prüft die Fehlerbehandlung bei ungültigem Wert."""
    data = {"code": "primary"}
    with pytest.raises(ValidationError):
        ValueCodeTestModel(**data)