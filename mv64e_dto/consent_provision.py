from enum import Enum

class ConsentProvision(str, Enum):
    DENY = "deny"
    PERMIT = "permit"