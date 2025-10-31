from enum import Enum

class VitalStatusCodingCode(str, Enum):
    ALIVE = "alive"
    DECEASED = "deceased"