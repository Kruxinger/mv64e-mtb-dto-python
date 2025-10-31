from mv64e_dto.coding import Coding

def test_coding_initialization():
    c = Coding(code="C123", display="Example Code")
    assert c.code == "C123"
    assert c.display == "Example Code"

def test_coding_alias_input():
    data = {"system": "http://example.org/systems", "version": "v1.0"}
    c = Coding(**data)
    assert c.system == "http://example.org/systems"
    assert c.version == "v1.0"