from enum import Enum

class OncoProcedureCodingCode(str, Enum):
    NUCLEAR_MEDICINE = "nuclear-medicine"
    RADIO_THERAPY = "radio-therapy"
    SURGERY = "surgery"