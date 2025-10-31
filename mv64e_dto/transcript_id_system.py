from enum import Enum

class TranscriptIdSystem(str, Enum):
    ENSEMBL_ORG = "https://www.ensembl.org"
    NCBI_NLM_NIH_GOV_REFSEQ = "https://www.ncbi.nlm.nih.gov/refseq"