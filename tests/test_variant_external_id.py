from mv64e_dto.variant_external_id import VariantExternalId
from mv64e_dto.external_id_system import ExternalIdSystem

def test_variant_external_id_initialization():
    v = VariantExternalId(
        system=ExternalIdSystem.CANCER_SANGER_AC_UK_COSMIC,
        value="COSM476"
    )
    assert v.system == ExternalIdSystem.CANCER_SANGER_AC_UK_COSMIC
    assert v.value == "COSM476"
    # Prüft die Serialisierung des Enums
    assert v.model_dump(by_alias=True)["system"] == "https://cancer.sanger.ac.uk/cosmic"

def test_variant_external_id_alias_input():
    data = {
        "system": "https://www.ensembl.org",
        "value": "ENSG000001"
    }
    v = VariantExternalId(**data)
    assert v.system == ExternalIdSystem.ENSEMBL_ORG
    assert v.value == "ENSG000001"