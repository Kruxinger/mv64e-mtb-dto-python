from mv64e_dto.age import Age
from mv64e_dto.unit import Unit

def test_age_initialization():
    a = Age(unit=Unit.MONTHS, value=12.0)
    assert a.unit == Unit.MONTHS
    assert a.value == 12.0
    assert a.model_dump(by_alias=True)["unit"] == "Months"

def test_age_alias_input():
    data = {"unit": "Years", "value": 5}
    a = Age(**data)
    assert a.unit == Unit.YEARS
    assert a.value == 5
