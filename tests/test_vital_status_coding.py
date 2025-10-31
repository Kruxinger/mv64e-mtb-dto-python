from mv64e_dto.vital_status_coding import VitalStatusCoding
from mv64e_dto.vital_status_coding_code import VitalStatusCodingCode

def test_vital_status_coding_deserialization_alive():
    data = {
        "code": "alive",
        "display": "lebend",
        "system": "http://mtb-codesystem.de/vital-status"
    }
    status = VitalStatusCoding(**data)

    assert status.code == VitalStatusCodingCode.ALIVE
    assert status.display == "lebend"

def test_vital_status_coding_deserialization_deceased():
    data = {"code": "deceased"}
    status = VitalStatusCoding(**data)

    assert status.code == VitalStatusCodingCode.DECEASED

def test_vital_status_coding_serialization():
    status = VitalStatusCoding(
        code=VitalStatusCodingCode.DECEASED
    )
    dump = status.model_dump(by_alias=True, exclude_none=True)
    assert dump["code"] == "deceased"
    assert "display" not in dump