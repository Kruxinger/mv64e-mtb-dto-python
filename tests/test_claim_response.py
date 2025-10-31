from datetime import date
from mv64e_dto.claim_response import ClaimResponse
from mv64e_dto.reference import Reference
from mv64e_dto.claim_response_status_coding import ClaimResponseStatusCoding
from mv64e_dto.claim_response_status_coding_code import ClaimResponseStatusCodingCode
from mv64e_dto.claim_response_status_reason_coding import ClaimResponseStatusReasonCoding
from mv64e_dto.claim_response_status_reason_coding_code import ClaimResponseStatusReasonCodingCode

# Dummy-Daten für abhängige DTOs
DUMMY_CLAIM_REF = Reference(id="claim123", type="Claim")
DUMMY_STATUS = ClaimResponseStatusCoding(code=ClaimResponseStatusCodingCode.ACCEPTED)
DUMMY_REASON = ClaimResponseStatusReasonCoding(code=ClaimResponseStatusReasonCodingCode.FORMAL_REASONS)


def test_claim_response_initialization():
    c = ClaimResponse(
        id="resp456",
        issued_on=date(2025, 11, 1),
        claim=DUMMY_CLAIM_REF,
        status=DUMMY_STATUS,
        status_reason=[DUMMY_REASON]
    )
    assert c.id == "resp456"
    assert c.issued_on == date(2025, 11, 1)
    assert c.claim.id == "claim123"
    assert c.status.code == ClaimResponseStatusCodingCode.ACCEPTED
    assert len(c.status_reason) == 1


def test_claim_response_alias_input_and_serialization():
    data = {
        "id": "resp789",
        "issuedOn": "2024-05-20",  # JSON-String-Eingabe für Datum
        "status": {"code": "rejected"},  # Status ist REJECTED
        "statusReason": [{"code": "insufficient-evidence"}, {"code": "other"}]  # Zwei Gründe
    }
    c = ClaimResponse(**data)

    # Überprüfung der Deserialisierung
    assert c.issued_on == date(2024, 5, 20)
    assert c.status.code == ClaimResponseStatusCodingCode.REJECTED
    assert c.status_reason[0].code == ClaimResponseStatusReasonCodingCode.INSUFFICIENT_EVIDENCE

    # Überprüfung der Serialisierung (Datum und Alias-Namen)
    dump = c.model_dump(by_alias=True)
    assert dump["issuedOn"] == "2024-05-20"
    assert dump["status"]["code"] == "rejected"
    assert dump["statusReason"][1]["code"] == "other"