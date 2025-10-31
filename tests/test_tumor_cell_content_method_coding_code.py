from pydantic import BaseModel
from mv64e_dto.tumor_cell_content_method_coding_code import TumorCellContentMethodCodingCode

class MethodCodeTestModel(BaseModel):
    code: TumorCellContentMethodCodingCode

def test_method_code_values():
    assert TumorCellContentMethodCodingCode.HISTOLOGIC.value == "histologic"

def test_method_code_serialization():
    model = MethodCodeTestModel(code=TumorCellContentMethodCodingCode.BIOINFORMATIC)
    dumped_data = model.model_dump()
    assert dumped_data["code"] == "bioinformatic"