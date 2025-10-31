from enum import Enum

class MtbDiagnosisGuidelineTreatmentStatusCodingCode(str, Enum):
    EXHAUSTED = "exhausted"
    IMPOSSIBLE = "impossible"
    NON_EXHAUSTED = "non-exhausted"
    NO_GUIDELINES_AVAILABLE = "no-guidelines-available"
    UNKNOWN = "unknown"