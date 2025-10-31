from mv64e_dto.tumor_cell_content import TumorCellContent
from mv64e_dto.reference import Reference
from mv64e_dto.tumor_cell_content_method_coding import TumorCellContentMethodCoding
from mv64e_dto.tumor_cell_content_method_coding_code import TumorCellContentMethodCodingCode
from pydantic import ValidationError
import pytest

DUMMY_METHOD = TumorCellContentMethodCoding(code=TumorCellContentMethodCodingCode.HISTOLOGIC)
DUMMY_REF = Reference(id="ref_tcc")


def test_tcc_initialization():
    tcc = TumorCellContent(
        id="tcc_1",
        value=0.60,
        patient=DUMMY_REF,
        method=DUMMY_METHOD
    )
    assert tcc.value == 0.60
    assert tcc.method.code == TumorCellContentMethodCodingCode.HISTOLOGIC
    assert isinstance(tcc.value, float)


def test_tcc_alias_input_and_serialization():
    data = {
        "id": "tcc_2",
        "value": 0.95,
        "method": {"code": "bioinformatic"}
    }
    tcc = TumorCellContent(**data)

    # Überprüfung der Deserialisierung
    assert tcc.value == 0.95
    assert tcc.method.code == TumorCellContentMethodCodingCode.BIOINFORMATIC

    # Überprüfung der Serialisierung (Alias-Namen)
    dump = tcc.model_dump(by_alias=True)
    assert dump["value"] == 0.95
    assert dump["method"]["code"] == "bioinformatic"


def test_tcc_missing_required_value():
    data = {"id": "tcc_c"}
    with pytest.raises(ValidationError):
        TumorCellContent(**data)