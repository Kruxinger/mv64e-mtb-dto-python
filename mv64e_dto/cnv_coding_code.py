from enum import Enum

class CnvCodingCode(str, Enum):
    HIGH_LEVEL_GAIN = "high-level-gain"
    LOSS = "loss"
    LOW_LEVEL_GAIN = "low-level-gain"