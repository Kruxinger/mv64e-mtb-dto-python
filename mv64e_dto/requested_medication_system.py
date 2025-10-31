from enum import Enum

class RequestedMedicationSystem(str, Enum):
    FHIR_DE_CODE_SYSTEM_BFARM_ATC = "http://fhir.de/CodeSystem/bfarm/atc"
    UNDEFINED = "undefined"
