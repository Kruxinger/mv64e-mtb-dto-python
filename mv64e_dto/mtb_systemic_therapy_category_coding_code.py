from enum import Enum

class MtbSystemicTherapyCategoryCodingCode(str, Enum):
    A = "A" # Könnte Antikörper sein
    I = "I" # Könnte Immuntherapie sein
    N = "N" # Könnte Neue Substanzen sein
    O = "O" # Könnte Onkologische Substanzen/Chemotherapie sein
    S = "S" # Könnte Small Molecules/Targeted Therapy sein