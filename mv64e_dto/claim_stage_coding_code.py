from enum import Enum

class ClaimStageCodingCode(str, Enum):
    FOLLOW_UP_CLAIM = "follow-up-claim"
    INITIAL_CLAIM = "initial-claim"
    REVOCATION = "revocation"
    UNKNOWN = "unknown"