from enum import Enum

class ValueCode(str, Enum):
    MAIN = "main"
    METACHRONOUS = "metachronous"
    SECONDARY = "secondary"