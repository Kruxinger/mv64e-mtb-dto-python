from enum import Enum

class MtbTherapyIntentCodingCode(str, Enum):
    K = "K" # Könnte 'Kurativ' sein
    P = "P" # Könnte 'Palliativ' sein
    S = "S" # Könnte 'Supportiv' sein
    X = "X" # Könnte 'Experimental' oder 'Unbekannt' sein