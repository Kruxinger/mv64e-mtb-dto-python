from enum import Enum

class MolecularDiagnosticReportCodingCode(str, Enum):
    ARRAY = "array"
    EXOME = "exome"
    FISH = "FISH"
    FUSION_PANEL = "fusion-panel"
    GENE_PANEL = "gene-panel"
    GENOME_LONG_READ = "genome-long-read"
    GENOME_SHORT_READ = "genome-short-read"
    KARYOTYPING = "karyotyping"
    OTHER = "other"
    PANEL = "panel"
    PCR = "PCR"
    SINGLE = "single"