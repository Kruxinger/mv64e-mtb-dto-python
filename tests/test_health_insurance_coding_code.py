from pydantic import BaseModel
from mv64e_dto.health_insurance_coding_code import HealthInsuranceCodingCode

class InsuranceCodeTestModel(BaseModel):
    code: HealthInsuranceCodingCode

def test_insurance_code_values():
    """Prüft die internen und JSON-Werte des Enums (deutsche Abkürzungen)."""
    assert HealthInsuranceCodingCode.GKV.value == "GKV" # Gesetzliche Krankenversicherung
    assert HealthInsuranceCodingCode.PKV.name == "PKV" # Private Krankenversicherung

def test_insurance_code_serialization():
    model = InsuranceCodeTestModel(code=HealthInsuranceCodingCode.GKV)
    dumped_data = model.model_dump()
    assert dumped_data["code"] == "GKV"

def test_insurance_code_deserialization_success():
    data = {"code": "PPV"}
    model = InsuranceCodeTestModel(**data)
    assert model.code == HealthInsuranceCodingCode.PPV