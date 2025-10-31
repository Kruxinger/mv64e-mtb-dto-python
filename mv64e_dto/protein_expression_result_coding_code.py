from enum import Enum

class ProteinExpressionResultCodingCode(str, Enum):
    EXP = "exp"
    NOT_EXP = "not-exp"
    CODE_1PLUS = "1+"
    CODE_2PLUS = "2+"
    CODE_3PLUS = "3+"
    UNKNOWN = "unknown"