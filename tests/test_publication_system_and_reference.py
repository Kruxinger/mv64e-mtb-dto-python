from pydantic import BaseModel
from mv64e_dto.publication_system import PublicationSystem
from mv64e_dto.publication_reference import PublicationReference


# --- Tests für PublicationSystem ---

class SystemTestModel(BaseModel):
    system: PublicationSystem


def test_system_enum_values():
    assert PublicationSystem.PUBMED_NCBI_NLM_NIH_GOV.value == "https://pubmed.ncbi.nlm.nih.gov"
    assert PublicationSystem.DOI_ORG.value == "https://www.doi.org"


def test_system_deserialization():
    model = SystemTestModel(system="https://www.doi.org")
    assert model.system == PublicationSystem.DOI_ORG


# --- Tests für PublicationReference ---

def test_publication_reference_initialization():
    ref = PublicationReference(
        id="36567341",
        system=PublicationSystem.PUBMED_NCBI_NLM_NIH_GOV,
        display="Example Publication Title"
    )
    assert ref.id == "36567341"
    assert ref.system == PublicationSystem.PUBMED_NCBI_NLM_NIH_GOV


def test_publication_reference_serialization_and_deserialization():
    data = {
        "id": "10.1001/jama.2024.1234",
        "system": "https://www.doi.org",
        "type": "DOI"
    }
    ref = PublicationReference(**data)

    # Überprüfung der Deserialisierung
    assert ref.id == "10.1001/jama.2024.1234"
    assert ref.system == PublicationSystem.DOI_ORG

    # Überprüfung der Serialisierung (Alias-Namen und Enum-Wert)
    dump = ref.model_dump(by_alias=True, exclude_none=True)
    assert dump["id"] == "10.1001/jama.2024.1234"
    assert dump["system"] == "https://www.doi.org"