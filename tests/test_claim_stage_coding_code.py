from pydantic import BaseModel, ValidationError
import pytest
from mv64e_dto.claim_stage_coding_code import ClaimStageCodingCode

class ClaimStageCodingCodeTestModel(BaseModel):
    code: ClaimStageCodingCode

def test_claim_stage_coding_code_values():
    """Überprüft die internen und JSON-Werte des Enums."""
    assert ClaimStageCodingCode.INITIAL_CLAIM.value == "initial-claim"
    assert ClaimStageCodingCode.REVOCATION.name == "REVOCATION"

def test_claim_stage_coding_code_serialization():
    """Überprüft die Serialisierung (Python-Objekt -> JSON)."""
    model = ClaimStageCodingCodeTestModel(code=ClaimStageCodingCode.FOLLOW_UP_CLAIM)
    dumped_data = model.model_dump()
    assert dumped_data["code"] == "follow-up-claim"

def test_claim_stage_coding_code_deserialization_success():
    """Überprüft die Deserialisierung (JSON-String -> Python-Enum)."""
    data = {"code": "unknown"}
    model = ClaimStageCodingCodeTestModel(**data)
    assert model.code == ClaimStageCodingCode.UNKNOWN

def test_claim_stage_coding_code_deserialization_failure():
    """Überprüft die Fehlerbehandlung bei ungültigem Wert."""
    data = {"code": "invalid_stage"}
    with pytest.raises(ValidationError):
        ClaimStageCodingCodeTestModel(**data)