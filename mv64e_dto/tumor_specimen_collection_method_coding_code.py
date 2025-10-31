from enum import Enum

class TumorSpecimenCollectionMethodCodingCode(str, Enum):
    BIOPSY = "biopsy"
    CYTOLOGY = "cytology"
    LIQUID_BIOPSY = "liquid-biopsy"
    RESECTION = "resection"
    UNKNOWN = "unknown"