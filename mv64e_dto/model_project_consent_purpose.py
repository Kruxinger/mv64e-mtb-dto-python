from enum import Enum

class ModelProjectConsentPurpose(str, Enum):
    CASE_IDENTIFICATION = "case-identification"
    REIDENTIFICATION = "reidentification"
    SEQUENCING = "sequencing"