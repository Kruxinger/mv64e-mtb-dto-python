from enum import Enum

class LevelOfEvidenceGradingCodingCode(str, Enum):
    M1A = "m1A"
    M1B = "m1B"
    M1C = "m1C"
    M2A = "m2A"
    M2B = "m2B"
    M2C = "m2C"
    M3 = "m3"
    M4 = "m4"
    UNDEFINED = "undefined"