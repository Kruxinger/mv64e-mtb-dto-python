from mv64e_dto.claim_stage_coding import ClaimStageCoding
from mv64e_dto.claim_stage_coding_code import ClaimStageCodingCode

def test_claim_stage_coding_initialization():
    c = ClaimStageCoding(code=ClaimStageCodingCode.INITIAL_CLAIM, display="Initialer Anspruch")
    assert c.code == ClaimStageCodingCode.INITIAL_CLAIM
    assert c.display == "Initialer Anspruch"
    # Prüft die Serialisierung des Enums
    assert c.model_dump(by_alias=True)["code"] == "initial-claim"

def test_claim_stage_coding_alias_input():
    data = {
        "code": "revocation",
        "system": "http://example.org/systems/stages"
    }
    c = ClaimStageCoding(**data)
    assert c.code == ClaimStageCodingCode.REVOCATION
    assert c.system == "http://example.org/systems/stages"
    assert c.model_dump()["code"].value == "revocation" # Prüft den internen Wert

def test_claim_stage_coding_missing_optional_fields():
    c = ClaimStageCoding(code=ClaimStageCodingCode.UNKNOWN)
    assert c.display is None
    assert c.model_dump()["display"] is None