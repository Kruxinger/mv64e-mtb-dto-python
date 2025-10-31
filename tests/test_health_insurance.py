from mv64e_dto.health_insurance import HealthInsurance
from mv64e_dto.reference import Reference
from mv64e_dto.health_insurance_coding import HealthInsuranceCoding
from mv64e_dto.health_insurance_coding_code import HealthInsuranceCodingCode

# Dummy-Daten
DUMMY_REF = Reference(id="versicherter_id_123", type="Patient")
DUMMY_TYPE = HealthInsuranceCoding(code=HealthInsuranceCodingCode.GKV, display="Gesetzliche Krankenversicherung")


def test_health_insurance_initialization():
    h = HealthInsurance(
        reference=DUMMY_REF,
        type=DUMMY_TYPE
    )
    assert h.reference.id == "versicherter_id_123"
    assert h.type.code == HealthInsuranceCodingCode.GKV


def test_health_insurance_alias_input_and_serialization():
    data = {
        "reference": {"id": "ref_bg"},
        "type": {"code": "BG", "system": "http://system.de"}
    }
    h = HealthInsurance(**data)

    # Überprüfung der Deserialisierung
    assert h.reference.id == "ref_bg"
    assert h.type.code == HealthInsuranceCodingCode.BG

    # Überprüfung der Serialisierung (Alias-Namen)
    dump = h.model_dump(by_alias=True)
    assert dump["reference"]["id"] == "ref_bg"
    assert dump["type"]["code"] == "BG"