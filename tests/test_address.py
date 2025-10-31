from mv64e_dto.address import Address

def test_address_initialization():
    a = Address(municipality_code="98765")
    assert a.municipality_code == "98765"
    assert a.model_dump(by_alias=True)["municipalityCode"] == "98765"


def test_address_alias_input():
    data = {"municipalityCode": "54321"}
    a = Address(**data)
    assert a.municipality_code == "54321"
