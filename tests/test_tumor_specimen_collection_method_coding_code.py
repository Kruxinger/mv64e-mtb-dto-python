from pydantic import BaseModel
from mv64e_dto.tumor_specimen_collection_method_coding_code import TumorSpecimenCollectionMethodCodingCode

class MethodCodeTestModel(BaseModel):
    code: TumorSpecimenCollectionMethodCodingCode

def test_method_code_values():
    assert TumorSpecimenCollectionMethodCodingCode.LIQUID_BIOPSY.value == "liquid-biopsy"
    assert TumorSpecimenCollectionMethodCodingCode.RESECTION.name == "RESECTION"

def test_method_code_serialization():
    model = MethodCodeTestModel(code=TumorSpecimenCollectionMethodCodingCode.BIOPSY)
    dumped_data = model.model_dump()
    assert dumped_data["code"] == "biopsy"