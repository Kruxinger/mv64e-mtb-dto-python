from enum import Enum

class NoSequencingPerformedReasonCode(str, Enum):
    NON_GENETIC_CAUSE = "non-genetic-cause"
    NOT_RARE_DISEASE = "not-rare-disease"
    OTHER = "other"
    PSYCHOSOMATIC = "psychosomatic"
    TARGETED_DIAGNOSTICS_RECOMMENDED = "targeted-diagnostics-recommended"
