from mv64e_dto.tumor_specimen_collection_localization_coding import TumorSpecimenCollectionLocalizationCoding
from mv64e_dto.tumor_specimen_collection_localization_coding_code import TumorSpecimenCollectionLocalizationCodingCode

def test_localization_coding_initialization():
    c = TumorSpecimenCollectionLocalizationCoding(
        code=TumorSpecimenCollectionLocalizationCodingCode.PRIMARY_TUMOR,
        display="Primary Tumor"
    )
    assert c.code == TumorSpecimenCollectionLocalizationCodingCode.PRIMARY_TUMOR
    assert c.display == "Primary Tumor"
    assert c.model_dump(by_alias=True)["code"] == "primary-tumor"

def test_localization_coding_alias_input():
    data = {"code": "regional-lymph-nodes", "system": "http://system"}
    c = TumorSpecimenCollectionLocalizationCoding(**data)
    assert c.code == TumorSpecimenCollectionLocalizationCodingCode.REGIONAL_LYMPH_NODES