from enum import Enum

class ExternalIdSystem(str, Enum):
    CANCER_SANGER_AC_UK_COSMIC = "https://cancer.sanger.ac.uk/cosmic"
    ENSEMBL_ORG = "https://www.ensembl.org"
    NCBI_NLM_NIH_GOV_ENTREZ = "https://www.ncbi.nlm.nih.gov/entrez"
    NCBI_NLM_NIH_GOV_SNP = "https://www.ncbi.nlm.nih.gov/snp"