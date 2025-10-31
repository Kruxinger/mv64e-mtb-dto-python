from enum import Enum

class MvhSubmissionType(str, Enum):
    ADDITION = "addition"
    CORRECTION = "correction"
    FOLLOWUP = "followup"
    INITIAL = "initial"
    TEST = "test"