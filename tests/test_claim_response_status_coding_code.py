from pydantic import BaseModel, ValidationError
import pytest
from mv64e_dto.claim_response_status_coding_code import ClaimResponseStatusCodingCode

class ClaimResponseStatusCodingCodeTestModel(BaseModel):
    code: ClaimResponseStatusCodingCode

def test_status_coding_code_values():
    assert ClaimResponseStatusCodingCode.ACCEPTED.value == "accepted"
    assert ClaimResponseStatusCodingCode.REJECTED.name == "REJECTED"

def test_status_coding_code_serialization():
    model = ClaimResponseStatusCodingCodeTestModel(code=ClaimResponseStatusCodingCode.ACCEPTED)
    dumped_data = model.model_dump()
    assert dumped_data["code"] == "accepted"

def test_status_coding_code_deserialization_success():
    data = {"code": "rejected"}
    model = ClaimResponseStatusCodingCodeTestModel(**data)
    assert model.code == ClaimResponseStatusCodingCode.REJECTED

def test_status_coding_code_deserialization_failure():
    data = {"code": "not-a-valid-status"}
    with pytest.raises(ValidationError):
        ClaimResponseStatusCodingCodeTestModel(**data)