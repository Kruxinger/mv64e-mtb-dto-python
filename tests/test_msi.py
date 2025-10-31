from mv64e_dto.msi import Msi
from mv64e_dto.reference import Reference
from mv64e_dto.msi_interpretation_coding import MsiInterpretationCoding
from mv64e_dto.msi_interpretation_coding_code import MsiInterpretationCodingCode
from mv64e_dto.msi_method_coding import MsiMethodCoding
from mv64e_dto.msi_method_coding_code import MsiMethodCodingCode
from pydantic import ValidationError
import pytest

# Dummy-Daten
DUMMY_REF_P = Reference(id="pat_msi")
DUMMY_INTERPRETATION = MsiInterpretationCoding(code=MsiInterpretationCodingCode.MSI_HIGH)
DUMMY_METHOD = MsiMethodCoding(code=MsiMethodCodingCode.BIOINFORMATIC)


def test_msi_initialization_and_access():
    msi_report = Msi(
        id="msi_1",
        value=0.15,
        patient=DUMMY_REF_P,
        interpretation=DUMMY_INTERPRETATION,
        method=DUMMY_METHOD
    )
    assert msi_report.id == "msi_1"
    assert msi_report.value == 0.15
    assert msi_report.interpretation.code == MsiInterpretationCodingCode.MSI_HIGH
    assert msi_report.method.code == MsiMethodCodingCode.BIOINFORMATIC


def test_msi_serialization_and_deserialization():
    data = {
        "id": "msi_2",
        "value": 0.005,
        "interpretation": {"code": "stable"},
        "method": {"code": "PCR"}
    }
    msi_report = Msi(**data)

    # Überprüfung der Deserialisierung
    assert msi_report.value == 0.005
    assert msi_report.interpretation.code == MsiInterpretationCodingCode.STABLE

    # Überprüfung der Serialisierung (Alias-Namen)
    dump = msi_report.model_dump(by_alias=True, mode='json')
    assert dump["value"] == 0.005
    assert dump["interpretation"]["code"] == "stable"
    assert dump["method"]["code"] == "PCR"


def test_msi_missing_required_value():
    data = {"id": "msi_c", "method": {"code": "IHC"}}
    with pytest.raises(ValidationError):
        Msi(**data)