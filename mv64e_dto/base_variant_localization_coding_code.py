from enum import Enum

class BaseVariantLocalizationCodingCode(str, Enum):
    CODING_REGION = "coding-region"
    INTERGENIC = "intergenic"
    INTRONIC = "intronic"
    REGULATORY_REGION = "regulatory-region"
    SPLICING_REGION = "splicing-region"
