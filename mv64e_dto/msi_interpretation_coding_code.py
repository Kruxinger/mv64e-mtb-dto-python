from enum import Enum

class MsiInterpretationCodingCode(str, Enum):
    MMR_DEFICIENT = "mmr-deficient"
    MMR_PROFICIENT = "mmr-proficient"
    MSI_HIGH = "msi-high"
    MSI_LOW = "msi-low"
    STABLE = "stable"
    UNKNOWN = "unknown"