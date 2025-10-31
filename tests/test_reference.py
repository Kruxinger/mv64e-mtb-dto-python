from mv64e_dto.reference import Reference

def test_reference_initialization():
    r = Reference(id="ref123", type="Patient")
    assert r.id == "ref123"
    assert r.type == "Patient"
    assert r.model_dump(by_alias=True)["id"] == "ref123"

def test_reference_alias_input():
    data = {"system": "system_a", "display": "Anzeige Name"}
    r = Reference(**data)
    assert r.system == "system_a"
    assert r.display == "Anzeige Name"

def test_reference_full_data():
    data = {
        "display": "Full Display",
        "id": "full_id_456",
        "system": "http://system/full",
        "type": "FullType"
    }
    r = Reference(**data)
    assert r.model_dump(by_alias=True) == data