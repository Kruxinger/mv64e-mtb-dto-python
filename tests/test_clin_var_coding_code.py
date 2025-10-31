from pydantic import BaseModel, ValidationError
import pytest
from mv64e_dto.clin_var_coding_code import ClinVarCodingCode

class ClinVarCodingCodeTestModel(BaseModel):
    code: ClinVarCodingCode

def test_clin_var_coding_code_values():
    """Überprüft die internen und JSON-Werte des Enums."""
    assert ClinVarCodingCode.CODE_3.value == "3"
    assert ClinVarCodingCode.CODE_5.name == "CODE_5"

def test_clin_var_coding_code_serialization():
    """Überprüft die Serialisierung (Python-Objekt -> JSON)."""
    model = ClinVarCodingCodeTestModel(code=ClinVarCodingCode.CODE_1)
    dumped_data = model.model_dump()
    assert dumped_data["code"] == "1"

def test_clin_var_coding_code_deserialization_success():
    """Überprüft die Deserialisierung (JSON-String -> Python-Enum)."""
    data = {"code": "4"}
    model = ClinVarCodingCodeTestModel(**data)
    assert model.code == ClinVarCodingCode.CODE_4

def test_clin_var_coding_code_deserialization_failure():
    """Überprüft die Fehlerbehandlung bei ungültigem Wert."""
    data = {"code": "99"}
    with pytest.raises(ValidationError):
        ClinVarCodingCodeTestModel(**data)