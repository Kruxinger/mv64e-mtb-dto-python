from mv64e_dto.unit import Unit

def test_unit_values():
    assert Unit.MONTHS.value == "Months"
    assert Unit.YEARS.value == "Years"
