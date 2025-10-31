from enum import Enum

class StudySystem(str, Enum):
    DRKS = "DRKS"
    EUDAMED = "EUDAMED"
    EUDRA_CT = "Eudra-CT"
    NCT = "NCT"