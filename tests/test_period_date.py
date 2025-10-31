from datetime import date
from mv64e_dto.period_date import PeriodDate


def test_period_date_initialization():
    period = PeriodDate(
        start=date(2023, 1, 1),
        end=date(2023, 12, 31)
    )
    assert period.start == date(2023, 1, 1)
    assert period.end == date(2023, 12, 31)


def test_period_date_serialization_and_deserialization():
    data = {
        "start": "2024-06-01",
        "end": "2024-09-30"
    }
    period = PeriodDate(**data)

    # Überprüfung der Deserialisierung
    assert period.start == date(2024, 6, 1)

    # Überprüfung der Serialisierung (Alias-Namen und Datumsformat)
    dump = period.model_dump(by_alias=True, exclude_none=True)
    assert dump["start"] == "2024-06-01"
    assert dump["end"] == "2024-09-30"


def test_period_date_partial_data():
    data = {"start": "2025-01-01"}
    period = PeriodDate(**data)
    assert period.start == date(2025, 1, 1)
    assert period.end is None