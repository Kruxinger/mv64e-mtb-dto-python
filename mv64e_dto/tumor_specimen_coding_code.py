from enum import Enum

class TumorSpecimenCodingCode(str, Enum):
    CRYO_FROZEN = "cryo-frozen"
    FFPE = "FFPE" # Formalin-Fixed Paraffin-Embedded
    FRESH_TISSUE = "fresh-tissue"
    LIQUID_BIOPSY = "liquid-biopsy"
    UNKNOWN = "unknown"