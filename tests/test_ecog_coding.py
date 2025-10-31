from mv64e_dto.ecog_coding import EcogCoding
from mv64e_dto.ecog_coding_code import EcogCodingCode

def test_ecog_coding_initialization():
    c = EcogCoding(
        code=EcogCodingCode.CODE_1,
        display="Restricted in physically strenuous activity"
    )
    assert c.code == EcogCodingCode.CODE_1
    assert c.display == "Restricted in physically strenuous activity"
    assert c.model_dump(by_alias=True)["code"] == "1"

def test_ecog_coding_alias_input():
    data = {
        "code": "4",
        "system": "http://system.org/ecog"
    }
    c = EcogCoding(**data)
    assert c.code == EcogCodingCode.CODE_4
    assert c.system == "http://system.org/ecog"

def test_ecog_coding_missing_optional_fields():
    c = EcogCoding(code=EcogCodingCode.CODE_0)
    assert c.display is None
    assert c.system is None