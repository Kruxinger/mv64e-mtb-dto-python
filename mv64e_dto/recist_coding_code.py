from enum import Enum

class RecistCodingCode(str, Enum):
    # CR: Complete Response
    CR = "CR"
    # MR: Mixed Response (manchmal verwendet, aber nicht offiziell in RECIST 1.1)
    MR = "MR"
    # NA: Not Applicable / Not Assessed
    NA = "NA"
    # PD: Progressive Disease
    PD = "PD"
    # PR: Partial Response
    PR = "PR"
    # SD: Stable Disease
    SD = "SD"