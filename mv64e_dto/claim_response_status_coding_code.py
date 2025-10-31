from enum import Enum

class ClaimResponseStatusCodingCode(str, Enum):
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    UNKNOWN = "unknown"