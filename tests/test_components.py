from mv64e_dto.components import Components
import pytest
from pydantic import ValidationError

def test_components_initialization():
    c = Components(loh=0.5, lst=10.0, tai=8.0)
    assert c.loh == 0.5
    assert c.lst == 10.0
    assert c.tai == 8.0
    assert isinstance(c.loh, float)

def test_components_alias_input():
    data = {"loh": 0.1, "lst": 5.0, "tai": 2.5}
    c = Components(**data)
    assert c.loh == 0.1
    assert c.lst == 5.0
    assert c.tai == 2.5

def test_components_serialization():
    c = Components(loh=0.2, lst=15.0, tai=1.0)
    dump = c.model_dump(by_alias=True)
    assert dump["loh"] == 0.2
    assert dump["lst"] == 15.0
    assert dump["tai"] == 1.0

def test_components_missing_required_field_loh():
    data = {"lst": 5.0, "tai": 2.5}
    with pytest.raises(ValidationError) as excinfo:
        Components(**data)
    assert "loh" in str(excinfo.value)
    assert "Field required" in str(excinfo.value)

def test_components_missing_required_field_tai():
    data = {"loh": 5.0, "lst": 2.5}
    with pytest.raises(ValidationError) as excinfo:
        Components(**data)
    assert "tai" in str(excinfo.value)