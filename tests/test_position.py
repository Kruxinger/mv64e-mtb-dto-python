from mv64e_dto.position import Position


def test_position_deserialization():
    data = {
        "start": 123456.0,
        "end": 123457.0
    }
    position = Position(**data)

    assert position.start == 123456.0
    assert position.end == 123457.0


def test_position_deserialization_single_point():
    data = {
        "start": 50000.0,
        "end": None
    }
    position = Position(**data)

    assert position.start == 50000.0
    assert position.end is None


def test_position_serialization():
    position = Position(
        start=9876.0,
        end=9876.0
    )
    dump = position.model_dump(by_alias=True, exclude_none=True)
    assert dump["start"] == 9876.0
    assert dump["end"] == 9876.0