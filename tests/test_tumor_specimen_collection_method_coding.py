from mv64e_dto.tumor_specimen_collection_method_coding import TumorSpecimenCollectionMethodCoding
from mv64e_dto.tumor_specimen_collection_method_coding_code import TumorSpecimenCollectionMethodCodingCode

def test_method_coding_initialization():
    c = TumorSpecimenCollectionMethodCoding(
        code=TumorSpecimenCollectionMethodCodingCode.RESECTION,
        version="v1"
    )
    assert c.code == TumorSpecimenCollectionMethodCodingCode.RESECTION
    assert c.version == "v1"
    assert c.model_dump(by_alias=True)["code"] == "resection"

def test_method_coding_alias_input():
    data = {"code": "liquid-biopsy", "display": "Liquid Biopsy"}
    c = TumorSpecimenCollectionMethodCoding(**data)
    assert c.code == TumorSpecimenCollectionMethodCodingCode.LIQUID_BIOPSY