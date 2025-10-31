from enum import Enum

class PublicationSystem(str, Enum):
    PUBMED_NCBI_NLM_NIH_GOV = "https://pubmed.ncbi.nlm.nih.gov"
    DOI_ORG = "https://www.doi.org"