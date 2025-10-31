from mv64e_dto.claim_response_status_reason_coding import ClaimResponseStatusReasonCoding
from mv64e_dto.claim_response_status_reason_coding_code import ClaimResponseStatusReasonCodingCode

def test_reason_coding_initialization():
    c = ClaimResponseStatusReasonCoding(
        code=ClaimResponseStatusReasonCodingCode.INSUFFICIENT_EVIDENCE,
        version="1.0"
    )
    assert c.code == ClaimResponseStatusReasonCodingCode.INSUFFICIENT_EVIDENCE
    assert c.version == "1.0"
    assert c.model_dump(by_alias=True)["code"] == "insufficient-evidence"

def test_reason_coding_alias_input():
    data = {
        "code": "formal-reasons",
        "system": "http://reason.org"
    }
    c = ClaimResponseStatusReasonCoding(**data)
    assert c.code == ClaimResponseStatusReasonCodingCode.FORMAL_REASONS