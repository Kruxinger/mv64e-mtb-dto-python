from enum import Enum

class ClaimResponseStatusReasonCodingCode(str, Enum):
    APPROVAL_REVOCATION = "approval-revocation"
    FORMAL_REASONS = "formal-reasons"
    INCLUSION_IN_STUDY = "inclusion-in-study"
    INSUFFICIENT_EVIDENCE = "insufficient-evidence"
    OTHER = "other"
    OTHER_THERAPY_RECOMMENDED = "other-therapy-recommended"
    STANDARD_THERAPY_NOT_EXHAUSTED = "standard-therapy-not-exhausted"
    UNKNOWN = "unknown"