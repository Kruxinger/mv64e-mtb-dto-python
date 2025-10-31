from enum import Enum

class TherapyStatusCodingCode(str, Enum):
    COMPLETED = "completed"
    NOT_DONE = "not-done"
    ON_GOING = "on-going"
    STOPPED = "stopped"
    UNKNOWN = "unknown"