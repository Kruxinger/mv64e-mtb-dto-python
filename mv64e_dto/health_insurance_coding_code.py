from enum import Enum

class HealthInsuranceCodingCode(str, Enum):
    BEI = "BEI"
    BG = "BG"
    GKV = "GKV"
    GPV = "GPV"
    PKV = "PKV"
    PPV = "PPV"
    SEL = "SEL"
    SKT = "SKT"
    SOZ = "SOZ"
    UNK = "UNK"