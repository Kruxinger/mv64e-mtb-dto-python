from mv64e_dto.gender_coding import GenderCoding
from mv64e_dto.gender_coding_code import GenderCodingCode

def test_gender_coding_initialization():
    c = GenderCoding(
        code=GenderCodingCode.FEMALE,
        display="Female"
    )
    assert c.code == GenderCodingCode.FEMALE
    assert c.display == "Female"
    assert c.model_dump(by_alias=True)["code"] == "female"

def test_gender_coding_alias_input():
    data = {
        "code": "other",
        "system": "http://terminology.hl7.org/CodeSystem/v3-AdministrativeGender"
    }
    c = GenderCoding(**data)
    assert c.code == GenderCodingCode.OTHER
    assert c.system == "http://terminology.hl7.org/CodeSystem/v3-AdministrativeGender"

def test_gender_coding_missing_optional_fields():
    c = GenderCoding(code=GenderCodingCode.UNKNOWN)
    assert c.display is None
    assert c.version is None