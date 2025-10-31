from mv64e_dto.atc_unregistered_medication_coding import AtcUnregisteredMedicationCoding
from mv64e_dto.requested_medication_system import RequestedMedicationSystem

def test_atc_unregistered_medication_coding_initialization():
    a = AtcUnregisteredMedicationCoding(
        code="A01",
        display="Test Drug",
        system=RequestedMedicationSystem.FHIR_DE_CODE_SYSTEM_BFARM_ATC,
        version="1.0"
    )
    assert a.code == "A01"
    assert a.display == "Test Drug"
    assert a.system == RequestedMedicationSystem.FHIR_DE_CODE_SYSTEM_BFARM_ATC
    assert a.version == "1.0"

def test_atc_unregistered_medication_coding_alias_input():
    data = {
        "code": "B02",
        "display": "Another Drug",
        "system": "undefined",
        "version": "2.0"
    }
    a = AtcUnregisteredMedicationCoding(**data)
    assert a.code == "B02"
    assert a.display == "Another Drug"
    assert a.system == RequestedMedicationSystem.UNDEFINED
    assert a.version == "2.0"
