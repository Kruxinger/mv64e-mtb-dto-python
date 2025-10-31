from mv64e_dto.recist_coding import RecistCoding
from mv64e_dto.recist_coding_code import RecistCodingCode

def test_recist_coding_deserialization():
    data = {
        "code": "CR",
        "display": "Complete Response",
        "system": "http://recist.de/codes"
    }
    recist = RecistCoding(**data)

    assert recist.code == RecistCodingCode.CR
    assert recist.display == "Complete Response"
    assert recist.system == "http://recist.de/codes"

def test_recist_coding_serialization():
    recist = RecistCoding(
        code=RecistCodingCode.PD,
        display="Progressive Disease"
    )
    dump = recist.model_dump(by_alias=True, exclude_none=True)
    assert dump["code"] == "PD"
    assert dump["display"] == "Progressive Disease"
    assert "system" not in dump