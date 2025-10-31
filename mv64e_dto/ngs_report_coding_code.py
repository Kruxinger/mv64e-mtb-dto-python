from enum import Enum

class NgsReportCodingCode(str, Enum):
    ARRAY = "array"
    EXOME = "exome"
    GENOME_LONG_READ = "genome-long-read"
    GENOME_SHORT_READ = "genome-short-read"
    KARYOTYPING = "karyotyping"
    OTHER = "other"
    PANEL = "panel"
    SINGLE = "single"