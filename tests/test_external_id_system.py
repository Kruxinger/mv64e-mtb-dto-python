from pydantic import BaseModel, ValidationError
import pytest
from mv64e_dto.external_id_system import ExternalIdSystem

class ExternalIdSystemTestModel(BaseModel):
    system: ExternalIdSystem

def test_external_id_system_values():
    """Überprüft die internen und JSON-Werte des Enums."""
    assert ExternalIdSystem.ENSEMBL_ORG.value == "https://www.ensembl.org"
    assert ExternalIdSystem.NCBI_NLM_NIH_GOV_SNP.name == "NCBI_NLM_NIH_GOV_SNP"

def test_external_id_system_serialization():
    """Überprüft die Serialisierung (Python-Objekt -> JSON)."""
    model = ExternalIdSystemTestModel(system=ExternalIdSystem.CANCER_SANGER_AC_UK_COSMIC)
    dumped_data = model.model_dump()
    assert dumped_data["system"] == "https://cancer.sanger.ac.uk/cosmic"

def test_external_id_system_deserialization_success():
    """Überprüft die Deserialisierung (JSON-URL -> Python-Enum)."""
    data = {"system": "https://www.ncbi.nlm.nih.gov/entrez"}
    model = ExternalIdSystemTestModel(**data)
    assert model.system == ExternalIdSystem.NCBI_NLM_NIH_GOV_ENTREZ