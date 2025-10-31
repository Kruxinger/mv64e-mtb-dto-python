from enum import Enum

class TumorSpecimenCollectionLocalizationCodingCode(str, Enum):
    CELLFREE_DNA = "cellfree-dna"
    LOCAL_RECURRENCE = "local-recurrence"
    METASTASIS = "metastasis"
    PRIMARY_TUMOR = "primary-tumor"
    REGIONAL_LYMPH_NODES = "regional-lymph-nodes"
    UNKNOWN = "unknown"