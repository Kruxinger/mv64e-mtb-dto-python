from pydantic import BaseModel, ValidationError
import pytest
from mv64e_dto.claim_response_status_reason_coding_code import ClaimResponseStatusReasonCodingCode

class ReasonCodeTestModel(BaseModel):
    code: ClaimResponseStatusReasonCodingCode

def test_reason_code_values():
    assert ClaimResponseStatusReasonCodingCode.INSUFFICIENT_EVIDENCE.value == "insufficient-evidence"
    assert ClaimResponseStatusReasonCodingCode.STANDARD_THERAPY_NOT_EXHAUSTED.name == "STANDARD_THERAPY_NOT_EXHAUSTED"

def test_reason_code_serialization():
    model = ReasonCodeTestModel(code=ClaimResponseStatusReasonCodingCode.FORMAL_REASONS)
    dumped_data = model.model_dump()
    assert dumped_data["code"] == "formal-reasons"

def test_reason_code_deserialization_success():
    data = {"code": "other-therapy-recommended"}
    model = ReasonCodeTestModel(**data)
    assert model.code == ClaimResponseStatusReasonCodingCode.OTHER_THERAPY_RECOMMENDED