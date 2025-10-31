from mv64e_dto.requested_medication_system import RequestedMedicationSystem

def test_requested_medication_system_values():
    assert RequestedMedicationSystem.FHIR_DE_CODE_SYSTEM_BFARM_ATC.value == "http://fhir.de/CodeSystem/bfarm/atc"
    assert RequestedMedicationSystem.UNDEFINED.value == "undefined"
