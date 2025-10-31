from mv64e_dto.claim_response_status_coding import ClaimResponseStatusCoding
from mv64e_dto.claim_response_status_coding_code import ClaimResponseStatusCodingCode

def test_status_coding_initialization():
    c = ClaimResponseStatusCoding(code=ClaimResponseStatusCodingCode.ACCEPTED, system="http://sys")
    assert c.code == ClaimResponseStatusCodingCode.ACCEPTED
    assert c.system == "http://sys"
    assert c.model_dump(by_alias=True)["code"] == "accepted"

def test_status_coding_alias_input():
    data = {
        "code": "rejected",
        "display": "Abgelehnt"
    }
    c = ClaimResponseStatusCoding(**data)
    assert c.code == ClaimResponseStatusCodingCode.REJECTED
    assert c.display == "Abgelehnt"