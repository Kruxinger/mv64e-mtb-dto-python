from mv64e_dto.confidence_range import ConfidenceRange
import pytest
from pydantic import ValidationError

def test_confidence_range_initialization():
    c = ConfidenceRange(min=0.9, max=0.99)
    assert c.min == 0.9
    assert c.max == 0.99
    assert isinstance(c.min, float)

def test_confidence_range_alias_input():
    data = {"min": 0.05, "max": 0.95}
    c = ConfidenceRange(**data)
    assert c.min == 0.05
    assert c.max == 0.95

def test_confidence_range_serialization():
    c = ConfidenceRange(min=0.1, max=0.8)
    dump = c.model_dump(by_alias=True)
    assert dump["min"] == 0.1
    assert dump["max"] == 0.8

def test_confidence_range_missing_required_field():
    data = {"max": 0.5}
    with pytest.raises(ValidationError):
        # 'min' ist als required float definiert
        ConfidenceRange(**data)