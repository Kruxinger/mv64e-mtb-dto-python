from mv64e_dto.end_range import EndRange
import pytest
from pydantic import ValidationError

def test_end_range_initialization():
    e = EndRange(start=1000.5, end=2000.0)
    assert e.start == 1000.5
    assert e.end == 2000.0
    assert isinstance(e.start, float)

def test_end_range_alias_input():
    data = {"start": 50.0}
    e = EndRange(**data)
    assert e.start == 50.0
    assert e.end is None

def test_end_range_missing_required_field():
    data = {"end": 50.0}
    with pytest.raises(ValidationError):
        # 'start' ist hier als required (float) angenommen
        EndRange(**data)