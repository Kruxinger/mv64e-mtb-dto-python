from enum import Enum

class MtbMedicationRecommendationUseTypeCodingCode(str, Enum):
    COMPASSIONATE = "compassionate"
    IN_LABEL = "in-label"
    OFF_LABEL = "off-label"
    SEC_PREVENTIVE = "sec-preventive"
    UNKNOWN = "unknown"