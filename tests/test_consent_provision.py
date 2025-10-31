from pydantic import BaseModel, ValidationError
import pytest
from mv64e_dto.consent_provision import ConsentProvision

class ConsentProvisionTestModel(BaseModel):
    provision: ConsentProvision

def test_consent_provision_values():
    """Überprüft die internen und JSON-Werte des Enums."""
    assert ConsentProvision.DENY.value == "deny"
    assert ConsentProvision.PERMIT.name == "PERMIT"

def test_consent_provision_serialization():
    """Überprüft die Serialisierung (Python-Objekt -> JSON)."""
    model = ConsentProvisionTestModel(provision=ConsentProvision.PERMIT)
    dumped_data = model.model_dump()
    assert dumped_data["provision"] == "permit"

def test_consent_provision_deserialization_success():
    """Überprüft die Deserialisierung (JSON-String -> Python-Enum)."""
    data = {"provision": "deny"}
    model = ConsentProvisionTestModel(**data)
    assert model.provision == ConsentProvision.DENY

def test_consent_provision_deserialization_failure():
    """Überprüft die Fehlerbehandlung bei ungültigem Wert."""
    data = {"provision": "maybe"}
    with pytest.raises(ValidationError):
        ConsentProvisionTestModel(**data)